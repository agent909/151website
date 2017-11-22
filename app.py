import models
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from form import addstudent,search
from config import database

app = Flask(__name__)

@app.route('/testing')
def exp():
    # form = search(request.form)
    return render_template("exp.html")


@app.route('/')
def index():
    form = search(request.form)
    return render_template("index.html")

@app.route('/addstudent', methods=['GET','POST'])
def student():
    form = addstudent(request.form)

    if request.method == 'POST':
        print("INSIDE SECOND CON")
        idk = models.db(form.firstname.data, form.middlename.data, form.lastname.data, form.gender.data, form.course.data)
        idk.register()
        return render_template("index.html")
    return render_template("addstudent.html", form=form)



@app.route('/updatestudent/<string:id>', methods=['GET','POST'])
def updatestudent(id):
    form = addstudent(request.form)

    if request.method == 'POST':
        firstname = form.firstname.data
        middlename = form.middlename.data
        lastname = form.lastname.data
        gender = form.gender.data
        course_id = form.course.data

        cur = database.cursor()
        cur.execute("UPDATE Student SET firstname='"+firstname+"', middlename='"+middlename+"', lastname='"+lastname+"', gender='"+gender+"', course_id="+str(course_id)+" WHERE student_id="+id+";")
        database.commit()
        cur.close()

        #present changes
        # return render_template("successupdate.html")
        return 'SUCCESS UPDATE'


    cur = database.cursor()
    cardinality = cur.execute("SELECT * FROM Student WHERE student_id="+id+";")
    if cardinality == 0:
        cur.close()
        return 'STUDENT DOES NOT EXIST'

    student = cur.fetchone()
    cur.close()

    form.firstname.data = student[0]
    form.middlename.data = student[1]
    form.lastname.data = student[2]
    form.gender.data = student[3]
    form.course.data = student[5]



    return render_template("addstudent.html", form=form)


# @app.route('/search', methods=['GET'])
# def searchstudent()
#         form = search(request.form)



if __name__ == "__main__":
    app.secret_key='whatataps'
    app.run(debug=True)
