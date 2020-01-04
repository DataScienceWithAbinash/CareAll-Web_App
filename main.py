from flask import Flask,render_template,request
import random
import sqlite3

app = Flask(__name__)

DATABASE='mydb.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/details')
def details():
    return render_template('Details.html')

@app.route('/addoldiesrec')
def addoldiesrec():
    random_number=random.randint(600001,899999)
    refno= random_number
    name= request.args.get ('name')
    gender= request.args.get ('gender')
    age = request.args.get('age')
    location = request.args.get('location')
    mobno = request.args.get('mobno')
    cct = request.args.get('cct')
    db=connect_db()
    sql = "insert into oldies(refno,name, gender,age,location,mobno,cct) values(?,?,?,?,?,?,?)"
    db.execute(sql,[refno,name,gender,age,location,mobno,cct])#
    db.commit()
    db.close()
    return render_template('OldiesDetails.html', name=name,gender=gender,age=age,location=location,mobno=mobno,cct=cct,refno=random_number)#

@app.route('/addyoungsrec')
def addyoungsrec():
    random_number=random.randint(600001,899999)
    refno= random_number
    name= request.args.get ('name')
    gender= request.args.get ('gender')
    age = request.args.get('age')
    location = request.args.get('location')
    mobno = request.args.get('mobno')
    cct = request.args.get('cct')
    db=connect_db()
    sql = "insert into youngs(refno,name, gender,age,location,mobno,cct) values(?,?,?,?,?,?,?)"
    db.execute(sql,[refno,name,gender,age,location,mobno,cct])#
    db.commit()
    db.close()
    return render_template('YoungsDetails.html', name=name,gender=gender,age=age,location=location,mobno=mobno,cct=cct,refno=random_number)#

@app.route('/formoldies')
def formoldies():
    return render_template('FormOldies.html')

@app.route('/formyoungs')
def formyoungs():
    return render_template('FormYoungs.html')

@app.route('/retrieveoldies')
def retrieveoldies():
    return render_template('RetrieveOldies.html')

@app.route('/retrieveyoungs')
def retrieveyoungs():
    return render_template('RetrieveYoungs.html')

@app.route('/availableyoungs')
def availableyoungs():
    return render_template('AvailableYoungs.html')

@app.route('/showoldiesdetails')
def showoldiesdetails():
    print('successfully done')
    db=connect_db()
    cur = db.cursor()
    refno = request.args.get('Enter Reference number')
    cur.execute("select name, age, location, cct, reviws, ratings from oldies where refno="+str(refno))
    rows = cur.fetchall()
    return render_template('ResultOldies.html',rows= rows)

@app.route('/showyoungsdetails')
def showyoungsdetails():
    print('successfully done')
    db=connect_db()
    cur = db.cursor()
    refno = request.args.get('Enter Reference number')
    cur.execute("select name,age,location,cct from youngs where refno="+str(refno))
    rows = cur.fetchall()
    return render_template('ResultYoungs.html',rows= rows)

@app.route('/result')
def result():
    print('hi there i am printed')
    return render_template('Result.html')


if __name__=='__main__':
    app.run(debug=True)