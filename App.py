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
    cur.execute("select * from Test_Cases")
    data=cur.fetchall()
    cur.close()
    return render_template('index_test.html',students=data)

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        flash("Data Inserted Successfully")
        Test_Case_Name=request.form['Test_Case_Name']
        Test_Case=request.form['Test_Case']
        Source_Query=request.form['Source_Query']
        Target_Query=request.form['Target_Query']

        cur = conn.cursor()
        cur.execute("insert into test_cases (Test_Case_Name,Test_Case,Source_Query,Target_Query) VALUES (%s,%s,%s,%s)",(Test_Case_Name,Test_Case,Source_Query,Target_Query))
        conn.commit()
        return redirect(url_for('index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method=="POST":

        id_Data=request.form['id']
        Test_Case_Name=request.form['Test_Case_Name']
        Test_Case=request.form['Test_Case']
        Source_Query=request.form['Source_Query']
        Target_Query=request.form['Target_Query']

        cur = conn.cursor()
        cur.execute("update test_cases set Test_Case_Name=%s,Test_Case=%s,Source_Query=%s,Target_Query=%s where id=%s",(Test_Case_Name,Test_Case,Source_Query,Target_Query,id_Data))
        conn.commit()

        flash("Data Updated Successfully")
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):

            cur = conn.cursor()
            cur.execute("delete from test_cases where id=%s",(id_data))
            conn.commit()
            flash("Data Updated Successfully")
            return redirect(url_for('index'))

@app.route('/signon')
def signon():
    return render_template('signon.html')

if __name__ == "__main__":
    app.run(port=5006,debug=True)
