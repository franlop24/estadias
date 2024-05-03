from django.shortcuts import render, redirect

from .forms import EnrollmentForm

from django.contrib.auth.models import User
from academy.models import Student

def home(request):
    form = EnrollmentForm()

    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.cleaned_data['enrollment']
            enrollment = enrollment.upper()
            user = User.objects.filter(username=enrollment)
            if user:
                return redirect('presentation:home', enrollment=enrollment)
            else:
                user = User.objects.create_user(username=enrollment, password=enrollment)
                Student.objects.create(user=user, enrollment=enrollment)
                return redirect('presentation:home', enrollment=enrollment)

    return render(request, 'home/home.html', {"form": form})