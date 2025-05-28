import os
from zad2_dataset import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset_script
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset_script
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
# Vashiot kod tuka
    dataset_v2 = []
    for row in dataset:
        row_v2 = [float(el) for el in row]
        dataset_v2.append(row_v2)

    train_set = dataset_v2[:int(len(dataset_v2) * 0.85)]
    train_x = [row [: -1] for row in train_set]
    train_y = [row [-1] for row in train_set]

    test_set = dataset_v2[int(len(dataset_v2) * 0.85):]
    test_x = [row [: -1] for row in test_set]
    test_y = [row [-1] for row in test_set]
    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = 0
    prediction = classifier.predict(test_x)
    for gt_class, pred_class in zip(test_y, prediction):
        if gt_class == pred_class:
            accuracy += 1

    acc = accuracy_score(test_y, prediction)
    print(accuracy/len(test_set))

    entry = [int(el) for el in input().split(' ')]
    print(int(classifier.predict([entry])[0]))
    print(classifier.predict_proba([entry]))


# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
#    submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
#    submit_test_data(test_X, test_Y)

# submit na klasifikatorot
#    submit_classifier(classifier)
#    submit_encoder(encoder)
# povtoren import na kraj / ne ja otstranuvajte ovaa linija
