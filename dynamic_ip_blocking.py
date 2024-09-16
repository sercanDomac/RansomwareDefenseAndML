import os
import json
import requests

def get_attacker_ips():
    response = requests.get('http://example.com/attacker_ips')
    data = response.json()
    return data['ips']

def block_ips(ip_list):
    for ip in ip_list:
        os.system(f"iptables -A INPUT -s {ip} -j DROP")
        print(f"{ip} adresi engellendi.")

if __name__ == "__main__":
    attacker_ips = get_attacker_ips()
    block_ips(attacker_ips)
