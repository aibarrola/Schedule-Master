import main
from app_folder.models import User, Event

def test_user():

	username = "bobross"
	email = "bobross@gmail.com"
	password = "bobrosspainting"

	new_user = main.create_new_user(username,email,password)

	assert new_user.username == "bobross"
	assert new_user.email == "bobross@gmail.com"
	assert new_user.check_password(password) == True

def test_event():
	
	username = "johncena"
	date = "5/5/2020"
	time = "8:00-9:00"
	guestname = "dwaynejohnson"
	description = "wrestling"
	military = "8.0"

	event = main.create_new_event(username,date,time,guestname,description,military)

	assert event.username == "johncena"
	assert event.eventDate == "5/5/2020"
	assert event.eventTime == "8:00-9:00"
	assert event.guestname == "dwaynejohnson"
	assert event.description == "wrestling"
	assert event.militaryTime == "8.0"





