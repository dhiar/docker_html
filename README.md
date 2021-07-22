# docker_html

[connexion-example] https://github.com/dhiar/connexion-example-1

Build code to container
```
docker build --tag python-docker-dev .
```

```
docker run --rm -d -v mysql:/var/lib/mysql \
  -v mysql_config:/etc/mysql -p 3306:3306 \
  --name mysqldb \
  -e MYSQL_ROOT_PASSWORD=manager247 \
  mysql:8.0.21
```

Build & run 
```
docker-compose -f docker-compose.yml up --build
```

Remove volume yang tidak digunakan
```
docker volume prune
```

Example POST /prediction data
```
[
    {
        "category": "talk.politics.misc",
        "text": "Angela Merkel just walked into her fourth term as chancellor of Germany.Her party, the Christian Democrats (CDU), picked up 32.5 percent of the votes in Sunday's election, according to the first exit polls issued at 6 pm German local time."
    }
]
```
