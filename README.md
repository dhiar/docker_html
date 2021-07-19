# docker_html

[started-app] https://docs.docker.com/get-started/02_our_app/

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