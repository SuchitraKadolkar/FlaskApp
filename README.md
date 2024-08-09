# FlaskApp
# Flask Data Retrieval and Processing Application

## Overview
This is simple flask application which returns the actual data as well as processed data.

1. **API Endpoint for Data Retrieval:** Fetches mock data (for now we have defined it earlier in code).
2. **Data Processing:** Processes the fetched data by transforming text values to uppercase.

## Setup Instructions

### Pre-requisites
Python3 should be installed on the system.

### 1. Clone the repository
git clone https://github.com/SuchitraKadolkar/FlaskApp.git
cd flask-app-task

### 2. Run the commands
pip install -r requirements.txt
python3 main.py

### 3. Test functionality
Use Postman tool or open the terminal and run the below curl commands

1. curl http://127.0.0.1:5000/fetch-data
2. curl http://127.0.0.1:5000/get-processed-data
