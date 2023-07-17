import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
DIS=pd.read_csv("DIS.csv")
x=np.linspace(2,13356,13356)
plt.plot(x,DIS['Close'])
plt.ylabel('Closing price')
plt.title('Value of DIS stock over time')
plt.savefig("Value of DIS over time.jpeg")
