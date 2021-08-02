from utilities.load_data import load_data
from model.model import NeuralNet
from model.dataset_model import ChatDataSet

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


X_train, y_train ,all_words, tags = load_data() #Loading the data

#Hyper parameters
batch_size = 64
hidden_size = 8
input_size = len(all_words)
output_size = len(tags)
learning_rate = 0.001
num_epocs = 10000

#Creating the dataset loader
dataset = ChatDataSet(X_train,y_train)
train_looader = DataLoader(dataset= dataset, batch_size = batch_size, shuffle =True) 
#Creating the model
device  =  torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model  = NeuralNet(input_size, hidden_size, output_size)    

# Calculate loss and optimzer
criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epocs):
    for (words, lables) in train_looader:
        words = words.to(device)
        lables = lables.to(device)

        #forward step
        outputs = model(words)
        loss = criterion(outputs, lables)

        #backward step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch + 1) % 100 ==0:
        print(f"epoch {epoch + 1}/{num_epocs}, loss={loss.item():.4f}")
print(f"final loss, loss={loss.item():.4f}")

 #Saving the trained model
data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "output/data.pth"
torch.save(data, FILE)

print('training complete. file saved to {FILE}')