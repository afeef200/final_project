from flask import Flask ,render_template
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



# @app.route("/about/")
# def load_page_2():
# 	return render_template("about.html")

# @app.route("/contact/")
# def load_page_3():
# 	return render_template("contact.html")

# @app.route("/hobbies/")
# def load_page_4():
# 	return render_template("hobbies.html")



if __name__ == '__main__':
	app.run()
