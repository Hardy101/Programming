import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv('C02 Emission/data/FuelConsumptionRating.csv', encoding= 'ISO-8859-1')

# Custom DataFrame
cdf = df[['Engine size (L)', 'Cylinders', 'CO2 emissions (g/km)']]

viz = cdf[['Engine size (L)', 'Cylinders', 'CO2 emissions (g/km)']]
viz.hist()
plt.show()
# print(cdf.head(11))