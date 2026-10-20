grades = {"History": [92,93,80], "English": [82,94,87], "Math": [97,93,89], "Science": [92,91,88]}
def main():
    print("hello")
    print(grades)
    addGrade("Art", 92)
    print(grades)

    print_average("Science")

    print_grades("Science")

#Function takes in a class and grade, and adds the grade to the class if it already in the dictonary and if not, adds the class to the dict then the grade
def addGrade(subject, grade):
    if grades.get(subject, -1) == -1:
        grades.update({subject: [grade]})
    else:
        grades.get(subject).append(grade)

#Function takes in a class and prints the average grade
def print_average(subject):
    average = 0
    for grade in grades.get(subject):
        average = average + grade
    average = average / len(grades.get(subject))
    print(average)

def print_grades(subject):
    for grade in grades.get(subject):
        print(grade)
    





if __name__ == '__main__':
    main()