from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species Name")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
