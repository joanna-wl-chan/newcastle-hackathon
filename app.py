from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index_page():
	return render_template('index.html');

@app.route('/profile_page')
def profile_page():
	return render_template('profile.html');

@app.route('/townsville_flood')
def disaster_townsville():
	return render_template('townsville.html');

@app.route('/donate')
def donate():
	return render_template('donate.html');

if __name__ == "__main__":
	app.run()    