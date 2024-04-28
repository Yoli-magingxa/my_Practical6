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

#Histogram, visualize how many goals scored per match in 2020
goals_per_match = df['Goals per match']
size = 365

plt.hist(goals_per_match)
plt.tittle("Histogram that shows the goaling performance of the team in 2020")
plt.xlabel("Goals per match")
plt.ylabel("Frequency")

#Bar chart that compares the goals and the own goals 
own_goals = df["Own goals"]
self_scored_goals = df["Goals"]

plt.figure(figsize=(12,6))
plt.bar(own_goals,self_scored_goals)
plt.xlabel("Own goals")
plt.ylabel("Self Scored goals")
plt.show()

#Pie chart showiing different ways of how the  goals were scored for the first match of Arsenal
goals= ['Own goals','Goals with right foot', 'Goals with left foot','pernalty scored']
scores = [1,4,3,0]

plt.figure(figsize=(7,7)
plt.pie(scores,label=goals,autput = '%1.1f%%',startangle=140)
plt.tittle('Different types of goals scored')
plt.show()
