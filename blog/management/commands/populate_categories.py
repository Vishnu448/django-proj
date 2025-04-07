from typing import Any

from django.core.management.base import BaseCommand

from blog.models import Category

class Command(BaseCommand):
    help="this command helps to  populate categories"

    def handle(self, *args: Any, **options: Any):
        #delete the posts
        
        Category.objects.all().delete()
        
        categories=['sports','entertainment','technology','politics','health']

        
        for category_name in categories:
            Category.objects.create(name=category_name)
            
        self.stdout.write(self.style.SUCCESS("Data populated successfully"))

