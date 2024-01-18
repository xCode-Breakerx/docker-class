# Naming

Although the name of the dockerfile doesn't really matter (you can specify the `--file` flag on docker to specify a specific file) it is a good practice to name it `Dockerfile`

# Contents

Original docker file

```
FROM nginx:alpine
COPY index.sh /usr/share/nginx/html/index.sh
RUN chmod +x /usr/share/nginx/html/index.sh

RUN cd /usr/share/nginx/html && \
bash ./index.sh && \
rm ./index.sh

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Correction proposal

```
# pull the nginx image
FROM nginx:alpine

# set the working directory so we don't have directory specify the full path each tim
WORKDIR /usr/share/nginx/html/

# COPY the desired file 
COPY index.sh .

# make the file executable
RUN chmod +x index.sh

# execute the file
CMD ./index.sh

# delete the script file
RUN rm index.sh

# EXPOSE port 80
EXPOSE 80

# entry point command
CMD ["nginx", "-g", "daemon off;"]
```

# Commands

To build the image we run the fallowing command:

```cmd
docker build -t bash .
```

This command builds a docker image named `bash`

To create a new container we run the following command

```cmd
docker run -d -p 127.0.0.1:8000:80 --name bash bash
```
This command creates a new docker container named `bash` from the template image also named `bash` and maps the port `80 -> 8000`. This is because **port 80 requires elevated privileges**, thus we bind it to another port for testing purposes. Otherwise, if not running with **admin/root privileges**, the container **will not run on port 80** 