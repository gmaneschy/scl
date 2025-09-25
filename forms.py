from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    IntegerField,
    FloatField,
    HiddenField,
    DateField,
    ValidationError)
from wtforms.validators import (
    DataRequired,
    Disabled,
    Length,
    ReadOnly,
    NumberRange)


class CadProf(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    data_nascimento = DateField('Idade', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    numero = None
