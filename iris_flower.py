#this is the program to show the implementation of Decision tree classifier with the help of iris flower

#import libraries
from sklearn.datasets import load_iris
import numpy
from sklearn.tree import DecisionTreeClassifier

#load dataset
iris=load_iris()
dir(iris)

print(iris.DESCR)

print(iris.data)

print(iris.feature_names)

print(iris.target)

print(iris.target_names)

#splitting of data into training and testing sets
x = [0,50,100]

target_training = numpy.delete(iris.target,x,axis=0)
print(target_training)
print(target_training.size)

data_training = numpy.delete(iris.data,x,axis=0)
print(data_training)
print(data_training.size)


test_target = iris.target[x]
print(test_target)

test_data = iris.data[x]
print(test_data)

#Decision tree classifier algorithm
clf = DecisionTreeClassifier()
trained = clf.fit(data_training, target_training)
output = trained.predict(test_data)
print(output)
