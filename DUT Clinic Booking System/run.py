from app import create_app, db  # <-- fixed import

app = create_app()

with app.app_context():
    db.create_all()  # create tables if they don't exist

if __name__ == "__main__":
    app.run(debug=True)
