# Python_automation

## Python Fundamentals
- Variables and Data Types:
```python
name = "Alice"
age = 25
is_active = True
```
- Input/Output:
```python
user_input = input("Enter your name: ")
print(f"Hello, {user_input}")
```
- Control Flow:
```python
if age > 18:
    print("Adult")
else:
    print("Minor")
```
- Loops:
```python
for i in range(5):
    print(i)

while age > 0:
    age -= 1
```
---
## Data Structures
- Lists:
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])
```

- Dictionaries:
```python
person = {"name": "Alice", "age": 25}
print(person["name"])
```

- Tuples:
```python
coordinates = (10, 20)
```
- Sets:
```python
unique_items = {1, 2, 3, 3}
```

---

## Functions
- Define and call functions:
```python
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```

- Lambda functions:
```python
add = lambda x, y: x + y
print(add(2, 3))
```
---
## File Handling
- Read/Write files:
```python
with open("test.txt", "w") as file:
    file.write("Hello, File!")

with open("test.txt", "r") as file:
    print(file.read())
```
---
## Object-Oriented Programming (OOP)

- Classes and Objects:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}!"

p = Person("Alice", 25)
print(p.greet())
```
---
- Inheritance:
```python
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

```

---
##  Modules and Packages
- Importing modules:
```python
import math
print(math.sqrt(16))
```
- Create your own module:
```python
mkdir mypackage
echo "def say_hello(): print('Hello!')" > mypackage/my_module.py
```
- Use it:
```python
from mypackage.my_module import say_hello
say_hello()
```

---
## Error Handling
- Try-Except:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
```
---

## Python for Scripting
### Web Scraping
- Using requests and BeautifulSoup:
```bash
pip install requests beautifulsoup4
```
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
```
---

###  Working with APIs
- Using requests:
```python
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    print(response.json())
```

---
## Automation with Python
### System Automation
- Automate tasks with os and subprocess:
```python 
import os
import subprocess
os.system("echo Hello")

subprocess.run(["ls", "-l"])
```
---

### Email Automation
- Using smtplib:
```python
import smtplib

with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login("user@example.com", "password")
    server.sendmail(
        "from@example.com", "to@example.com", "Subject: Test\nHello!"
    )
```
---
### File Transfer
- Using paramiko for SSH:
```bash
pip install paramiko
```
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect("hostname", username="user", password="password")
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read().decode())
```

---
### Cloud Automation
- Using boto3 for AWS:
```bash
pip install boto3
```
```python
import boto3

s3 = boto3.client("s3")
for bucket in s3.list_buckets()["Buckets"]:
    print(bucket["Name"])

```

---

### File and Directory Automation
- Automate routine file operations like creating, deleting, or archiving files.
```python
import os
import shutil
from datetime import datetime

# Backup log files
log_dir = "/var/logs"
backup_dir = "/backup/logs"

os.makedirs(backup_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

for log_file in os.listdir(log_dir):
    if log_file.endswith(".log"):
        shutil.copy2(os.path.join(log_dir, log_file), os.path.join(backup_dir, f"{log_file}_{timestamp}"))

print("Logs backed up successfully!")
```

- Execute Commands on Remote Servers
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.100", username="admin", password="password")

stdin, stdout, stderr = ssh.exec_command("df -h")
print(stdout.read().decode())

ssh.close()
```
- Automate File Transfer
```python
from paramiko import Transport, SFTPClient

host = "192.168.1.100"
port = 22
username = "admin"
password = "password"

transport = Transport((host, port))
transport.connect(username=username, password=password)
sftp = SFTPClient.from_transport(transport)

# Upload file
sftp.put("local_file.txt", "/remote/path/local_file.txt")

# Download file
sftp.get("/remote/path/remote_file.txt", "local_file.txt")

sftp.close()
transport.close()
```
- Monitoring and Alerts

```python
import shutil
import smtplib

# Check disk usage
total, used, free = shutil.disk_usage("/")
threshold = 10 * 1024 * 1024 * 1024  # 10 GB

if free < threshold:
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("user@example.com", "password")
        server.sendmail(
            "from@example.com",
            "to@example.com",
            "Subject: Disk Space Alert\n\nDisk space is critically low!"
        )
```

---

### CI/CD Pipeline Automation
- Example: Trigger GitHub Actions Workflow
```python
import requests

url = "https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
headers = {
    "Authorization": "Bearer YOUR_GITHUB_TOKEN",
    "Accept": "application/vnd.github.v3+json"
}
data = {"ref": "main"}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 204:
    print("Workflow triggered successfully!")
else:
    print(f"Failed to trigger workflow: {response.text}")
```

---
###  Scheduling Automation
- Schedule tasks with schedule or APScheduler.
```bash
pip install schedule
```
```python
import schedule
import time

def job():
    print("Task executed!")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---
### Deploying Code to Multiple Servers

```python
import paramiko

servers = [
    {"host": "192.168.1.100", "user": "admin", "password": "password"},
    {"host": "192.168.1.101", "user": "admin", "password": "password"},
]

for server in servers:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server["host"], username=server["user"], password=server["password"])

    # Pull latest code from Git
    ssh.exec_command("cd /path/to/app && git pull")

    # Restart the application
    ssh.exec_command("systemctl restart my-app")

    ssh.close()

print("Deployment completed!")
```