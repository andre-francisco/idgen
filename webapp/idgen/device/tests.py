from django.test import TestCase
from django.urls import reverse
from device.views import RegistrationView

class TestRegistration(TestCase):

	def test_registration(self):

		response = self.client.post(reverse('register'), bytes.fromhex('a3506c6b2696'), content_type='application/octet-stream')
		self.assertEqual(response.status_code, 200)

	def test_registration_error_empty(self):

		response = self.client.post(reverse('register'), bytes.fromhex(''), content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_too_short(self):

		response = self.client.post(reverse('register'), bytes.fromhex('a3506c6b2696eb'), content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_too_big(self):

		response = self.client.post(reverse('register'), bytes.fromhex('A3506C6B2696EBD00000'), content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_no_user(self):

		response = self.client.post(reverse('register'), bytes.fromhex('A3506C6B'), content_type='application/octet-stream')
		self.assertEqual(response.status_code, 422)

	def test_registration_error_real(self):

		response = self.client.post(reverse('register'), bytes.fromhex('9c3dbfd1ffffffff'), content_type='application/octet-stream')
		self.assertEqual(response.status_code, 200)
