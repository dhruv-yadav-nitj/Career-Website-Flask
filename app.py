from flask import Flask, render_template, jsonify
from livereload import Server
from database import load_job_from_db


app = Flask(__name__)

@app.route('/')
def home():
    jobs = load_job_from_db()
    return render_template('index.html', job_data=jobs)


@app.route('/api/jobs')  # its standard to have json routing in this format '/api/route'
def get_jobs():
    jobs = load_job_from_db()
    return jsonify(jobs)