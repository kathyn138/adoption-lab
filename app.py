from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "whiskey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


@app.route('/')
def index():
    """ Lists the pets """

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def display_addpet():
    """Display the page that shows form to add pets. """
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        flash(f"Added {name}")
        newest_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(newest_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet-form.html', form=form)
