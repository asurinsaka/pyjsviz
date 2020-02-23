# nobel_viz.py
from flask import Flask, render_template
app = Flask(__name__)

winners = [
    {'name': 'Albert Einstein', 'category': 'Physics'},
    {'name': 'V.S. Naipaul', 'category': 'Literature'},
    {'name': 'Dorothy Hodgkin', 'category': 'Chemistry'}
]

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/demolist')
def demo_list():
    return render_template('testj2.html',
            heading="A little winners/' list",
            winners=winners
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
