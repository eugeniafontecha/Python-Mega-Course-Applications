import time
from datetime import datetime as dt


#this program blocks certain websites during working hours.
#It runs as a background process (.pyw)
#A task schedule needs to be created (go to create_task_schedule.txt)

hosts_temp="hosts" #for testing, doesn't need admin privileges
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" #needs to be run as admin
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.netflix.com","netflix.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+ "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)