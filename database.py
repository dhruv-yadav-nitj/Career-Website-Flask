from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
conn_info = os.getenv("DATABASE_CONNECTION")

engine = create_engine(conn_info, echo=True)


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
            jobs.append(dict(row._mapping))
        return jobs


def load_this_job(id):
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM Jobs WHERE id = :val'), [{"val": id}])
        rows = result.all()  # either 1 or 0 rows
        if len(rows) == 0:
            return None
        else:
            return (rows[0]._mapping)


def send_data_db(id, data):
    with engine.connect() as conn:
        query = text(
            """
            INSERT INTO Applications (
                job_id, first_name, last_name, email, phone, address1, city, state, zip, link
            ) VALUES
            (:job_id, :first_name, :last_name, :email, :phone, :add1, :city, :state, :zip, :resume);
            """
        )
        
        params = {
            "job_id": id,
            "first_name": data['firstname'],
            "last_name": data['lastname'],
            "email": data['email'],
            "phone": str(data['phone']),
            "add1": data['address1'],
            "city": data['city'],
            "state": data['state'],
            "zip": data['zip'],
            "resume": data['resumelink']
        }
        
        conn.execute(query, params)
        conn.commit()  # needed when we need to write new data to the database
