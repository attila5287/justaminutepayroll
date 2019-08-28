# from models import Employee
from flask_sqlalchemy import SQLAlchemy
import os
from flask import (Flask, render_template, redirect, jsonify, request)
from flask_pymongo import PyMongo
import json
from Pay_stub import Pay_stub
from flask_wtf import FlaskForm  
from forms import ContactForm, Timesheet, Tim3sheet, EmployeeForm
app = Flask(__name__)
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)
# db.create_all()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://doffzajcqxfelhp:5b59eac5a5ea676b7229695cd65f3d44344d00ba1cf15f53143c4a0f8c91ce19@ec2-174-129-27-3.compute-1.amazonaws.com:5432/d6lf1ishviubld'
# ===================== DEFINE DATABASE MODEL ======================
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        return '<Pet %r>' % (self.name)
# ======================  ======================
@app.route("/")
def home():
    return render_template("index.html")

# ======================  ======================
# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["petName"]
        lat = request.form["petLat"]
        lon = request.form["petLon"]

        pet = Pet(name=name, lat=lat, lon=lon)
        db.session.add(pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

# ======================  ======================
@app.route("/api/pals")
def pals():
    results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

    hover_text = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    pet_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(pet_data)
# ============================================
@app.route('/eeinfo', methods = ['GET', 'POST']) 
def cont4ct():
   pass
   form = EmployeeForm()
   if request.method == 'POST':
      if form.validate() == False:
         return render_template('forms_employee.html', form=form)
   elif request.method == 'GET':
      return render_template('forms_employee.html', form=form)
   else:
      return render_template('form_data_employee.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("form_data_employee.html", result=result)

@app.route('/timesheet', methods = ['POST', 'GET'])
def Tim3sheet_first_week():
    pass
    days_list = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    forms_l1st = [
      Timesheet(day) for day in days_list
    ]
    if request.method == 'POST':
        result = request.form
        print(result)

    return render_template('forms_timesheet.html', forms_list = forms_l1st)

@app.route('/paystubviewer')
def Pay_stub_generet0r():
    pass
    test_a_paystub = Pay_stub()
    return render_template('pay_stub_viewer.html', Pay_stub = test_a_paystub)

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
   pass
   form = ContactForm()
   if request.method == 'POST':
      pass
      result = request.form
      print(result)
      return render_template("result.html", result=result)
   return render_template('contact.html', form = form)

# ============ THE END ==============
if __name__ == '__main__':
  app.run(debug=True)
