# server code
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, send_from_directory, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
async def index():
    return render_template('index.html')

@app.route('/sidebar_demo')
async def demo():
    return render_template('sidebar.html')

@app.route('/tailwind')
async def tailwind():
    return send_from_directory('.', "tailwind.css")

app = WsgiToAsgi(app)
if __name__=="__main__":
    app.run()
