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

# delete the file
RUN rm index.sh

# EXPOSE port 80
EXPOSE 80

# entry point command
# TODO: make sure this command is actually correct
CMD ["nginx", "-g", "daemon off;"]