# ZYWA Card Status API Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Setup](#setup)
4. [Configuration](#configuration)
5. [Running the Application Flow](#running-the-application-flow)
6. [Usage](#usage)
7. [Dependencies](#dependencies)

## Introduction

This documentation provides an overview of the ZYWA Card Status API, which is designed to return the current status of a user's card based on data provided by partner companies. The API is built with Flask, SQLAlchemy, and utilizes CSV files to gather information about card status.

## Project Structure

The project follows the structure below:

```plaintext
project 1.0/
|-- app/
|  |-- __init__.py
|  |-- models.py
|  |-- routes.py
|  |-- services.py
|  |-- templates/
|  |  |-- index.html
|-- data/
|  |-- Sample Card Status Info - Pickup.csv
|  |-- Sample Card Status Info - Delivery exceptions.csv
|  |-- Sample Card Status Info - Delivered.csv
|  |-- Sample Card Status Info - Returned.csv
|-- config.py
|-- main.py
|-- requirements.txt
```

1. **app/__init__.py:** Initializes the Flask application and sets up the database.

2. **app/models.py:** Defines the CardStatus model using SQLAlchemy.

3. **app/routes.py:** Contains the API endpoints, including `/get_card_status`.

4. **app/services.py:** Includes functions for database setup, data population, and other utility functions.

5. **app/templates/index.html:** Provides a simple HTML template for the web interface.

6. **main.py:** The entry point of the application, responsible for creating tables and populating data.

7. **requirements.txt:** Lists the dependencies required to run the application.

## Setup

To set up the project, follow these steps:

1. Clone the repository: `git clone https://github.com/Sayyad-Abdul-Bari/ZYWA-CARD-STATUS.git
2. Install dependencies: `pip install -r requirements.txt`
3. Update configuration: Open `config.py` and modify the database configuration variables according to your setup.

## Configuration

Open `config.py` and modify the following variables based on your database configuration:


Certainly! Below is the textual representation of the flow after running `main.py`, formatted for inclusion in the `readme.md`:

## Running the Application Flow

1. **Run `main.py`:**
   - Execution starts at the `main.py` file.

2. **Create Tables:**
   - The `create_all_tables()` function is called from `app/services.py`.
   - Flask's SQLAlchemy is used to create the necessary tables in the database based on the defined models.

3. **Populate Tables:**
   - The `populate_tables()` function is called from `app/services.py`.
   - The function reads CSV files from the `data` folder and processes them.
   - For each CSV file, the data is extracted and used to populate the `CardStatus` table in the database.
   - Timestamps are converted to datetime objects, and relevant data is stored in the database.

4. **Flask Application Setup:**
   - Flask initializes the application from `app/__init__.py`.
   - The application configuration is set up, including the database URI and tracking modifications.

5. **Flask Application Run:**
   - The Flask application is run from `main.py`.
   - The application starts listening for incoming requests on a specified host and port (by default, `localhost:5000`).

6. **Access Web Interface:**
   - Users can access the web interface by navigating to `http://localhost:5000/`.
   - The web interface is served using the Flask `render_template` function, displaying a form to input search parameters.

7. **API Request:**
   - Users can make API requests by entering search parameters and clicking the "SUBMIT" button on the web interface.
   - The request is sent to the `/get_card_status` endpoint.

8. **`/get_card_status` Endpoint Handling:**
   - The `/get_card_status` endpoint is defined in `app/routes.py`.
   - The endpoint receives the parameters from the request.
   - It checks for missing or invalid parameters and returns appropriate error responses if necessary.

9. **Database Query:**
   - The endpoint uses SQLAlchemy to query the `CardStatus` table based on the provided parameters.
   - If a matching record is found, the latest card status information is retrieved.

10. **API Response:**
   - The `/get_card_status` endpoint returns a JSON response with the card status information.
   - If an error occurs (e.g., missing parameters or no matching record), an error response is returned.

11. **Web Interface Update:**
   - The web interface, if used, dynamically updates to display the timestamp, comment, and any error message received from the API response.

12. **Application Continues to Run:**
   - The Flask application continues to run, listening for additional requests.


## Usage

1. Access the web interface at `http://localhost:5000/` to interact with the API visually.
2. Use the `/get_card_status` API endpoint programmatically by making a GET request with the required parameters.

## Dependencies

- Flask==2.3.3
- Flask-SQLAlchemy==3.1.1
- pandas==1.5.0
- mysql-connector-python==8.3.0
- Flask-migrate==4.0.5
- Flask-Script==2.0.6

Make sure to have these dependencies installed before running the application.