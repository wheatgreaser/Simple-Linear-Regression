import sklearn
from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit([[0, 1] , [2 , 3], [4, 5], [5, 6]], [0, 1 ,2 ,3])
print(reg.coef_)
print(reg.predict([[2, 3]]))


