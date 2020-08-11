import torch
import numpy as np
from flask import jsonify
import torch.nn as nn

class OneDimCNN(nn.Module):
    def __init__(self):
        super(OneDimCNN, self).__init__()
        self.num_class = 34

        self.conv = nn.Conv2d(1, 32, kernel_size=(1, 71), stride=(1, 1))
        self.pool = nn.MaxPool2d(1, 2)
        self.hidden1 = nn.Linear(50*32*1, 128)
        self.hidden2 = nn.Linear(128, self.num_class)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax()

    def forward(self, x):
        x = self.relu(self.conv(x))
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.relu(self.hidden1(x))
        x = self.softmax(self.hidden2(x))

        return x

def infer(data):
    model = OneDimCNN()
    model.load_state_dict(torch.load('./model/output_dir/1DCNN_0809_15e-4.pt'))

    model.eval()

    with open(f'./input/{data}') as f:
        x = np.loadtxt(f)

    # with open(f'./input/{data}') as f:
    #     y = np.loadtxt(f)

    with open('./model/labels.txt') as f:
        labels = f.readlines()

    with open('./model/cancer_names.txt') as f:
        names = f.readlines()

    x = torch.from_numpy(x)
    x = x.unsqueeze(0)
    x = x.reshape(x.shape[0], 1, 100, 71)
    x = x.float()

    pred = model(x)

    y_hat = torch.max(pred, 1)[1]
    # y = np.argmax(y, -1)

    return labels[y_hat], names[y_hat]

def top_ten(data):
    curr = np.loadtxt(f'./input/{data}')

    with open('./model/average.txt') as f:
        avgs = f.readlines()

    with open('./model/gene_names.txt') as f:
        genes = f.readlines()

    abs_diff = []
    for i in range(7100):
        abs_diff.append(abs(curr[i] - float(avgs[i])))

    top_10_idx = np.argsort(abs_diff)[-10:]
    top_10_labels = [genes[i].strip() for i in top_10_idx]
    top_10_normal = [float(avgs[i]) for i in top_10_idx]
    top_10_input = [curr[i] for i in top_10_idx]

    return top_10_labels, top_10_normal, top_10_input

def model_inference(data):
    cohort, name = infer(data)
    top_labels, top_normal, top_input = top_ten(data)

    return cohort, name, top_labels, top_normal, top_input
