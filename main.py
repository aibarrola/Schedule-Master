from app_folder.models import User, Event

def create_new_user(username,email,password):

	user = User(username = username,email = email)
	user.set_password(password)

	return user

def create_new_event(username,date,time,guestname,description,military):
	event = Event(username = username, eventDate = date, eventTime = time,guestname = guestname, description = description,militaryTime = military)

	return event