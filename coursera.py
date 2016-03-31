import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv('~/Downloads/titanic.csv', index_col='Survived')
new = pandas.DataFrame(data, columns=['Pclass', 'Fare', 'Age', 'Sex'])
new = new.dropna()
new = new.replace({'Sex': {'male': True, 'female': False}})
y = new.index
X = new.values
clf = DecisionTreeClassifier(random_state=241)
clf.fit(X, y)
importances = clf.feature_importances_
print(new.head())
print(importances)
