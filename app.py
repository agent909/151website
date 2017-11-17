import models
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from form import addstudent

app = Flask(__name__)


@app.route('/')
def index():
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



@app.route('/updatestudent/<int:id>', methods=['GET','POST'])
def updatestudent(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Student WHERE id="+str(id)+";")

    student = cur.fetchone()

    form = student(request.form)
    form.firstname.data = student[0]
    form.middlename.data = student[1]
    form.lastname.data = student[2]
    form.gender.data = student[3]
    form.course.data = student[5]

    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        middlename = form.middlename.data
        lastname = form.lastname.data
        gender = form.gender.data
        course_id = form.course.data

        cur.execute("UPDATE Student SET firstname="+firstname+" middlename="+middlename+" lastname="+lastname+" gender="+gender+" course_id="+course_id+";")
        mysql.connection.commit()
        cur.commit()

        #present changes
        return render_template("successupdate.html")

    return render_template("addstudent.html", form=form)


if __name__ == "__main__":
    app.secret_key='whatataps'
    app.run(debug=True)
