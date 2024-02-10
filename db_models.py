# models.py
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense.db'  # SQLite database URI
db = SQLAlchemy(app)

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

    # Add more fields as needed

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, phone={self.phone})"
    
    @app.route('/')
    def index():
        return render_template('index.html')

    def add_daily_expense():
        amount = float(request.form['amount'])
        category = request.form['categegory']
        if category == "food":
            User.daily_food = amount
        elif category == "transportation":
            User.daily_transportation = amount
        elif category == "entertainment":
            User.daily_entertainment = amount

        db.session.commit()

        return "Expense added successfully! "
    
if __name__ == '__main__':
    app.run(debug=True)





