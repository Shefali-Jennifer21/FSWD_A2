# Group 5 University System 

This is a University Student Management System developed in Python using Object-Oriented Programming (OOP) principles. The system supports both a command-line interface (CLI) and a graphical user interface (GUI). It allows students to register, log in, enrol in subjects, view or remove enrolled subjects, and update their passwords. Admin users can manage student records, including grouping students by grades, partitioning pass/fail results, and clearing the database. 


The project’s GUI component is composed of modular files, each handling a specific function, offering a user-friendly visual alternative to the CLI.

# Features 

### Student Functions
Students can register with a university email and a secure password, then log in to access their personalized course menu. From there, they can enrol in up to four subjects, remove any enrolled subjects if needed, view a list of their current subjects, and update their password—provided it meets the required security standards.

### Admin Functions
Administrators have access to tools that allow them to manage the student database efficiently. They can clear all student data, group students by their grades, separate students into pass or fail categories, remove specific students by ID, and display a complete list of all registered students.

### Password Requirements
To ensure account security, passwords must meet several criteria. A valid password must include at least one uppercase letter, at least one lowercase letter, and a minimum of three digits. It must also contain at least one special character from the set @ # $ & ! % *, and have at least five alphabetical letters in total. Additionally, the overall password length must be between 8 and 20 characters.

### Email Format
Student email addresses must follow the structure of a valid university domain format. Specifically, the email should be in the form of firstname.lastname@university.com, using only letters, periods, and hyphens before the "@" symbol. This ensures the identity and format are consistent across all student accounts.

# How to run the project (CLI Version)

**1.Ensure Python 3 is Installed**


Make sure that Python 3.x is installed on your system.

**2.Download or Clone the Repository**


Obtain the project files by downloading the ZIP archive from the repository.



**3.Verify Required Files Are Present**


Ensure the following essential files are in the project folder:
main.py


student.py


subject.py


admin.py


database.py


students.json (optional, will be created if not found)


**4.Run the Application**


Launch the system by executing the main Python file from the terminal: python main.py


**5. Interact with the Application**


Upon running, the program will prompt you to select between Admin and Student modes.


Choosing Admin will provide access to database management tools.


Choosing Student allows you to register, log in, manage subjects, and update your password.


# How to run the project (GUI Version)

The GUI offers a more user-friendly version of the student functions.


**1.Make sure you have all the required GUI files in the same directory:**

GUI_main_app.py

GUI_login_view.py

GUI_view_subjects_view.py

GUI_manage_subjects_view.py

As well as supporting files: student.py, subject.py, database.py, and students.json.

**2.Open your terminal and run:**


GUI_main_app.py


**3.This will launch the GUI-based system** 

Students can log in, view enrolled subjects, and manage their enrolments visually.


# Group Members 

Jisu Sim					      ID: 25687411 

Nattira Savetsila			  ID: 25633708

Yi Zhong					      ID: 13473804

Jennifer Raja Shankar		ID: 25002472

