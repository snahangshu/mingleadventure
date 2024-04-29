from flask import Flask, render_template
app = Flask(__name__,template_folder='template')

@app.route("/")
def hello():
  return render_template('index.html')
@app.route("/blog")
def blog():
  return render_template('blog.html')
@app.route("/login")
def login():
  return render_template('login.html')

app.run(debug=True,port=2030)
