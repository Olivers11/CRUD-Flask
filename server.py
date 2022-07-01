from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL



app = Flask(__name__)


#Configuracion de Mysql
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba'


app.secret_key = "mysecretkey"
mysql = MySQL(app)




#rutas
@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    query = "select * from estudiante"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template("index.html", estudiantes=data)



@app.route("/add_est", methods=['POST'])
def add_est():
    if request.method == 'POST':
        pass

if __name__ == '__main__':
    app.run(port=3000, debug=True)

