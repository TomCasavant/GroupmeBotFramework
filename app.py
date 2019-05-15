import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from plugins.ExamplePlugin import ExamplePlugin

active_plugins = [ExamplePlugin()]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	if data['name'] != os.getenv('BOT_ID'):
		for (plugin in active_plugins):
			response = plugin.process(data)
			if response:
				send_message(response)

	return "ok", 200


def send_message(msg):
	url = 'https://api.groupme.com/v3/bots/post'

	data = {
		'bot_id' : os.getenv('GROUPME_BOT_ID'),
		'text' : msg,
		}

	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()

