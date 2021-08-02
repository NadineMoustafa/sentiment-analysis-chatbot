import torch.nn as nn
#Here is the model itself it contains three hidden layers
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        #Layer number 1 with size= input_size X hidden_size
        self.layer1 = nn.Linear(input_size, hidden_size)
        #Layer number 2 with size= hidden_size X hidden_size
        self.layer2 = nn.Linear(hidden_size, hidden_size)
        #Layer number 3 with size= hidden_size X num_classes
        self.layer3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
#The forward stage with the ractifier.
    def forward(self, input):
        output = self.layer1(input)
        output = self.relu(output)
        output = self.layer2(output)
        output = self.relu(output)
        output = self.layer3(output)
        output = self.relu(output)
        return output
