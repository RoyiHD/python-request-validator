#### API Request Validation

This project create a simple implementation to add schema request validation to python based apis
It can be used with Flask, Django or any other api framework. 

#### Installation
create your project folder and a virtual environment

```sh

# If you choose to use a dedicated virtual env, I recommend using virtualenv
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