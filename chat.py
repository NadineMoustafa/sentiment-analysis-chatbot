import random
import json
from nltk.util import pr

import torch

from model.model import NeuralNet
from utilities.nltk_utils import bag_of_words, tokenize
from google_trans_new import google_translator

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#Reading our translated dataset
with open('/Users/abdelrahman/Desktop/Abdelrahman/Python/Chatbot/Dataset/Train/train.json', 'r') as json_data:
    intents = json.load(json_data)

#Loading the trained model
FILE = "output/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#The chat itself
bot_name = "البوت "

print("(هيا بنا نتحدث لإغلاق المحادثة اكتب (خروج ")

while True:

    sentence = input("انت: ") #Taking the input/message from the user
    translator = google_translator()
    if sentence == "خروج": #If it is Quit we will Exit the chat.
        break
    
    # transform the input
    sentence = tokenize(sentence) #Tokenzing the input.
    X = bag_of_words(sentence, all_words) #Getting the bag of words for this sentence
    X = X.reshape(1, X.shape[0]) #Reshaping it.
    X = torch.from_numpy(X).to(device)

    # predict the output
    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()] #Getting the Sentiment Analysis of the sentence.
    # print(tag)
    probs = torch.softmax(output, dim=1) #Getting the highest probability using Softmax to get the type.
    prob = probs[0][predicted.item()] 
    # print(prob)
    if prob.item() > 0.55: #Selecting the response randomly with matching value = 55% which can be changed.
        for intent in intents['dataset']:
            if tag == intent["context"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}") #Sending the response back to the user.
    else:
        print(f"{bot_name}: لم افهم") #If it does not match any of the dataset it will reply by I do not understand in Arabic.