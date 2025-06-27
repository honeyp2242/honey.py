# Extract All Number Divisible by 3

# arr = [4 , 9 , 1 , 6 , 3 , 7 , 12]

# div_by_3 = [num for num in arr if num % 5 == 0]

# print(div_by_3)

# Accept user input for the array

# arr_input = input("Enter array Element seperated by space : ")

# arr = list(map(int , arr_input.split()))

# print(arr)

# # Array Program : Menu-Driven Array Operations

# print("Array Operation Program")
# print(f"{"=" * 25}")


# input by user

arr_input = input("Enter array Element seperted by space : ")
arr = []
arr = list(map(int , arr_input.split()))

while True:

     print("============== Menu ==============")
     print("1. Display Array")
     print("2. Reverse Array")
     print("3. sort Array in Ascending order")
     print("4. sort Array in Descending order")
     print("5. Search an Element")
     print("6. Remove an Element")
     print("7. Insert an Element")
     print("8. Exit")

     choice = int(input("Enter your choice (1 - 8): "))

     if choice == 1:
          print("Display Array:", arr)

     elif choice == 2:
          reverse_arr = list(reversed(arr))
          print("Reverse Array:", reverse_arr)

     elif choice == 3:
          sort_arr = sorted(arr)
          print("Sort Array in Ascending order:", sort_arr)

     elif choice == 4:
          print("sort Array in Descending order :" , sorted(arr , reverse=True))

     elif choice == 5:
          val = int(input("Enter your search element :"))

          if val in arr:
               print(f"{val} is available in array.")
          else:
               print(f"{val} is not found in array.")

     elif choice == 6:

          val = int(input("Enter delete element :"))

          if val in arr:
               arr.remove(val)
               print(f"{val} is deleted from array.")
          else:
               print(f"{val} is not found in array.")

     elif choice == 7:

          val = int(input("Enter insert element :"))

          pos = int(input("Enetr position of array :"))

          if 0 <= pos <= len(arr):
               arr.insert(pos , val)
               print("Updated Array :" , arr)

          else:

               print("position not valid!")

     elif choice == 8:

          print("Exit Successfully , Thank You 🤣")

     else:

          print("invalid Choice , Please Enter Right Choice (1 - 8)")
          
     # break