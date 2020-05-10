# About Schedule-Master

https://cmpe131-team7.herokuapp.com/home

Digital calendars are incredibly useful for setting up reminders for one-time events, as well as annual events, but digital calendars fall behind when it comes to a platform that can allow multiple users to add, delete, and modify non-overlapping events.
  
  

## System Requirements
* Python 3.7
* Flask 1.1.1
* SQLAlchemy 1.3.13

## Libraries used
* calendar
* datetime
* numpy

**Sources**:
  * Source for python calendar: https://docs.python.org/3/library/calendar.html
  * Source for datetime: https://docs.python.org/3/library/datetime.html
  * Source for numpy: https://numpy.org/
  * Calendar template from: https://codepen.io/gabrielcolombo/pen/LGzNwq

## Install pip and homebrew
For Homebrew:

```terminal
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install python
```

For pip:

```terminal
python get-pip.py
```


## Download requirements

```terminal
pip install Flask
pip install -U Flask-SQLAlchemy
pip install numpy
brew install python3
```




## How to run this app

  First, clone our repository to your desired location
```terminal
git clone https://github.com/cmpe131-spring2020/Team7.git
```
Next, enter the Project file location where you cloned the repository
```terminal
cd Team7
```
And finally, run the app 

 ```terminal
python3 run.py
```

## Navigating our website

On the homepage:

Follow the instructions on the left card if you are a guest and want to book appointments
  * Click on a person from a list of creators, and click a day on the calendar as well as the time
  * Enter your name and why you want to this meeting and submit!

Follow the instructions on the right card if you are a creator and you want to create events
  * In your settings, choose your availability times and meeting durations and click update settings and you are good to go!

