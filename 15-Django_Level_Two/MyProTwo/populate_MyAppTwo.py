import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from MyAppTwo.models import AccessRecord, Webpage, Topic
from faker import Faker

fakergen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populate complete!")
