grades = {"History": [92,93,80], "English": [82,94,87], "Math": [97,93,89], "Science": [92,91,88]}
def main():
    print("hello")
    print(grades)
    addGrade("Art", 92)
    print(grades)

def addGrade(subject, grade):
    if grades.get(subject, -1) == -1:
        grades.update({subject: [grade]})
    else:
        grades.get(subject).append(grade)







if __name__ == '__main__':
    main()