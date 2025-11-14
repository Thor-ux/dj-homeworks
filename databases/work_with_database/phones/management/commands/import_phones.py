import csv
from django.core.management.base import BaseCommand
from your_app.models import Phone
from django.utils.text import slugify
from datetime import datetime

class Command(BaseCommand):
    help = "Import phones from CSV"

    def handle(self, *args, **options):
        file_path = 'phones.csv' 
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';') 
            for row in reader:
                phone, created = Phone.objects.get_or_create(
                    id=row['id'],
                    defaults={
                        'name': row['name'],
                        'price': float(row['price']),
                        'image': row['image'],
                        'release_date': datetime.strptime(row['release_date'], '%Y-%m-%d').date(),
                        'lte_exists': row['lte_exists'].lower() in ['true', '1', 'yes'],
                        'slug': slugify(row['name']),
                    }
                )
                if created:
                    self.stdout.write(f"Create {phone.name}")
                else:
                    self.stdout.write(f"Skip {phone.name}")
