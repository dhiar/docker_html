from flask import Flask
import connexion

def post_users(query):
  users = []
  return query

options = {"swagger_ui": True}
app = connexion.FlaskApp(__name__, specification_dir='openapi/',
  options=options)

app.add_api('swagger.yaml', arguments={'api_local': 'local_value'})

if __name__ == '__main__':
  app.run(port=5000)
    # app.run(port=8080, server='gevent')