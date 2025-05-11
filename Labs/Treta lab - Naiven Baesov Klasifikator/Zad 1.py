import os
from zad1_dataset import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset

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
    encoder.fit([row for row in dataset])
    train_set = dataset[:int(len(dataset)*0.75)]
    train_x = [row [: -1] for row in train_set]
    train_y = [row [-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(len(dataset)*0.75):]
    test_x = [row [: -1] for row in test_set]
    test_y = [row [-1] for row in test_set]
    test_x = encoder.transform(test_x)
    classifier = CategoricalNB()

    classifier.fit(train_x, train_y)
    accuracy = 0
    for i in range(len(test_set)):
        prediction = classifier.predict([test_x[i]])[0]
        if prediction == test_y[i]:
            accuracy += 1
    print(accuracy/len(test_set))

    entry = [el for el in input().split(' ')]
    encoded_entry = encoder.transform([entry])
    print(classifier.predict(encoded_entry)[0])
    print(classifier.predict_proba(encoded_entry))


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
