from django.views.generic import View
from django.http import HttpResponse
from device.models import Device
import io
import re

class RegistrationView(View):

	def post(self, request):

		content = request.body

		try:

			realm = self._parse_identifier(content)
			user = self._parse_identifier(content[len(realm):])

		except IndexError:

			# Invalid size
			return HttpResponse(b'', content_type="application/octet-stream", status=422)

		if len(realm) != self._expected_size(realm) or len(user) != self._expected_size(user):
			return HttpResponse(b'', content_type="application/octet-stream", status=422)

		# e.g. the input wasn't all consumed
		if len(realm) + len(user) != len(content):
			return HttpResponse(b'', content_type="application/octet-stream", status=422)

		device = Device.objects.create(**{
			'realm': realm.hex(),
			'user': user.hex(),
			'os': request.user_agent.os.family,
			'os_version': request.user_agent.os.version_string
		})

		print("==> User agent %s" % (request.META['HTTP_USER_AGENT']))
		print("==> Returning  %s %s" % (device.identifier, bytes.fromhex(device.identifier)))

		return HttpResponse(bytes.fromhex(device.identifier), content_type="applicatoin/octet-stream")

	def _parse_identifier(self, content):

		return content[:self._expected_size(content)]

	def _expected_size(self, content):

		return 4 if content[0] & 0x80 else 2