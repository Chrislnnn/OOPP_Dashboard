import sqlite3

class StudentRepository:
    # Methode zum Initialisieren der Datenbank und den darin vorhanden Tabellen (wurde beim ersten Starten aufgerufen, damit die study_database.db erstellt wurde)
    def initialize_database(self):
        # Eine Datenbank muss erstellt werden
        conn = sqlite3.connect('study_database.db')
        # Ein Cursor wird benötigt
        cursor = conn.cursor()
        # Table für Studenten erstellen
        cursor.execute("""CREATE TABLE students (
                                                  student_surname text,
                                                  student_lastname text,
                                                  student_id integer,
                                                  study text,
                                                  semester integer,
                                                  semester_start_date DATE,
                                                  semester_end_date DATE)""")
        # Table für aktuelle Kurse erstellen
        cursor.execute("""CREATE TABLE courses (
                                      course_name text,
                                      course_description text,
                                      course_grade integer,
                                      course_examination text)""")
        # Table für abgeschlossene Kurse erstellen
        cursor.execute("""CREATE TABLE finished_courses (
                                      course_name text,
                                      course_description text,
                                      course_grade integer,
                                      course_examination text)""")
        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

    def reset_database(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Einträge aus den Tabellen entfernen
        cursor.execute("DELETE FROM students")
        cursor.execute("DELETE FROM courses")
        cursor.execute("DELETE FROM finished_courses")

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()


    def save_student(self, student, study, semester):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Daten vom Studenten und den Studiengang einpflegen
        cursor.execute(
            "INSERT INTO students VALUES (:student_surname, :student_lastname, :student_id, :study, :semester, :semester_start_date, :semester_end_date)",
            {
                'student_surname': student.surname,
                'student_lastname': student.lastname,
                'student_id': student.id,
                'study': study.name,
                'semester': semester.semester,
                'semester_start_date': semester.start.isoformat(),
                'semester_end_date': semester.end.isoformat()
            })

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

    def get_all_student_records(self):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Daten aus finished courses auswählen
        cursor.execute("SELECT *, oid FROM students")
        records = cursor.fetchall()

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return records


    def get_semester_data(self, student_id):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Alle Daten extrahieren
        cursor.execute("SELECT semester, semester_start_date, semester_end_date FROM students WHERE student_id = ?",(student_id,))
        semester_data = cursor.fetchone()

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

        return semester_data

    def update_semester(self, semester, start, end, student_id):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        # Datenbankeintrag aktualisieren
        cursor.execute("""UPDATE students SET semester = ?, semester_start_date = ?, semester_end_date = ? WHERE student_id = ?""",(semester, start.isoformat(), end.isoformat(), student_id))

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()

    def update_student(self, surname, lastname, student_id):
        # Datenbank öffnen
        conn = sqlite3.connect('study_database.db')
        # Cursor erstellen
        cursor = conn.cursor()

        cursor.execute("""UPDATE students SET student_surname = ?, student_lastname = ? WHERE student_id = ?""",(surname, lastname, student_id))

        # Änderungen speichern
        conn.commit()
        # Schließen der Verbindung
        conn.close()




