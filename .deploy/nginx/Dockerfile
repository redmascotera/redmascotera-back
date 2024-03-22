FROM nginx:1.25.2-alpine

# Copy nginx configuration
COPY ./nginx.conf /etc/nginx/nginx.conf
# Copy conf.d configuration
COPY ./conf.d /etc/nginx/conf.d

# Remove default.conf
RUN rm /etc/nginx/conf.d/default.conf