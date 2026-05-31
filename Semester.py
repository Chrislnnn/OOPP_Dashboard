from datetime import date
from dateutil.relativedelta import relativedelta
from StudentRepository import StudentRepository

class Semester:
    def __init__(self, semester, start_date):
        self.semester = semester
        self.start = start_date
        self.end = self.start + relativedelta(months=6)

    def update_semester(self, student_id):
        today = date.today()
        student_repository = StudentRepository()

        semester_data = student_repository.get_semester_data(student_id)
        current_semester = semester_data[0]
        start_date_string = semester_data[1]
        end_date_string = semester_data[2]

        # Das jeweilige Datum ist in der Datenbank als String gespeichert und muss somit wieder umgewandelt werden
        start_date_db = date.fromisoformat(start_date_string)
        end_date_db = date.fromisoformat(end_date_string)

        # Nach 6 Monaten soll das nächste Semester starten
        if today <= end_date_db:
            self.semester = current_semester
            self.start = start_date_db
            self.end = end_date_db
            # Datenbankeintrag muss aktualisiert werden
            student_repository.update_semester(self.semester, start_date_db, end_date_db, student_id)

