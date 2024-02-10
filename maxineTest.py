from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

@app.route('/')
def add(): #returns template of a form to accwept expense info
    return render_template('add.html')

# Define a route and its corresponding view function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)