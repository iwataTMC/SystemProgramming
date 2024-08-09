from flask import Flask
from datetime import datetime

app = Flask(__name__)


def get_greeting():
    day = datetime.now().strftime("%A")
    greetings = {
        "Monday": "How was your weekend?",
        "Tuesday": "Hope your week is off to a good start!",
        "Wednesday": "Happy hump day!",
        "Thursday": "The weekend is almost here!",
        "Friday": "Thank God It's Friday! Any plans for the weekend?",
        "Saturday": "Enjoy your weekend!",
        "Sunday": "Have a relaxing Sunday!",
    }
    return greetings.get(day, "Hello! Have a great day!")


@app.route("/")
def home():
    return f"<h1>{get_greeting()}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
