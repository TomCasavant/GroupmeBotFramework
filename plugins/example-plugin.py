

class ExamplePlugin():
	def process(msg):
		response = f"I have received your message, {msg['name']}"
		return response


