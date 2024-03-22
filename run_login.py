from login.app import create_app_login


create_app_login()

app_login = create_app_login()


if __name__ == '__main__':
    app_login.run(debug=True, port=5000)