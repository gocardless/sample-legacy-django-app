from django.test import TestCase
from django.test.client import Client


class GoCardlessTest(TestCase):
    def test_index(self):
        response = self.client.get('/gocardless/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('GoCardless sample application' in response.content)

    def test_buy(self):
        response = self.client.post('/gocardless/buy/', {'name': 'Test'})

        self.assertEqual(response.status_code, 301)
        self.assertTrue('https://sandbox.gocardless.com/connect/bills/new' in
                        response['Location'])

    def test_subscription(self):
        response = self.client.post('/gocardless/subscribe/', {'name': 'Test'})

        self.assertEqual(response.status_code, 301)
        self.assertTrue('https://sandbox.gocardless.com/connect/subscriptions/new' in
                        response['Location'])

    def test_preauth(self):
        response = self.client.post('/gocardless/preauth/', {'name': 'Test'})

        self.assertEqual(response.status_code, 301)
        self.assertTrue('https://sandbox.gocardless.com/connect/pre_authorizations/new' in
                        response['Location'])

