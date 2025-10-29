from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

app.config["SECRET_KEY"] = "super-secret-value" # dla CSRF
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqllite:///tmp/test.db' # os.environ('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

'''
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)

@app.route('/initdb')
def init_db():
    db.create_all()
    return "Baza danych zostala utworzona"

@app.route('/seed')
def seed_data():
    post = Post(title="pierwszy wpis",body="przykladowy wpis")
    db.session.add(post)
    db.session.commit()
    return "Dodano przykladowe dane"

@app.route('/posts')
def show_posts():
    posts = Post.query.order_by(Post.title.desc().all())
    return render_template("posts.html", posts=posts)
'''

# ----------------------------------------------------------------------------------- #

class ContactForm(FlaskForm):
    name = StringField("Imie", validators=[DataRequired(), Length(max=100)])
    email = StringField("E-mail", validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField("Wiadomosc", validators=[DataRequired(), Length(min=5,max=1000)])
    submit = SubmitField("Wyslij")

@app.route('/contact', methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Dziekujemy za uzupelnienie formularza!")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)






@app.route('/')
def hello_python():
    return("Hello from the other side")

@app.route('/hello/<name>', methods=["GET"])
def greet(name):
    return render_template("hello.html", name=name)

    #lang = request.args.get("lang", "pl") # query string np. /hello/Aleksandra?lang=pl
    #msg = {"pl": "Czesc", "en": "Hello"}.get(lang, "Czesc")
    #return f"{msg}, {name} !"

@app.post("/echo")
def echo():
    data = request.form or request.json or {}
    return {"wyslane": data}, 201

if __name__ == '__main__':
    app.run()