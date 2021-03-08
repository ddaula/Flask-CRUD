from flask import Flask,render_template,request,redirect,url_for
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Raptor_85")

app=Flask(__name__)

app.config['host']="localhost"
app.config['database']="postgres"
app.config['user']="postgres"
app.config['password']="Raptor_85"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']

        cur = conn.cursor()
        cur.execute("insert into students (ename,email,phone) VALUES (%s,%s,%s)",(name,email,phone))
        conn.commit()
        return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(port=5006,debug=True)
