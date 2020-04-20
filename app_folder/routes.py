from flask import render_template, redirect, flash, request
from app_folder import app, db, login
from .forms import LoginForm, RegisterForm, DeleteForm
from app_folder.models import User, Post
from flask_login import current_user, login_required, logout_user, login_user


# different URL the app will implement
@app.route("/")
@login_required
def hello():
    ''' This function will greet the user. This function welcomes the user with their username after they login.

        Returns:
            Will render the index page A.K.A. home page.
    '''
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' This is the Login function. This function checks if username and password is valid.
        
        Returns:
            Will redirect to the home page or login page depending on the flow of logic.
    '''
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect("login")
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('login.html', title='Sign In', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    ''' This is the Register function.

        Returns:
            Will redirect to the home page, login page, or registration page depending of the flow of logic.
    '''
    if current_user.is_authenticated:
        return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, your account has been created!')
        return redirect('login')
    return render_template('register.html', title='Register', form=form)
    

@app.route('/logout')
def logout():
    ''' This is the Logout function. This function will logout the user and will not allow access to any info.

        Returns:
            Will redirect to the home page.
    '''
    logout_user()
    return redirect("home")

@app.route('/delete', methods = ['GET','POST'])
def delete_account():
    ''' This is the delete account function.
    
        Returns:
            Will redirect to home or delete account page based on the flow of logic.
    '''
    form = DeleteForm()
    if form.validate_on_submit():
        if "cancel_button" in request.form:
            return redirect("settings")
        else:
            user = current_user
            db.session.delete(user)
            db.session.commit()
            flash('Sorry to see you go.')
            return redirect("home")
    return render_template('delete.html', title = 'Delete Account',form = form)
    

@app.route('/goodbye',methods = ['GET','POST'])
def goodbye():
    ''' This function brings the former user to a farewell page.
    
        Returns:
            Will redirect the user to the goodbye page.
    '''
    return render_template('goodbye.html',title = "Goodbye")
    
@app.route('/viewEvents')
def viewEvents():
    ''' This is the veiwEvents function.
    
        Returns:
            Will redirect the user to the view events page.
    '''
    return render_template('viewEvents.html', title='View Events')
    
   
@app.route('/settings')
def settings(): 
    ''' This is the settings function.
    
        Returns:
            Will redirect the user to the settings page.
    '''
    return render_template('settings.html', title='settings')
    
@app.route("/home")
def home():
    ''' This is the home function.
    
        Returns:
            This will redirect the user home.
    '''
    return render_template('home.html', title='home') 
 
    
