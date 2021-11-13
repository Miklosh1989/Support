import random
import string

from celery import shared_task

from .models import Ticket


@shared_task
def create_new_ticket():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_ticket = Ticket.objects.create(name = random_name)
    return new_ticket





