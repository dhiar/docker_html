FROM httpd:2.4-alpine

# COPY index.html /usr/local/apache2/htdocs
COPY . /usr/local/apache2/htdocs
# seluruh file di copy ke /usr/local/apache2/htdocs
