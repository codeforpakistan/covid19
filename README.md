# COVID-19 Dashboard
This is a simple Django application that loads some datasets from Google Sheets and shows some basic analytics.


<img width="1122" alt="Screen Shot 2021-04-20 at 1 36 26 PM" src="https://user-images.githubusercontent.com/743962/115365544-e9f62880-a1dd-11eb-8401-a1cb914b2eb9.png">



### Data Source
We are using the COVID-19 Daily Sitreps published by the National Institute of Health, and compiling them into a [Google Sheets](https://docs.google.com/spreadsheets/d/1ljt1URrDZRqTK0qke2yV3lD24CqrfnemhLKClMBYYrQ/) document. Please send us a request if you want access to the document. 

### Contributing
You can checkout the code and run the following commands to get started. 

    python -m venv env               # Setup virtual environment
    source env/bin/activate          # Activate virtual environment
    pip install -r requirements.txt  # Install required packages

Use `.env.example` to create or update values in `.env`. 

Run the management commands to import data from Google Sheets.

    python manage.py sheets	     # Import national data
    python manage.py comparison      # Import international comparison

Run the development server.

    python manage.py runserver	     # Run development server
