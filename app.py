from flask import (
    Flask, 
    render_template, 
    redirect, 
    jsonify, 
    request
    )
from flask_pymongo import PyMongo
import json
import jinja2
from Pay_stub import Pay_stub
from forms import ContactForm, Timesheet, Tim3sheet
# create instance of Flask app
app = Flask(__name__)

# add configuration as Heroku requirement
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug
app.config['WTF_CSRF_ENABLED'] = False
test_a_paystub = Pay_stub()
print(test_a_paystub)


@app.route('/', methods = ['POST', 'GET'])
def Tim3sheet_first_week():
    pass
    days_list = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    forms_l1st = [
      Timesheet(day) for day in days_list
    ]
    print(forms_l1st)
    
    if request.method == 'POST':
        result = request.form
        print(result)

    return render_template('forms_timesheet.html', forms_list = forms_l1st)

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
   form = ContactForm()
   if request.method == 'POST':
      pass
      result = request.form
      print(result)
      return render_template("result.html", result=result)
   return render_template('contact.html', form = form)

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("result.html", result=result)
      
@app.route('/paystubviewer')
def Pay_stub_generet0r():
    pass
    return render_template('pay_stub_viewer.html', Pay_stub = test_a_paystub)

@app.route('/beforeobjectoriented')
def forms():
  test_userName = 'Abuzer Kadayif'
  test_companyName = 'Baklava, Inc'
  rate = 10
  hours = 15
  current = rate * hours
  pay_count = 2
  year2date = current * pay_count
  return render_template(
    'forms.html',
    user_name=test_userName,
    company_name = test_companyName,
    rate = rate,
    hours = hours,
    current = current,
    year2date =   year2date
  )

@app.route('/play')
def blackjack_table():
  player_cards = []
  dealer_cards = []
  test_game = blackjack_1on1()
  # method below returns a tuple playerCards, dealerCards
  test_sim_roundd = test_game.simulation_mode_1on1()
  # first list of tuple
  player_cards = [
    card for card in test_sim_roundd[0]
  ]
  # second list of tuple
  dealer_cards = [
    card for card in test_sim_roundd[-1]
  ]
  return render_template(
    'home.html',
    player_c4rds=player_cards,
    dealer_c4rds=dealer_cards
    )

@app.route('/bstemp') 
def show_me_bootstrap_templates():
    return render_template('bstemp.html')

# ============ THE END ==============
if __name__ == '__main__':
  app.run(debug=True)