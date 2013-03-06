from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .models import Subscription
from .views import suscribe_newsletter, unsuscribe_newsletter


def is_subscribed(user):
    try:
        return Subscription.objects.get(user=user)
    except Subscription.DoesNotExist:
        return False


def subscribe(email):
    data = {
        'email_user': email
    }
    request = RequestFactory().post('/', data)
    request.user = AnonymousUser()
    return suscribe_newsletter(request)


def unsubscribe(email):
    user = User.objects.get(email=email)
    assert is_subscribed(user), "A user has to be subscribed to unsubscribe"

    data = {
        'email': email,
        'val_token': user.profile.newsletter_token,
    }
    request = RequestFactory().get('/', data)
    request.user = AnonymousUser()
    return unsuscribe_newsletter(request)


class SubscribeTestCase(TestCase):
    def setUp(self):
        self.email = 'edgar@poe.com'

    def test_an_anonymous_user_can_subscribe(self):
        response = subscribe(self.email)
        self.assertEqual(response.status_code, 200)

        user = User.objects.filter(email=self.email)
        self.assertTrue(is_subscribed(user))

    def test_a_previously_subscribed_user_can_unsubscribe(self):
        subscribe(self.email)
        response = unsubscribe(self.email)
        self.assertEqual(response.status_code, 200)

        user = User.objects.filter(email=self.email)
        self.assertFalse(is_subscribed(user))
