import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import VAR

# https://www.kaggle.com/gunhee/amdgoogle/data
amd_df = pd.read_csv('vector_auto_regression/AMD.csv')
googl_df = pd.read_csv('vector_auto_regression/GOOGL.csv')

print("\n\namd_df shape:")
print(amd_df.shape)
print("googl_df shape:")
print(googl_df.shape)


def make_volume_df(s_1: pd.DataFrame, s_2: pd.DataFrame):
    df = pd.DataFrame()
    df['Volume_1'] = s_1['Volume']
    df['Volume_2'] = s_2['Volume']
    date = s_1['Date']
    date = pd.to_datetime(date)
    df = df.set_index(date)
    # index = pd.date_range(start='2000', periods=2335, freq='A')
    # print(index)
    # df = df.set_index(index)
    return df


# https://machinelearningmastery.com/time-series-data-stationary-python/
volume_df = make_volume_df(amd_df, googl_df)
volume_np = volume_df.to_numpy()
result = adfuller(volume_np[:, 0])
print(result)

# stationarity test fail
# try using difference to pass stationarity test
volume_df = volume_df.diff().dropna()
print(volume_df)

# stationary check needed to be done!!!
# using augmented dickey-fuller test
volume_np = volume_df.to_numpy()
print(volume_np[:, 0])
print(volume_np)
result = adfuller(volume_np[:, 0])
print("\nVolume_1 result: ")
print(result)
result = adfuller((volume_np[:, 1]))
print("\nVolume_2 result: ")
print(result)
# stationarity test success

model = VAR(volume_df)
result = model.fit(maxlags=15, ic='aic')
print(result.summary())

print(type(result))

# result.plot()
print(result.test_causality('Volume_1', 'Volume_2', kind='wald').summary())
print(result.test_causality('Volume_2', 'Volume_1', kind='f').summary())

result.plot_acorr()
plt.show()
