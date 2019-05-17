import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

# import all the plugins from the plugin directory
from yapsy.PluginManager import PluginManager

manager = PluginManager()
manager.setPluginPlaces(["plugins"])
manager.collectPlugins()


app = Flask(__name__)


@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if data["name"] != os.getenv("GROUPME_BOT_NAME"):
        # Loop through active plugins
        client = GroupmeClient()
        for plugin in manager.getAllPlugins():
            response = plugin.plugin_object.process(data, client)

    return "ok", 200


class GroupmeClient:
    def send_message(self, msg):
        """Sends a simple text message to a group"""
        url = "https://api.groupme.com/v3/bots/post"

        data = {"bot_id": os.getenv("GROUPME_BOT_ID"), "text": msg}

        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()

    def send_message_with_image(self, image_url, msg):
        """Sends a message with a an image_url. NOTE: You must upload image to Groupme first"""
        url = "https://api.groupme.com/v3/bots/post"
        data = {
            "bot_id": os.getenv("GROUPME_BOT_ID"),
            "text": msg,
            "picture_url": image_url,
        }
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()

    def upload_image(self, image, content_type):
        """Uploads image to Groupme's image service and returns url"""
        url = "https://image.groupme.com/pictures"
        headers = {
            "Content-Type": content_type,
            "X-Access-Token": os.getenv("GROUPME_ACCESS_TOKEN"),
        }
        request = Request(url, image, headers)
        response = json.load(urlopen(request))
        print(response)
        return response["payload"]["picture_url"]
