# from config import mysql

from config import database




class db(object):
    def __init__(self, firstname, middlename, lastname, gender, course):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.gender = gender
        self.course = course

    def register(self):
        # try:
            cur = database.cursor()
            cur.execute("INSERT INTO Student VALUES('" +self.firstname+ "','" +self.middlename+"','" +self.lastname+ "','"+self.gender+"',NULL,"+self.course+");")

            database.commit()
            cur.close()
            print("USED REGISTER")
            return
        # except:
        #     print("something went wrong")
        #     database.rollback()
        #     return 'ERROR: SOMETHING WENT WRONG IN THE DATABASE, ROLLBACK'
