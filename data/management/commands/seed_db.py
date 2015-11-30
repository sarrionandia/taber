from data.models import Institution, Judge, Team, Speaker, Venue
from django.core.management.base import NoArgsCommand
from random import randint


class Command(NoArgsCommand):
    def handle_noargs(self, **options):

        Judge.objects.all().delete()
        Speaker.objects.all().delete()
        Team.objects.all().delete()
        Institution.objects.all().delete()


        for i in institutions:
            institution = Institution(name=i)
            institution.save()

        for n in names:
            judge = Judge()
            judge.institution = self.random_institution()
            judge.name = n
            judge.save()

        for institution in Institution.objects.all():
            for i in range(0, randint(0, 3)):
                team = Team()
                team.institution = institution
                team.name = str(i)
                team.save()

                speaker1 = Speaker(name=self.random_name(), team=team)
                speaker1.save()

                speaker2 = Speaker(name=self.random_name(), team=team)
                speaker2.save()

        for v in venues:
            venue = Venue(name=v)
            venue.save()

    def random_institution(self):
        return  Institution.objects.order_by('?').first()

    def random_name(self):
        return names[randint(0, len(names)-1)]

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

venues = [
    'Room of Requirement',
    'Chamber of Secrets',
    'Ravenclaw Tower',
    'Great Hall',
    'Slytherin Dungeon',
    'Forbidden Forest',
    'Greenhouse 1',
    'Charms Classroom',
    'Hospital Tower'


]