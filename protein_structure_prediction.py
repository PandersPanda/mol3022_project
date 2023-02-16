import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.layers import Conv1D, MaxPooling1D, Flatten

# Load the dataset and preprocess the data
data = pd.read_csv("./Data/2018-06-06-ss.cleaned.csv")
X = data.iloc[:, 2].values
y = data.iloc[:, 4].values

# Encode the target variable
encoder = LabelEncoder()
X = encoder.fit_transform(X)
y = encoder.fit_transform(y)
print(X)
print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model architecture
model = Sequential()
model.add(Dense(32, input_dim=1, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='relu'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

print(model.summary())

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=128, validation_data=(X_test, y_test))

# Evaluate the model on the test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)
