# Uncomment if you want to run tests in transaction mode with a final rollback
#from django.test import TestCase
# uncomment this if you want to keep data after running tests
from unittest import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
from application.models import *

# python ./manage.py test rango.tests.UserAuthenticationTests --keepdb
# class UserAuthenticationTests(TestCase):
def populate():
    d1 = add_doc(1, 'doctor1')
    p1 = add_pat(1, 'patient1')
    r1 = add_presc(1, d1, p1)
    r2 = add_presc(2, d1, p1)
    r3 = add_presc(3, d1, p1)
    r4 = add_presc(4, d1, p1)


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


class ApplicationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test(self):
        Prescription.objects.all().delete()
        Doctor.objects.all().delete()
        Patient.objects.all().delete()
        populate()
        response = self.client.get(reverse('prescription'))
        self.assertEqual(response.status_code, 200)
        example = b'1 </th>\n\t<td>patient1 </td>\n\t<td>doctor1 </td>'
        self.assertIn(example, response.content)
        example = b'2 </th>\n\t<td>patient1 </td>\n\t<td>doctor1 </td>'
        self.assertIn(example, response.content)
        example = b'3 </th>\n\t<td>patient1 </td>\n\t<td>doctor1 </td>'
        self.assertIn(example, response.content)
        example = b'4 </th>\n\t<td>patient1 </td>\n\t<td>doctor1 </td>'
        self.assertIn(example, response.content)