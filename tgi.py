import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class newTGI():
    fig = None
    field = None

    recent = None

    data = []
    graphs = []

    def __init__(self, MDmode=False, recent=20, darkmode=False):
        self.recent = recent

        self.fig = plt.figure()

        if MDmode:
            self.field = self.fig.add_subplot(111, projection='3d')
        else:
            self.field = self.fig.add_subplot()
        

        if darkmode:
            plt.style.use('dark_background')
        
        self.fig.show()

    def update(self):
        
        while len(self.field.lines) > 0:
            self.field.lines.pop(0)

        for x in range(len(self.graphs)):
            if self.graphs[x][1] is None:
                self.field.plot(self.data[x], c='b')
            # elif self.graphs[x][1] is 1:
                # self.field.scatter(self.data[x][0], self.data[x][1], c='y', s=0.1)
                # self.graphs[x][1].set_ydata(self.data[x])
        

        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def plotLines(self, id, data):
        i = None
        for x in range(len(self.graphs)):
            if self.graphs[x][0] is id:
                i = x
        
        if i is not None:
            self.data[i] = data
        else:
            self.data.append(data)
            self.graphs.append([id, None])
    
    def plotAppendLines(self, id, value):
        i = None
        for x in range(len(self.graphs)):
            if self.graphs[x][0] is id:
                i = x
        
        if i is not None:
            print(self.data[i])
            self.data[i].append([value])
            print(self.data[i])
            # if self.recent is not None: #TODO
            #     print(self.data[i].shape)
            #     if self.recent < self.data[i].shape[i]:
            #         self.data[i] = np.delete(self.data[i], 0)
        else:
            self.data.append([[value]])
            self.graphs.append([id, self.field.plot(self.data[len(self.data)-1])[0]])

    def plotDots2D(self, id, data):
        i = None
        for x in range(len(self.graphs)):
            if self.graphs[x][0] is id:
                i = x
        
        if i is not None:
            self.data[i] = data
        else:
            self.data.append(data)
            self.graphs.append([id, 1])
        
        for x in range(len(self.graphs)):
            if self.graphs[x][0] is id:
                i = x

        self.field.scatter(self.data[i][0], self.data[i][1], c='y', s=0.001)
    
    def plotDots3D(self, id, data):
        i = None
        for x in range(len(self.graphs)):
            if self.graphs[x][0] is id:
                i = x
        
        if i is not None:
            self.data[i] = data
        else:
            self.data.append(data)
            self.graphs.append([id, 1])
        
        for x in range(len(self.graphs)):
            if self.graphs[x][0] is id:
                i = x

        self.field.scatter(self.data[i][0], self.data[i][1], self.data[i][2], c='y', s=0.1)

    def playSound(self):
        pass
