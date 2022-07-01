from flask import Flask, render_template
from flask_mysqldb import MySQL



app = Flask(__name__)


#Configuracion de Mysql

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba'


app.secret_key = "mysecretkey"
mysql = MySQL(app)




#rutas
@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from estudiante")
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=3000, debug=True)

