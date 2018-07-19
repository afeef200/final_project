from flask import Flask ,render_template , request
import random

app = Flask(__name__)

@app.route("/")
def load_page():
	return render_template("home.jinja")

@app.route('/<page_name>/')
def go_to_page(page_name):
	# hobbies = ["karate","basket", "watch_anime"]
	# hobby_list = random.sample(hobbies , 2)

	return render_template(page_name + ".jinja" ,title = page_name)

@app.route("/formsubmit", methods = ["GET" , "POST"])
def formExmaple():
	return "Thank You "


# @app.route("/formsubmite", methods=["GET", "POST"])
# def formExmaple():
#   if request.method == "GET":
#     render_template("login.jinja")
#   else:
#     form = request.form
#     contentValue = form["content"]
#     return contentValue






if __name__ == '__main__':
	app.run()
