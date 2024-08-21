from django.core.management.base import BaseCommand
from NewsAlert.cron import *

class Command(BaseCommand):
    help = 'Runs the custom cron job'

    def handle(self, *args, **kwargs):
        findstock()
        self.stdout.write(self.style.SUCCESS('Successfully ran cron job'))
