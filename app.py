import models
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from form import addstudent,search
from config import database

app = Flask(__name__)


@app.route('/')
def index():
    form = search(request.form)
    return render_template("index.html")

@app.route('/addstudent', methods=['GET','POST'])
def student():
    form = addstudent(request.form)

    if request.method == 'POST':
        idk = models.db(form.firstname.data, form.middlename.data, form.lastname.data, form.gender.data, form.course.data)
        idk.register()
        return render_template("student_added.html")
    return render_template("addstudent.html", form=form)


@app.route('/updatestudent', methods=['GET','POST'])
def update():
    form = search(request.form)

    if request.method == 'POST':
        src = str(form.find.data)
        cur = database.cursor()

        a = "WHERE (firstname LIKE '"+src+"%' OR middlename LIKE '"+src
        b = "%' OR lastname LIKE '"+src+"%' OR student_id LIKE '"+src+"%')"+" AND student.course_id=course.course_id"
        query = "SELECT firstname,middlename,lastname,gender,student_id,course.course FROM student,course "+str(a)+str(b)
        cur.execute(query)

        result = cur.fetchall()
        cur.close()

        return render_template('search.html', form=form, students=result)

    return render_template('search.html', form=form)

@app.route('/delete/<string:id>', methods=['GET','POST'])
def delete(id):
    cur = database.cursor()
    cur.execute("DELETE FROM student WHERE student_id="+id+";")
    database.commit()
    cur.close()
    return render_template('delete.html')


@app.route('/updatestudent/<string:id>', methods=['GET','POST'])
def updatestudent(id):
    print(id)
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
        return render_template('student_updated.html')

    cur = database.cursor()
    cur.execute("SELECT *FROM student WHERE student_id="+id+";")
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
