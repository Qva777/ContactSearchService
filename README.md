<h1>📍How to install: </h1>


<details><summary><h1>⬇Manual start:</h1></summary><br>
<h4>1 - Connect venv:</h4> 

```
python3 -m venv venv
```

<h4>2 - Activate it:</h4>
<p>For Windows</p>

``` 
.\venv\Scripts\activate
```

<p>For MacOS</p>

``` 
source venv/bin/activate 
```

<h4>3 - Install libraries:</h4>

```
pip install -r requirements.txt
```

<h4>Create DB in PostgreSQL:</h4>

```
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR
);

COPY contacts(first_name, last_name, email)
FROM '/path/to/file/nimble_contacts.csv'
DELIMITER ',' CSV HEADER;

```


<h4>Create Your .env</h4>
In order to run the application, you need to set up a .env file with the following configuration:

```
DB_NAME=<your_database_name>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
DB_HOST=<your_database_host>
DB_PORT=<your_database_port>
```

<h4>Run Celery:</h4>

```
celery -A tasks worker --loglevel=info
```

<h4>Run server:</h4>

```
python contacts_search_service.py
```

<h4>Run Tests:</h4>

```
python -m unittest discover tests
```


</details>



<details><summary><h1>📮How to connect Postman:</h1></summary><br/>
<h4>1 - Import Nimble Search into Postman</h4> 
<h4>2 - The Nimble Search collection contains requests</h4>
</details>
