from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/Todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Todo(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	complete = db.Column(db.Boolean)
	Date = db.Column(db.Date)

	def __init__(self, title, complete, Date):
		
		self.title = title 
		self.complete = complete 
		self.Date = Date


 

@app.route('/')
def home():
	
	return render_template("home.html")


@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/Todo')
def index():
	todo_list = Todo.query.all()
	#print(todo_list)
	return render_template("base.html",todo_list=todo_list)

@app.route("/add",methods=["POST"])
def add():
	title = request.form.get("title")
	Date = request.form.get("Date")
	new_todo = Todo(title=title, complete=False, Date=Date)
	db.session.add(new_todo)
	db.session.commit()
	return redirect(url_for("index"))

@app.route("/update/<int:todo_id>")
def update(todo_id):

	todo = Todo.query.filter_by(id=todo_id).first()
	todo.complete = not todo.complete
	db.session.commit()
	return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):

	todo = Todo.query.filter_by(id=todo_id).first()
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for("index"))

if __name__ == "__main__":


	app.run(debug=True)

