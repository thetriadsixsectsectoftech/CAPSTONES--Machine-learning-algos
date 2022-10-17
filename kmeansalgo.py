
import csv
import numpy as np
import matplotlib.pyplot as plt


#################################################################################
#notes
    #the k in k means is a free variable
    #and in the algorithm k can be determined
    # k in the dataset will be used to determine K random points which are to be considerd
    #centers of the number of the chosen k clusters/also know as centriods
    #the distance refers to how far the data points are from their  centriods
    #"adjust centriods so that they are the gravity for a given cluster"
    #these re - adjustments are done until the data points stop switching clusters
    # i understand k in this example to be 3 beacuse there are three featuers to this data set
        #countries,birth rate and life expectancy
    # there is also a method in order to determine a good k number
        #sum of squared errors



#################################################################################


##################################################################EQUIVILANT OF MAIN FUNCRION BELOW############################################################

def DriverCode(filename, clusterCount, IterationCount):
    # The code reads in a CSV file and creates a list of random clusters.

          
    CSVDATA = datareaderfunc(filename)
    RandomCluster = np.random.choice(len(CSVDATA),clusterCount)
    # RandomCluster = np.random.choice(len(CSVDATA),clusterCount) This line creates a random number between 1-clusterCount (the maximum number of clusters).
#  Then it uses this random number to choose one out of len(CSVData)-1 (the total amount of rows in our dataset).
#  So if RandomCluster was chosen at 2, then there would be two clusters created - one with 3 countries and another with 4 countries; or if RandomCluster was chosen at 5, then there would be five clusters


    centroids =[]
    for index in RandomCluster:
      centroids.append(CSVDATA[index])
    # It then iterates through the list of clusters, assigning each cluster's centroids to new_centroids.

    for centroidposition in range(IterationCount):
      assign_centroids = centroid_func(CSVDATA,centroids)
      #It then randomly chooses a cluster of countries to analyze, and assigns each country's centroid as its own data point.

      new_centroids =[np.mean(assign_centroids[centroid],axis=0) for centroid in assign_centroids.keys()]
      #The code iterates through all of the countries in that cluster, calculating their mean life expectancy and birth rate for that cluster.

      centroids = new_centroids

    final_cluster_data = centroid_func(CSVDATA,centroids)

    

    for centroidposition in range(len(centroids)):
      print(f"Number of countries in cluster with centroid {centroids[centroidposition]} = {len(final_cluster_data[centroidposition])}")

    data =[]
    with open(filename) as DataFile:
        reader = csv.DictReader(DataFile, delimiter=',')
        for row in reader:
          data.append(list(row.values()))

    for centroidposition in range(len(centroids)):
      print(f"\nCountries in cluster with centroid {centroids[centroidposition]}\n")

      for cluster in final_cluster_data[centroidposition]:
        country = [values[0] for values in data if values[1]==str(cluster[0]) and values[2] == str(cluster[1])]
        if len(country)>0:

          print(country[0]) 

    for centroidposition in range(len(centroids)):
      print(f"The mean Life Expectancy and Birth Rate for cluster with centroid {centroids[centroidposition]} = {round(np.mean(final_cluster_data[centroidposition],axis=0)[1],3)},{round(np.mean(final_cluster_data[centroidposition],axis=0)[0],3)}")


    ##################################################################EQUIVILANT OF MAIN FUNCRION Above ############################################################





################################################################ FUNCION ONE ###########################################################################################
# Define a function that reads data in from the csv files  

def datareaderfunc(combinedData):
  with open(combinedData) as FileOne:
    readFile = csv.DictReader(FileOne, delimiter=',')
    dataList =[]
    # The code reads a CSV file and then creates an empty list called dataList.

    for row in readFile:
      dataList.append(row)
      #The code then iterates through the rows of the CSV file, appending each row to the list.

  listDict = [list(dictionary.values())[1:] for dictionary in dataList]
    #After that, it takes each value in the list and converts it into a list of dicts with one element for each column in the original data set.

  listvals = [list(map(float,value)) for value in listDict]
  # The list of dictionaries will be used to create a list of lists which is then used to create a list of floats.

  return listvals
################################################################ FUNCION ONE ###########################################################################################



################################################################ FUNCION Two ###########################################################################################

# Define a function that finds the closest centroid to each point out of all the centroids
    #The code iterates through the list of data points
    #The code then stores this information into a dictionary called "centriodDict".

def centroid_func(data,centroids):

  centriodDict = {}
  for DataPoint in range(len(centroids)):
    centriodDict[DataPoint] = []


  for lastIndex in data:
    distance = []

    for DataPoint in centroids:
      distance.append(distantFunc(np.array(lastIndex),np.array(DataPoint)))
      #  This calculation returns two values: one representing how far away from another coordinate on our 2-dimensional plane we are = Ec_dist(np.array(i)
        #    and one representing how close we are relative to them (in terms of their position on our 2-dimensional plane). = np.array(DataPoint)

    centriodDict[np.argmin(distance)].append(lastIndex)
    # np.argmin() to find the index of the smallest value in the list  "distance", which is then used as an index into "centriodDict" to store that value's coordinates.
    #The last item in this list is then assigned as being equal to lastIndex, which is the index for that particular point.


  return centriodDict
    #Finally, it returns the smallest value from all these distances as its result.
################################################################ FUNCION Two ###########################################################################################



# Define a function that computes the distance between two data points
def distantFunc(pointOne, PointTwo):

    return(np.sum((pointOne - PointTwo)**2))**0.5
        #np sum
            # Sum of array elements over a given axis
            # params are both arrays





############################## KMEANS START ###############################################
filename = 'data1953.csv'
clusterCount = int(input("Please enter the number of Clusters "))

IterationCount = int(input("Please enter the number of iterations "))
DriverCode(filename, clusterCount, IterationCount)
############################## KMEANS START ###############################################
