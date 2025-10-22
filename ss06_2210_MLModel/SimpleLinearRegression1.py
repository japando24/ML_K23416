import numpy as np
from matplotlib import pyplot as plt

x = np.array([[1,2,3,4,5,6, 7, 8, 9, 10]]) . T
y = np.array([[2,4,3,6,9,12,13,15,18, 20]]) . T

def calculateB1B0(x,y):
    #Average
    xbar = np.mean(x)
    ybar = np.mean(y)
    x2bar = np.mean(x**2)
    xybar = np.mean(x*y)

    #B0 &  B1
    b1 = (xbar * ybar - xybar) / (xbar **2 - (x2bar))
    b0 = ybar - b1 * xbar
    return b1, b0

#Calculate b1, b0
b1, b0 = calculateB1B0(x,y)
print("B1 = ",b1)
print("B0 = ",b0)
y_pred = b1*x + b0
print("y_pred = ",y_pred)

def showGraph (x,y,y_pred, title="",xlabel="",ylabel=""):
    plt.figure(figsize=[14,8])
    plt.plot(x,y,'r-o',label="value sample")
    plt.plot(x,y_pred,'b-*',label="predicted value")
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    # Mean y
    ybar = np.mean(y)

    plt.axhline(ybar, linestyle="--", linewidth=4, label="mean")
    plt.axis([x_min*0.95,x_max*1.05,y_min*0.95,y_max*1.05])
    plt.xlabel(xlabel,fontsize=16)
    plt.ylabel(ylabel,fontsize=16)
    plt.text(x_min,ybar*1.01,"mean",fontsize=16)
    plt.legend(fontsize=15)
    plt.title(title,fontsize=20)
    plt.show()

showGraph(x,y,y_pred,
          title = "Value Y follow X",
          xlabel = "Value of X",
          ylabel = "Value of Y")