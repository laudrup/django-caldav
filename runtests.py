import sys
import django

from django.test.runner import DiscoverRunner
from django.conf import settings

if not settings.configured:
    settings_dict = dict(
        INSTALLED_APPS=(
            'django_caldav',
            'tests',
        ),
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
                "USER": "",
                "PASSWORD": "",
                "HOST": "",
                "PORT": "",
            }
        },
        MIDDLEWARE_CLASSES=()
    )

    settings.configure(**settings_dict)
    django.setup()

failures = DiscoverRunner(verbosity=1, interactive=True, failfast=False).run_tests([])
sys.exit(failures)
