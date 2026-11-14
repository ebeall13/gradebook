grades = {"History": [92,93,80], "English": [82,94,87], "Math": [97,93,89], "Science": [92,91,88]}
import csv
csv_N = 'gradebook/grades.csv'

def main():
    ans = True
    gradebook = { }
    
    try:
        with open(csv_N, 'r') as f:
            data = csv.reader(f)
            for row in data:
                if row:
                    key = row[0]
                    values = row[1:]
                    gradebook[key] = values
            print(gradebook)

    except FileNotFoundError:
        print("no file found")  


    while (ans):
        keys = list(gradebook.keys())
        data = gradebook.copy()
        print("Hello! Which of these would you like to see ? (1,2,3,4 or 5) \n 1. Print out each class and your average grade in that class (and your best and worst subjects) \n 2. Print out all you grades in a specific class (will indicate later) \n 3. Print out your total GPA \n 4. Add to your grades \n 5. Exit")
        user_choice = int(input(""))
        nums = [1,2,3,4,5]
        while(user_choice not in nums ):
            user_choice = int(input("Please try again! enter a number 1-5"))
        if user_choice == 1:
            print_all_averages(data)
        elif user_choice ==2:
            print("Current classes: ")
            print_subs(data)
            class_name = (input("Which class would you like to print your grades for?")).lower()
            while(class_name not in keys):
                class_name = (input("Please try again! enter a class")).lower()
            print_grades(class_name, data)
        elif user_choice ==3:
            print("Your GPA is ", get_GPA(data))
        elif user_choice ==4:
            sub = (input("Which subject would you like to add a grade to?")).lower()
            grade = int(input("What is the grade you would like to add?"))
            addGrade(sub , grade, data)
            print("Added!")
        elif user_choice ==5:
            ans = False

#Function takes in a class and grade, and adds the grade to the class if it already in the dictonary and if not, adds the class to the dict then the grade
def addGrade(subject, grade, data):
    if data.get(subject, -1) == -1:
        data.update({subject: [grade]})
    else:
        data.get(subject).append(grade)

#Function takes in a class and prints the average grade
def print_average(subject, data):
    average = 0
    for grade in data.get(subject):
        average = average + int(grade)
    average = average / len(data.get(subject))
    print(average)

#function that takes in a class and prints all the grades associated with it
def print_grades(subject, data):
    for grade in data.get(subject):
        print(grade)
#helper method that returns the average of the input subject
def get_average(subject, data):
    average = 0
    for grade in data.get(subject):
        average = average + int(grade)
    average = average / len(data.get(subject))
    return average

#function that prints your average in all subjects and then prints your worst and best subjects
def print_all_averages(data):
    low = next(iter(data))
    high = next(iter(data))

    for key in data:
        print("In " , key , " you have a:")
        print_average(key, data)

        average = key
        if get_average(average, data) < get_average(low, data):
            low = average
        if get_average(average, data) > get_average(high, data):
            high = average

    print("Your best subject is " , high)
    print("Your worst subject is " ,low)

#The get_GPA method returns the users GPA on a 4.0 scale
def get_GPA(data):
    average = 0
    num = 0
    for key in data:
        average = average + get_average(key, data)
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
    
#function that prints all the classes the user has
def print_subs(data):
    for sub in data:
        print(sub)

#function that edits the added data to the csv file
def edit_csv(data):
    try:
        with open(csv_N, 'w', newline= "") as file:
            writer = csv.writer(file)
            for key, value in data.items():
                writer.writerow([key, value])
                print("successfully stored in csv")
    except FileNotFoundError:
        print("no file found")  




if __name__ == '__main__':
    main()