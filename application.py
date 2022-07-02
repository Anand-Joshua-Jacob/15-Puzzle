import os, random
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_FILE_DIR"] = mkdtemp()
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")


nums = random.sample(range(1, 16), 15)
nums.append(' ')
#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ' ', 15]

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "GET":
        return render_template("game.html", nums=nums)
    else:
        for i in range(16):
            if nums[i] == ' ':
                break

        if request.form['name'] == 'up':
            if i < 4:
                nums[i+12], nums[i], nums[i+4], nums[i+8] = nums[i], nums[i+4], nums[i+8], nums[i+12]
            else:
                nums[i], nums[i-4] = nums[i-4], nums[i]


        elif request.form['name'] == 'down':
            if i > 11:
                nums[i], nums[(i+3)%15], nums[(i+7)%15], nums[(i+11)%15] = nums[(i+11)%15], nums[i], nums[(i+3)%15], nums[(i+7)%15]
            else:
                nums[i], nums[i+4] = nums[i+4], nums[i]


        elif request.form['name'] == 'left':
            if (i%4) == 0:
                nums[i+3], nums[i], nums[i+1], nums[i+2] = nums[i], nums[i+1], nums[i+2], nums[i+3]
            else:
                nums[i], nums[i-1] = nums[i-1], nums[i]

        elif request.form['name'] == 'right':
            if (i%4) == 3:
                nums[i-3], nums[i], nums[i-1], nums[i-2] = nums[i], nums[i-1], nums[i-2], nums[i-3]
            else:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, " "]

        if nums == key:
            return render_template("won.html")

        return render_template("game.html", nums=nums)
