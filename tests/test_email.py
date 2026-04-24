# app/tests/test_email.py

from django.test import TestCase, Client, override_settings
from django.urls import reverse
from unittest.mock import patch

@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class ContactoEmailTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("contacto")

    @patch("django.core.mail.EmailMessage.send")  # patches the actual send method
    def test_email_is_sent_on_valid_form(self, mock_send):
        response = self.client.post(self.url, {
            "from_name": "Juan Pérez",
            "reply_to": "juan@example.com",
            "title": "Consulta",
            "message": "Hola, quiero más info.",
        })

        # Email was attempted
        self.assertTrue(mock_send.called)

        # User gets redirected after success
        self.assertRedirects(response, self.url)

    @patch("django.core.mail.EmailMessage.send")
    def test_no_email_on_invalid_form(self, mock_send):
        response = self.client.post(self.url, {
            "from_name": "",   # invalid: empty required field
            "reply_to": "not-an-email",
            "title": "",
            "message": "",
        })

        # Email should NOT be sent
        self.assertFalse(mock_send.called)

    @patch("django.core.mail.EmailMessage.send", side_effect=Exception("SMTP error"))
    def test_email_failure_shows_error(self, mock_send):
        response = self.client.post(self.url, {
            "from_name": "Juan",
            "reply_to": "juan@example.com",
            "title": "Test",
            "message": "Test message",
        })

        # Should NOT redirect — stays on the page with an error
        self.assertEqual(response.status_code, 200)