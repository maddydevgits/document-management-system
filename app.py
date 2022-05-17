from flask import Flask,render_template,redirect,request,session
import json
import os
from werkzeug.utils import secure_filename

def store_data_into_db(name,email,password):
    data={}
    data['name']=name
    data['email']=email
    data['password']=password
    data=json.dumps(data)
    f=open('dataset.txt','a')
    f.writelines(data) 
    f.write('\n')
    f.close()

def read_data_from_db():
    f=open('dataset.txt','r')
    k=f.readlines()
    f.close()
    return(k)

app=Flask(__name__)
app.secret_key='makeskilled'
app.config["UPLOAD_FOLDER"] = "uploads/"

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/registerUser',methods=['GET','POST'])
def registerUser():
    name=request.form['name']
    email=request.form['email']
    password=request.form['pass']
    print(name,email,password)
    store_data_into_db(name,email,password)
    return render_template('index.html')

@app.route('/loginUser',methods=['POST','GET'])
def loginUser():
    name=request.form['your_name']
    password=request.form['your_pass']
    print(name,password)
    k=read_data_from_db()
    print(k)
    for i in k:
        dummy=json.loads(i)
        if (dummy['name']==name and dummy['password']==password):
            return redirect('/dashboard')
    return render_template('index.html')

@app.route('/uploadDocument',methods=['POST','GET'])
def uploadDocument():
    doc=request.files['chooseFile']
    doc1=secure_filename(doc.filename)
    doc.save(app.config['UPLOAD_FOLDER']+doc1)
    return render_template('dashboard.html')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
