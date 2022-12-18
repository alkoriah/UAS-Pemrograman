from flask import Flask, render_templates
import pymysql

app = Flask(__name__)


db = pymysql.connect(
    database='database5b-klp2',
    user='root',
    password='',
    port=3306
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mahasiswa')
def home():
    return render_template('mahasiswa.html')

@app.route('/dosen')
def home():
    return render_template('dosen.html')

@app.route('/matakuliah')
def home():
    return render_template('matakuliah.html')

@app.route('/nilai')
def home():
    return render_template('nilai.html')

@app.route('/krs')
def home():
    return render_template('khs.html')

@app.route('/krs')
def home():
    return render_template('krs.html')

@app.route('/jurusan')
def home():
    return render_template('jurusan.html')


if __name__ =='__main__':
    app.run()
