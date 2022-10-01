from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Info(db.Model):
    Sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    course = db.Column(db.String(200),nullable = False)
    date_time = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
         return f"{self.Sno} -> {self.name}"
@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route('/report')
def report():
    return render_template('use.html')
@app.route('/About')
def about():
        return render_template('about.html')
@app.route('/Contact')
def contact():
    return render_template('contact.html') 
@app.route('/delete/<int:Sno>')
def delete(Sno):
    info = Info.query.filter_by(Sno = Sno).first() 
    db.session.delete(info)
    db.session.commit()
    return redirect('/Register')
@app.route('/edu',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        ed = Info(name = name, course = course)
        db.session.add(ed)
        db.session.commit()
    allinfo = Info.query.all()
    return render_template('edu.html','use.html',allinfo = allinfo) 
@app.route('/Register',methods = ['GET','POST'])
def Edu():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        info = Info(name = name, course = course)
        db.session.add(info)
        db.session.commit()
    allinfo = Info.query.all()
    return render_template('info.html',allinfo = allinfo)            
if __name__ == "__main__" :
    app.run(debug = True, port=8000)    