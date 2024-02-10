import uuid
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

current_user_id = ""

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "expensesdatabase.db")
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

# Model for expense
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)
    expensename = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    userId= db.Column(db.String(100), nullable=False)


class User(db.Model):
    name = db.Column(db.String(100), nullable=True)
    id = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Integer, primary_key=True)

    
# Create tables within the context of the application
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if current_user_id=="":
        return redirect("/signup")
    else:
        return render_template('homePage.html')

@app.route('/addexpense', methods=['POST'])
def addexpense(): #get all the data from the add form
    date = request.form['date']
    expensename = request.form['expensename']
    amount = request.form['amount']
    category = request.form['category']

    #print for now to confirm we get the right data
    print(date+' '+expensename+' '+amount+' '+ category)

    expense = Expense(date=date, expensename=expensename, amount=amount, category=category, userId = current_user_id)
    #add the expense to the database
    db.session.add(expense)
    db.session.commit() #changes are committed to db

    return redirect("/")

@app.route('/expenses')
#get all expenses fr    om the database
def expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)

@app.route('/signup')
def user_info():
    return render_template('user.html') 

@app.route('/createUser', methods=['POST'])
def createUser():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Create a new instance of the User class
        new_user = User(name=name,id = str(uuid.uuid4()), email=email, password=password)
        global current_user_id

        current_user_id = new_user.id

        db.session.add(new_user)
        db.session.commit() 

    return redirect("/users")

@app.route('/BudgetPlan')
def bp():
    return render_template('BudgetPlan.html') 
@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/Daily_Expense')
def min_page():
    return render_template('min_page.html')

# def addexpense(): #get all the data from the add form
#     date = request.form['date']
#     expensename = request.form['expensename']
#     amount = request.form['amount']
#     category = request.form['category']

#     #print for now to confirm we get the right data
#     print(date+' '+expensename+' '+amount+' '+ category)

#     expense = Expense(date=date, expensename=expensename, amount=amount, category=category, userId = current_user_id)
#     #add the expense to the database
#     db.session.add(expense)
#     db.session.commit() #changes are committed to db

#     return redirect("/Daily_Expense")


@app.route('/homePage')
def homePage():
    return render_template("homePage.html")

@app.route('/stockChecking')
def stock():
    return render_template("stockChecking.html")


if __name__ == '__main__':
    app.run(debug=True)
