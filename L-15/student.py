print("Welcome to the student data organizer!")

student = {}

while True:

    print("Select an option:")
    print("1. Add Students")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects offered")
    print("6. Exit")

    choice = input("Enter Your Choice (1 - 6)!!!! : ")
    if choice == "1":

        try:

            std_id = int(input("Enter Student ID : "))
            name = input("Enter Student Name : ")
            age = input("Enter Student Age : ")
            grade = input("Enter Student Grade : ")
            dob = input("Enter Student DOB (YYYY-MM-DD) : ")
            subjects = input("Enter Student Subject : ").split(",")

            student[std_id] = ( name , age , grade , dob , subjects )

            print("Studnt Added Successfully!!")

        except:

            print("Invalid Input , Please try again..")

    elif choice == "2":

            if len(student) == 0:
                print("No student record found!")
            else:
                for std_id , data in student.items():
                    print(f"Student id : {std_id}")
                    print(f"Student Name : {data[0]}")
                    print(f"Student Age : {data[1]}")
                    print(f"Student Grade : {data[2]}")
                    print(f"Student dob : {data[3]}")
                    print(f"Student Subject : {','.join(data[2])}")