#### API Request Validation

This project create a simple implementation to add schema request validation to python based apis
It can be used with Flask, Django or any other api framework. 

#### Installation
create your project folder and a virtual environment

```sh
mkdir request-validation
cd request-validation

# Make sure you have virtualenv setup
virtaulenv packges

pip install .
```

#### Running the flask webserver
```sh
python app.py
```

#### Invoking the API

The below snippet requires using httpie https://httpie.io/

```sh
http POST http://localhost:3000/api/v1/foo \
--raw '{
    "user":{
        "name": "foo bar"
    }
}'

```