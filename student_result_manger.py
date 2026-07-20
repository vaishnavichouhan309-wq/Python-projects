student = {}
FILE_NAME = "student.txt"

while True:
    print("\n ------STUDENT RESULT MANAGER APP--------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Student")
    print("4. Exit")


    choice = input("Enter student choice : ")

#Add Student

    if choice == "1":
        name = input("Enter Student name: ")
        marks = int(input("Enter marks :"))
        student[name] = marks     # {NAME : MARKS}

        #save to file
        with open(FILE_NAME,"a")as f:
            f.write(f"{name},{marks}\n")

        print(f"{name} Sucessfully Added .")

#view student
    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as f:
                data = f.readlines()
                if not data:
                    print("No Student Found!")
                else:
                    for line in data:
                        name, marks = line.strip().split(",")
                        print(name, ":", marks)
        except FileNotFoundError:
            print("No Student File Found!")
    
#check Result
    elif choice == "3":
        name = input("Enter student name : ")
        found = False
        try:
            with open(FILE_NAME, "r") as f:
                for line in f:
                    s_name, s_marks = line.strip().split(",")
                    if s_name == name:
                        found = True
                        marks = int(s_marks)
                        if marks >= 40:
                            print("PASS")
                        else:
                            print("FAIL")
                        break
            if not found:
                print("Student Not Found!")
        except FileNotFoundError:
            print("No Student File Found!")
#exit
    elif choice == "4":
        print("Exiting......")
        break
    
  
    else:
        print("Invalid input")

  