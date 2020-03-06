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


# Photography gallery Routing
@app.route("/photo")
def photo():
	names = []
	photos = os.listdir('static/imgs/photos')
	for i in photos:
		names.append(i.split('.')[0])
	return render_template('photo.html', photos=photos, names=names)


@app.route("/Documentary")
def documentary():
	left = os.listdir('static/imgs/documentary/left')
	middle = os.listdir('static/imgs/documentary/middle')
	right = os.listdir('static/imgs/documentary/right')
	return render_template('documentary.html', left=left, middle=middle, right=right )

@app.route("/People")
def people():
	left = os.listdir('static/imgs/people/left')
	middle = os.listdir('static/imgs/people/middle')
	right = os.listdir('static/imgs/people/right')
	return render_template('people.html', left=left, middle=middle, right=right )


@app.route("/Places")
def places():
	left = os.listdir('static/imgs/places/left')
	middle = os.listdir('static/imgs/places/middle')
	right = os.listdir('static/imgs/places/right')
	return render_template('places.html', left=left, middle=middle, right=right )


# Video routing
@app.route("/video")
def video():
	videos = [
	"https://www.youtube.com/embed/X9TZzdsQw54",
	"https://www.youtube.com/embed/YCWXgM5Wn70",
	"https://www.youtube.com/embed/UcdLmmuSjNU",
	"https://www.youtube.com/embed/0nAfgvR3IDc",
	"https://www.youtube.com/embed/si8MGxd7GJs",
	"https://www.youtube.com/embed/9JJXv1te4SM"
	]
	return render_template('video.html', videos=videos)


# Info routing
@app.route("/about")
def about():
	about_img = os.listdir('static/imgs/about')[0]
	return render_template('about.html', about_img=about_img)


# Contact routing
@app.route("/contact")
def contact():
	contact_img = os.listdir('static/imgs/contact')[0]
	return render_template('contact.html', contact_img=contact_img)
	

if __name__ == '__main__':
	app.run(host='0.0.0.0')
