from flask import Flask, render_template, request,redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        connection = sqlite3.connect('da_answers.db')
        cursor = connection.cursor()

        #Diri tong makuha ang answer gikan sa form nimo ga request ka para makuha to nimong mga data 
        answer1 = request.form.get('answer')
        answer2 = request.form.get('answer2')
        answer3 = request.form.get('answer3')
        answer4 = request.form.get('answer4')
        answer5 = request.form.get('answer5')

        #way nga mag insert kag data sa imong database
        cursor.execute('''
            INSERT INTO da_answer (answer, answer2, answer3, answer4, answer5)
            VALUES (?, ?, ?, ?, ?)
        ''', (answer1, answer2, answer3, answer4, answer5))

        #mag save ka saimong gi insert
        connection.commit()
        connection.close()
    return render_template('index.html')

@app.route('/display')
def display():
    connection = sqlite3.connect('da_answers.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM da_answer')
    data = cursor.fetchall()
    connection.close()

    return render_template('display.html', data=data)


@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        connection = sqlite3.connect('da_answers.db')
        cursor = connection.cursor()

        answer1 = request.form.get('answer')
        answer2 = request.form.get('answer2')
        answer3 = request.form.get('answer3')
        answer4 = request.form.get('answer4')
        answer5 = request.form.get('answer5')

        cursor.execute('''
            UPDATE da_answer
            SET answer=?, answer2=?, answer3=?, answer4=?, answer5=?
            WHERE id=?
        ''', (answer1, answer2, answer3, answer4, answer5, id))

        connection.commit()
        connection.close()
        return redirect(url_for('display'))

    connection = sqlite3.connect('da_answers.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM da_answer WHERE id = ?', (id,))
    data = cursor.fetchone()
    connection.close()

    return render_template('update.html', data=data)


@app.route('/<int:id>/delete', methods = ['GET','POST'])
def delete(id):
    connection = sqlite3.connect('da_answers.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM da_answer WHERE id = ?', (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('display'))


if __name__ == '__main__':
    app.run(debug=True)

