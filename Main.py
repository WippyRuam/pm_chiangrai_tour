import Decorate as dd
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


df = pd.read_csv("Data/TourPM.csv")

x = df.iloc[:,[85,84]]
y = df.iloc[:,[46]]

x = sm.add_constant(x)

fit = sm.OLS(y,x).fit()

print(fit)

c = df.iloc[:,[85]]/10
r = df.iloc[:,[46]]/10000000
a = df.iloc[:,[84]]
y = (pd.to_datetime(df['Year']))


plt.plot(y, c, label='PM')
plt.plot(y, r, label='Revernue CR')
plt.plot(y, a, label='Argiculature')

plt.title('test1')
plt.xlabel('Year')
plt.ylabel('Values')

plt.legend()
plt.show()



