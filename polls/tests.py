from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from polls import views


class TestPoll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'


    def testList(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
