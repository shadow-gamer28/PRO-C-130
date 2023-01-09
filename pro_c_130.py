import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

df.to_csv('main.csv') 