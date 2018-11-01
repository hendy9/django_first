import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Second.settings')
import django
django.setup()
import random

from Second_test.models import AccessRecord, Topic, WebPage
from faker import Faker
fakegen=Faker()
topics=['Search','Social','MarketPlace','News']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=4):
    for entry in range(N):
        top = add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec= AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
if __name__=='__main__':
    print('populating script')
    populate(20)
