from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField
from django.core import checks
from django.utils.deconstruct import deconstructible
from device.crypto import generate_cryptsafe_code
import string
import six

@deconstructible
class GenerateIdentifier(object):
	
	def __init__(self, length, alphabet=None):

		# Make sure the length is even
		assert length % 2 == 0

		self.length = length
		self.alphabet = alphabet or string.digits + string.ascii_letters
		
	def __call__(self):

		# Generates lhs + rhs only if lhs has HO bit set
		lhs = generate_cryptsafe_code(int(self.length / 2), self.alphabet)
		rhs = generate_cryptsafe_code(int(self.length / 2), self.alphabet) if lhs[0] in '89ABCDEF' else ''

		return lhs + rhs

class RandomIdentifierField(models.CharField):

	def __init__(self, *args, **kwargs):

		max_length = kwargs.get('max_length', 16)
		self.alphabet = kwargs.pop('alphabet', '0123456789ABCDEF')

		kwargs['default'] = kwargs.get('default', GenerateIdentifier(max_length, self.alphabet))

		super(RandomIdentifierField, self).__init__(*args, **kwargs)

	def check(self, **kwargs):
		errors = super(RandomIdentifierField, self).check(**kwargs)
		errors.extend(self._check_alphabet_attribute(**kwargs))
		return errors
	
	def _check_alphabet_attribute(self, **kwargs):
		
		if not isinstance(self.alphabet, six.string_types):
			return [
				checks.Error(
					"The 'alphabet' attribute must be a string",
					hint=None,
					obj=self,
					id='hype.E001'
				)
			]
		
		return []

class Device(models.Model):

	identifier = RandomIdentifierField(primary_key=True, max_length=16,
		help_text=_('Device identifier'))

	realm = CharField(max_length=8,
		help_text=_('Device realm'))

	user = CharField(max_length=8,
		help_text=_('Device user'))

	creation_date = models.DateTimeField(auto_now_add=True,
		help_text=_('Creation date'))

	last_update = models.DateTimeField(auto_now=True,
		help_text=_('Last update'))
