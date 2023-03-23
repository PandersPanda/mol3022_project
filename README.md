# MOL3022 Project - Protein Secondary Structure Prediction Using Machine Learning

## About the application:

The application takes in a protein sequence of a length up to 128 amino acids and predicts the secundary structure of the protein. The application uses a Neural Network (machine learning) to make perdictions. There are two parts to the application: [frontend](#frontend) and [backend](#backend). The backend was written in Python, and consists of a trained model and a simple web framework (Flask). The frontend was written using React (TypeScript), and is used to as a "communicator" between the user and the prediction model by providing a simple user-friendly user interface. 

## About the dataset

The dataset we use to train the model was downloaded from [kaggle](https://www.kaggle.com/datasets/alfrandom/protein-secondary-structure).

---------

&nbsp;

## Setup (Only need to do once)

It is highly recommended to do this in Windows Subsystem for Linux (WSL) or a VM. Also to use a conda environment. We used a conda environment with <mark>python 3.9</mark>. To create such an environment simply add the `python=3.9` at the end when creating the environment.

### Backend Setup
Make sure you are in your correct environment then run these commands.

Install flask
```
pip install flask
pip install flask_restful
pip install flask_cors
```

Other necessary installs
```
pip install tensorflow==2.11.*
pip install pandas
pip install -U scikit-learn
pip install matplotlib
```

This should be all the prerequisites for the backend.


### Frontend setup

Make sure npm is installed
```
sudo apt install npm
```

Then enter the frontend folder of the project
```
cd frontend
```
And run

```
npm install
```

This should be all the prerequisites for the frontend.

## Starting the application

If the setup is done properly then this is the only thing you have to do every time you wish to start the application.

### Starting the Backend

Backend uses Flask, which is a simple web framework written in Python. The backend application file is 'app.py' inside 'backend' folder. Change directories using:

Make sure you are in the `backend` folder and in the `correct environment` then run this command

```
FLASK_APP=app.py flask run
```

If the above doesn't work for some reason, you can also try running this:

```
python3 -m flask run
```

&nbsp;

### Starting the Frontend

In a <mark>new terminal</mark> Make sure you are in the `frontend` folder then run this command
```
npm start
```

### Using the application
The application should now be available for you through localhost. Enter any browser with the url at port 3000
[localhost:3000](http://localhost:3000)