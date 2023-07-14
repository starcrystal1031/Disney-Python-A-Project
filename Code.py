import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
DIS=pd.read_csv("DIS.csv")
plt.savefig("DIS.png")
x=np.linspace(2,13356,13356)
plt.plot(x,DIS['Close'])
