import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from application.models import *

from random import randint

def populate():
    d1 = add_doc(1,'doctor1')
    d2 = add_doc(2,'doctor2')
    d3 = add_doc(3,'doctor3')
    d4 = add_doc(4,'doctor4')
    p1 = add_pat(1,'patient1')
    p2 = add_pat(2,'patient2')
    r1 = add_presc(1,d1,p1)
    r2 = add_presc(2,d2,p1)
    r3 = add_presc(3,d1,p2)
    r4 = add_presc(4,d2,p2)
    r5 = add_presc(5,d3,p2)

def add_doc(id, name):
    d = Doctor.objects.get_or_create(id=id, nameD=name)[0]
    d.save()
    return d

def add_pat(id, name):
    d = Patient.objects.get_or_create(id=id, nameP=name)[0]
    d.save()
    return d

def add_presc(id, doc, pat):
    d = Prescription.objects.get_or_create(id=id, doctor=doc, patient=pat)[0]
    d.save()
    return d
# Start execution here!
if __name__ == '__main__':
    populate()
