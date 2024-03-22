from main import create_app

app_gestao = create_app()

if __name__ == '__main__':
    app_gestao.run(debug=True, port=8080)