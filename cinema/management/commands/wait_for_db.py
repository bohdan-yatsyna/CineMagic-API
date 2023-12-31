import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command that waits for database to be available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"].cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 3 seconds...")
                time.sleep(3)

        self.stdout.write(self.style.SUCCESS("Database available!"))
