from yapsy.IPlugin import Iplugin

class ExamplePlugin(IPlugin):
	def process(self, msg):
		response = f"I have received your message, {msg['name']}"
		return response


