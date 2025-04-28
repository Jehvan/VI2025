import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

def read_file(filename):
    with open (filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset

if __name__ == '__main__':
    dataset = read_file('car.csv')
    encoder = OrdinalEncoder()
    encoder.fit([row [: -1] for row in dataset])

    train_set = dataset[:int(len(dataset)*0.7)]
    train_x = [row [: -1] for row in train_set]
    train_y = [row [-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(len(dataset)*0.7):]
    test_x = [row[: -1] for row in test_set]
    test_y = [row [-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)

    accuracy = 0

    for i in range(len(test_set)):
        predictions = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predictions == true_class:
            accuracy += 1
    print(accuracy / len(test_set))

    entry = [el for el in input().split(' ')]
    print(entry)
    entry = encoder.transform([entry])
    print(entry)


    print(classifier.predict(entry))