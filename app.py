from flask import Flask , render_template , request
from flask_script import Manager
app = Flask(__name__ , static_url_path = '/templates')
manager = Manager(app)
app.config["JSON_AS_ASCII"] = False
app.debug = True

@app.route('/' , methods = ['POST' , 'GET'])
def index():
	return render_template("index.html")

@app.route('/order' , methods = ['POST'])
def order():
	username = request.form['usr']
	password = request.form['psd']
	print('帳號:')
	print(username)
	print('密碼:')
	print(password)
	return render_template("login.html" , usr = username , psd = password)

@manager.command 
def hello():
	"""Print Hello"""
	print("hello")

if __name__ == "__main__":
	app.run()