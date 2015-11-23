from data.models import Institution, Judge
from django.core.management.base import NoArgsCommand
from random import randint


class Command(NoArgsCommand):
    def handle_noargs(self, **options):

        Judge.objects.all().delete()
        Institution.objects.all().delete()


        for i in institutions:
            institution = Institution(name=i)
            institution.save()

        for n in names:
            judge = Judge()
            judge.institution = self.random_institution()
            judge.name = n
            judge.save()


    def random_institution(self):
        return  Institution.objects.order_by('?').first()


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

names = [
    'Kaylee Wengerd',
    'Dania Sprung',
    'Joannie Busby',
    'Tammera Begum',
    'Aura Eudy',
    'Candida Champagne',
    'Domitila Dufresne',
    'Rosalyn Durrah',
    'See Diez',
    'Carlota Sheller',
    'Lanell Cremeans',
    'Angelic Ester',
    'Neda Iverson',
    'Eunice Chiodo',
    'Pansy Mackenzie',
    'Cole Claxton',
    'Suellen Cooperman',
    'Elisa Trentham',
    'Gregorio Middlebrooks',
    'Jung Siers',
    'Altha Marrin',
    'Sunni Nantz',
    'Loan Izzard',
    'Cinda Damiani',
    'Kellee Domingue',
    'Dominic Purves',
    'Denese Mcgibbon',
    'Geraldo Flecha',
    'Shay Sarinana',
    'Trula Forbus',
]