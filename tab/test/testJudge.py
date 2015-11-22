from tab.models import Institution, Judge
from django.test import TestCase


class JudgeTestCase(TestCase):

    def setUp(self):
        Institution.objects.create(name='University')
        Judge.objects.create(name="Judge Judy", institution = Institution.objects.get(name='University'))

    def test_return_string(self):
        expected = 'Judge Judy <University>'
        actual = Judge.objects.get(name='Judge Judy').__str__()
        self.assertEqual(expected, actual)