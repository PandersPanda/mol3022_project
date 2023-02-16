import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv("./Data/2018-06-06-ss.cleaned.csv")

sequences = data.iloc[:, 2].values
structures = data.iloc[:, 4].values


# Convert the structures to classes


print(structures)
# Encode the sequences and structures
encoder = LabelEncoder()
sequences = encoder.fit_transform(sequences)
print("seq",sequences.dtype)
structures = encoder.fit_transform(structures)


# Define the model architecture
class SecondaryStructureModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SecondaryStructureModel, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x):
        return self.net(x)

# Define the hyperparameters and optimizer
input_size = 1
hidden_size = 64
output_size = 3
lr = 0.01
epochs = 10

model = SecondaryStructureModel(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

# Training loop
for epoch in range(epochs):
    model.train()
    for i in range(len(sequences)):
        x = torch.tensor(sequences[i], dtype=torch.float32).unsqueeze(0)
        y = torch.tensor(structures[i], dtype=torch.float32).unsqueeze(0)
        optimizer.zero_grad()
        output = model(x)
        predicted = torch.softmax(output, dim=0).argmax(dim=0)
        loss = criterion(predicted, y)
        loss.backward()
        optimizer.step()

    # Validation loop
    model.eval()
    with torch.inference_mode():

        total = 0
        correct = 0
        for i in range(len(sequences)):
            x = torch.tensor(sequences[i]).unsqueeze(0)
            y = torch.tensor(structures[i]).unsqueeze(0)
            output = model(x)
            predicted = torch.softmax(output, dim=1).argmax(dim=1)
            total += y.shape[1]
            correct += (predicted == y).sum().item()

        accuracy = correct / total
        print(f"Test Accuracy: {accuracy:.4f}")