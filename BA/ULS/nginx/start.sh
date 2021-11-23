docker build -t nginx_image .
docker run --name reverse_proxy -dp 8080:80 nginx_image