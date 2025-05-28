import os

from sklearn.ensemble import RandomForestClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset_script
from zad2_dataset import dataset
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset_script
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
# Vashiot kod tuka
    indeks = int(input())
    drva = int(input())
    criteria = input()
    vlez = input().split()
    vlez = [int(el) for el in vlez]
    vlez = vlez[:indeks] + vlez[indeks + 1:]
    dataset = [row[:indeks] + row[indeks + 1:] for row in dataset]
    train_set, test_set = dataset[:int(0.85 * len(dataset))],dataset[int(0.85 * len(dataset)):]
    train_x, train_y = [row [:-1] for row in train_set], [row [-1] for row in train_set]
    test_x, test_y = [row [:-1] for row in test_set], [row [-1] for row in test_set]
    classifier = RandomForestClassifier(n_estimators=drva,criterion=criteria,random_state=0)
    classifier.fit(train_x, train_y)

    accuracy = 0.0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        if predicted_class == test_y[i]:
            accuracy += 1
    print('Accuracy:', accuracy / len(test_set))
    prediction = classifier.predict([vlez])[0]
    print(prediction)
    print(classifier.predict_proba([vlez])[0])

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
# i klasifikatorot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
#    submit_train_data(train_x, train_y)

# submit na testirachkoto mnozestvo
#    submit_test_data(test_x, test_y)

# submit na klasifikatorot
#    submit_classifier(classifier)
