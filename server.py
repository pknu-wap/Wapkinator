from flask import Flask, render_template, request
import pymysql, db

app = Flask(__name__)


@app.route('/')
@app.route('/question1')
def question1():
    return render_template('phase.html')


@app.route('/question2', methods=['POST'])
def question2():
    global phase
    phase = request.form["bool"]
    return render_template('grade.html')


@app.route('/question3', methods=['POST'])
def question3():
    global num
    num = request.form["bool"]
    return render_template('sex.html')


@app.route('/question4', methods=['POST'])
def question4():
    global gender
    gender = request.form["bool"]
    return render_template('age.html')


@app.route('/question5', methods=['POST'])
def question5():
    global age
    age = request.form["bool"]
    return render_template('major.html')


@app.route('/question6', methods=['POST'])
def question6():
    global depart
    depart = request.form["bool"]
    return render_template('major_it.html')


@app.route('/question7', methods=['POST'])
def question7():
    global depart_it
    depart_it = request.form["bool"]
    return render_template('last_name.html')


@app.route('/question8', methods=['POST'])
def question8():
    global last_name
    last_name = request.form["bool"]
    return render_template('jeong.html')


@app.route('/result', methods=['POST'])
def result():
    global jeong_in_name
    jeong_in_name = request.form["bool"]
    answer = db.choice(phase, num, gender, age, depart, depart_it, last_name, jeong_in_name)
    if len(answer) == 0:
        return render_template('result.html') #찾기 실패
    else:
        print(answer)
    return render_template('result.html', data=answer)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)



