import json
import numpy as np

from utilities.nltk_utils import tokenize, stem, bag_of_words
def load_data(data_path = '/Users/abdelrahman/Desktop/Abdelrahman/Python/Chatbot/Dataset/Train/train.json'):
    with open(data_path,'r') as file: #Reading the trained dataset.
        train_dataset = json.load(file)


    all_words = []
    tags = []
    traning_pair = []
    #Transforming the dataset by doing tokenization also getting the bag of words for the trained dataset and then Stemming to be in format X_train and Y_train by calling functions that are in different file and we imported them.
    for sample in train_dataset['dataset']: 
        tag = sample['context']
        tags.append(tag)
        for pattern in sample['patterns']:
            tokenized_pattern = tokenize(pattern) 
            all_words.extend(tokenized_pattern)
            traning_pair.append((tokenized_pattern, tag))
    ignore_words = ['.',',','?','!']
    all_words = [stem(word) for word in all_words if word not in ignore_words]
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))

    X_train = []
    y_train = []
    for(tokenized_pattern, tag) in traning_pair:
        bag = bag_of_words(tokenized_pattern, all_words)
        X_train.append(bag)
        lable= tags.index(tag)
        y_train.append(lable)

    X_train = np.array(X_train)
    y_train = np.array(y_train)
    return X_train, y_train, all_words, tags