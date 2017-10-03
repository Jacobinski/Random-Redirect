import random
from flask import Flask, redirect

app = Flask(__name__)

# Note: http:// or https:// must be the prefix for proper redirection
websites = [
        "http://www.github.com",
        "https://www.twitter.com",
        "http://www.reddit.com",
    ]

@app.route('/')
def index():
    website = random.choice(websites)
    return redirect(website)

if __name__ == "__main__":
    app.run()
