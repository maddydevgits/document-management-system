from flask import Flask,render_template,redirect,request,session

app=Flask(__name__)
app.secret_key='makeskilled'

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/registerUser',methods=['GET','POST'])
def registerUser():
    name=request.form['name']
    email=request.form['email']
    password=request.form['pass']
    print(name,email,password)
    return render_template('index.html')

@app.route('/loginUser',methods=['POST','GET'])
def loginUser():
    name=request.form['your_name']
    password=request.form['your_pass']
    print(name,password)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
