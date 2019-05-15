from yapsy.IPlugin import IPlugin

class ExamplePlugin(IPlugin):
	def process(self, msg, client):
		response = f"I have received your message, {msg['name']}"
		client.send_message(response)
