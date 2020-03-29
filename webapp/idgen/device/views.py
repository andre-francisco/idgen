from django.views.generic import View
from django.http import HttpResponse
from device.models import Device
import re

class RegistrationView(View):

	def post(self, request):

		content = request.body

		if len(content) == 0:
			return HttpResponse(b'', content_type="application/octet-stream", status=422)

		expected = 8 if content[0] & 0x80 else 4

		if len(content) != expected:
			return HttpResponse('', content_type="application/octet-stream", status=422)

		realm = content[:expected]
		user = content[expected:]

		device = Device.objects.create(**{
			'realm': realm.hex(),
			'user': user.hex()
		})

		print("==> Meta <==")
		print(bytes.fromhex(device.identifier).hex())
		print(device.realm)
		print(device.user)

		return HttpResponse(bytes.fromhex(device.identifier), content_type="application/octet-stream")
