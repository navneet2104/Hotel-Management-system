from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hotel3():
    return render_template("index.html")

@app.route('/ho')
def hotel4():
    return render_template("admin.html")

@app.route('/panel1')
def hi():
    return render_template("panel.html")

@app.route('/hi')
def hi3():
    return render_template("showlist.html")


@app.route('/admlog',methods=["POST"])
def hello5():
    Email = request.form['email']
    Pass = request.form['pwd']
    print(Email,Pass)

    con = mysql.connector.connect(host="localhost",user="root",password="",db="db2")

    cursor = con.cursor()
    cursor.execute("select * from table3 where email = '"+Email+"' and pass = '"+Pass+"'  ")
    if cursor.fetchone():
        return render_template("admin.html")
    else:
        return render_template("index.html")

@app.route('/showli',methods=["POST"])
def showlist():

    name = str(request.form['it'])
    price = str(request.form['it2'])
    description = str(request.form['it3'])

    con = mysql.connector.connect(host="localhost", user="root", password="", db="db2")

    cur = con.cursor()
    cur.execute("insert into table4 values ('" "','" + name + "','" + price +"','" + description + "')")

    con.commit()

    return render_template("admin.html")

@app.route('/updateli')
def updatelist():
    conn=mysql.connector.connect(host='localhost',db='db2',user='root',password='')
    cur=conn.cursor()
    cur.execute("select * from table4")
    ar = cur.fetchall()
    return render_template('showlist.html' , data=ar)

@app.route('/updatelist')
def update():
    conn=mysql.connector.connect(host='localhost',db='db2',user='root',password='')
    cur=conn.cursor()
    id=request.args.get('id')
    cur.execute("update table4 set status='true' where id="+id)

if __name__ == '__main__':
    app.run()
