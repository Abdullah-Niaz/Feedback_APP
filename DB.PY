from app import app, db

# Use the app context to access the database
with app.app_context():
    db.create_all()
