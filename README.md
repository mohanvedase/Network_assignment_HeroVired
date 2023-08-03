# Network_assignment_HeroVired

## QUESTION 1
## website on localhost using apache . create a DNS name of website as "awesomeweb"
As per given statement we write the total process  in step-wise manner in detailed way in 'awesomeweb Q1.pdf' file
### Step-1 
In this step we check the localhost portal in local search engine for any issues. if any issues are sort it out for further process  
### Step-2 
In this step we download the wamp server application this will help the system to connect the apache server. 
### Step-3
In this setp we check the localhost portal in search engine . If application properly installed , it shown wampserver webpage on localhost website 
### Step-4
in this step we copy a normal HTML code and past it in C:\wamp64\www location as 'awesomeweb' name . Then we enter localhost/awesomeweb in search engine that site host the html code which is given by us.
these are the step required for the question 1.

## QUESTION 2

## Python script to check the status of subdomains which are up and down
Here in this code we check the up and downs of the domaines of a website for this we need *request* package
###  requests package is a popular Python package for making HTTP requests. It is a simple and easy-to-use package that can be used to make requests to a variety of different websites and APIs.
<import requests>
<import time> # time package is used to time gap for the frequency of checks

def check_subdomain_status(subdomain):
### Checks the status of a subdomain
  try:
    response = requests.get("https://herovired.belong.education/profile"+ subdomain)
    if response.status_code == 404:
      return "DOWN"
    else:
      return "UP"
  except requests.exceptions.ConnectionError:
    return "DOWN"

def main():
  subdomains = ["herovired", "belong", "profile","education"]  #Checks the status of the subdomains of a website
  table = []
  for subdomain in subdomains:
    status = check_subdomain_status(subdomain)
    table.append([subdomain, status])

  print("Subdomain | Status")
  print("----------|---------")
  for row in table:
  ### the 0 and 1 represents the position arguments of the subdomain
  ### The :15 and :10 syntaxes specify the width of the columns.
    print("{0:15} | {1:10}".format(*row)) 

  while True:
   ### Time check for every min
    time.sleep(60)
    for i in range(len(table)):
      status = check_subdomain_status(table[i][0])
      table[i][1] = status
    print("Subdomain | Status")
    print("----------|---------")
    for row in table:
      print("{0:15} | {1:10}".format(*row)) 

if __name__ == "__main__":
  main()
### from this we get the status of the domains in the given website for every one minute

## QUESTION 3 
## Hosting and Scanning a website on Virtual Machine

## Install ubuntu
Install the vm virtual box and install a ubuntu instance using ubuntu 22.04 image 

## Installing Nginx

To install Nginx, use following command:
*sudo apt update
sudo apt install nginx*
check the localhost in search engine 

## Creating our own website
Default page is placed in /var/www/html/ location. 
Let’s create simple HTML page in /var/www/mohan/ (it can be anything you want). 
Create index.html file in this location.
*cd /var/www
sudo mkdir mohan
cd mohan
sudo "${EDITOR:-vi}" index.html
Paste the following to the index.html file:
<!doctype html>
<html>
<head>
 <meta charset="utf-8">
 <title>Hello, Nginx!</title>
</head>
<body>
 <h1>Hello, Nginx!</h1>
 <p>We have just configured our Nginx web server on Ubuntu Server!</p>
</body>
</html>
Save this file.
## Setting up virtual host
paste the code in
cd /etc/nginx/sites-enabled
sudo "${EDITOR:-vi}" mohan
server {
 listen 84;
 listen [::]:84;
 server_name mohan.com;
 root /var/www/mohan;
 index index.html;
 location / {
 try_files $uri $uri/ =404;
 }
}
## Activating virtual host and testing results
To make our site working, simply restart Nginx service.
sudo service nginx restart
in search engine search *localhost:84*
## Scan the virtual machine using Nmap
check the ipaddress of ubuntu server by using $ifconfig
then check the ipaddress and check the ports which are opened


  
