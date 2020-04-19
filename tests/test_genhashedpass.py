'''Unit tests for the 'genhashedpass' management command.'''

from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class GenHashedPassTest(TestCase):

    def test_genhashedpass(self):
        out = StringIO()
        call_command('genhashedpass', '--password=123456', stdout=out)
        self.assertTrue(len(out.getvalue()) > 0)
