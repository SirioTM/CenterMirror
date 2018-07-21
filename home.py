from flask import Flask, render_template
from weather import Weather

app = Flask(__name__)

Info = Weather("Napoli")

@app.route('/')
def index():
    return render_template('home.html', info = Info)

if __name__ == '__main__':
    app.run()
