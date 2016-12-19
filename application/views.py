from django.shortcuts import render
from application.models import *
# Create your views here.
def prescription(request):
	a = Prescription.objects.all()
	context_dict = { 'prescriptions': Prescription.objects.all()}
	return render(request, 'application/prescription.html', context_dict)