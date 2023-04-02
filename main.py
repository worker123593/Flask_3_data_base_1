from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)


def add_jobs_item():
    db_sess = db_session.create_session()
    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = '15'
    jobs.collaborators = '2, 3'
    jobs.is_finished = False
    db_sess.add(jobs)
    db_sess.commit()


def add_person():
    db_sess = db_session.create_session()
    user = User()
    user.surname = '4'
    user.name = '4'
    user.age = 4
    user.position = '4'
    user.speciality = '4'
    user.address = '4'
    user.email = '4@mars.org'
    db_sess.add(user)
    db_sess.commit()



@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()