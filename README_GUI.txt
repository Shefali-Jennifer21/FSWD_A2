GUIUniApp

GUI Files:  
    main_app.py:
        This is the main file to run the application.
        It controls switching between the login and enrolment windows.
    login_view.py:
        Shows the login screen where students enter their email and password.
        Handles the login process and shows success or error messages.
    enrolment_view.py:
        Shows the enrolment screen after a student logs in.
        Allows students to add (enrol) or remove (drop) subjects.
        Displays the student's current subjects and shows messages for actions.
        Has a logout button.
How to Run:
- Place main_app.py, login_view.py, enrolment_view.py, and all other necessary Python files in the same folder.
    (like student.py, subject.py, your data handling file e.g., database.py, and students.json)
- Run : main_app.py