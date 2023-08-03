# write a python script to check the status of the subdomains which are up and down.


import requests
import time

def check_subdomain_status(subdomain):
  #Checks the status of a subdomain
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
    print("{0:15} | {1:10}".format(*row)) # the 0 and 1 represents the position arguments of the subdomain 

  while True:
    time.sleep(60) #Time check for every min
    for i in range(len(table)):
      status = check_subdomain_status(table[i][0])
      table[i][1] = status
    print("Subdomain | Status")
    print("----------|---------")
    for row in table:
      print("{0:15} | {1:10}".format(*row)) # The :15 and :10 syntaxes specify the width of the columns.

if __name__ == "__main__":
  main()