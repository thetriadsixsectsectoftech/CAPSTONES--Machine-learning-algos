import matplotlib.pyplot as plt
import numpy as np 
from sklearn.datasets import load_diabetes

def Getdata():
    dataset=load_diabetes()

    datafeatuers = dataset.data[:, np.newaxis, 2]
    #newaxis is generally used with slicing. It indicates that you want to add an additional dimension to the array


    # Split the data into training/testing sets

    datafeatuertraining = datafeatuers[:-20]
    dataresultstraining = dataset.target[:-20]
    ### training sets for the featuers and targets/results

    datafeatuertest = datafeatuers[-20:]
    datatargettest = dataset.target[-20:]
     ### testing sets for the featuers and targets
    usemodel(datafeatuertraining,dataresultstraining,datafeatuers,datafeatuertest,datatargettest) #2
        #par 1 and two of this function calll are going to be used in the linear regfunc #3


def usemodel(datafeatuertrainingset,dataresultstrainingset,datafeatuers,datafeatuertest,datatargettest):
    #prediction
    finalform,linearmodelresult=Linear_Regression(datafeatuertrainingset,dataresultstrainingset)#3 returns #  finalform,linearmodelresul
    predictionPoint = linearmodelresult+finalform*datafeatuers
    #######################################################################################

    plotData(datafeatuertrainingset,dataresultstrainingset,datafeatuers,datatargettest,predictionPoint,datafeatuertest)

def plotData(datafeatuertrainingset,dataresultstrainingset,datafeatuers,datatargettest,predictionPoint,datafeatuertest):
    #plotting data
    plt.scatter(datafeatuertrainingset,dataresultstrainingset,c='r')
    plt.scatter(datafeatuertest,datatargettest,c='g')
    plt.plot(datafeatuers,predictionPoint,c='b')
    plt.show()

def Linear_Regression(datafeatuers,dataresults):
  datafetuersmean = np.mean(datafeatuers)
  #Compute the arithmetic mean along the specified axis.
    #Returns the average of the array elements. 
    #the first paremeter of this function is an Array containing numbers whose mean is desired.

  datatrainingmean=np.mean(dataresults)

  finalform = np.dot(np.transpose(datafeatuers-datafetuersmean),dataresults-datatrainingmean) /np.dot(np.transpose(datafeatuers-datafetuersmean),datafeatuers-datafetuersmean)
  # np.dot = Returns the dot product of a and b.
  #a being the a modified permuteated array // # np.transpose = Reverse or permute the axes of an array; returns the modified array.
  # b being an array 
    
    #Algebraically, the dot product is the sum of the products of the corresponding entries of the two sequences of numbers. (sounds like arrays)
      
#If a and b are both scalars or both 1-D arrays then a scalar is returned; otherwise an array is returned

# so formula 1 & 2 contain the value obtained by multiplying each pair of arrays and then adding the individual totals.



  



  

  linearmodelresult = datatrainingmean-finalform*datafetuersmean
  return [finalform,linearmodelresult]

Getdata() # 1


