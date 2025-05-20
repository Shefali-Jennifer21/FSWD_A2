# FSWD_A2

Group 5 University System 

Group Members 
Jisu Sim					      ID: 25687411 
Nattira Savetsila			  ID: 25633708
Yi Zhong					      ID: 13473804
Jennifer Raja Shankar		ID: 25002472

Introduction 
A console-based university student management system developed in Python using Object-Oriented Programming (OOP). This system allows students to register, log in, enrol in subjects, view and remove subjects, and update their passwords. Admins can manage student records with options to group, partition, and clear data.

Project Structure 

main.py:
Main control file (contains menu and logic)

main.py feature:

Student

1. Regiter (r)
   
Students can register using a valid university email (firstname.lastname@university.com) and a secure password. Password requirements include:At least one uppercase letter, At least one lowercase letter, At least three digits, At least one special character (@ # $ & ! % *), At least five letters total and Password length: 8–20 characters

2.Login (l)

Students can log in using their email and password.

3.Course Menu (c/e/r/s/x)

After login, students can:

e: Enrol in new subjects (up to 4)

r: Remove (drop) enrolled subjects by ID

s: View their current subject list

c: Change password

x: Exit to the main menu

Admin

1.Admin Menu (c/g/p/r/s/x)

Accessible by choosing "Admin" in the main menu:

c: Clear all student data 

g: Group students by grade

p: Partition students by pass/fail

r: Remove a student by ID

s: Show all registered students

x: Exit admin mode

student.py:
Contain Student class and related validations

subject.py: 
Contain Subject class

admin.py:
Contain Admin class with admin functions

database.py:
Handles reading and writing student data

students.data: 
Binary file to store student information

