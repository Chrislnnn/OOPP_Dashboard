from tkinter import *

class StudentView(Toplevel):
    def __init__(self, parent, controller, student):
        super().__init__(parent)
        self.controller = controller
        self.student = student
        self.title('Persönliche Informationen anpassen')
        self.geometry('500x500')

        # Eingabefeld für den Vornamen
        surname_label = Label(self, text="Vorname: ")
        surname_label.grid(row=1, column=0, pady=10, padx=20)
        self.surname_input = Entry(self, width=30)
        self.surname_input.grid(row=1, column=1, pady=10, padx=20)

        # Eingabefeld für den Nachnamen
        lastname_label = Label(self, text="Nachname: ")
        lastname_label.grid(row=2, column=0, pady=10, padx=20)
        self.lastname_input = Entry(self, width=30)
        self.lastname_input.grid(row=2, column=1, pady=10, padx=20)

        info_label = Label(self, text="Neue Informationen werden erst nach einem Neustart korrekt angezeigt")
        info_label.grid(row=3, columnspan=2, pady=10, padx=20)

        # Buttom zum Speichern (ruft Methode im Controller auf)
        create_dashboard_button = Button(self, text="Speichern", command=lambda: self.controller.update_info(student, self.surname_input.get(), self.lastname_input.get()))
        create_dashboard_button.grid(row=4, columnspan=2, pady=10, padx=20)

    def display_info(self):
        # Fenster schließen
        saved_label = Label(self, text="Deine Angaben wurden gespeichert! Du kannst das Fenster nun schließen.")
        saved_label.grid(row=5, columnspan=2, pady=10, padx=20)