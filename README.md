# docker_html

https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages

Running docker-compose
```
docker-compose up
```

Running docker-compose
```
docker-compose up -d
```

Aktivasi venv
```
source env/bin/activate
```

Install module
```
python3 -m pip install gunicorn
```

Install multiple module
```
python3 -m pip install -r requirements.txt
```

Running simple function using flask
```
export FLASK_APP="app.main:create_app"
flask run
```

Running simple function using gunicorn
```
gunicorn -w 2  -b 0.0.0.0:8089 'app.main:create_app(testing="false")'
```