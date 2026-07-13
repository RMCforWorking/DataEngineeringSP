def sortList(e):
    return e[1]

def sortare(lista):
    # sortare
    lista.sort(reverse=True, key=sortList)
    print(lista)

def avg(lista):
    a=0.0
    for student in lista:
        a+=student[1]

    print('\navgrageul este')
    avrg=a/len(lista)
    print(round(avrg,1))

def numerotare(i):
    if i == 1:
        return '1st'
    if i == 2:
        return '2nd'
    if i == 3:
        return '3rd'
    return f"{i}th"

def rank(lista):
    print('\nClasamentul este: \n')
    for index, student in enumerate(lista,start=1):
        print(f"{numerotare(index)} {student[0]} cu scorul {student[1]}")


if __name__ == '__main__':
    students = [('Alice',92),('Bob',88),('Carol',74),('Dave',55),('Eve',61),('Frank',95),('Grace',48)]

    sortare(students)

    #cei care au trecut
    print('\nStudentii trecuti sunt')
    for student in students:
        if student[1]>=60:
            print(student)

    #lowest and highest score
    print('\nPrimul si ultimul')
    print(students[0])
    print(students[-1])

    avg(students)

    rank(students)

