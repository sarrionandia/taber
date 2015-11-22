from tab.models import Institution
from django.test import TestCase


class InstitutionTestCase(TestCase):

    def setUp(self):
        Institution.objects.create(name='University of Whoville')

    def test_return_string(self):
        expected = 'University of Whoville'
        actual = Institution.objects.get(name='University of Whoville').__str__()
        self.assertEqual(expected, actual)