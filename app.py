from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index_page():
	return render_template('index.html');

@app.route('/profile.html')
def profile_page():
	return render_template('profile.html');

@app.route('/townsville_flood.html')
def disaster_townsville():
	return render_template('townsville_flood.html');

@app.route('/donate.html')
def donate():
	return render_template('donate.html');

@app.route('/success.html')
def success():
	return render_template('success.html')

@app.route('/townsville_flood2.html')
def t2():
	return render_template('townsville_flood2.html');


if __name__ == "__main__":
	app.run()    