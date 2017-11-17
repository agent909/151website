# from flask_mysqldb import MySQL

# from flaskext.mysql import MySQL
# from flask import Flask

# from app import app

# app = Flask(__name__)
# mysql = MySQL()
#
# app.config['MYSQL_DATABASE_HOST'] = 'localhostasdasd'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'MELANcholicEMvill909'
# app.config['MYSQL_DATABASE_DB'] = 'dbvill'
#
# mysql.init_app(app)
# cur = mysql.get_db().cursor()

import pymysql

database = pymysql.connect(host='localhost',
                           user='root',
                           password='MELANcholicEMvill909',
                           db='dbvill'
                           )
# cur = cursor= database.cursor()
