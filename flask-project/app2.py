from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_profile():
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    prof_list=[]
    for i in c.execute('select * from persons'):
        prof_list+=[{'id':i[0],'name':i[1],'age':i[2],'sex':i[3]}]
    conn.commit()
    conn.close()
    return prof_list

def update_profile(prof):
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    c.execute('update persons set name=?,age=?,sex=? WHERE id= ?',
    )
    conn.commit()
    conn.close()

def insert_profile(prof_dict):
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    c.execute('insert into persons(name,age,sex) values(:name, :age, :sex);', prof_dict)
    conn.commit()
    conn.close()

def delete_profile(id):
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    c.execute('delete from persons where id = ?', (id,)) 
    conn.commit()
    conn.close()


@app.route('/profile')
def profile():

    prof_dict = get_profile()
    return render_template('profile1.html', title='json', user=prof_dict)

@app.route('/edit/<int:id>')
def edit(id):
    prof_list = get_profile()
    prof_dict = prof_list[id-1]
    return render_template('edit1.html', title='sql', user=prof_dict)

@app.route('/add')
def add():
    return render_template('add.html', title='sql')

@app.route('/insert', methods=['POST'])
def insert():
    prof_dict = {}
    # prof_dictの値を変更
    prof_dict['name'] = request.form['name']
    prof_dict['age'] = request.form['age']
    prof_dict['sex'] = request.form['sex']

    insert_profile(prof_dict)

    return redirect(url_for('profile'))

@app.route('/delete/<int:id>')
def delete(id):
    delete_profile(id)

    return redirect(url_for('profile'))


if __name__ == "__main__":
    app.run(debug=True)
