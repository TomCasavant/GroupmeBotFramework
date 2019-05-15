from yapsy.IPlugin import IPlugin

class ExamplePlugin(IPlugin):
	def process(self, msg):
		response = f"I have received your message, {msg['name']}"
		return response
