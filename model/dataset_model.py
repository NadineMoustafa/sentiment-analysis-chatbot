from torch.utils.data import DataLoader
#Loading the dataset "overriding data loader of Pytorch to satisfy our use case"
class ChatDataSet(DataLoader):
    def __init__(self,X_train,y_train):
        self.numer_of_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    def __len__(self):
        return self.numer_of_samples