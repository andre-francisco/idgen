from django.views.generic import View
from django.http import HttpResponse
from device.models import Device
import re

class RegistrationView(View):

	def post(self, request):

		content = request.body.decode('ascii')

		if len(content) == 0:
			return HttpResponse('', content_type="application/octet-stream", status=422)

		if re.fullmatch(r'^[0-9a-fA-F]+$', content) is None:
			return HttpResponse('', content_type="application/octet-stream", status=422)

		expected = 16 if content[0] in '89ABCDEF' else 8

		if len(content) != expected:
			return HttpResponse('', content_type="application/octet-stream", status=422)

		realm = content[:expected]
		user = content[expected:]

		device = Device.objects.create(**{
			'realm': realm,
			'user': user
		})

		return HttpResponse(device.identifier, content_type="application/octet-stream")
