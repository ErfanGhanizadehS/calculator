Program Topic: Advanced Calculator with Storage Capability
Known Values: User's menu selection, input numbers from the user
Relationship: Performing mathematical operations and managing result lists
Solution Method:

First File: simple_calculater.py

This file contains the main program functions and menu:

Main Menu:

Power operation

Sum operation

Show lists

Remove item

Exit

Storage Lists:

Power results list

Sum results list

Available Functions:

Menu display function and user selection input

Power calculation function (first number to the power of second number)

Sum calculation function (addition of two numbers)

List display function

Item removal function from lists

Second File: simple_calculator_part_2.py

This file runs the main program:

The program runs in an infinite loop until the user selects option 5

Execution Details:

If user selects option 1:

Two numbers are received from the user

First number is raised to the power of the second number

Result is calculated and displayed

Result is added to the power list

If user selects option 2:

Two numbers are received from the user

Sum of two numbers is calculated

Result is calculated and displayed

Result is added to the sum list

If user selects option 3:

All lists with stored values are displayed

If user selects option 4:

User selects which list to remove from

Selected item is removed from the chosen list

If user selects option 5:

Program ends with goodbye message

If user enters invalid number:

Error message is displayed

