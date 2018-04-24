from matplotlib import pyplot as plt
import numpy as np
import math

class Inspector:
    def __init__(self, x, y, precision=3, displayOptions=""):
        self.x, self.y = x,y
        self.precision = precision
        self.displayOptions = displayOptions

        self.lastPoint = None
        self.lastText = None

        self.figure  = plt.figure("")
        self.subplot = self.figure.add_subplot(111)

        self.figure.canvas.mpl_connect('button_press_event', self.event_mouse)
        plt.plot(self.x,self.y,self.displayOptions)
        plt.show()

    @staticmethod
    def distance2D(p1,p2):
        X = p2[0]-p1[0]
        Y = p2[1]-p1[1]
        return(math.sqrt(  ((X)**2) + ((Y)**2))   )

    def find_closest(self, x,y):
        arrCoord = map( lambda tupl: ( self.x[tupl[0]],tupl[1] ), enumerate(self.y))
        arrDistance = list(map(lambda coord: Inspector.distance2D(coord, (x,y)), arrCoord))

        mini = 0
        for i, e in enumerate(arrDistance):
            if(e <= arrDistance[mini]):
                mini = i

        return(mini)

    def event_mouse(self,event):

        x,y = event.xdata, event.ydata
        if(x is None or y is None):
            return

        index_mini = self.find_closest(x,y)
        # print(index_mini)
        print("Coords x:{x} y:{y}".format(x=self.x[index_mini],y=self.y[index_mini]) )

        if(self.lastPoint):
            self.lastPoint.remove()
            self.lastText.remove()
            del self.lastPoint

        self.updateDisplay(index_mini)

    def updateDisplay(self, n):
        self.lastPoint, = plt.plot(self.x[n], self.y[n],"ro")
        self.lastText = self.subplot.annotate(
                                "x:{x}\ny:{y}".format(
                                    x=round(self.x[n],self.precision),
                                    y=round(self.y[n],self.precision)),
                                xy=(self.x[n], self.y[n]))
        plt.draw()


if(__name__=="__main__"):

    import numpy as np
    step=0.01
    nb=1000

    X=np.linspace(0,nb*step,nb)
    Y=2*np.cos(X)


    Inspector(X,Y)
    # Inspector(X,Y, precision=3, displayOptions="g")
    # Inspector(X,Y, precision=3, displayOptions="go")
    # Inspector(X,Y, precision=3, displayOptions="r+")

    if(False): # if user run this script as it, only show default behavior

        # You can use it in a Thread or a Process,
        # to avoid waiting for it to close,
        # or avoid to interfere with other pyplot
        from multiprocessing import Process
        import time
        process = Process(target=lambda : Inspector(X,Y, precision=3, displayOptions=""))
        process.start()
        time.sleep(4)
        process.terminate()



# pas = 0.01
# nb = 1000
# t=np.linspace(0,nb*pas,nb)
# A=2*np.cos(t)
#
# precision = 3
#
# figure = plt.figure("")
# subplot = figure.add_subplot(111)
# plt.plot(t,A)


# lastPoint = None
# lastText = None

# def distance2D(p1,p2):
#     X = p2[0]-p1[0]
#     Y = p2[1]-p1[1]
#     return(math.sqrt(  ((X)**2) + ((Y)**2))   )
#
# def find_closest(arr, x,y):
#     arrCoord = map( lambda tupl: ( t[tupl[0]],tupl[1] ), enumerate(arr))
#     arrDistance = list(map(lambda coord: distance2D(coord, (x,y)), arrCoord))
#
#     mini = 0
#     for i, e in enumerate(arrDistance):
#         if(e <= arrDistance[mini]):
#             mini = i
#
#     return(mini)



# def event_mouse(event):
#     global lastPoint
#     global lastText
#
#     x,y = event.xdata, event.ydata
#     if(x is None or y is None):
#         return
#
#     index_mini = find_closest(A,x,y)
#     # print(index_mini)
#     print("Coords x:{x} y:{y}".format(x=t[index_mini],y=A[index_mini]) )
#
#     if(lastPoint):
#         lastPoint.remove()
#         lastText.remove()
#         del lastPoint
#
#     lastPoint, = plt.plot(t[index_mini], A[index_mini],"ro")
#     lastText = subplot.annotate("x:{x}\ny:{y}".format(x=round(t[index_mini],precision),y=round(A[index_mini],precision)), xy=(t[index_mini], A[index_mini]))
#     plt.draw()


#
# figure.canvas.mpl_connect('button_press_event', event_mouse)
# plt.show()
# plt.close('all')
