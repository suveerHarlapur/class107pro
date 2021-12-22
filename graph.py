import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("data.csv")
mean = df.groupby(["id", "level"], as_index=False)["attempt"].mean()
print(mean)
fig = px.scatter(mean, x="id", y="level", size="attempt", color="attempt")
fig.show()