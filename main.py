from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_info')
def user_info():
    return render_template('user.html')


if __name__ == '__main__':
    app.run(debug=True)
#### MIn peng