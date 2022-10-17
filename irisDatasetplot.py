import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def plotfunction(figuer,data,colours):
    


    figuer[0][0].scatter(data[:,0], data[:,1],c=colours)
    #The data positions = data[:,0] = x , y = data[:,1], c = array-like or list of colors or color, optional

    figuer[2][1].scatter(data[:,2], data[:,1],c=colours)
    figuer[2][2].scatter(data[:,2], data[:,3],c=colours)


    figuer[1][0].scatter(data[:,1], data[:,0],c=colours)
    figuer[1][1].scatter(data[:,1], data[:,2],c=colours)
    figuer[1][2].scatter(data[:,1], data[:,3],c=colours)


    figuer[2][0].scatter(data[:,2], data[:,0],c=colours)

    figuer[3][1].scatter(data[:,3], data[:,1],c=colours)
    figuer[3][2].scatter(data[:,3], data[:,2],c=colours)

    figuer[0][1].scatter(data[:,0], data[:,2],c=colours)
    figuer[0][2].scatter(data[:,0], data[:,3],c=colours)


    figuer[3][0].scatter(data[:,3], data[:,0],c=colours)


    plt.show() 


#############################################CODE BLOCK ONE############################################################

fig,plotOne = plt.subplots(4,3,figsize=(11,8)) 
#plotOne has 2 row, 1 columns, and this plot is the first plot.
##The figsize attribute allows us to specify the width and height of a figure in-unit inches.


iris = load_iris()
data = np.array(iris['data'])
# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
# the list being passed into np.array is the data from the iris dataset // print(type(iris['data']))

IrisFeatuers = np.array(iris['target'])
#In this dataset, there are 4 features sepal length, sepal width, petal length and petal width and the target variable has 3 classes namely ‘setosa’, ‘versicolor’, and ‘virginica’
 
colors = {0:'r',1:'b',2:"g"}
columndesign= np.array([colors[IrisFeatuers] for IrisFeatuers in IrisFeatuers])
# a enumerate type for loop to create the colour sccheme of the plot
#############################################CODE BLOCK ONE############################################################


plotfunction(plotOne,data,columndesign)

