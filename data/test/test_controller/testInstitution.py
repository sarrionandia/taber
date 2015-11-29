from django.http import Http404
from django.test import TestCase
from data.test import generate_objects
from data.views import DeleteInstitutionView, CreateInstitutionView
from data.models import Institution
from django.test.client import RequestFactory
import json


class InstitutionTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def testDeleteRemovesObject(self):
        institution = generate_objects.valid_institution();
        institution.save()
        institution_id = institution.id

        view = DeleteInstitutionView()
        view.post(None, institution_id)

        self.assertEqual(0, Institution.objects.filter(id=institution_id).count(), "Didn't delete institution")

    def testInstitutionDoesntExist(self):
        institution = generate_objects.valid_institution()
        institution.save()
        institution_id = institution.id

        institution.delete()

        with self.assertRaises(Http404):
            view = DeleteInstitutionView()
            view.post(None, institution_id)

    def testCreateInstitution(self):
        count = Institution.objects.all().count()
        request = self.factory.post('/data/institution/create', data={'name' : 'New University'})

        view = CreateInstitutionView()
        response = json.loads(view.post(request).content)

        self.assertEqual(count+1, Institution.objects.all().count(), "Didn't create a new Institution")

        createdInstitution = Institution.objects.get(id=int(response['id']));
        self.assertEqual(createdInstitution.name, 'New University', "Didn't save the university with the correct name")

