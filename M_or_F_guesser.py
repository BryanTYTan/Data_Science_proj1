from sklearn import tree
from sklearn import linear_model
from sklearn import svm


# [Height, Weight, Shoe Size]
x = [[183,85,44], [170,70,43], [160,60,40], [145,55,40], [180,60,45], [190,80,46], [165,69,43], [173,66,39], [184,71,37], [165,65,44], [185,59,42], [166,76,39]]

y = ['male','female','female','female','male','male','female','female','male','female','male','female']
Y = [1,0,0,0,1,1,0,0,1,0,1,0]

# Tree Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
print(clf.predict([[190,70,45]]))

# Bayesian Classifier
clf2 = linear_model.BayesianRidge()
clf2.fit(x,Y)
pred = clf2.predict([[190,70,45]])
if pred[0] >= .5:
    print("male")
else:
    print("female")

# Support Vector Machines
clf3 = svm.SVC()
clf3.fit(x,y)
pred2 = clf3.predict([[190,70,45]])
print(pred2)