from django.http import Http404
from django.test import TestCase
from data.test import generate_objects
from data.views import DeleteInstitutionView, CreateInstitutionView, UpdateInstitutionView
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

    def testInstitutionUpdates(self):
        institution = generate_objects.valid_institution()
        view = UpdateInstitutionView()
        request = self.factory.post('/data/institution/' + str(institution.id) + '/update/',
                                    data = {'name' : 'Updated Name'})

        view.post(request, institution.id)

        institution.refresh_from_db()
        self.assertEqual('Updated Name', institution.name, "Did not update the name of the institution")

    def test404WhenUpdatingInstitutionDoesntExist(self):
        view = UpdateInstitutionView()

        with self.assertRaises(Http404):
            view.post(None, 0)

    def testReturnsInstitutionInformation(self):
        view = UpdateInstitutionView();
        institution = generate_objects.valid_institution()
        request = self.factory.post('/data/institution/' + str(institution.id) + '/update/',
                            data = {'name' : 'Updated Name'})
        response = json.loads(view.post(request, institution.id).content)
        institution.refresh_from_db()

        self.assertEqual(response['name'], institution.name, "Didn't return the updated name of the institution")
        self.assertEqual(int(response['id']), institution.id, "Didn't return the ID of the updated institution")
