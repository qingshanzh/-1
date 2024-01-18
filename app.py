from flask import Flask,render_template


app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return "succese"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)