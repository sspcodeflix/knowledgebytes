# Deployment Instructions

Before running the deployment script (deploy.sh), ensure the following steps are completed:

## Prerequisites:

1. **Install Docker**

Ensure Docker is installed. If not, refer to the Docker installation documentation.

   ```sh
   https://docs.docker.com/engine/install/
   ```

2. **Open Ports 80 TCP & 443 TCP**

   Port 80 TCP & 443 TCP is required to be open and accessible from any kind of firewall which includes Network Layer Firewall, Or Server Level Firewall so that Certbot can complete DNS Verification Challange & SSL Generation can be completed & if certbot fails to complete dns challance it will fail to generate ssl certficate as well & due to this Nginx Production Server will fail to start due to SSL certificates no being present in this ssl certificate location "/deploy/certbot/letsencrypt"

3. **Update DNS of Your Domain**

   Ensure that you update your DNS settings as follows:

   DNS Record Details:

   Type: 'A'

   Name: "example.com"

      For root domain (e.g., 'example.com'): '@'
      or subdomain (e.g., 'api.example.com'): 'api'

   Content: "127.0.0.1" 
   
      Replace '127.0.0.1' with your server's public IP address.

4. **Clone The Repository**

   ```sh
   git clone https://github.com/sspcodeflix/knowledgebytes
   ```

5. **Update the ".env" file.**

   Copy all contents from the ".env-sample" file and create a new file named ".env"

   The content of the .env file should appear like this:

   ```sh
   SECRET_KEY="your-secret-key" # HERE ANY SECRET CAN BE USED, IT WILL BE USED BY PYTHON
   FLASK_APP="manage.py"
   FLASK_ENV="production" #VALUES CAN BE "development" or "production" 
   DB_USER="root"  #MYSQL ROOT USERNAME
   DB_PASSWORD="password" #MYSQL ROOT USER PASSWORD # consumed by docker & python
   DB_HOST="172.17.0.1" #172.17.0.1 #MYSQL HOST # consumed by python
   DB_PORT="3306" #MYSQL PORT # consumed by python
   DB_NAME="db" #MYSQL DB NAME # consumed by docker & python
   HOSTNAME="example.com"  #THIS DOMAIN WILL BE USED BY CERTBOT & NGINX TO GET SSL & RUN IT
   EMAIL="info@example.com" # THIS EMAIL WILL BE USED TO GET SSL THROUGH CERTBOT
   ```

4. **Please run 'deploy.sh' as 'root'.**

   Ensure you are logged in as the 'root' user and have the necessary permissions to execute this code.

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

## Configuration, logs, and data directories are for reference purposes only:

   1. **MySQL Data Directory**

      ```sh
      deploy/mysql/mysql_data/
      ```

   2. **SSL Certificate Directory**

      ```sh
      deploy/certbot/letsencrypt/live/example.com/
      ```

   3. **Nginx Configuration Directory**

      ```sh
      deploy/nginx/
      ```

   4. **Gunicorn Logs Directory**

      ```sh
      gunicorn-logs/
      ```

## Troubleshooting:

   1. If you encounter an error like 'failed to create network,' your Docker might not be running correctly. Simply restart Docker as 'root' to resolve this issue.

         ```sh
         sudo systemctl restart docker
         ```

   2. To reset the MySQL server and delete all its data, delete everything inside the following directory and then restart the MySQL server.

         ```sh
         deploy/mysql/mysql_data/
         ```

   3. If Python fails, it could be because the MySQL server isn't running and you've set the 'production' environment variable in the .env file. Alternatively, recent updates to your Python code may be causing the error. To test, change the .env variable to 'development'; if the code is correct, it should start with a local DB file as the database.

   4. If Certbot fails, it could be because you haven't opened TCP ports 80 and 443. This can cause SSL DNS verification to fail, leading to Nginx failure since it can't obtain the SSL certificate.

      Other possible reasons include:

         1. The hostname isn't pointing to your server's public IP. Update the 'A' record to reflect your server's public IP.

         2. TCP ports 80 and 443 are blocked, either by a network firewall or your server's firewall. Ensure these ports are allowed in your firewall rules.

         3. The SSL generation limit for your hostname has been reached, causing the failure. Try using a different domain or subdomain.

   5. If Nginx fails, it may be due to Certbot's inability to obtain or generate an SSL certificate for the hostname specified in the .env file. Consider trying another hostname.

   6. Starting Nginx in Production Mode with Custom SSL Certificate

      1. Navigate to the directory /deploy/certbot/letsencrypt.

            Create a directory named "live", and inside it, create another directory named after your "hostname" (e.g., "example.com" or "api.example.com").

      2. Save your SSL certificate files in this directory structure so that Nginx can load them:

            SSL Certificate: /deploy/certbot/letsencrypt/live/example.com/fullchain.pem;
            SSL Certificate Key: /deploy/certbot/letsencrypt/live/example.com/privkey.pem;

