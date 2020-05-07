import main
from app_folder.models import User

def test_main():
    # set up test
    a = [1,2,3]
    b = [4,5]
    assert main.concat_lists(a,b) == [1,2,3,4,5]

def test_user():

	username = "bobross"
	email = "bobross@gmail.com"
	password = "bobrosspainting"

	new_user = main.create_new_user(username,email,password)

	assert new_user.username == "bobross"
	assert new_user.email == "bobross@gmail.com"
	assert new_user.check_password(password) == True