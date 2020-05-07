from app_folder.models import User
def concat_lists(list_A, list_B):
    return list_A + list_B

def create_new_user(username,email,password):

	user = User(username = username,email = email)
	user.set_password(password)

	return user