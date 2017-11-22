from config import database
from wtforms import Form, StringField, RadioField, SelectField, validators, SubmitField
from flask_wtf import FlaskForm


class addstudent(FlaskForm):
    cur = database.cursor()
    cur.execute("SELECT *FROM Course;")
    courses = cur.fetchall()
    cur.close()

    choices =[]
    for data in courses:
        choices+=[(data[1], data[0]),]

    firstname = StringField('firstname',[validators.Length(min=1,max=100, message="min 1 max 100")])
    middlename = StringField('middlename',[validators.Length(min=1,max=100, message="min 1 max 100")])
    lastname = StringField('lastname',[validators.Length(min=1,max=100, message="min 1 max 100")])
    gender = RadioField('Gender',choices=[('m','Male'),('f','Female')])
    course = SelectField('Branches', choices=choices)
    submit = SubmitField('Add')

class search(FlaskForm):
    find = StringField('search', [validators.Length(min=1,max=100, message="requires 1 - 100 characters")])
