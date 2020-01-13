from flask import Flask, render_template, request, redirect, url_for
import json
import sqlite3
app = Flask(__name__)

def get_profile():
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    for i in c.execute('select * from persons'):
        prof_dict={'name':i[1],'age':i[2],'sex':i[3]}
    conn.commit()
    conn.close()
    return prof_dictt

def update_profile(prof):
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    c.execute('update persons set name=?,age=?,sex=? WHERE id= 1',(prof['name'],prof['age'],prof['sex']))
    conn.commit()
    conn.close()


@app.route('/get')
def get():
    num = request.args.get('num')
    num = int(num)
    num_flag = 0
    for i in range(2, num):
        if num % i == 0:
            num_flag += 1
    return render_template('p-m.html', title='Flask GET request', num_flag = num_flag)

@app.route('/profile')
def profile():
    prof_dict = get_profile()
    return render_template('profile.html', title='json', user=prof_dict)

@app.route('/edit')
def edit():
    prof_dict = get_profile()
    return render_template('edit.html', title='json', user=prof_dict)

@app.route('/update', methods=['POST'])
def update():
    prof_dict = get_profile()
    # prof_dictの値を変更
    prof_dict['name'] = request.form['name']
    prof_dict['age'] = request.form['age']
    prof_dict['sex'] = request.form['sex']

    update_profile(prof_dict)

    return redirect(url_for("profile"))

@app.route('/fizzbuzz')
def fizzbuz():
    return render_template('fizz.html')


if __name__ == "__main__":
	app.run(debug=True)
