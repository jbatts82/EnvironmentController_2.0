###############################################################################
# File Name  : forms.py
# Date       : 08/24/2020
# Description: Fields are defined as class variables. 
###############################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from config import Config

class GraphConfigForm(FlaskForm):
	channel = SelectField(u'Channel Number', choices=[('ch1', 'Channel 1'), ('ch2', 'Channel 2'), ('ch3', 'Channel 3'), ('ch4', 'Channel 4')])
	time = IntegerField('Begin Graph X Mins Ago')
	submit = SubmitField('Submit')

class Data_To_Show(FlaskForm):
	show_temperature = BooleanField("Temperature")
	show_humidity = BooleanField("Humidity")
	show_heater = BooleanField("Heater")
	show_light = BooleanField("Light")
	show_fan = BooleanField("Fan")
