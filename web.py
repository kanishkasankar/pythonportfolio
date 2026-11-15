<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
>>>>>>> 3cffd27d4ac79156f1c90dc6de8e4bffa0326710
    app.run(debug=True)