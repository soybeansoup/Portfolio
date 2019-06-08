from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	left = os.listdir('static/imgs/home/left')
	middle = os.listdir('static/imgs/home/middle')
	right = os.listdir('static/imgs/home/right')
	return render_template('home.html', left=left, middle=middle, right=right )

@app.route("/photo")
def photo():
	photos = os.listdir('static/imgs/photos')
	return render_template('photo.html', photos=photos)

if __name__ == '__main__':
	app.run(debug=True)
