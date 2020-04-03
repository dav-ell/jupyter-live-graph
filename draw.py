import matplotlib.pyplot as plt

class Draw(object):
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        plt.ion()
        self.fig.show()
        self.fig.canvas.draw()
    
    def graph(self, y):
        self.ax.clear()
        self.ax.plot(y)
        self.fig.canvas.draw()
