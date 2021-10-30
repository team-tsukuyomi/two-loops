# server code
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, send_from_directory, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
async def index():
    return render_template('index.html', cards=[])

@app.route('/sidebar_demo')
async def sdemo():
    return render_template('sidebar.html')

@app.route('/flashcard_demo')
async def fdemo():
    return render_template('index.html', cards=[['a','b','c'], ['c','b','a']])

@app.route('/css/<name>')
async def css(name):
    return send_from_directory('css', name)

@app.route('/images/<name>')
async def images(name):
    return send_from_directory('images', name)

@app.route('/js/<name>')
async def js(name):
    return send_from_directory('js', name)

app = WsgiToAsgi(app)
if __name__=="__main__":
    app.run()
