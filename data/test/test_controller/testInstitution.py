from django.http import Http404
from django.test import TestCase
from data.test import generate_objects
from data.views import DeleteInstitutionView
from data.models import Institution

class InstitutionTestCase(TestCase):

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