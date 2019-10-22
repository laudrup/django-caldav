import unittest
from unittest.mock import patch

from django.test import RequestFactory, TestCase

import caldav
from django_caldav.views import CalDavView


class TestCalDavView(CalDavView):
    pass


def caldav_request(method, url, data='', headers={}, proxies={}, auth=None, verify=True):
    factory = RequestFactory()
    request = factory.generic(method, url, data=data, **headers)
    request.user = unittest.mock.MagicMock()
    request.user.username = auth.username

    view = TestCalDavView.as_view()
    response = view(request, path=request.path)
    response.headers = response.items()
    response.reason = response.status_code

    return response


class CalDavViewTests(TestCase):

    @patch('caldav.davclient.requests.request', caldav_request)
    def test_calendar(self):
        client = caldav.DAVClient('http://localhost:5232', username='oleodder')
        principal = client.principal()
        self.assertFalse(principal.calendars())
