# It is basically a project to Learn how the ML models are trained and used in websites to predict outcomes in real time

# the things we did 

1. Load the data set 
2. Perform EDA on dataset to handle missing values... 
3. Go through the entire dataset to find relations within the dependent and independent features ...  
4. Split the data in two halfs ... X_train, X_test, y_train,y_test
5. Perform standardization on independent features to scale features on the same scale ...
6. fit the model using specified Ml model ... 
7. for predicting the model with x_test .. only transform the data with previous fitted scaler 
8. use performance metrics to check the model ... if performs well .. use scatter plot or see the y_pred , y_test in graph to analyse the dataset ...

once tested and predicted your model is ready for unseen data ... test it with unseen data 

... 
Now Pickle the model to file ( serialize it to byte stream so that this already trained model can be used anywhere without training it again and again....)


# create a new env whenver starting project..

python3 -m venv myenv

python3 -m venv → Command to create virtual environment
myenv → Name of your virtual environment folder (you can name it anything)

# Activate the env

source myenv/bin/activate


# name the tools or dependices or framwworks required for this project to requirements.txt

and then .... 
in terminal

pip install -r requirements.txt


# create a Flask Application and frontend 

load the model and predict with data coming from frontend ..
