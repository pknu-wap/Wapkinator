from flask import Flask, render_template, request
import pymysql, db

app = Flask(__name__)

phase = 0
num = 0
gender = 0
age = 0
depart = 0


@app.route('/')
@app.route('/question1')
def question1():
    return render_template('phase.html')


@app.route('/question2')
def question2():
    #phase = request.form["phase"]
    return render_template('grade.html')


@app.route('/question3')
def question3():
    num = request.form["grade"]
    return render_template('sex.html')


@app.route('/question4')
def question4():
    gender = request.form["sex"]
    return render_template('age.html')


@app.route('/question5')
def question5():
    age = request.form["age"]
    return render_template('major.html')


@app.route('/result')
def result():
    depart = request.form["major"]
    answer = db.choice(phase, num, gender, age, depart)
    print(answer)  # 프론트로 반환
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)



