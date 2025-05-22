import os

from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset
from zad1_dataset import dataset
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
           ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
           ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
# Vashiot kod tuka
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    procent = int(input()) / 100.0
    criteria = input()
    train_set = dataset[int(procent * len(dataset)):]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)
    test_set = dataset[:int(procent * len(dataset))]
    test_x = [row [:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)
    classifier = DecisionTreeClassifier(criterion=criteria, random_state=0)
    classifier.fit(train_x, train_y)

    print("Depth:",classifier.get_depth())
    print("Number of leaves:", classifier.get_n_leaves())

    accuracy = 0.0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        if predicted_class == test_y[i]:
            accuracy += 1
    print("Accuracy:", accuracy/len(test_set))

    features_importance = list(classifier.feature_importances_)
    print("Most important feature:", features_importance.index(max(features_importance)))

    print("Least important feature:", features_importance.index(min(features_importance)))



# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
#    submit_train_data(train_x, train_y)

# submit na testirachkoto mnozestvo
#    submit_test_data(test_x, test_y)

# submit na klasifikatorot
#    submit_classifier(classifier)

# submit na encoderot
#    submit_encoder(encoder)
