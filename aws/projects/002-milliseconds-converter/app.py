from flask import Flask, render_template,request

app = Flask(__name__)

def convert(milliseconds):
    # one hour in milliseconds
    hour_in_milliseconds = 60*60*1000
    # calculate the hours within given milliseconds
    hours = milliseconds // hour_in_milliseconds
    # calculate milliseconds left over when hours subtracted
    milliseconds_left = milliseconds % hour_in_milliseconds
    # one minute in milliseconds
    minutes_in_milliseconds = 60*1000
    # calculate the minutes within remainder milliseconds
    minutes = milliseconds_left // minutes_in_milliseconds
    # calculate milliseconds left over when minutes subtracted
    milliseconds_left %= minutes_in_milliseconds
    # calculate the seconds within remainder milliseconds
    seconds = milliseconds_left // 1000
    # format the output string
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)

@app.route("/")
def index():
    return render_template("index.html", developer_name = "E2139-Hasan")

@app.route("/", methods = ["POST"])
def result():
    alpha = request.form["number"]
    if not alpha.isdecimal() or int(alpha) <= 0:
        return render_template("index.html", not_valid = True)

    return render_template("result.html", milliseconds = alpha, result =convert(int(alpha)), developer_name = "E2139-Hasan")







if __name__ == "__main__":
    app.run(debug=True)
