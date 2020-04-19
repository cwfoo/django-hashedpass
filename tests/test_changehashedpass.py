'''Unit tests for the 'changehashedpass' management command.'''

from django.core.management import call_command
from django.core.management.base import CommandError
from django.contrib.auth.models import User
from django.test import TestCase


NEWPASS = 'pbkdf2_sha256$150000$bvlcfgiCd9Ss$iq57sAsZ2uSCROS4TotA/tdOsPlRDQfue9WwpkLXnhc='


class ChangeHashedPass(TestCase):

    def test_changehashedpass(self):
        # Create user.
        User.objects.create_user(username='admin',
                                 email='admin@example.com',
                                 password='SeCr3Tpa55w0rD')
        # Change hashed password through the management command.
        call_command('changehashedpass', 'admin', NEWPASS)
        # Check that the hashed password has been changed.
        user = User.objects.get(username='admin')
        self.assertEqual(user.password, NEWPASS)

    def test_non_existent_user(self):
        '''Test the command when provided with a non-existent user.'''
        self.assertRaises(
            CommandError,
            lambda: call_command('changehashedpass', 'non-existent-user', NEWPASS))
