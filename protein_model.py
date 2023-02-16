import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

# Load the data into a pandas DataFrame
data = pd.read_csv("./Data/2018-06-06-ss.cleaned.csv")

# Only extract the data from the 2nd and 4th columns
data = data[['seq', 'sst3']]

# Split the data into training and test sets
train_data = data[:int(0.8*len(data))]
test_data = data[int(0.8*len(data)):]

# Concatenate the training and test data to fit the encoder on the complete dataset
all_data = pd.concat([train_data, test_data])

# Fit the label encoder on the complete dataset
encoder = LabelEncoder()
encoder.fit(all_data['seq'].values)

# Convert the protein sequences into numerical representations
train_sequences = encoder.transform(train_data['seq'].values)
test_sequences = encoder.transform(test_data['seq'].values)

# One-hot encode the secondary structure labels
train_labels = pd.get_dummies(train_data['sst3']).values
test_labels = pd.get_dummies(test_data['sst3']).values

# Check that the number of unique labels matches the expected number of classes
n_classes = len(np.unique(encoder.inverse_transform(np.arange(train_sequences.max() + 1))))
assert n_classes == train_labels.shape[1]

# Define the neural network model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(train_sequences.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(train_labels.shape[1], activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_sequences, train_labels, epochs=50, batch_size=32)

# Evaluate the model on the test data
test_loss, test_accuracy = model.evaluate(test_sequences, test_labels)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)