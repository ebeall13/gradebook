grades = {"History": [92,93,80], "English": [82,94,87], "Math": [97,93,89], "Science": [92,91,88]}
keys = list(grades.keys())
def main():


    ans = True
    while (ans):
        print("Hello! Which of these would you like to see ? (1,2,3,4 or 5) \n 1. Print out each class and your average grade in that class (and your best and worst subjects) \n 2. Print out all you grades in a specific class (will indicate later) \n 3. Print out your total GPA \n 4. Add to your grades \n 5. Exit")
        user_choice = int(input(""))
        nums = [1,2,3,4,5]
        while(user_choice not in nums ):
            user_choice = int(input("Please try again! enter a number 1-5"))
        if user_choice == 1:
            print_all_averages()
        elif user_choice ==2:
            class_name = input("Which class would you like to print your grades for?")
            while(class_name not in keys):
                class_name = input("Please try again! enter a class")
            print_grades(class_name)
        elif user_choice ==3:
            print("Your GPA is ", get_GPA())
        elif user_choice ==4:
            sub = input("Which subject would you like to add a grade to?")
            grade = int(input("What is the grade you would like to add?"))
            addGrade(sub,grade)
            print("Added!")
        elif user_choice ==5:
            ans = False

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

#The get_GPA method returns the users GPA on a 4.0 scale
def get_GPA():
    average = 0
    num = 0
    for key in grades:
        average = average + get_average(key)
        num = num +1
    gpa = average / num
    if (gpa >= 92.5):
        return 4.0
    elif (gpa >= 89.5):
        return 3.7
    elif (gpa >= 79.5):
        return 3.0
    elif (gpa >= 69.5):
        return 2.0
    elif (gpa >= 65):
        return 1.0
    else:
        return 0

if __name__ == '__main__':
    main()