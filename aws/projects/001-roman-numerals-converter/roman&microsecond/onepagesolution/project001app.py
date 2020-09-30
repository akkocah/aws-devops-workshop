from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def convert(decimal_num):
    # set the dictionary for roman numerals
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    # initialize the result variable
    num_to_roman = ''
    # loop the roman numerals, calculate for each symbol and add to the result
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i      
    return num_to_roman

def convert1(milliseconds):
    hour_in_milliseconds = 60*60*1000
    hours = milliseconds // hour_in_milliseconds
    milliseconds_left = milliseconds % hour_in_milliseconds
    minutes_in_milliseconds = 60*1000
    minutes = milliseconds_left // minutes_in_milliseconds
    milliseconds_left %= minutes_in_milliseconds
    seconds = milliseconds_left // 1000
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)

@app.route("/")
def index():
    return render_template("index.html", developer_name = "E2150 - Ali Ihsan")

@app.route("/", methods = ["POST"])
def result():
    roman_num = request.form["number"]
    milli_num = request.form["second"]
    if roman_num: 
        if (not roman_num.isdecimal()) or (not (0 < int(roman_num) < 4000)):
            return render_template("index.html", not_valid = True, developer_name = "E2150 - Ali Ihsan")
        return render_template("index.html", roman = True, developer_name = "E2150 - Ali Ihsan", number_decimal = roman_num, number_roman = convert(int(roman_num)))
    elif milli_num:
        if not milli_num.isdecimal() or int(milli_num) <= 0:
            return render_template('index.html', not_valid_second = True, developer_name = "E2150-Ali ihsan")
        return render_template('index.html', micro = True, milliseconds = milli_num, result = convert1(int(milli_num)), developer_name = "E2150-Ali ihsan")



if __name__ == "__main__":
    app.run(debug = True)
    # app.run(host='0.0.0.0', port=80)
