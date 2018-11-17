from django.core.management.base import BaseCommand, CommandError
from products.models import Product


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--range', type=int, required=False, default=10)

    def handle(self, *args, **options):
        try:
            query = Product.objects.filter(title__startswith='[test]')
            query.delete()
            self.stdout.write(
                self.style.SUCCESS('Test products are successfully removed!')
            )
        except Exception as err:
            raise CommandError(err)
