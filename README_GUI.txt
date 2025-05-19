GUIUniApp

GUI Files:  
    GUI_main_app.py:
        This is the main file to run the application.
        It controls switching between the login, view subjects, and manage subjects windows.
    GUI_login_view.py:
        Shows the login screen where students enter their email and password.
        Handles the login process and shows success or error messages.
    GUI_view_subjects_view.py:
        Shows after a student logs in. Displays the list of currently enrolled subjects.
        Has a button to go to the "Manage Subjects" screen and a "Logout" button.
    GUI_manage_subjects_view.py:
        Allows students to add (enrol) new subjects and remove (drop) existing ones from their list.
        Has a button to go back to the "View Subjects" screen.

How to Run:
- Run gui_main_app.py. 
(Typically, you would open a terminal, navigate to the file's directory, ensure all gui_*.py files
 and other necessary files like student.py, subject.py, database.py, students.json are present, 
 and type python gui_main_app.py)