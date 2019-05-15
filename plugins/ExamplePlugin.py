

class ExamplePlugin():
	def process(self, msg):
		response = f"I have received your message, {msg['name']}"
		return response


