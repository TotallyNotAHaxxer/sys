import os 
import sys
import socket 
import requests 
from requests import get 
import time as t
import speedtest 
import datetime 
from datetime import datetime
import psutil
import platform
import colorama 
from colorama import Fore, Back, Style 


#disk 
partitions = psutil.disk_partitions()

# username 
#u = gethostname()

## speed 
st = speedtest.Speedtest()

# gather public IP 
ip = get('https://api.ipify.org').text


# socket for localhost gathering 
sock1 = socket.gethostbyname(socket.gethostname())
uname = platform.uname() # system 

import os, platform, subprocess, re

def get_processor_name():
    if platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        for line in all_info.split(''):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line, 1)

def sysplat():
    print(f"______________________________Sys info for {uname.node}_____________________________")
    print(f".-----.             | System          => {uname.system}     ")
    print(f"|__ --|             | Node Name       => {uname.node}       ")
    print(f"|_____|             | Release         => {uname.release}    ")
    print(f"                    | Architecture    => {uname.machine}    ")
    print(f".--.--.             |-------------Networking-------------------")
    print(f"|  |  |             | Local Host IP    => ", sock1)
    print('|___  |             | Public IP        => {}' .format(ip))
    print('|_____|             | Download Speed   => ',end='')
    print(st.download())
    print('                    | UpLoad Speed     => ', end='')
    print(st.upload())
    print("                    |---------------CPU Info--------------------")
    print(".-----.             |Physical cores    => ", psutil.cpu_count(logical=False))
    print("|__ --|             |Total cores       => ", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"|_____|             |Max Frequency     => {cpufreq.max:.2f}Mhz")
    print(f"                    |Min Frequency     => {cpufreq.min:.2f}Mhz")
    print(f"                    |Current Frequency => {cpufreq.current:.2f}Mhz")
    print("                    |CPU Usage          =>")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"                    |Core {i}          => {percentage}%")
    print(f"                    |Total CPU Usage   => {psutil.cpu_percent()}%")
    
    
    servernames = []
    st.get_servers(servernames)

def s(X):
    t.sleep(X)

def sc(X):
    t.sleep(X)
    os.system('clear')



sc(1)


if __name__ == ("__main__"):
    sc(1)
    sysplat()
