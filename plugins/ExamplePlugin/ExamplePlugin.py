from yapsy.IPlugin import IPlugin

class ExamplePlugin(IPlugin):
	def process(self, msg, client):
		response = f"I have received your message, {msg['name']}"
		client.send_message(response)
		data = open('plugins/ExamplePlugin/test.jpg', 'rb').read()
		image_url = client.upload_image(data, "image/jpeg")
		print(image_url)
		client.send_message_with_image(image_url, "Test image")
