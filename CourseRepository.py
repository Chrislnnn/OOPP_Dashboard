import sqlite3

class CourseRepository:
    def insert_finished_course(self, course, grade):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Kurs aus den aktuellen Kursen entfernen
        cursor.execute("DELETE FROM courses WHERE course_name = ?", (course.name,))

        # Kurs in die abgeschlossenen Kurse einpflegen
        cursor.execute(
            "INSERT INTO finished_courses VALUES (:course_name, :course_description, :course_grade, :course_examination)",
            {
                'course_name': course.name,
                'course_description': course.description,
                'course_grade': grade,
                'course_examination': course.examination.name,
            })

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

    def get_course_data(self, name):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Daten extrahieren für die Eintragung in den Textfeldern
        cursor.execute("SELECT * FROM courses WHERE course_name = ?", (name,))
        course_details = cursor.fetchone()

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return course_details

    def add_new_course(self, name, description, examination):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Daten in die Datenbank einpflegen.
        # Der Einfachheit halber wurde dem Nutzer nicht erlaubt spezifische Angaben zur Klausur oder Projekt zu tätigen (bspw. die duration oder deadline), da sonst eine weitere Tabelle für die Prüfungsleistungen notwendig wäre
        # und die beiden Tabellen über einen Primary Key verbunden werden müssten
        cursor.execute(
            "INSERT INTO courses VALUES (:course_name, :course_description, :course_grade, :course_examination)",
            {
                'course_name': name,
                'course_description': description,
                'course_grade': None,
                'course_examination': examination
            })

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

    def get_all_active_courses(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle aktiven Kurse auswählen
        cursor.execute("SELECT *, oid FROM courses")
        active_courses = cursor.fetchall()

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return active_courses

    def get_all_finished_courses(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle abgeschlossenen Kurse auswählen
        cursor.execute("SELECT *, oid FROM finished_courses")
        finished_courses = cursor.fetchall()

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return finished_courses

    def get_finished_courses_count(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Anzahl der abgeschlossenen Kurse erhalten
        cursor.execute("SELECT COUNT(*) FROM finished_courses")
        finished_courses_count = cursor.fetchone()[0]

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return finished_courses_count

    def get_finished_courses_grades(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Noten erhalten
        cursor.execute("SELECT *, oid FROM finished_courses")
        finished_courses_grades = cursor.fetchall()

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return finished_courses_grades

    def get_all_course_data(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Noten erhalten
        cursor.execute("SELECT * FROM courses")
        courses_data = cursor.fetchall()

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return courses_data
