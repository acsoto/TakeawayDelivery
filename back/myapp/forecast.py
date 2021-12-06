# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import torch.nn as nn
import torch
import matplotlib.pyplot as plt
import math


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.linear1 = nn.Linear(4, 8)
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


def predict(model, dl):
    model.eval()
    with torch.no_grad():
        result = model(torch.FloatTensor(dl))
    return result.item()


def getTag(weekday, hour, storeId, receiveAddress):
    tagTime = 0.5 * weekday / 7.0
    tagTime = tagTime + 0.4 * (0.0000004 * math.pow(hour, 6) - 0.0003 * math.pow(hour, 5) + 0.0099 * math.pow(hour,
                                                                                                              4) - 0.1428 * math.pow(
        hour, 3) + 0.9121 * math.pow(hour, 2) - 1.7723 * hour + 1.4367) / 5
    tagTime = tagTime + 0.1 * (receiveAddress + storeId) / 16.0
    tagTime = tagTime * 60.0 + random.randint(-5, 5)
    if tagTime <= 5:
        tagTime = 5
    if tagTime > 60:
        tagTime = 60
    return tagTime


def train_model():
    global loss
    trainData = []
    tagData = []

    epochs = 1
    for epoch in range(epochs):
        for weekday in range(7):
            for hour in range(24):
                for storeId in range(1, 10):
                    for receiveAddress in range(1, 8):
                        trainData.append([weekday, hour, storeId, receiveAddress])
                        tagData.append([getTag(weekday, hour, storeId, receiveAddress)])
    # print(trainData)
    # cnt = 0
    # index = 0
    # for index in range(len(tagData)):
    #     if tagData[index][0] > 50:
    #         cnt = cnt + 1
    # print(cnt)
    # print(tagData)

    trainData = torch.FloatTensor(trainData)
    tagData = torch.FloatTensor(tagData)
    model = Net()
    model.optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    model.loss_func = torch.nn.L1Loss()
    epochs = 10
    branch = 5
    losses = []
    for epoch in range(epochs):
        for index in range(int(trainData.shape[0] / branch)):
            model.optimizer.zero_grad()
            prediction = model(trainData[index * branch:(index + 1) * branch])
            loss = model.loss_func(prediction, tagData[index * branch:(index + 1) * branch])
            print("--------" + str(epoch))
            print("pre:" + str(prediction))
            print("tag:" + str(tagData[index * branch:(index + 1) * branch]))
            print(loss)

            loss.backward()
            model.optimizer.step()
        losses.append(loss)

    epochsImage = range(1, epochs + 1)
    print(losses)
    plt.plot(epochsImage, losses, "bo--")
    plt.title('Training')
    plt.xlabel("Epochs")
    plt.ylabel("loss")
    plt.legend(["train_loss"])
    ## plt.show()
    plt.savefig("./test.png")
    torch.save(model.state_dict(), "./model_parameter.pkl")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    train_model()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
