from flask import Flask
from flask_mysqldb import MySQL
from flask import render_template, url_for, jsonify, json, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'myweb'
mysql = MySQL(app)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS = False,
    MAIL_USERNAME='fedeleo9415@gmail.com',
    MAIL_PASSWORD='giqxotvklpulahnp'
)
mail = Mail(app)
app.secret_key = 'Devpass123.'

@app.route('/')
def index(name = None):
    url_for('static', filename='style.css')
    return render_template('index.html', name = name)

@app.route('/contacto', methods = ['GET','POST'])
def contacto(name = None):
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']
        msg = Message(asunto, sender=email, recipients=['fedeleo9415@gmail.com'])
        msg.body = f"Name: {nombre}\nEmail: {email}\nMessage: {mensaje}"
        mail.send(msg)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `formsubinfo` (`id`, `nombre`, `email`, `asunto`) VALUES (NULL,'" + str(nombre) + "','" + str(email) + "','" + str(asunto) + "');" )
        mysql.connection.commit()
    return render_template('contacto.html', name = name)

@app.route('/juegos-index', methods = ['GET', 'POST'])
def juegosIndex(name = None):
    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json' and str(request.get_json() == 'preguntados'):
        respJson = request.get_json()
        resp = str(respJson.get('response')) 
        print(resp)  
        return redirect(url_for('answersGame'))
    else:
        return render_template('juegos-index.html', name = name)
    
@app.route('/answersGame', methods = ['GET', 'POST'])
def answersGame():
    print("answersGame")
    if request.method == 'POST' :
        respJson = request.get_json()
        resp = str(respJson.get('response'))
        print(resp)
        return redirect(url_for('juegosIndex'))
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `historyquiz`")
        mysql.connection.commit()
        rowsDB = cur.fetchall()
        data = []
        for row in rowsDB:
            d = {
                'id': row[0],
                'pregunta': row[1],
                'opcion_1': row[2],
                'opcion_2': row[3],
                'opcion_3': row[4],
                'opcion_4': row[5],
                'opcion_correcta': row[6]
            }
            data.append(d)
        return render_template('answersGame.html', data = data)
        
        