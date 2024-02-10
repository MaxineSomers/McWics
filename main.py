from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from classes import UserInfo

global currentUser

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "expensesdatabase.db")
)

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'  # SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

# Model for expense
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)
    expensename = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)

# Create tables within the context of the application
with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))

    #### Daily_Page
    daily_food = db.Column(db.Float)
    daily_transportation = db.Column(db.Float)
    daily_utilities = db.Column(db.Float)
    daily_entertainment = db.Column(db.Float)

@app.route('/')
def index():
    return render_template('add.html')

@app.route('/addexpense', methods=['POST'])
def addexpense(): #get all the data from the add form
    date = request.form['date']
    expensename = request.form['expensename']
    amount = request.form['amount']
    category = request.form['category']

    #print for now to confirm we get the right data
    print(date+' '+expensename+' '+amount+' '+ category)

    expense = Expense(date=date, expensename=expensename, amount=amount, category=category)
    #add the expense to the database
    db.session.add(expense)
    db.session.commit() #changes are committed to db

    return redirect("/")
    #return  
    

@app.route('/expenses')
#get all expenses from the database
def expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)

@app.route('/signup')
def user_info():
    return render_template('user.html') 

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Create a new instance of the User class
        new_user = UserInfo(name, email, password)
        print("New User:", new_user.email)
    

    return redirect("/")



@app.route('/Daily_Expense')
def min_page():
    return render_template('min_page.html')

def addexpense(): #get all the data from the add form
    date = request.form['date']
    expensename = request.form['expensename']
    amount = request.form['amount']
    category = request.form['category']

    #print for now to confirm we get the right data
    print(date+' '+expensename+' '+amount+' '+ category)

    expense = Expense(date=date, expensename=expensename, amount=amount, category=category)
    #add the expense to the database
    db.session.add(expense)
    db.session.commit() #changes are committed to db

    return redirect("/Daily_Expense")



def homePage():
    return render_template("homePage.html")

if __name__ == '__main__':
    app.run(debug=True)
