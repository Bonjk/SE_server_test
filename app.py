from flask import Flask , render_template , request , url_for , redirect , flash
from flask_script import Manager
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
app = Flask(__name__ , static_url_path = '/templates')
manager = Manager(app)
app.config["JSON_AS_ASCII"] = False
app.debug = True
app.secret_key = app.config.get('flask' , 'b9696332895257bb088ba05ca8fc6bd9')

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

@app.route('/login' , methods = ["GET" , "POST"])
def login():
	if request.method == "GET":
		return render_template("index2.html")
	user_now = request.form["usr"]
	if (user_now in users) and (request.form["psd"] == users[user_now]["password"]):
		user = User()
		user.id = user_now
		login_user(user)
		flash(f"{user_now}！歡迎登入！")
		return redirect(url_for("login2" , user_now = user_now))
	else:
		flash("你是誰 我不認識你")
		#return render_template("index2.html")
		return "NOT"

@app.route('/login2/<user_now>' , methods = ["GET"])
def login2(user_now):
	return render_template("login2.html" , user_name = user_now)

@app.route('/logout')
def logout():
	user_now = current_user.get_id()
	login_user()
	flash(f"{user_now}你已經成功登出")
	return "已經登出"

login_mananger = LoginManager()
login_mananger.init_app(app)
login_mananger.session_protection = "strong"
login_mananger.login_view = "login"
login_mananger.login_message = "你三小"

class User(UserMixin):
	pass

@login_mananger.user_loader
def user_loader(user_now):
	if user_now not in users:
		return

	user = User()
	user.id = user_now
	return user

@login_mananger.request_loader
def request_loader(request):
	user_now = request.form.get("user_id")
	if user_now not in users:
		return
	
	user = User()
	user.id = user_now
	user.is_authenticated = request.form["psd"] == users[user_now]["password"]
	return user

users = {"Bang" : {"password" : "40747016S"}}

if __name__ == "__main__":
	app.run()