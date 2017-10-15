import random
from flask import Flask, redirect

app = Flask(__name__)

# Note: http:// or https:// must be the prefix for proper redirection
websites = [
        "https://goo.gl/forms/FWuOP1Ytw8T0cM3a2",
        "https://goo.gl/forms/aBfYH3CsoonSzBUn1",
        "https://goo.gl/forms/AKWAOvOFRmjSUJAV2",
        "https://goo.gl/forms/DsFBq1C4cSELvLTj1",
        "https://goo.gl/forms/sU1CZDEjjfsTiBsz1",
        "https://goo.gl/forms/7Kba0aGql39nL2jg2",
        "https://goo.gl/forms/HFs8VPinD7gA3HWF3",
        "https://goo.gl/forms/NZeJPoVcfgO5Xk903"
    ]

@app.route('/')
def index():
    website = random.choice(websites)
    return redirect(website)

if __name__ == "__main__":
    app.run()
