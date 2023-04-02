from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)


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


def main():
    db_session.global_init("db/blogs.db")
    add_person()



if __name__ == '__main__':
    main()