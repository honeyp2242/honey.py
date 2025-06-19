# Initialize user list
users = []

# Start main loop
while True:
    print("\nCRUD Operation in Python!!!!")
    print("1. create user")
    print("2. read user")
    print("3. update user")
    print("4. delete user")
    print("5. exit")

    choice = input("Enter your Choice(1-5): ")

    # CREATE
    if choice == "1":
        try:
            user_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            users.append({"id": user_id, "name": name, "age": age})
            print("User added successfully.")
        except ValueError:
            print("Invalid input. ID and Age must be numbers.")

    # READ
    elif choice == "2":
        if not users:
            print("No users found.")
        else:
            print("User List:")
            for user in users:
                print(f"ID: {user['id']}, Name: {user['name']}, Age: {user['age']}")

    # UPDATE
    elif choice == "3":
        try:
            user_id = int(input("Enter update user ID: "))
            found = False
            for user in users:
                if user["id"] == user_id:
                    field = input("Enter field to update (name/age): ").lower()
                    if field == "name":
                        user["name"] = input("Enter new name: ")
                        print("Name updated successfully.")
                    elif field == "age":
                        user["age"] = int(input("Enter new age: "))
                        print("Age updated successfully.")
                   
                    found = True
                    break
                if not found:
                  print("User not found.")
        except ValueError:
            print("Invalid input. Please enter numbers for ID and age.")

    # DELETE
    elif choice == "4":
        try:
            user_id = int(input("Enter ID to delete user: "))
            new_users = [user for user in users if user["id"] != user_id]
            if len(new_users) == len(users):
                print("User not found.")
            else:
                users = new_users
                print("User deleted successfully.")
        except ValueError:
            print("Invalid input. ID must be a number.")

    # EXIT
    elif choice == "5":
        print("Program exit successfully.")
        break

    # INVALID CHOICE
    else:
        print("Invalid choice. Please select a number from 1 to 5.")