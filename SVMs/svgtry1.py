from sklearn import svm
from sklearn import datasets
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC(C=1)
print clf.fit(X, y)
print clf.predict([[2., 2.]])
print clf.predict([[0., 0.]])
print clf.support_vectors_
print clf.support_
print clf.n_support_
digits = datasets.load_digits()
print digits.data
clf = svm.SVC(C=100)
print clf.fit(digits.data[:-1], digits.target[:-1])
# SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
#   gamma=0.001, kernel='rbf', max_iter=-1, probability=False,
#   random_state=None, shrinking=True, tol=0.001, verbose=False)