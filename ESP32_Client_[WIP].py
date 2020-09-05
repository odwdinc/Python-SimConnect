# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
import socket
import json


def do_connect():
	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	if not wlan.isconnected():
		print('connecting to network...')
		wlan.connect('<your ID>', '<your pass>')
		while not wlan.isconnected():
			pass
	print('network config:', wlan.ifconfig())


def http_get(url):
	_, _, host, path = url.split('/', 3)
	addr = socket.getaddrinfo(host, 5000)[0][-1]
	s = socket.socket()
	s.connect(addr)
	s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break
	s.close()


def http_put(url, body):
	_, _, host, path = url.split('/', 3)
	addr = socket.getaddrinfo(host, 5000)[0][-1]
	s = socket.socket()
	s.connect(addr)
	s.send(bytes('PUT /%s HTTP/1.0\r\nHost: %s\r\nContent-Type: application/json\r\nContent-Length: %d\r\n\r\n%s' %
		   (path, host, len(body), body), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break
	s.close()


do_connect()
webrepl.start()


http_get('http://<your server ip>/pysim/api/v0.1/requests/1') 

http_put('http://<your server ip>/pysim/api/v0.1/events/4', '{"value": 900}')
