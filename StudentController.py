from StudentRepository import StudentRepository
from StudentView import StudentView
from tkinter import messagebox

class StudentController:
    def __init__(self):
        self.view = None
        self.student_repository = StudentRepository()

    def open_update_window(self, student, login):
        self.view = StudentView(login, self, student)

    def update_info(self, student, new_surname, new_lastname):
        # Warnung, wenn Eingabe fehlt
        if not new_surname or not new_lastname:
            messagebox.showinfo("Eingabe fehlt", "Bitte geben deinen/einen Namen an!")
            return

        student.surname = new_surname
        student.lastname = new_lastname

        # Informationen in der Datenbank abspeichern
        self.student_repository.update_student(student.surname, student.lastname, student.id)
        # Nutzer informieren
        self.view.display_info()

