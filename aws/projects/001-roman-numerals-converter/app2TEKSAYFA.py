from flask import Flask,render_template,redirect,url_for,request

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

@app.route("/")
def root():
    return render_template("index.html", not_valid = False, developer_name="E2139-Hasan Ak")

@app.route("/", methods = ["POST"])
def result():
    alpha = request.form["number"]
    if (not alpha.isdecimal()) or (not (0 < int(alpha) < 4000)):
        return render_template("index.html", not_valid = True, developer_name="E2139-Hasan Ak")
    number = int(alpha)
    return render_template("index.html", number_decimal = number, number_roman =convert(number), not_valid1 = True )

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)