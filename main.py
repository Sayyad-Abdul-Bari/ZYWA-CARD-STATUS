from app import app
from app.services import create_all_tables, populate_tables

if __name__ == "__main__":
    print("Running main.py...")  # Add this line for debugging
    create_all_tables()
    populate_tables()
    app.run(debug=True, use_reloader=False)