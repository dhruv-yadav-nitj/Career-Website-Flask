from flask import Flask, render_template, jsonify
from livereload import Server

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Gurgaon, India'
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Bengaluru, India'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Hyderabad, India'
    }
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', job_data=jobs)


@app.route('/api/jobs')
def get_jobs():
    return jsonify(jobs)