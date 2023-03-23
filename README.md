# MOL3022 Project - Protein Secondary Structure Prediction Using Machine Learning

## About the application:

The application takes in a protein sequence of a length up to 128 amino acids and predicts the secundary structure of the protein. The application uses a Neural Network (machine learning) to make perdications. There are two parts to the application: [frontend](#frontend) and [backend](#backend). The backend was written in Python, and consists of a trained model and a simple web framework (Flask). The frontend was written using React (TypeScript), and is used to as a "communicator" between the user and the prediction model by providing a simple user-friendly user interface. 

---------

&nbsp;

## Setup

### Frontend

The frontend application can be found in the 'mol3022' folder. Run the following command to change the directory:

```
cd mol3022
```

Install npm:

```
sudo apt install npm
```

Install dependencies:

```
npm install
```

Finally, to run the frontend application, run the following command:
```
npm start
```

&nbsp;

### Backend

Backend uses Flask, which is a simple web framework written in Python. The backend application file is 'app.py'.

Remember to install Flask (possible flask_restful and flask_cors too) by running the following commands:

```
pip install flask
pip install flask_restful
pip install flask_cors
```

Run the application like this:

```
FLASK_APP=app.py flask run
```

If the above doesn't work for some reason, you can also try running this:

```
python3 -m flask run
```