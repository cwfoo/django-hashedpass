import sys
import django
from django.test.runner import DiscoverRunner
from django.conf import settings


settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django_hashedpass',
    ]
)

django.setup()
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['tests'])
if failures:
    sys.exit(failures)
