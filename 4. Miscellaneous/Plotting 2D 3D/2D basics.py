import matplotlib.pyplot as plt
import numpy as np

#straight line plot
##x1 = [1,5,8]
##y1 = [4,12,6]
##
##x2 = [9,7,5]
##y2 = [2,4,6]
##
##plt.plot(x1,y1,'r')  #continous plot
##plt.scatter(x1,y1)
##
##plt.title('Info')
##plt.ylabel('Y-axis')
##plt.xlabel('X-axis')
##plt.grid()
##plt.show()

#Cosine plot
#Polynomial plot
##t = np.linspace(-5,5,100)
##
##f = lambda x : (x**3) - (2*(x**2)) + (2*x) + 5
##
##plt.plot(t,f(t))
##plt.grid()
##plt.show()

#Gaussian Surface plot
##x = np.linspace(-20,20,20)
##
##y = np.exp(-(x**2))
##
##plt.plot(x,y)
##plt.grid()
##plt.show()

#Sinc plot
##x = np.linspace(-20,20,2000)
##
##y = np.sinc(x)
##
##plt.plot(x,y)
##plt.grid()
##plt.show()

#advance use of linspace
##N = 8
##
##y = np.zeros(N)
##x1 = np.linspace(0, 10, N, endpoint=True)
##x2 = np.linspace(0, 10, N, endpoint=False)
##
##plt.plot(x1, y, 'o')            #at y = 0 (y is zero vector)
##plt.plot(x2, y + 0.5, 'o')      #at y = 0.5
##
##plt.ylim([-0.5, 1])
##plt.show()
