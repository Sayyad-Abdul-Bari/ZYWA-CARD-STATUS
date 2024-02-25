from app import app, db
import os
import pandas as pd
from app.models import CardStatus, db
from sqlalchemy import text

def create_all_tables():
    with app.app_context():
        db.create_all()

def populate_tables(data_folder="data"):
    with app.app_context():
        try:
            # Clear existing data from the table
            db.session.query(CardStatus).delete()

            # Reset the primary key sequence
            db.session.execute(text("ALTER TABLE card_status AUTO_INCREMENT = 1"))

            table_count = 0
            # db.session.query(CardStatus).delete()
            for filename in os.listdir(data_folder):
                if filename.startswith("Sample Card Status Info -"):
                    filepath = os.path.join(data_folder, filename)
                    df = pd.read_csv(filepath)

                    
                    # Process CSV data and populate CardStatus table
                    for _, row in df.iterrows():
                        if table_count == 0 or table_count == 1:
                            user_phone = str(row.get("User contact", "")).replace('"',"")
                            comment = row.get("Comment", "")
                        elif table_count == 2:
                            comment = 'Pickuped'
                            user_phone = row.get("User Mobile", "")
                        elif table_count == 3:
                            comment = 'Returned'
                            user_phone = row.get("User contact", "")
                        # Convert timestamp string to datetime object
                        timestamp = pd.to_datetime(row.get("Timestamp"), errors='coerce')

                        card_status = CardStatus(
                            card_id=row.get('Card ID', ''),
                            user_phone=user_phone,
                            timestamp=timestamp,
                            comment=comment,
                        )
                        db.session.add(card_status)
                    
                    # Commit changes to the database after processing each file
                    db.session.commit()

                table_count += 1
        except Exception as e:
            # Log the error with timestamp
            print(f"Timestamp: {pd.to_datetime('now')}, Services error: {e}")
            db.session.rollback()

if __name__ == "__main__":
    create_all_tables()
    populate_tables()
