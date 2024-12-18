from flask import Flask, render_template, jsonify, request
from livereload import Server
from database import load_job_from_db, load_this_job, send_data_db, load_applications_from_db


app = Flask(__name__)

@app.route('/')
def home():
    jobs = load_job_from_db()
    return render_template('index.html', job_data=jobs)


@app.route('/api/jobs')  # its standard to have json routing in this format '/api/route'
def get_jobs():
    jobs = load_job_from_db()
    return jsonify(jobs)


@app.route('/jobs/<id>')  # dynamic routing
def get_this_job(id):
    job = load_this_job(id)
    if job is None:
        return "Not Found", 404
    else:
        return render_template('jobpage.html', job=job)


@app.route('/jobs/<id>/apply', methods=['POST'])
def send_this_data(id):
    data = request.form
    # send this data to db
    send_data_db(id, data)
    # send email about application received using some api
    '''will do later'''
    # show application success message
    return render_template('final.html')
    # return jsonify(data)


@app.route('/api/jobs/<id>')
def jobs_api(id):
    data = load_applications_from_db(id)
    return data
