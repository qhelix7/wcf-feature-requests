# WCF Application Exercise #

This is the beginnings of a web application which views and submits feature requests for a hypothetical product.


## Build the Vue app ##
From the project directory
```
cd app
npm install
npm run build
```

## Set up server ##
### .env ###
From the project directory, copy the `example.env` file to `.env` and adjust the values as desired.
Especially make sure to set the `DIST_DIR` to the correct path of the built Vue app code (`/path/to/wcf-feature-requests/app/dist`).

If Pipenv is installed and run
```
cd server

pipenv install
pipenv install --dev
```

Otherwise, create a Python virtualenv for the project and run
```
cd server
pip install -r requirements.txt
```


### Start the database ###
From the project directory, run
```
docker-compose up -d database
```

### Set up the database ###
From the project/server directory (and with the virtualenv active), run
```
alembic upgrade head
```

### Start the server ###
```
python -m feature_server.main
```

You should now be able to view the application in a local browser window.


## Testing ##
From the `server` directory
```
pytest
```


## Things I Didn't Get To: ##
1. Data validation on the front and backends. Using something like Swagger would be helpful for sharing the schemas between Python and JavaScript.
2. Form validation.
3. Editing and completing requests.
4. Date picker for the frontend.
5. Authentication.
6. Error handling and logging.
7. Frontend unit tests.
8. Getting the server to run from Docker.
9. nicer-looking interface, etc.