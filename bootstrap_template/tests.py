from django.test import TestCase
from django.urls import reverse


class DashboardViewTests(TestCase):
    def test_homepage_renders_at_root(self):
        response = self.client.get(reverse('bootstrap_template:home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertContains(response, 'Dashboard')
        self.assertContains(response, '/static/css/sb-admin-2.min.css')

    def test_dashboard_has_dedicated_url(self):
        response = self.client.get(reverse('bootstrap_template:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
