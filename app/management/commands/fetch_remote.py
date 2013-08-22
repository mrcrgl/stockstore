__author__ = 'riegel'

from django.core.management.base import BaseCommand, CommandError
from app.models import Share, DailyShareRate


class Command(BaseCommand):

    def handle(self, *args, **options):

        shares = Share.objects.filter()

        for share in shares:
            self.stdout.write("Proceed Share %s" % share.name)
        #raise CommandError('Test Error')