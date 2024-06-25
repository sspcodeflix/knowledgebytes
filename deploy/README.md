# Deployment Instructions


## Prerequisites:

Ensure Docker is installed. If not, refer to the Docker installation documentation.

https://docs.docker.com/engine/install/


Before running the deployment script (deploy.sh), ensure the following steps are completed:


## Environment Setup:

Create an ".env" file from ".env-sample" as per your requirements located in the main directory.



## Deployment Steps:

1. **Deploy All Services**

   ```sh
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. **Stop All Services**

   ```sh
   chmod +x stop.sh
   ./stop.sh
   ```

3. **MySQL Data Directory**

   ```sh
   /deploy/mysql/mysql_data/
   ```

4. **SSL Certificate Directory**

   ```sh
   deploy/certbot/letsencrypt/live/${HOSTNAME}/
   ```

5. **Nginx Configuration Directory**

   ```sh
   deploy/nginx/
   ```

6. **Gunicorn Logs Directory**

   ```sh
   gunicorn-logs/
   ```
