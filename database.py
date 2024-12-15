from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
conn_info = os.getenv("DATABASE_CONNECTION")

engine = create_engine(conn_info)


# --> testing purpose
'''
with engine.connect() as conn:
    res = conn.execute(text("SELECT * FROM Jobs"))  # list of all the rows
    all_res = res.all()

    print(type(res), type(all_res), type(all_res[0]))

    jobs = []
    for row in all_res:
        jobs.append(row._mapping)  # found this type conversion somewhere -> was earlier using dict(row)
    print(jobs)
    
'''

def load_job_from_db():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM Jobs"))  # list of all the rows
        all_res = res.all()
        jobs = []
        for row in all_res:
            jobs.append(row._mapping)  # found this type conversion in the comments section -> was earlier using dict(row)
        return jobs
