"""Build a new web page to display the student grades prettytable from HW11 as a web page"""

import os
import sqlite3
from flask import Flask, render_template, redirect
from typing import Dict

app: Flask = Flask(__name__)

@app.route('/')
def index() -> str:
    """Redirect index to students page"""
    return redirect('/students')

@app.route('/students')
def student_summary() -> str:
    """ Query for Students Grades """
    db_path: str = "810_startup.db"

    try:
        db: sqlite3.Connection = sqlite3.connect(db_path)
    except sqlite3.OperationalError:
        return f'Error: Unable to open database at path {db_path}'
    else:
        query: str = "select students.Name, students.CWID, grades.Course, grades.Grade, instructors.Name from students,grades,instructors where students.CWID=StudentCWID and InstructorCWID=instructors.CWID order by students.Name"
        data: Dict[str, str] = [{'Name': name, 'CWID': cwid, 'Course': course, 'Grade': grade, 'Instructor': instructor} for name, cwid, course, grade, instructor in db.execute(query)]

        db.close()

        return render_template(
            'students.html',
                title = 'Stevens Repository',
                table_title = 'Students Summary',
                students = data)
    
app.run(debug=True)