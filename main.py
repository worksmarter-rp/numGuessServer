from flask import Flask
from random import randint

app = Flask(__name__)
def create_index():
    a_string = ""
    for i in range(0,10):
        a_string += f'<a href="{i}"> {i} </a>'
    return f'<br><br><p> {a_string}</p>'


my_num = randint(0,9)
@app.route('/')
def landing():
    return f'{create_index()}<br><b>'\
           '<h1>Guess a number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def evaluate(guess):
    global my_num
    if guess < my_num:
        return f'{create_index()}<br><b>{guess}</b> is too low!!<br><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > my_num:
        return f'{create_index()}<br><em>{guess}</em> is too high!!<br><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:

        my_num = randint(0,9)
        return 'That was my number!</h2><br><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"><br><p><a href="#">You can replay if you want.</a></p>'







if __name__ == '__main__':
    app.run()
