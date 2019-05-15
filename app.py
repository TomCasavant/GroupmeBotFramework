import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

#import all the plugins from the plugin directory
from yapsy.PluginManager import PluginManager
manager = PluginManager()
manager.setPluginPlaces(["plugins"])
manager.collectPlugins()


app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	if data['name'] != os.getenv('GROUPME_BOT_NAME'):
		#Loop through active plugins
		client = GroupmeClient()
		for plugin in manager.getAllPlugins():
			response = plugin.plugin_object.process(data, client)

	return "ok", 200

class GroupmeClient():
	def send_message(self, msg):
		url = 'https://api.groupme.com/v3/bots/post'

		data = {
			'bot_id' : os.getenv('GROUPME_BOT_ID'),
			'text' : msg,
			}

		request = Request(url, urlencode(data).encode())
		json = urlopen(request).read().decode()


