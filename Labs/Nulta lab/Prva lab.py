import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def ocena(teorija, prakticno, lab):
    poeni = teorija + prakticno + lab
    if poeni % 10 == 0:
        return poeni // 10
    return poeni // 10 + 1


if __name__ == "__main__":
    students = {}
    while True:
        data = input()
        if data == "end":
            break

        ime, prezime, indeks, predmet, teorija, prakticno, lab = data.split(',')
        indeks = int(indeks)
        teorija = int(teorija)
        prakticno = int(prakticno)
        lab = int(lab)
        kluc = (ime, prezime, indeks)
        if kluc not in students:
            students[kluc] = [predmet + ": " + str(ocena(teorija, prakticno, lab))]
        else:
            students[kluc].append(predmet + ": " + str(ocena(teorija, prakticno, lab)))

    for student in students:
        print("Student: " + student[0] + " " + student[1])
        for predmet in students[student]:
            print("----" + predmet)
        print("")
