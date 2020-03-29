from django.test import TestCase
from django.urls import reverse
from device.views import RegistrationView

class TestRegistration(TestCase):

	def test_registration(self):

		response = self.client.post(reverse('register'), 'A3506C6B2696EBDF', content_type='application/octet-stream')
		self.assertEqual(response.status_code, 200)

	def test_registration_error_empty(self):

		response = self.client.post(reverse('register'), '', content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_too_short(self):

		response = self.client.post(reverse('register'), 'A3506C6B2696EBD', content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_too_big(self):

		response = self.client.post(reverse('register'), 'A3506C6B2696EBD___', content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_lie(self):

		response = self.client.post(reverse('register'), 'A3506C6B', content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_non_hex(self):

		# Correct size
		response = self.client.post(reverse('register'), '8should_fail_err', content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)
