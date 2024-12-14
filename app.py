from flask import Flask, render_template, jsonify
from livereload import Server

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Gurgaon, India',
        'experience': '0-1 years'
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Bengaluru, India',
        'experience': '0-1 years'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Hyderabad, India',
        'experience': '5-6 years'
    }
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', job_data=jobs)


@app.route('/api/jobs')
def get_jobs():
    return jsonify(jobs)