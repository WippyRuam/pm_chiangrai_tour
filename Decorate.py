import numpy as np 
import pandas as pd 

df19 = pd.read_csv("Data/PM2.5(2019).csv")
df20 = pd.read_csv("Data/PM2.5(2020).csv")
df21 = pd.read_csv("Data/PM2.5(2021).csv")
df22 = pd.read_csv("Data/PM2.5(2022).csv")
df23 = pd.read_csv("Data/PM2.5(2023).csv")


df_con = pd.concat([df19.loc[:,("Date","73T")],df20.loc[:,("Date","73T")],
                    df21.loc[:,("Date","73T")],df22.loc[:,("Date","73T")],
                    df23.loc[:,("Date","73T")]],axis=0)

df_con = pd.concat([df19.loc[:, ["Date", "73T", "22T"]],
                    df20.loc[:, ["Date", "73T", "22T"]],
                    df21.loc[:, ["Date", "73T", "22T"]],
                    df22.loc[:, ["Date", "73T", "22T"]],
                    df23.loc[:, ["Date", "73T", "22T"]]], axis=0, ignore_index=True)

df = df_con.dropna()
