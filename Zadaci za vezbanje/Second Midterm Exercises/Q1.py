import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB
# Script imported from FINKI courses
from dataset_script import dataset

if __name__ == '__main__':
    c = int(input())
    p = int(input())
    new_dataset = []
    for row in dataset:
        row[0] = row[0] + row[-2]
        new_row = row[0:-2] + row[-1:]
        new_dataset.append(new_row)
    dataset = new_dataset

    class_good, class_bad = [], []
    for row in dataset:
        if row[-1] == 'good':
            row[-1] = 1
            class_good.append(row)
        elif row[-1] == 'bad':
            row[-1] = 0
            class_bad.append(row)

    if c == 0:
        class_good_train = class_good[:int(len(class_good) * (p/100))]
        class_good_test = class_good[int(len(class_good) * (p/100)):]
        class_bad_train = class_bad[:int(len(class_bad) * (p/100))]
        class_bad_test = class_bad[int(len(class_bad) * (p/100)):]

    else:
        class_good_train = class_good[int(len(class_good) * (100 - p)/100):]
        class_good_test = class_good[:int(len(class_good) * (100 - p)/100)]
        class_bad_train = class_bad[int(len(class_bad) * (100 - p)/100):]
        class_bad_test = class_bad[:int(len(class_bad) * (100 - p)/100)]

    train_set = class_good_train + class_bad_train
    test_set = class_good_test + class_bad_test

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]


    classifier_nonScaled = GaussianNB()
    classifier_nonScaled.fit(train_x, train_y)

    print("Tochnost so zbir na koloni:", classifier_nonScaled.score(test_x, test_y))

    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_x)
    train_x = scaler.transform(train_x)
    test_x = scaler.transform(test_x)

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    print("Tochnost so zbir na koloni i skaliranje:", classifier.score(test_x, test_y))
