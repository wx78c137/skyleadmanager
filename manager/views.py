from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@staff_member_required
def training(request):
    return render(request, 'training.html')
