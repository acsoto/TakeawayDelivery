# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import torch.nn as nn
import torch
import matplotlib.pyplot as plt

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.linear1 = nn.Linear(5, 8)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(8, 16)
        self.relu = nn.ReLU()
        self.linear3 = nn.Linear(16, 32)
        self.relu = nn.ReLU()
        self.linear4 = nn.Linear(32, 16)
        self.relu = nn.ReLU()
        self.linear5 = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        x = self.linear3(x)
        x = self.relu(x)
        x = self.linear4(x)
        x = self.relu(x)
        y = self.linear5(x)
        return y

    def predict(self, x):
        return self.forward(x)


def init(trainData, tagData):
    trainData = [
        [4, 3, 2, 1, 1],
        [4, 3, 2, 1, 1],
        [4, 3, 2, 1, 1],
        [5, 5, 4, 9, 4],
        [5, 5, 4, 9, 4],
        [5, 5, 4, 9, 4],
    ]
    tagData = [
        [4], [4], [4], [10], [10], [10]
    ]


def train_model():
    global loss
    trainData = [
        [4, 3, 2, 1, 1],
        [4, 3, 2, 1, 1],
        [4, 3, 2, 1, 1],
        [4, 3, 2, 1, 1],
        [4, 3, 2, 1, 1],
        [5, 5, 4, 9, 4],
        [5, 5, 4, 9, 4],
        [5, 5, 4, 9, 4],
    ]
    tagData = [
        [4], [4], [4], [4], [4], [10], [10], [10]
    ]
    trainData = torch.FloatTensor(trainData)
    tagData = torch.FloatTensor(tagData)
    model = Net()
    model.optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    model.loss_func = torch.nn.L1Loss()
    epochs = 100
    branch = 5
    losses = []
    for epoch in range(epochs):
        for index in range(int(trainData.shape[0]/branch)):
            model.optimizer.zero_grad()
            prediction = model(trainData[index*branch:(index+1)*branch])
            loss = model.loss_func(prediction, tagData[index*branch:(index+1)*branch])
            print("--------" + str(epoch))
            print("pre:" + str(prediction))
            print("tag:" + str(tagData[index*branch:(index+1)*branch]))
            print(loss)

            loss.backward()
            model.optimizer.step()
        losses.append(loss)

    epochsImage = range(1, epochs+1)
    print(losses)
    plt.plot(epochsImage, losses, "bo--")
    plt.title('Training')
    plt.xlabel("Epochs")
    plt.ylabel("loss")
    plt.legend(["train_loss"])
    ## plt.show()
    plt.savefig("./test.png")




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    train_model()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
