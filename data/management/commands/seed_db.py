from data.models import Institution
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    def handle_noargs(self, **options):

        Institution.objects.all().delete()


        for i in institutions:
            institution = Institution(name=i)
            institution.save()

institutions = [
    'Abertay University',
    'Aberystwyth University',
    'Anglia Ruskin University',
    'Aston University',
    'Bangor University',
    'University of Bath',
    'Bath Spa University',
    'University of Bedfordshire',
    'University of Birmingham',
    'Birmingham City University',
    'University College Birmingham',
    'Bishop Grosseteste University',
    'University of Derby',
    'University of Dundee',
    'University of Glasgow',
    'Glasgow Caledonian University',
    'Kingston University',
    'Lancaster University',
    'University of Law',
    'University of Leeds',
    'Leeds Beckett University',
    'Leeds Trinity University',
    'UCL',
    'University of Oxford',
    'University of Cambridge'
]