from matplotlib import pyplot as plt
import numpy as np
import math

pas = 0.01
nb = 1000
t=np.linspace(0,nb*pas,nb)
A=2*np.cos(t)

precision = 3

figure = plt.figure("")
subplot = figure.add_subplot(111)
plt.plot(t,A)


lastPoint = None
lastText = None

def distance2D(p1,p2):
    X = p2[0]-p1[0]
    Y = p2[1]-p1[1]
    return(math.sqrt(  ((X)**2) + ((Y)**2))   )

def find_closest(arr, x,y):
    arrCoord = map( lambda tupl: ( t[tupl[0]],tupl[1] ), enumerate(arr))
    arrDistance = list(map(lambda coord: distance2D(coord, (x,y)), arrCoord))

    mini = 0
    for i, e in enumerate(arrDistance):
        if(e <= arrDistance[mini]):
            mini = i

    return(mini)



def event_mouse(event):
    global lastPoint
    global lastText

    x,y = event.xdata, event.ydata
    if(x is None or y is None):
        return

    index_mini = find_closest(A,x,y)
    # print(index_mini)
    print("Coords x:{x} y:{y}".format(x=t[index_mini],y=A[index_mini]) )

    if(lastPoint):
        lastPoint.remove()
        lastText.remove()
        del lastPoint

    lastPoint, = plt.plot(t[index_mini], A[index_mini],"ro")
    lastText = subplot.annotate("x:{x}\ny:{y}".format(x=round(t[index_mini],precision),y=round(A[index_mini],precision)), xy=(t[index_mini], A[index_mini]))
    plt.draw()



figure.canvas.mpl_connect('button_press_event', event_mouse)
plt.show()
plt.close('all')
