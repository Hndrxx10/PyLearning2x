#HW 1 Task #1 - Take a user input (name, age, roll_number, phone_number) and print the user details.
name=input("Enter Your Name:")
age=int(input("Enter Your Age:"))
roll_number=float(input("Enter Your Roll Number:"))
phone_number=int(input("Enter Your Phone Number:"))
print("Name:",name,"\n","Age:", age, "\n" "Roll Number:",roll_number,"\n","Phone Number:",phone_number)


#Task #2 - Print the Table of 2 by using the command print()

number = int(input("Enter the number of which the user wants to print the multiplication table: "))
print ("The Multiplication Table of: ", number)
for count in range(1, 20):
   print (number, 'x', count, '=', number * count)



