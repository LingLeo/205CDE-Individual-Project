from flask import Flask, render_template, redirect, url_for, request, session
import pymysql

app = Flask(__name__)


db = pymysql.connect("localhost","phpmyadmin","Kamenride1234","bookshop")
@app.route('/')
def home():
    return render_template('home.html')
#    return '<h1>Hello, World!</h1>'
#    return (getbooknewid())


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginrec', methods=['POST', 'GET'])
def loginrec():
    error = None
    if request.method == 'POST':
       if valid_login(request.form['username'],
                      request.form['password']):

            return ('Hello!'+request.form['username'])
       else:
            error = 'Invalid username/password'
            return (error)

def valid_login(Officer_Login_Key,Officer_Password):
    tmp_Officer_Login_Key = Officer_Login_Key
    tmp_Officer_Password = Officer_Password
    cursor = db.cursor()
    sql = ("SELECT Officer_Login_Key, Officer_Password FROM officer where Officer_Login_Key = '"+tmp_Officer_Login_Key+"'")
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    for row in result:
        Officer_Login_Key = row[0]
        Officer_Password = row[1]

    if Officer_Password == tmp_Officer_Password:
        return (True)
    else:
        return (False)

@app.route("/officerqueryrec0")
def officerqueryrec0():
	return render_template('officerqueryrec0.html')

@app.route('/officerqueryrec1', methods=['POST', 'GET'])
def officerqueryrec1():
    error = None
    if request.method == 'POST':
        tmp_Officer_Name = request.form['Officer_Name']
        tmp_Officer_Login_Key = request.form['Officer_Login_Key']
        cursor = db.cursor()
        sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key FROM officer where " + officersqlfilter(tmp_Officer_Name,tmp_Officer_Login_Key) + " order by Officer_Key asc")
        cursor.execute(sql)
        db.commit()
#       db.close()
        result = cursor.fetchall()
#        for row in result:
#            Officer_Name = row[0]
#            Officer_Login_Key = row[1]
#        return (Officer_Name)
        return render_template('officerqueryrec1.html', result = result)

@app.route('/officerqueryrec2', methods=['POST', 'GET'])
def officerqueryrec2():
    if request.method == 'POST':
        tmp_Officer_Key = request.form['In_Officer_Key']
        cursor = db.cursor()
        sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key, Officer_Password FROM officer where Officer_Key = '"+tmp_Officer_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Officer_Key = row[0]
#            Officer_Name = row[1]
#        return (Officer_Name)
        return render_template('officerqueryrec2.html', result = result)
    else:
        return 'End'

@app.route("/officeraddrec0")
def officeraddrec0():
    return render_template('officeraddrec0.html')

@app.route('/officeraddrec1', methods=['POST', 'GET'])
def officeraddrec1():
    if request.method == 'POST':
        try:
            tmp_Officer_Key = request.form['Officer_Key']
            tmp_Officer_Name = request.form['Officer_Name']
            tmp_Officer_Login_Key = request.form['Officer_Login_Key']
            tmp_Officer_Password = request.form['Officer_Password']

            tmp_Officer_Key = getofficernewid()
            cursor = db.cursor()
            sql = ("INSERT INTO officer (Officer_Key, Officer_Name, Officer_Login_Key, Officer_Password) VALUES ('"+tmp_Officer_Key+"','"+tmp_Officer_Name+"','"+tmp_Officer_Login_Key+"','"+tmp_Officer_Password+"')")
#            sql = ("INSERT INTO officer (Officer_Key, Officer_Login_Key, Officer_Password, Officer_Name, Officer_Sex, Officer_DOE, Officer_Address, Officer_Login_Key) VALUES ('"+tmp_Officer_Key+"','5a','5b','5c','5','1990-01-02','5e','5f')")
#            sql = ("INSERT INTO officer (Officer_Key, Officer_Login_Key, Officer_Password, Officer_Name, Officer_Sex, Officer_DOE, Officer_Address, Officer_Login_Key) VALUES ('"+tmp_Officer_Key+"','5','5a','5b','5','1998-11-07','5e','5f')")
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully added"
        except:
            db.rollback()
            msg = "error in insert operation"
            msg = sql

        finally:
 #           return (sql)
            sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key, Officer_Password FROM officer where Officer_Key = '"+tmp_Officer_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('officeraddrec1.html', msg = msg, result = result)
            cursor.close()

def getofficernewid():
    officernewid = str(int(getlastkey('officer','Officer_Key'))+1)
    return (officernewid)

def getlastkey(tablename,keyname):
    querylastkeysql = 'select ' + keyname + ' from ' + tablename + ' order by ' + keyname + ' desc'
    cursor = db.cursor()
    cursor.execute(querylastkeysql)
    db.commit()
    result = cursor.fetchall()
    for row in result:
    	outkeyname = row[0]
#        result.close ()
#        db.close()
    	return (str(outkeyname))

def officersqlfilter(tmp_Officer_Name, tmp_Officer_Login_Key):
    officersqlfilter = "1 = 1"
    if tmp_Officer_Name != '':
        officersqlfilter = officersqlfilter + " and Officer_Name like '%"+tmp_Officer_Name+"%'" 
    if tmp_Officer_Login_Key != '':
        officersqlfilter = officersqlfilter + " and Officer_Login_Key like '%"+tmp_Officer_Login_Key+"%'" 
    return (officersqlfilter)
    
@app.route('/officerupdaterec0')
def officerupdaterec0():    
    return render_template('officerupdaterec0.html',)


@app.route('/officerupdaterec1', methods=['POST', 'GET'])
def officerupdaterec1():
    error = None
    if request.method == 'POST':
        tmp_Officer_Name = request.form['Officer_Name']
        tmp_Officer_Login_Key = request.form['Officer_Login_Key']
        cursor = db.cursor()
        sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key FROM officer where " + officersqlfilter(tmp_Officer_Name,tmp_Officer_Login_Key) + " order by Officer_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('officerupdaterec1.html', result = result)

@app.route('/officerupdaterec2', methods=['POST', 'GET'])
def officerupdaterec2():
    if request.method == 'POST':
#        tmp_Officer_Key = request.form['Officer_Key']
        tmp_Officer_Key = request.form['In_Officer_Key']
#        return (tmp_Officer_Key)
        cursor = db.cursor()
        sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key, Officer_Password FROM officer where Officer_Key = '"+tmp_Officer_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Officer_Key = row[0]
#            Officer_Name = row[1]
#        return (Officer_Name)
        return render_template('officerupdaterec2.html', result = result)
    else:
        return 'End'

@app.route('/officerupdaterec3', methods=['POST', 'GET'])
def officerupdaterec3():
    if request.method == 'POST':
        try:
            tmp_Officer_Key = request.form['Officer_Key']
            tmp_Officer_Name = request.form['Officer_Name']
            tmp_Officer_Login_Key = request.form['Officer_Login_Key']
            tmp_Officer_Password = request.form['Officer_Password']

            cursor = db.cursor()
            tmp_Officer_Name = request.form['Officer_Name']
            sql = ("update officer set Officer_Name = '"+tmp_Officer_Name+"', Officer_Login_Key = '"+tmp_Officer_Login_Key+"', Officer_Password = '"+tmp_Officer_Password+"' where Officer_Key = '"+tmp_Officer_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully updated"
        except:
            db.rollback()
            msg = "error in Update operation"

        finally:
            cursor = db.cursor()
            sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key, Officer_Password FROM officer where Officer_Key = '"+tmp_Officer_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('officerupdaterec3.html', msg = msg, result = result)
            cursor.close()

@app.route('/officerdeleterec0')
def officerdeleterec0():    
    return render_template('officerdeleterec0.html',)


@app.route('/officerdeleterec1', methods=['POST', 'GET'])
def officerdeleterec1():
    error = None
    if request.method == 'POST':
        tmp_Officer_Name = request.form['Officer_Name']
        tmp_Officer_Login_Key = request.form['Officer_Login_Key']
        cursor = db.cursor()
        sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key FROM officer where " + officersqlfilter(tmp_Officer_Name,tmp_Officer_Login_Key) + " order by Officer_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('officerdeleterec1.html', result = result)

@app.route('/officerdeleterec2', methods=['POST', 'GET'])
def officerdeleterec2():
    if request.method == 'POST':
        tmp_Officer_Key = request.form['In_Officer_Key']
#        return (tmp_Officer_Key)
        cursor = db.cursor()
        sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key, Officer_Password FROM officer where Officer_Key = '"+tmp_Officer_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('officerdeleterec2.html', result = result)
    else:
        return 'End'

@app.route('/officerdeleterec3', methods=['POST', 'GET'])
def officerdeleterec3():
    if request.method == 'POST':
        try:
            tmp_Officer_Key = request.form['Officer_Key']
            tmp_Officer_Name = request.form['Officer_Name']
            tmp_Officer_Login_Key = request.form['Officer_Login_Key']
            tmp_Officer_Password = request.form['Officer_Password']

            cursor = db.cursor()
            tmp_Officer_Name = request.form['Officer_Name']
            sql = ("delete from officer where Officer_Key = '"+tmp_Officer_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully deleted"
        except:
            db.rollback()
            msg = "error in Delete operation"

        finally:
            sql = ("SELECT Officer_Key, Officer_Name, Officer_Login_Key, Officer_Password FROM officer where Officer_Key = '"+tmp_Officer_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('officerdeleterec3.html', msg = msg, result = result)
            cursor.close()


@app.route("/readerqueryrec0")
def readerqueryrec0():
	return render_template('readerqueryrec0.html')

@app.route('/readerqueryrec1', methods=['POST', 'GET'])
def readerqueryrec1():
    error = None
    if request.method == 'POST':
        tmp_Reader_Name = request.form['Reader_Name']
        tmp_Reader_Phone_no = request.form['Reader_Phone_no']
        cursor = db.cursor()
        sql = ("SELECT Reader_Key, Reader_Name, Reader_Phone_no FROM reader where " + readersqlfilter(tmp_Reader_Name,tmp_Reader_Phone_no) + " order by Reader_Key asc")
        cursor.execute(sql)
        db.commit()
#       db.close()
        result = cursor.fetchall()
#        for row in result:
#            Reader_Name = row[0]
#            Reader_Phone_no = row[1]
#        return (Reader_Name)
        return render_template('readerqueryrec1.html', result = result)

@app.route('/readerqueryrec2', methods=['POST', 'GET'])
def readerqueryrec2():
    if request.method == 'POST':
        tmp_Reader_Key = request.form['In_Reader_Key']
        cursor = db.cursor()
        sql = ("SELECT Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no FROM reader where Reader_Key = '"+tmp_Reader_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Reader_Key = row[0]
#            Reader_Name = row[1]
#        return (Reader_Name)
        return render_template('readerqueryrec2.html', result = result)
    else:
        return 'End'

@app.route("/readeraddrec0")
def readeraddrec0():
    return render_template('readeraddrec0.html')

@app.route('/readeraddrec1', methods=['POST', 'GET'])
def readeraddrec1():
    if request.method == 'POST':
        try:
            tmp_Reader_Key = request.form['Reader_Key']
            tmp_Reader_Login_Key = request.form['Reader_Login_Key']
            tmp_Reader_Password = request.form['Reader_Password']
            tmp_Reader_Name = request.form['Reader_Name']
            tmp_Reader_Sex = request.form['Reader_Sex']
            tmp_Reader_DOE = request.form['Reader_DOE']
            tmp_Reader_Address = request.form['Reader_Address']
            tmp_Reader_Phone_no = request.form['Reader_Phone_no']

            tmp_Reader_Key = getreadernewid()
            cursor = db.cursor()
#            sql = ("INSERT INTO reader (Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no) VALUES ('"+tmp_Reader_Key+"','"+tmp_Reader_Login_Key+"','"+tmp_Reader_Password+"','"+tmp_Reader_Name+"','"+tmp_Reader_Sex+"','"+tmp_Reader_DOE+"','"+tmp_Reader_Address+"','"+Reader_Phone_no+"')")
            sql = ("INSERT INTO reader (Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no) VALUES ('"+tmp_Reader_Key+"','"+tmp_Reader_Login_Key+"','"+tmp_Reader_Password+"','"+tmp_Reader_Name+"','"+tmp_Reader_Sex+"','"+tmp_Reader_DOE+"','"+tmp_Reader_Address+"','"+Reader_Phone_no+"')")
#            sql = ("INSERT INTO reader (Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no) VALUES ('"+tmp_Reader_Key+"','5','5a','5b','5','1998-11-07','5e','5f')")
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully added"
        except:
            db.rollback()
            msg = "error in insert operation"
            msg = sql

        finally:
 #           return (sql)
            sql = ("SELECT Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no FROM reader where Reader_Key = '"+tmp_Reader_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('readeraddrec1.html', msg = msg, result = result)
            cursor.close()

def getreadernewid():
    readernewid = str(int(getlastkey('reader','Reader_Key'))+1)
    return (readernewid)

def getlastkey(tablename,keyname):
    querylastkeysql = 'select ' + keyname + ' from ' + tablename + ' order by ' + keyname + ' desc'
    cursor = db.cursor()
    cursor.execute(querylastkeysql)
    db.commit()
    result = cursor.fetchall()
    for row in result:
    	outkeyname = row[0]
#        result.close ()
#        db.close()
    	return (str(outkeyname))

def readersqlfilter(tmp_Reader_Name, tmp_Reader_Phone_no):
    readersqlfilter = "1 = 1"
    if tmp_Reader_Name != '':
        readersqlfilter = readersqlfilter + " and Reader_Name like '%"+tmp_Reader_Name+"%'" 
    if tmp_Reader_Phone_no != '':
        readersqlfilter = readersqlfilter + " and Reader_Phone_no like '%"+tmp_Reader_Phone_no+"%'" 
    return (readersqlfilter)
    
@app.route('/readerupdaterec0')
def readerupdaterec0():    
    return render_template('readerupdaterec0.html',)


@app.route('/readerupdaterec1', methods=['POST', 'GET'])
def readerupdaterec1():
    error = None
    if request.method == 'POST':
        tmp_Reader_Name = request.form['Reader_Name']
        tmp_Reader_Phone_no = request.form['Reader_Phone_no']
        cursor = db.cursor()
        sql = ("SELECT Reader_Key, Reader_Name, Reader_Phone_no FROM reader where " + readersqlfilter(tmp_Reader_Name,tmp_Reader_Phone_no) + " order by Reader_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('readerupdaterec1.html', result = result)

@app.route('/readerupdaterec2', methods=['POST', 'GET'])
def readerupdaterec2():
    if request.method == 'POST':
        tmp_Reader_Key = request.form['In_Reader_Key']
#        return (tmp_Reader_Key)
        cursor = db.cursor()
        sql = ("SELECT Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no FROM reader where Reader_Key = '"+tmp_Reader_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Reader_Key = row[0]
#            Reader_Name = row[1]
#        return (Reader_Name)
        return render_template('readerupdaterec2.html', result = result)
    else:
        return 'End'

@app.route('/readerupdaterec3', methods=['POST', 'GET'])
def readerupdaterec3():
    if request.method == 'POST':
        try:
            tmp_Reader_Key = request.form['Reader_Key']
            tmp_Reader_Login_Key = request.form['Reader_Login_Key']
            tmp_Reader_Password = request.form['Reader_Password']
            tmp_Reader_Name = request.form['Reader_Name']
            tmp_Reader_Sex = request.form['Reader_Sex']
            tmp_Reader_DOE = request.form['Reader_DOE']
            tmp_Reader_Address = request.form['Reader_Address']
            tmp_Reader_Phone_no = request.form['Reader_Phone_no']

            cursor = db.cursor()
            tmp_Reader_Name = request.form['Reader_Name']
            sql = ("update reader set Reader_Login_Key = '"+tmp_Reader_Login_Key+"', Reader_Password = '"+tmp_Reader_Password+"', Reader_Name = '"+tmp_Reader_Name+"', Reader_Sex = '"+tmp_Reader_Sex+"', Reader_DOE = '"+tmp_Reader_DOE+"', Reader_Address = '"+tmp_Reader_Address+"', Reader_Phone_no = '"+tmp_Reader_Phone_no+"' where Reader_Key = '"+tmp_Reader_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully updated"
        except:
            db.rollback()
            msg = "error in Update operation"

        finally:
            sql = ("SELECT Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no FROM reader where Reader_Key = '"+tmp_Reader_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('readerupdaterec3.html', msg = msg, result = result)
            cursor.close()

@app.route('/readerdeleterec0')
def readerdeleterec0():    
    return render_template('readerdeleterec0.html',)


@app.route('/readerdeleterec1', methods=['POST', 'GET'])
def readerdeleterec1():
    error = None
    if request.method == 'POST':
        tmp_Reader_Name = request.form['Reader_Name']
        tmp_Reader_Phone_no = request.form['Reader_Phone_no']
        cursor = db.cursor()
        sql = ("SELECT Reader_Key, Reader_Name, Reader_Phone_no FROM reader where " + readersqlfilter(tmp_Reader_Name,tmp_Reader_Phone_no) + " order by Reader_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('readerdeleterec1.html', result = result)

@app.route('/readerdeleterec2', methods=['POST', 'GET'])
def readerdeleterec2():
    if request.method == 'POST':
        tmp_Reader_Key = request.form['In_Reader_Key']
#        return (tmp_Reader_Key)
        cursor = db.cursor()
        sql = ("SELECT Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no FROM reader where Reader_Key = '"+tmp_Reader_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('readerdeleterec2.html', result = result)
    else:
        return 'End'

@app.route('/readerdeleterec3', methods=['POST', 'GET'])
def readerdeleterec3():
    if request.method == 'POST':
        try:
            tmp_Reader_Key = request.form['Reader_Key']
            tmp_Reader_Login_Key = request.form['Reader_Login_Key']
            tmp_Reader_Password = request.form['Reader_Password']
            tmp_Reader_Name = request.form['Reader_Name']
            tmp_Reader_Sex = request.form['Reader_Sex']
            tmp_Reader_DOE = request.form['Reader_DOE']
            tmp_Reader_Address = request.form['Reader_Address']
            tmp_Reader_Phone_no = request.form['Reader_Phone_no']

            cursor = db.cursor()
            tmp_Reader_Name = request.form['Reader_Name']
            sql = ("delete from reader where Reader_Key = '"+tmp_Reader_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully deleted"
        except:
            db.rollback()
            msg = "error in Delete operation"

        finally:
            sql = ("SELECT Reader_Key, Reader_Login_Key, Reader_Password, Reader_Name, Reader_Sex, Reader_DOE, Reader_Address, Reader_Phone_no FROM reader where Reader_Key = '"+tmp_Reader_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('readerdeleterec3.html', msg = msg, result = result)
            cursor.close()

@app.route("/bookqueryrec0")
def bookqueryrec0():
	return render_template('bookqueryrec0.html')

@app.route('/bookqueryrec1', methods=['POST', 'GET'])
def bookqueryrec1():
    error = None
    if request.method == 'POST':
        tmp_Book_Name = request.form['Book_Name']
        tmp_Book_Author = request.form['Book_Author']
        cursor = db.cursor()
        sql = ("SELECT Book_Key,  Book_Name, Book_Author FROM book where " + booksqlfilter(tmp_Book_Name,tmp_Book_Author) + " order by Book_Key asc")
        cursor.execute(sql)
        db.commit()
#       db.close()
        result = cursor.fetchall()
#        for row in result:
#            Book_Name = row[0]
#            Book_Author = row[1]
#        return (Book_Name)
        return render_template('bookqueryrec1.html', result = result)

@app.route('/bookqueryrec2', methods=['POST', 'GET'])
def bookqueryrec2():
    if request.method == 'POST':
        tmp_Book_Key = request.form['In_Book_Key']
        cursor = db.cursor()
        sql = ("SELECT Book_Key, Book_Name, Book_Author, Book_Publisher, Book_Description FROM book where Book_Key = '"+tmp_Book_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Book_Key = row[0]
#            Book_Name = row[1]
#        return (Book_Name)
        return render_template('bookqueryrec2.html', result = result)
    else:
        return 'End'

@app.route("/bookaddrec0")
def bookaddrec0():
    return render_template('bookaddrec0.html')

@app.route('/bookaddrec1', methods=['POST', 'GET'])
def bookaddrec1():
    if request.method == 'POST':
        try:
            tmp_Book_Key = request.form['Book_Key']
            tmp_Book_Name = request.form['Book_Name']
            tmp_Book_Author = request.form['Book_Author']
            tmp_Book_Publisher = request.form['Book_Publisher']
            tmp_Book_Description = request.form['Book_Description']

            tmp_Book_Key = getbooknewid()
            cursor = db.cursor()
            sql = ("INSERT INTO book (Book_Key, Book_Name, Book_Author, Book_Publisher, Book_Description) VALUES ('"+tmp_Book_Key+"','"+tmp_Book_Name+"','"+tmp_Book_Author+"','"+tmp_Book_Publisher+"','"+tmp_Book_Description+"')")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully added"
        except:
            db.rollback()
            msg = "error in insert operation"

        finally:
            sql = ("SELECT Book_Key, Book_Name, Book_Author, Book_Publisher, Book_Description FROM book where Book_Key = '"+tmp_Book_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('bookaddrec1.html', msg = msg, result = result)
            cursor.close()

def getbooknewid():
    booknewid = str(int(getlastkey('book','Book_Key'))+1)
    return (booknewid)

def getlastkey(tablename,keyname):
    querylastkeysql = 'select ' + keyname + ' from ' + tablename + ' order by ' + keyname + ' desc'
    cursor = db.cursor()
    cursor.execute(querylastkeysql)
    db.commit()
    result = cursor.fetchall()
    for row in result:
    	outkeyname = row[0]
#        result.close ()
#        db.close()
    	return (str(outkeyname))

def booksqlfilter(tmp_Book_Name, tmp_Book_Author):
    booksqlfilter = "1 = 1"
    if tmp_Book_Name != '':
        booksqlfilter = booksqlfilter + " and Book_Name like '%"+tmp_Book_Name+"%'" 
    if tmp_Book_Author != '':
        booksqlfilter = booksqlfilter + " and Book_Author like '%"+tmp_Book_Author+"%'" 
    return (booksqlfilter)
    
@app.route('/bookupdaterec0')
def bookupdaterec0():    
    return render_template('bookupdaterec0.html',)


@app.route('/bookupdaterec1', methods=['POST', 'GET'])
def bookupdaterec1():
    error = None
    if request.method == 'POST':
        tmp_Book_Name = request.form['Book_Name']
        tmp_Book_Author = request.form['Book_Author']
        cursor = db.cursor()
        sql = ("SELECT Book_Key,  Book_Name, Book_Author FROM book where " + booksqlfilter(tmp_Book_Name,tmp_Book_Author) + " order by Book_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('bookupdaterec1.html', result = result)

@app.route('/bookupdaterec2', methods=['POST', 'GET'])
def bookupdaterec2():
    if request.method == 'POST':
        tmp_Book_Key = request.form['In_Book_Key']
#        return (tmp_Book_Key)
        cursor = db.cursor()
        sql = ("SELECT Book_Key, Book_Name, Book_Author, Book_Publisher, Book_Description FROM book where Book_Key = '"+tmp_Book_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Book_Key = row[0]
#            Book_Name = row[1]
#        return (Book_Name)
        return render_template('bookupdaterec2.html', result = result)
    else:
        return 'End'

@app.route('/bookupdaterec3', methods=['POST', 'GET'])
def bookupdaterec3():
    if request.method == 'POST':
        try:
            tmp_Book_Key = request.form['Book_Key']
            tmp_Book_Name = request.form['Book_Name']
            tmp_Book_Author = request.form['Book_Author']
            tmp_Book_Publisher = request.form['Book_Publisher']
            tmp_Book_Description = request.form['Book_Description']

            cursor = db.cursor()
            tmp_Book_Name = request.form['Book_Name']
            sql = ("update book set Book_Name = '"+tmp_Book_Name+"', Book_Author = '"+tmp_Book_Author+"', Book_Publisher = '"+tmp_Book_Publisher+"', Book_Description = '"+tmp_Book_Description+"' where Book_Key = '"+tmp_Book_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully updated"
        except:
            db.rollback()
            msg = "error in Update operation"

        finally:
            sql = ("SELECT Book_Key, Book_Name, Book_Author, Book_Publisher, Book_Description FROM book where Book_Key = '"+tmp_Book_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('bookupdaterec3.html', msg = msg, result = result)
            cursor.close()

@app.route('/bookdeleterec0')
def bookdeleterec0():    
    return render_template('bookdeleterec0.html',)


@app.route('/bookdeleterec1', methods=['POST', 'GET'])
def bookdeleterec1():
    error = None
    if request.method == 'POST':
        tmp_Book_Name = request.form['Book_Name']
        tmp_Book_Author = request.form['Book_Author']
        cursor = db.cursor()
        sql = ("SELECT Book_Key,  Book_Name, Book_Author FROM book where " + booksqlfilter(tmp_Book_Name,tmp_Book_Author) + " order by Book_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('bookdeleterec1.html', result = result)

@app.route('/bookdeleterec2', methods=['POST', 'GET'])
def bookdeleterec2():
    if request.method == 'POST':
        tmp_Book_Key = request.form['In_Book_Key']
#        return (tmp_Book_Key)
        cursor = db.cursor()
        sql = ("SELECT Book_Key, Book_Name, Book_Author, Book_Publisher, Book_Description FROM book where Book_Key = '"+tmp_Book_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('bookdeleterec2.html', result = result)
    else:
        return 'End'

@app.route('/bookdeleterec3', methods=['POST', 'GET'])
def bookdeleterec3():
    if request.method == 'POST':
        try:
            tmp_Book_Key = request.form['Book_Key']
            tmp_Book_Name = request.form['Book_Name']
            tmp_Book_Author = request.form['Book_Author']
            tmp_Book_Publisher = request.form['Book_Publisher']
            tmp_Book_Description = request.form['Book_Description']

            cursor = db.cursor()
            tmp_Book_Name = request.form['Book_Name']
            sql = ("delete from book where Book_Key = '"+tmp_Book_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully deleted"
        except:
            db.rollback()
            msg = "error in Delete operation"

        finally:
            sql = ("SELECT Book_Key, Book_Name, Book_Author, Book_Publisher, Book_Description FROM book where Book_Key = '"+tmp_Book_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('bookdeleterec3.html', msg = msg, result = result)
            cursor.close()

@app.route("/reservequeryrec0")
def reservequeryrec0():
	return render_template('reservequeryrec0.html')

@app.route('/reservequeryrec1', methods=['POST', 'GET'])
def reservequeryrec1():
    error = None
    if request.method == 'POST':
        tmp_Reserve_Key = request.form['Reserve_Key']
        tmp_Reserve_Date  = request.form['Reserve_Date']
        cursor = db.cursor()
        sql = ("SELECT Reserve_Key, Reserve_Date, Reader_Key FROM reserve where " + reservesqlfilter(tmp_Reserve_Key,tmp_Reserve_Date) + " order by Reserve_Key asc")
        cursor.execute(sql)
        db.commit()
#       db.close()
        result = cursor.fetchall()
#        for row in result:
#            Reserve_Name = row[0]
#            Reserve_Phone_no = row[1]
#        return (Reserve_Name)
        return render_template('reservequeryrec1.html', result = result)

@app.route('/reservequeryrec2', methods=['POST', 'GET'])
def reservequeryrec2():
    if request.method == 'POST':
        tmp_Reserve_Key = request.form['In_Reserve_Key']
        cursor = db.cursor()
        sql = ("SELECT Reserve_Key, Reserve_Date , Reader_Key, Book_Key, Officer_Key FROM reserve where Reserve_Key = '"+tmp_Reserve_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Reserve_Key = row[0]
#            Reserve_Name = row[1]
#        return (Reserve_Name)
        return render_template('reservequeryrec2.html', result = result)
    else:
        return 'End'

@app.route("/reserveaddrec0")
def reserveaddrec0():
    return render_template('reserveaddrec0.html')

@app.route('/reserveaddrec1', methods=['POST', 'GET'])
def reserveaddrec1():
    if request.method == 'POST':
        try:
            tmp_Reserve_Key = request.form['Reserve_Key']
            tmp_Reserve_Date  = request.form['Reserve_Date']
            tmp_Reader_Key = request.form['Reader_Key']
            tmp_Book_Key = request.form['Book_Key']
            tmp_Officer_Key = request.form['Officer_Key']

            tmp_Reserve_Key = getreservenewid()
            cursor = db.cursor()
            sql = ("INSERT INTO reserve (Reserve_Key, Reserve_Date, Reader_Key, Book_Key, Officer_Key) VALUES ('"+tmp_Reserve_Key+"','"+tmp_Reserve_Date+"','"+tmp_Reader_Key+"','"+tmp_Book_Key+"','"+tmp_Officer_Key+"')")
#            sql = ("INSERT INTO reserve (Reserve_Key, Reserve_Login_Key, Reserve_Password, Reserve_Name, Reserve_Sex, Reserve_DOE, Reserve_Address, Reserve_Phone_no) VALUES ('"+tmp_Reserve_Key+"','5a','5b','5c','5','1990-01-02','5e','5f')")
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully added"
        except:
            db.rollback()
            msg = "error in insert operation"
            msg = sql

        finally:
 #           return (sql)
            sql = ("SELECT Reserve_Key, Reserve_Date, Reader_Key, Book_Key, Officer_Key FROM reserve where Reserve_Key = '"+tmp_Reserve_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('reserveaddrec1.html', msg = msg, result = result)
            cursor.close()

def getreservenewid():
    reservenewid = str(int(getlastkey('reserve','Reserve_Key'))+1)
    return (reservenewid)

def getlastkey(tablename,keyname):
    querylastkeysql = 'select ' + keyname + ' from ' + tablename + ' order by ' + keyname + ' desc'
    cursor = db.cursor()
    cursor.execute(querylastkeysql)
    db.commit()
    result = cursor.fetchall()
    for row in result:
    	outkeyname = row[0]
#        result.close ()
#        db.close()
    	return (str(outkeyname))

def reservesqlfilter(tmp_Reserve_Key, tmp_Reserve_Date):
    reservesqlfilter = "1 = 1"
    if tmp_Reserve_Key != '':
        reservesqlfilter = reservesqlfilter + " and Reserve_Key like '%"+tmp_Reserve_Key+"%'" 
    if tmp_Reserve_Date != '':
        reservesqlfilter = reservesqlfilter + " and Reserve_Date like '%"+tmp_Reserve_Date+"%'" 
    return (reservesqlfilter)
    
@app.route('/reserveupdaterec0')
def reserveupdaterec0():    
    return render_template('reserveupdaterec0.html',)


@app.route('/reserveupdaterec1', methods=['POST', 'GET'])
def reserveupdaterec1():
    error = None
    if request.method == 'POST':
        tmp_Reserve_Key = request.form['Reserve_Key']
        tmp_Reserve_Date = request.form['Reserve_Date']
        cursor = db.cursor()
        sql = ("SELECT Reserve_Key, Reserve_Date, Reader_Key, Book_Key, Officer_Key FROM reserve where " + reservesqlfilter(tmp_Reserve_Key,tmp_Reserve_Date) + " order by Reserve_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('reserveupdaterec1.html', result = result)

@app.route('/reserveupdaterec2', methods=['POST', 'GET'])
def reserveupdaterec2():
    if request.method == 'POST':
        tmp_Reserve_Key = request.form['In_Reserve_Key']
#        return (tmp_Reserve_Key)
        cursor = db.cursor()
        sql = ("SELECT Reserve_Key, Reserve_Date, Reader_Key, Book_Key, Officer_Key FROM reserve where Reserve_Key = '"+tmp_Reserve_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
#        for row in result:
#            Reserve_Key = row[0]
#            Reserve_Name = row[1]
#        return (Reserve_Name)
        return render_template('reserveupdaterec2.html', result = result)
    else:
        return 'End'

@app.route('/reserveupdaterec3', methods=['POST', 'GET'])
def reserveupdaterec3():
    if request.method == 'POST':
        try:
            tmp_Reserve_Key = request.form['Reserve_Key']
            tmp_Reserve_Date  = request.form['Reserve_Date']
            tmp_Reader_Key = request.form['Reader_Key']
            tmp_Book_Key = request.form['Book_Key']
            tmp_Officer_Key = request.form['Officer_Key']

            cursor = db.cursor()
#            tmp_Reserve_Name = request.form['Reserve_Name']
            sql = ("update reserve set Reserve_Date = '"+tmp_Reserve_Date+"', Reader_Key = '"+tmp_Reader_Key+"', Book_Key = '"+tmp_Book_Key+"', Officer_Key = '"+tmp_Officer_Key+"' where Reserve_Key = '"+tmp_Reserve_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully updated"
        except:
            db.rollback()
            msg = "error in Update operation"

        finally:
            sql = ("SELECT Reserve_Key, Reserve_Date, Reader_Key, Book_Key, Officer_Key FROM reserve where Reserve_Key = '"+tmp_Reserve_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('reserveupdaterec3.html', msg = msg, result = result)
            cursor.close()

@app.route('/reservedeleterec0')
def reservedeleterec0():    
    return render_template('reservedeleterec0.html',)


@app.route('/reservedeleterec1', methods=['POST', 'GET'])
def reservedeleterec1():
    error = None
    if request.method == 'POST':
        tmp_Reserve_Key = request.form['Reserve_Key']
        tmp_Reserve_Date  = request.form['Reserve_Date']
        cursor = db.cursor()
        sql = ("SELECT Reserve_Key, Reserve_Date FROM reserve where " + reservesqlfilter(tmp_Reserve_Key,tmp_Reserve_Date) + " order by Reserve_Key asc")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('reservedeleterec1.html', result = result)

@app.route('/reservedeleterec2', methods=['POST', 'GET'])
def reservedeleterec2():
    if request.method == 'POST':
        tmp_Reserve_Key = request.form['In_Reserve_Key']
#        return (tmp_Reserve_Key)
        cursor = db.cursor()
        sql = ("SELECT Reserve_Key, Reserve_Date, Reader_Key, Book_Key, Officer_Key FROM reserve where Reserve_Key = '"+tmp_Reserve_Key+"'")
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        return render_template('reservedeleterec2.html', result = result)
    else:
        return 'End'

@app.route('/reservedeleterec3', methods=['POST', 'GET'])
def reservedeleterec3():
    if request.method == 'POST':
        try:
            tmp_Reserve_Key = request.form['Reserve_Key']
            tmp_Reserve_Date  = request.form['Reserve_Date']
            tmp_Reader_Key = request.form['Reader_Key']
            tmp_Book_Key = request.form['Book_Key']
            tmp_Officer_Key = request.form['Officer_Key']

            cursor = db.cursor()
            tmp_Reserve_Key = request.form['Reserve_Key']
            sql = ("delete from reserve where Reserve_Key = '"+tmp_Reserve_Key+"'")
			
            cursor.execute(sql)
            db.commit()
            msg = "Record successfully deleted"
        except:
            db.rollback()
            msg = "error in Delete operation"

        finally:
            sql = ("SELECT Reserve_Key, Reserve_Date, Reader_Key, Book_Key, Officer_Key FROM reserve where Reserve_Key = '"+tmp_Reserve_Key+"'")
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()

            return render_template('reservedeleterec3.html', msg = msg, result = result)
            cursor.close()

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=8000)
