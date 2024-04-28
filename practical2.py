import matplotlib.pyplot as plt
import panda as pd
import numy as nm

df = pd.read_csv("C:/Users/cash/practical6/.git/")

#Histogram, visualize how many goals scored per match in 2020
goals_per_match = df['Goals per match']
size = 365

plt.hist(goals_per_match)
plt.tittle("Histogram that shows the goaling performance of the team in 2020")
plt.xlabel("Goals per match")
plt.ylabel("Frequency")