from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def hello():
	return "hello world"

@app.route("/goodbye")
def goodbye():
	return "goodbye"

@app.route("/randomname")

def randomname():
	qwe = ["ahmad" , "basil" , "afeef"  ,"anwar"]
	return random.choice(qwe)



if __name__ == "__main__":
	app.run()

