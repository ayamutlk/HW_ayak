from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random, string
from flask_migrate import Migrate, migrate
import os

def randomword(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg', 'gif','jfif']
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
db = SQLAlchemy(app)
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    director = db.Column(db.String(20), unique=False, nullable=False)
    release_year = db.Column(db.Integer, unique=False, nullable=False)
    filename = db.Column(db.String(100), unique=False, nullable=True)
    actor =  db.Column(db.String, unique=False, nullable=True)
    video = db.Column(db.String, unique=False, nullable=False)
    def __repr__(self):
        return f"Title: {self.movie_title}, Director: {self.director}"
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Integer,unique=False, nullable=True)
    def __repr__(self):
        return f"Name: {self.name}, Content: {self.review_text}"


migrate = Migrate(app, db)
@app.route("/")
def home():
    movies_data = Movies.query.all()
    # print(movies_data)
    return render_template("index.html", movies_data=movies_data)

@app.route("/add_data")
def add_data():
    return render_template("add_profile.html")

@app.route("/add", methods=["POST", "GET"])
def movie_management():
    if request.method == "POST":
        movie_title = request.form.get("movie_title")
        description = request.form.get("description")
        director = request.form.get("director")
        release_year = request.form.get("release_year")
        file = request.files.get("filename")
        randomstring = randomword(10)
        actor = request.form.get("actor")
        video = request.form.get("video")
        # print(video)
        if allowed_file(file.filename):
            file_split = file.filename.split(".")
            final_name = f"{file_split[0]}_{randomstring}.{file_split[1]}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],final_name))
        movie_row = Movies(movie_title=movie_title, description=description, director=director,
                           release_year=release_year,filename=final_name, actor=actor, video=video)
        db.session.add(movie_row)
        db.session.commit()
        return redirect("/")


@app.route("/home", methods=["GET"])
def home_user():
    return render_template("index1.html")

@app.route('/login', methods=['GET'])
def display_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if is_valid_credentials(username, password):
        return redirect('/home')
    else:
        return render_template('login.html', error='Invalid username or password')

def is_valid_credentials(username, password):
    return username == 'aya' and password == '123'

@app.route('/')
def home1():
    return render_template('index1.html')



@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename))
@app.route('/movie_info/<movie_id>')
def movie_info(movie_id):
    movie_specific = Movies.query.get(movie_id)
    print(movie_specific)
    reviews_specific = Reviews.query.filter(Reviews.movie_id == movie_id)
    return render_template("movie_info.html", movie_specific=movie_specific, reviews_specific=reviews_specific)


@app.route("/add_review", methods=["POST"])
def review_management():
    if request.method == "POST":
        name = request.form.get("name")
        review_text = request.form.get("review_text")
        movie_id = request.form.get("movie_id")
        rating=request.form.get("rating")
        review_row = Reviews(name=name, review_text=review_text, movie_id=movie_id,rating=rating)
        db.session.add(review_row)
        db.session.commit()
        return redirect(url_for('movie_info', movie_id=movie_id))


@app.route("/delete/<int:id>")
def erase(id):
    data = Movies.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.movie_id == id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")


@app.route("/alter_movie/<int:id>", methods=["POST", "GET"])
def alter_movie(id):
    if request.method == "POST":
        data = Movies.query.get(id)
        movie_title = request.form.get("movie_title")
        description = request.form.get("description")
        director = request.form.get("director")
        release_year = request.form.get("release_year")
        file = request.files.get("filename")
        actor = request.form.get("actor")
        video = request.form.get("video")
        # print(video)
        # print(actor)

        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        if request.form.get("movie_title"):
            data.movie_title = movie_title
        if request.form.get("description"):
            data.description = description
        if request.form.get("director"):
            data.director = director
        if request.form.get("release_year"):
            data.release_year = release_year
        if request.files.get("filename"):
            data.filename = file_name
        if request.form.get("actor"):
            data.actor = actor
        if request.form.get("video"):
            data.video = video
        db.session.commit()
        return redirect(url_for('movie_info', movie_id=id))
    else:
        return render_template("alter_movie.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search = request.form["search"].lower()
        if len(Movies.query.filter(Movies.movie_title.like(search)).all()) > 0:
            movie_specific = Movies.query.filter(Movies.movie_title.like(search)).all()[0]
        else:
            movie_specific = []
        return render_template('movie_info.html', movie_specific=movie_specific)





@app.route("/about_me", methods=["GET"])
def about_me():
    return render_template("about_me.html")

@app.route('/delete_review', methods=['POST', "GET"])
def delete_review():
    review_id = request.form.get('review_id')
    review = Reviews.query.get(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('movie_info', movie_id=review.movie_id))

if __name__ == "__main__":
    app.run()