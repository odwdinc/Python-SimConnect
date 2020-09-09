# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import webrepl
import network
import socket
import json
import machine
from machine import Pin, ADC
from time import sleep

esp.osdebug(None)

server_address = 'http://<server_address>'
server_port = 5000


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
	addr = socket.getaddrinfo(host, server_port)[0][-1]
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


def http_post(url, body):
	_, _, host, path = url.split('/', 3)
	addr = socket.getaddrinfo(host, server_port)[0][-1]
	s = socket.socket()
	s.connect(addr)
	s.send(bytes('POST /%s HTTP/1.0\r\nHost: %s\r\nContent-Type: application/json\r\nContent-Length: %d\r\n\r\n%s' % (
		path, host, len(body), body), 'utf8')
	)
	while True:
		data = s.recv(100)
		if not data:
			break
	s.close()


def scale(val, src, dst):
	"""
	Scale the given value from the scale of src to the scale of dst.
	"""
	return ((val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]


def set_throttle_lever(value, index=1):
	http_post(server_address + '/datapoint/GENERAL_ENG_THROTTLE_LEVER_POSITION:index/set', '{"index":%d, "value_to_use": %d}' % (index, value))


def get_scaled_adc(_pin):
	adc = ADC(Pin(_pin))        # create ADC object on ADC pin
	adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
	adc.width(ADC.WIDTH_11BIT)  # set 9 bit return values (returned range 0-511)
	return scale(adc.read(), (0, 520), (0, 100))  # read value using the newly configured attenuation and width


do_connect()
webrepl.start()

buff = 2
o_te = 0
pin_to_read = 32
while True:
	c_te = int(get_scaled_adc(pin_to_read))
	if c_te > (o_te + buff) or c_te < (o_te - buff):
		set_throttle_lever(c_te)
		o_te = c_te
	sleep(1)
