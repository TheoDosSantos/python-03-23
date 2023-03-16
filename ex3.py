from flask import Flask, render_template
import platform
import socket
import getpass

app = Flask(__name__)

# print(platform.platform()) # Platform
# print("--------------------")
# print(platform.uname().system) # OS
# print(platform.uname().release) # OS Version
# print(socket.gethostname()) # Desktop name
# print(socket.gethostbyname(socket.gethostname())) # IP Adress
# print("--------------------")
# print(platform.uname().processor) # Processor

class Config(object):
    def __init__(self, platform, os, os_version, desktop_name, ip_adress, processor):
        self.platform = platform
        self.os = os
        self.os_version = os_version
        self.desktop_name = desktop_name
        self.ip_adress = ip_adress
        self.processor = processor

    def get_platform(self):
        return self.platform
        # Return Platform

    def get_os(self):
        return self.os
        # Return OS

    def get_os_version(self):
        return self.os_version
        # Return OS Version

    def get_desktop_name(self):
        return self.desktop_name
        # Return Desktop name

    def get_ip_adress(self):
        return self.ip_adress
        # Return IP Adress

    def get_processor(self):
        return self.processor
        # Return Processor
    
    def get_infos(self):
        return {'Platform' : self.platform, 'OS' : self.os, 'OS Version' : self.os_version, 'Desktop name' : self.desktop_name, 'IP adress' : self.ip_adress, 'Processor' : self.processor}
        # Return all infos in an arra

current_config = Config(platform.platform(), platform.uname().system, platform.uname().release, socket.gethostname(), socket.gethostbyname(socket.gethostname()), platform.uname().processor)

current_config_infos = current_config.get_infos()
# Variable declaration to send datas in HTML file

username = getpass.getuser()
# Variable declaration to send desktop's user name in HTML file

@app.route('/')
def index():
    return render_template('index.html' , infos=current_config_infos, username=username)

# export FLASK_APP=ex3
# export FLASK_ENV=development
# flask run