from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from models import Memory


class Command(BaseCommand):
	help = 'sends a single memory written by one party to the other'

	def handle(self, **options):
		pass
		send_mail
		