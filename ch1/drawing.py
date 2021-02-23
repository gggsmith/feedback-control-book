import matplotlib.pyplot as plt
import numpy as np

class Drawing:
    def __init__(self, data):
        self.data = data
        self.fig = plt.figure()
        self.fig.set_size_inches(15,10)
        self.axes = self.fig.add_axes([0,0,1,1])

    def xy(self, xi, yi, fmt="-", label="", color="black"):
        self.axes.plot(self.data[:,xi], self.data[:,yi], fmt, label=label, color=color)

    def trend(self, xi, yi, power=10, label="Trend", color="blue"):
        z = np.polyfit(self.data[:,xi], self.data[:,yi], power)
        p = np.poly1d(z)
        self.axes.plot(self.data[:,xi], p(self.data[:,xi]), label=label, color=color)
    
    def labels(self, xlabel, ylabel):
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)

    def draw(self):
        self.axes.legend()
        plt.show()

