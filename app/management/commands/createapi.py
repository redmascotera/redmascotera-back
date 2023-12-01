"""
Creates a new API module in app/api with the given name using the boilerplate templates.
"""
from django.core.management.base import BaseCommand, CommandError

from app.management.module_maker import make_api_module


class Command(BaseCommand):
    """
    Command for executing make_api_module with the given name.
    """
    help = (
        "Creates a new API module in app/api with the given name using the boilerplate "
        "templates."
    )

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='The name of the new API module.')

    def handle(self, *args, **options):
        try:
            make_api_module(options['name'])
        except FileExistsError as e:
            raise CommandError(e) from e
        self.stdout.write(self.style.SUCCESS(f'Successfully created API module {options["name"]}'))
