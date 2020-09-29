import requests
import re
from aiohttp import ClientSession
import asyncio
import time
import datetime
valid_ips = []
from concurrent.futures import ThreadPoolExecutor, as_completed


res = requests.get('https://free-proxy-list.net/')
m = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)


def get_ip(ip):
    try:
        res=requests.get('https://api.ipify.org?format=json',proxies={'http':ip,'https':ip},timeout=5)
        valid_ips.append(ip)
        print(res.json())
        pass
    except :
        print(f"fail => {ip}")
        pass




processes = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for ip in m:
        processes.append(executor.submit(get_ip, ip))

for task in as_completed(processes):
    print(task.result())

print(len(m))
print(len(valid_ips))
