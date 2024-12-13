from flask import Flask
import random

app = Flask(__name__)  # Flask uygulaması oluşturuluyor.


def random_number():
    return random.randint(0,9)
numb = random_number()
print(numb)

@app.route("/")  # Ana rota tanımlanıyor.
def hello_world():
    return ("<h1 style='text-align: center'>Guess a number between 0-9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<int:guess>")
def guessing_check(guess):
    if guess == numb:
        return ("<h1 stlye='text-align: center'>CORRECT</h1>"
                    "<img src= 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif guess < numb:
        return ("<h1 stlye='text-align: center'>LOW</h1>"
                    "<img src= 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    else:
        return ("<h1 stlye='text-align: center'>HIGH</h1>"
                        "<img src= 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")





if __name__ == "__main__":
    app.run(debug=True)

