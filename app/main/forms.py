from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class UpdateProfile(FlaskForm):
    bio = StringField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category=SelectField("Category",
        choices=[("Interview","Interview"),("Motivation","Motivation"),("Product","Product"),("Promotion","Promotion")],validators = [DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[DataRequired()])
    submit=SubmitField('Submit')