from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

@app.route('/')
def add():
    return render_template('add.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)