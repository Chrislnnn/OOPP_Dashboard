import tkinter
from tkinter import ttk
from DashboardView import DashboardView
from StudentRepository import StudentRepository
from LoginController import LoginController
from StudentController import StudentController

class LoginView(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard Projekt")
        self.student_repoository = StudentRepository()
        self.student_controller = StudentController()
        self.controller = LoginController(self)
        self.dashboard = DashboardView(self)
        self.login_page.pack(fill="both", expand=True)

    def show_new_user_form(self):
        # Definierte Auswahl an möglichen Studiengängen (der einfachheit halber nur 2)
        # Diese werden die voreingestellten Kurse im Dashboard beeinflussen
        courses_of_study = ["Software Engineering", "Mathematics"]

        # Login-Seite
        self.login_page = tkinter.Frame(self)
        self.login_page.pack(fill="both", expand=True)
        tkinter.Label(self.login_page, text="Willkommen! Du kannst hier dein neues Dashboard erstellen.").grid(
            row=0, column=0, columnspan=2, pady=20, padx=20)

        # Eingabefeld für den Vornamen
        surname_label = tkinter.Label(self.login_page, text="Vorname: ")
        surname_label.grid(row=1, column=0, pady=10, padx=20)
        self.surname_input = tkinter.Entry(self.login_page, width=30)
        self.surname_input.grid(row=1, column=1, pady=10, padx=20)

        # Eingabefeld für den Nachnamen
        lastname_label = tkinter.Label(self.login_page, text="Nachname: ")
        lastname_label.grid(row=2, column=0, pady=10, padx=20)
        self.lastname_input = tkinter.Entry(self.login_page, width=30)
        self.lastname_input.grid(row=2, column=1, pady=10, padx=20)

        # Auswahl vom Studiengang mit drop box
        studies_label = tkinter.Label(self.login_page, text="Studiengang: ")
        studies_label.grid(row=3, column=0, pady=10, padx=20)
        self.studies_drop_box = ttk.Combobox(self.login_page, values=courses_of_study)
        self.studies_drop_box.current(0)
        self.studies_drop_box.grid(row=3, column=1, pady=10, padx=20)

        # Button zum Erstellen des Dashboards
        create_dashboard_button = tkinter.Button(self.login_page, text="Dashboard erstellen",command=lambda: self.controller.init_dashboard(self.surname_input.get(), self.lastname_input.get(), self.studies_drop_box.get()))
        create_dashboard_button.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="ew")


    def show_exisiting_user(self, student, study, semester):
        # Login-Seite
        self.login_page = tkinter.Frame(self)
        self.login_page.pack(fill="both", expand=True)
        tkinter.Label(self.login_page, text="Willkommen zurück!").grid(row=0, column=0, columnspan=2, pady=20,
                                                                       padx=20)

        # Eingabefeld für den Vornamen
        surname_label = tkinter.Label(self.login_page, text="Vorname: " + student.surname)
        surname_label.grid(row=1, columnspan=2, pady=10, padx=20)

        # Eingabefeld für den Nachnamen
        lastname_label = tkinter.Label(self.login_page, text="Nachname: " + student.lastname)
        lastname_label.grid(row=2, columnspan=2, pady=10, padx=20)

        # Auswahl vom Studiengang mit drop box
        studies_label = tkinter.Label(self.login_page, text="Studiengang: " + study.name)
        studies_label.grid(row=3, columnspan=2, pady=10, padx=20)

        # Button zum Bearbeiten von persönlichen Informationen
        create_dashboard_button = tkinter.Button(self.login_page, text="Persönliche Informationen anpassen",
                                                 command=lambda: self.student_controller.open_update_window(student, self))
        create_dashboard_button.grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

        # Button zum Erstellen des Dashboards
        create_dashboard_button = tkinter.Button(self.login_page, text="Zum Dashboard",
                                                 command=lambda: self.controller.open_dashboard(student, study, semester))
        create_dashboard_button.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

        # Button zum Zurücksetzen des Dashboards (dies wird auch den Namen und Studiengang löschen)
        reset_dashboard_button = tkinter.Button(self.login_page, text="Alles zurücksetzen",
                                                command=lambda: self.controller.reset_all())
        reset_dashboard_button.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="ew")


    def restart_app(self):
        # Aktuelles Fenster schließen und erneut starten
        self.destroy()
        app = LoginView()
        app.mainloop()

    def open_dashboard(self, student, study, semester):
        self.dashboard = DashboardView(self)
        # Die initialize-Methode in der Klasse Dashboard wird aufgerufen
        self.dashboard.initialize(student, study, semester)
        # Alle anderen Seiten schließen
        self.login_page.pack_forget()
        # Dashboard verpacken
        self.dashboard.pack(fill="both", expand=True)


# Es soll immer zuerst die Login-Seite gestartet werden bei der Ausführung
if __name__ == "__main__":
    app = LoginView()
    app.mainloop()