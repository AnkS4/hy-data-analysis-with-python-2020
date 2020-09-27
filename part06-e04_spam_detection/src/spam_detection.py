#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def spam_detection(random_state=0, fraction=1.0):
	with gzip.open('src/spam.txt.gz', 'rb') as f:
		file_content = f.readlines()
	spam = file_content[:int(0.1 * len(file_content))]
	with gzip.open('src/ham.txt.gz', 'rb') as f:
		file_content = f.readlines()
	ham = file_content[:int(0.1 * len(file_content))]
	
	X = ham + spam
	vectorizer = CountVectorizer()
	X = vectorizer.fit_transform(X).toarray()
	
	y = np.zeros(len(X))
	y[len(ham):] = 1
	
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, train_size=0.75)
	model = MultinomialNB()
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)
	
	score = accuracy_score(y_test, y_pred)
	miss = (y_test != y_fitted).sum()
	#miss = int((1-score) * (len(y_pred)))
	return score, len(X_test), miss

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
