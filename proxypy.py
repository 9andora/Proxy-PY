import requests
import re
import socket
import threading
import random

def writer(items):
    file = open("proxy_list.txt", "a")
    # for the item in items:
    file.write(items)
    file.write('\n')


def get_proxies():
	url = "https://free-proxy-list.net/"
	response = requests.get(url)
	data = response.text
	proxies = set()
	ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b:\d+"  # Regular expression pattern for IP addresses with port numbers
	ips_with_ports = re.findall(ip_pattern, data)
	# Separate IP addresses and port numbers
	for proxy in ips_with_ports:
	    proxies.add(proxy)
	#print(list(proxies))
	return (list(proxies))

def fpxypro():


	proxy=get_proxies()
	ipcheck = 'https://httpbin.org/ip'
	count=0
	for i in proxy:
		print(i)
		try:
			response = requests.get(ipcheck,proxies={"http": i, "https": i},timeout=30)
			writer(i)
			print(f"ip_working={response.text}")

			#break
		except:
			print(f"ip_fault={i}")
			count=count+1
			# if count > 20:
			# fpxypro()
			continue

threads = []
thread = threading.Thread(target=fpxypro)
thread.start()
threads.append(thread)

# Wait for all threads to finish
for thread in threads:
	thread.join()  # getting ip:port
