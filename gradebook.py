grades = {"History": [92,93,80], "English": [82,94,87], "Math": [97,93,89], "Science": [92,91,88]}
def main():
    print("hello")
    print(grades)
    addGrade("Art", 92)
    print(grades)

    print_average("Science")

    print_grades("Science")
    print_all_averages()

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

#function that takes in a class and prints all the grades associated with it
def print_grades(subject):
    for grade in grades.get(subject):
        print(grade)
#helper method that returns the average of the input subject
def get_average(subject):
    average = 0
    for grade in grades.get(subject):
        average = average + grade
    average = average / len(grades.get(subject))
    return average

#function that prints your average in all subjects and then prints your worst and best subjects
def print_all_averages():
    
    low = next(iter(grades))
    high = next(iter(grades))

    for key in grades:
        print("In " , key , " you have a:")
        print_average(key)

        average = key
        if get_average(average) < get_average(low):
            low = average
        if get_average(average) > get_average(high):
            high = average
    print("Your best subject is " , high)
    print("Your worst subject is " ,low)


if __name__ == '__main__':
    main()