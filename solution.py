def main():
    a = input()
    global_init(a)
    session = create_session()
    for user in session.query(User).filter(User.address == "module_1" and 'engineer'
                                           not in User.speciality and 'engineer' not in User.position):
        print(user.id)


if __name__ == '__main__':
    main()
