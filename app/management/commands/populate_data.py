import random
from django.core.management.base import BaseCommand
from faker import Faker
from app.models import Author, Book

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Générez des auteurs fictifs
        for _ in range(10):
            Author.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                birth_date=fake.date_of_birth(),
                nationality=fake.country(),
                biography=fake.text(),
                website=fake.url(),
                active=fake.boolean(chance_of_getting_true=50)  # 50% de chance que l'auteur soit actif
            )

        # Générez des livres fictifs liés à des auteurs existants
        authors = Author.objects.all()
        for _ in range(30):
            Book.objects.create(
                title=fake.catch_phrase(),
                publication_date=fake.date_between(start_date='-30y', end_date='today'),
                author=random.choice(authors),
                genre=fake.word(),  # Remplacez par des genres de livre fictifs
                ISBN=fake.unique.random_number(digits=13),  # Générez un numéro ISBN unique
                rating=fake.pydecimal(left_digits=1, right_digits=2, positive=True)  # Générez une notation aléatoire
            )

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
