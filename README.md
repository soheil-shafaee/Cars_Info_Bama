# Audi Car Price Prediction Project <a href="https://www.truecar.com/used-cars-for-sale/listings/audi/?page=1">Truecar.com</a>

## Overview

This project aims to predict the prices of Audi cars by utilizing web scraping techniques to gather data from TrueCar.com and implementing a machine learning model using scikit-learn. The dataset includes information such as car name, model, city, and operation.

## Project Structure

The project is organized into three main files:

1. **`create_table.sql`**: SQL script to create the MySQL database table for storing Audi car data.
2. **`web_scraping.py`**: Python script for web scraping Audi car data from TrueCar.com and inserting it into the MySQL database.
3. **`predict_price.py`**: Python script that uses the collected data to predict car prices based on car name, model, city, and operation.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/audi-car-price-prediction.git
    cd audi-car-price-prediction
    ```

2. Install required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up a MySQL database and configure connection details in the scripts.

## Database Creation

Execute the following command to create the required MySQL database table:


##Web Scraping and Data Insertion
Run the web scraping script to collect Audi car data and insert it into the MySQL database:

bash
Copy code
python web_scraping.py
This script utilizes BeautifulSoup and requests to scrape data from TrueCar.com and inserts it into the MySQL database.
