import subprocess
import numpy as np

class grapher(object):
    np = __import__('numpy')
    subprocess = __import__('subprocess')
    graphOutput = [] 					#a list of strings to store the graph in
    x = []						#a list to store 100 most recent X values in
    y = []    						#a list to sore 100 most recent Y values in
    graphSize = 100					#an integer defining the maximum number of data points to track
    							#set graphSize to the number of seconds of data you want displayed * 10 (b/c serial sends values at 10 hz)
    def __init__(self, y):
        for i in range(self.graphSize):
            self.x.append(i)
        self.y = y
        self.update(self.x,self.y)
        self.graphOutput = self.getGraph()
        
    def update(self, x, y, label='DMM'):									#reimplementation of update method to allow setting label
        self.x = x
        self.y = y
        self.gnuplot = subprocess.Popen(["/usr/bin/gnuplot"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.gnuplot.stdin.write("set term dumb 150 25\n")
        self.gnuplot.stdin.write("plot '-' using 1:2 title '" + label + "' with linespoints \n")
        for i,j in zip(x,y):
            self.gnuplot.stdin.write("%f %f\n" % (i,j))
        self.gnuplot.stdin.write("e\n")
        self.gnuplot.stdin.flush()
        i = 0
        output = []
        while self.gnuplot.poll() is None:
            output.append(self.gnuplot.stdout.readline())
            i+=1
            if i == 24:
                break
        self.graphOutput = output


    def getGraph(self):					#return a list of lines that when printed out show a graph
        return self.graphOutput

    def getValues(self):				#return a list of x,y value pairs (that are currently on the graph)
        return zip(self.x,self.y)

    def append(self, yVal):				#append a yValue to the graph
        if len(self.x) == len(self.y):			#if we already graphSize variables, then delete the oldest value and add the newest
            # tempX = self.x
            # tempY = self.y
            self.y = np.delete(self.y, 0)
            self.y = np.append(self.y, yVal)
        else:
            if len(self.x) > len(self.y):
                self.y = np.append(self.y, yVal)
        self.update(self.x, self.y)  

    def appendWithLabel(self, yVal,label):
        if len(self.x) == len(self.y):
            # tempX = self.x
            # tempY = self.y
            # self.y = np.delete(self.y, 0)
            self.y = np.append(self.y, yVal)
        else:
            if len(self.x) > len(self.y):
                self.y = np.append(self.y, yVal)
        self.update(self.x, self.y, label)
      