from flask import Flask ,render_template ,flash, request , session, abort , redirect, url_for
from flask_table import Table, Col
from validate_email import validate_email
import re
import os
import dataset
import random

app = Flask(__name__)

db_url = "postgres://sbpiprknypeqgy:594c4a7b735602d9b3fea48306922eeb64206ed44740476f891291a46feb9d39@ec2-54-227-240-7.compute-1.amazonaws.com:5432/d9mpa1qghsi2hi"
db = dataset.connect(db_url)
s_l = db['s_l']
food = db["food"]

pages = ["about.jinja","contact.jinja","hobbies.jinja","home.jinja","projects.jinja"]

wh = ""
wh_type = ""
option_1 = ""
option_2 = ""
option_3 = ""
count_1 = 0
count_2 = 0
count_3 = 0


@app.route('/<page_name>/')
def go_to_page(page_name):
    global wh_type
    if not session.get('logged_in'):
        if page_name == 'signup':
            return render_template('signup.jinja')
        else:
            return render_template('login.jinja' )
    else:
        return render_template(page_name + ".jinja" ,title = page_name, user_type=wh_type)


@app.route('/')
def home():
    # s_l.delete()
    userList = list(db['s_l'].all())
    print "THIS IS USERLIST"
    print(userList)
    if not session.get('logged_in'):
        return render_template('login.jinja')
    else:
        return render_template("home.jinja" ,title = "Home", user_type=wh_type)


 
@app.route('/login', methods=['POST'])
def login():
    global wh_type
    name = request.form['username']
    password = request.form['password']
    result = s_l.find_one(password=password, username=name)
    if result:
        session['logged_in'] = True
        wh = name
        wh_type = result["type"]
    else:
        flash('wrong password!')
    return home()

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['username']
    Email = request.form['email']
    password = request.form['password']
    re_password = request.form['re_password']
    is_valid = validate_email(Email,verify=True)
    if s_l.find_one(username=name) ==None and s_l.find_one(Email=Email) == None and password == re_password:
        if is_valid == True:       
            s_l.insert(dict(username=name , Email = Email , password = password, type = "student"))
            session['logged_in'] = True
            return render_template("home.jinja", user_type=wh_type) 
    return render_template("signup.jinja")



# def show_food(option_1,option_2,option_3):

@app.route("/kit" ,methods=['POST'])
def kit():
    return render_template("kit.jinja",option_1 = option_1 ,option_2 = option_2 ,option_3 = option_3, user_type=wh_type)

@app.route("/kitchen" ,methods=['POST'])
def optionmn():
    global option_1
    global option_2
    global option_3

    global count_1
    global count_2
    global count_3
    if wh_type == "admin" or wh_type == "chef":
        option_1 = request.form['o_1']
        option_2 = request.form['o_2']
        option_3 = request.form['o_3']
        food.insert(dict(option_1 = option_1 ,option_2 = option_2 ,option_3 = option_3))
        return render_template("vote.jinja" ,count_1 = count_1, count_2 = count_2 , count_3 = count_3)
    else:
        v_1 = request.form['v_1']
        v_2 = request.form['v_2']
        v_3 = request.form['v_3']
        if v_1 == True:
            count_1 = count_1 + 1
        if v_2 == True:
            count_2 = count_2 + 1
        if v_3 == True:
            count_3 = count_3 + 1 
        return render_template("vote.jinja",count_1 = count_1, count_2 = count_2 , count_3 = count_3)
  



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template("logout.jinja")


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

