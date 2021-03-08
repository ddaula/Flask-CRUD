from flask import Flask,render_template,request,redirect,url_for,flash
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Raptor_85")

app=Flask(__name__)
app.secret_key="flash message"

@app.route('/')
def index():
    cur = conn.cursor()
    cur.execute("select * from students")
    data=cur.fetchall()
    cur.close()
    return render_template('index.html',students=data)

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        flash("Data Inserted Successfully")
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']

        cur = conn.cursor()
        cur.execute("insert into students (ename,email,phone) VALUES (%s,%s,%s)",(name,email,phone))
        conn.commit()
        return redirect(url_for('index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method=="POST":

        id_Data=request.form['id']
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']

        cur = conn.cursor()
        cur.execute("update students set ename=%s,email=%s,phone=%s where id=%s",(name,email,phone,id_Data))
        conn.commit()

        flash("Data Updated Successfully")
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):

            cur = conn.cursor()
            cur.execute("delete from students where id=%s",(id_data))
            conn.commit()
            flash("Data Updated Successfully")
            return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=5006,debug=True)
