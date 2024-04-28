import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/cash/practical6/.git/")
# Summary of the dataset 
print(df.describe())
#Identifying any columns and rows with mising values 
missing_values = df.isnull().sum()
print("There are : " , missing_values , " missing values in each column ")
duplicated_rows = df.duplicate().sum()
print("The number of the duplicated entries is : ", duplicated_rows)
#Accessing the column labels of the DataFrame \
columns = df.columns
#Displaying the columns of the DataFrame
print("The columns of the dataFrame are: ", columns)
#Counting the number of elements in DataFrame : rows, columns & missing values 
no_of_elements = df.size
print("The total number of all the elements in a DataFrame is: ", no_of_elements)
#Shape of the DataFrame 
shape = df.shape
print("The shape of the dataFrame : " , shape)
#Data visualization: Scatter plot, Histogram, Bar graph & Pie Chart

#Scatter 
#Accessing the values of each column in a DataFrame 
wins = df['Wins']
losses = ['Losses']

plt.scatter(wins,losses)
plt.tittle("Wins vs Losses of the Football team")
plt.xlabel("wins")
plt.ylabel("Losses")
plt.show()


