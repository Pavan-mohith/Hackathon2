from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import FeedbackForm


# Create your views here.

def home(request):
    return render(request, 'base.html')  # Correctly render the 'base.html' template


from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)

                # Redirect to 'admin.html' if username is 'admin'
                if username == "admin":
                    return redirect('administrator:admin_page')  # Use the URL name for admin_page

                return redirect('home')  # Redirect to the home page for other users

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')

from django.shortcuts import render



from django.contrib.auth import login as auth_login, authenticate





from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            username = form.cleaned_data.get('username')

            # Redirect to 'admin.html' if username is 'admin'
            if username == "admin":
                auth_login(request, user)
                return redirect('administrator:admin.html')  # Assuming 'administrator' app has 'admin' URL name

            # Check if username is a 4-digit number
            elif username.isdigit() and len(username) == 4:
                auth_login(request, user)
                return render(request, 'faculty.html')  # Redirect to faculty.html
            else:
                auth_login(request, user)
                return render(request, 'home.html')  # Redirect to home.html
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')


from django.shortcuts import render, redirect
from .forms import AssignmentForm
from .models import Assignment


def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignments')  # Redirect back to assignments list after saving
    else:
        form = AssignmentForm()  # If it's a GET request, just display the empty form

    return render(request, 'assignments/assignment.html', {'form': form})


from django.shortcuts import render
from django.views import View

class CoursesView(View):
    def get(self, request):
        return render(request, 'courses.html')

class MaterialsView(View):
    def get(self, request):
        return render(request, 'study_materials.html')

from django.views.generic import TemplateView

class BuyCoursesView(TemplateView):
    template_name = 'buy_courses.html'  # Path to your buy_courses.html template


def buy_courses_view(request):
    return render(request, 'buy_courses.html')
def notes_view(request):
    return render(request, 'notes.html')

def schedule_view(request):
    # You can fetch the user's schedule from the database, for now we'll pass a dummy schedule
    schedule_data = [
        {'day': 'Monday', 'time': '9:00 AM - 10:30 AM', 'course': 'Mathematics'},
        {'day': 'Tuesday', 'time': '10:00 AM - 11:30 AM', 'course': 'Computer Science'},
        {'day': 'Wednesday', 'time': '1:00 PM - 2:30 PM', 'course': 'Physics'},
        {'day': 'Thursday', 'time': '3:00 PM - 4:30 PM', 'course': 'Chemistry'},
        {'day': 'Friday', 'time': '10:30 AM - 12:00 PM', 'course': 'Biology'},
    ]

    return render(request, 'schedule.html', {'schedule_data': schedule_data})



# views.py
from django.shortcuts import render
from django.http import HttpResponse


# Example view for rendering the add_student page
def add_student(request):
    if request.method == 'POST':
        # Handle form submission and add the student to the database
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        # Save student data to the database here
        # For simplicity, we're just returning a message for now
        return HttpResponse(f"Student {name} with ID {student_id} added!")

    # Render the add_student page if the method is GET
    return render(request, 'add_student.html')


from .models import Student


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        student = Student.objects.create(name=name, student_id=student_id)
        return HttpResponse(f"Student {name} with ID {student_id} added!")

    return render(request, 'add_student.html')
from django.shortcuts import render

def faculty_view(request):
    # Add any context if necessary
    return render(request, 'faculty.html')

class MaterialsView2(View):
    def get(self, request):
        return render(request, 'study_materials2.html')
from django.shortcuts import render, redirect
from .models import OfficeHour
from .forms import OfficeHourForm

def office_hours(request):
    # Display all office hours
    office_hours = OfficeHour.objects.all()
    return render(request, 'office_hours.html', {'office_hours': office_hours})

def add_office_hour(request):
    # Add a new office hour
    if request.method == 'POST':
        form = OfficeHourForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new office hour
            return redirect('office_hours')  # Redirect to office hours list
    else:
        form = OfficeHourForm()
    return render(request, 'office_hours.html', {'form': form})

class Quiz(View):
    def get(self, request):
        return render(request, 'quiz.html')

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm

def assignments_view(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments': assignments})

def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignments')
    else:
        form = AssignmentForm()
    return render(request, 'assignments.html', {'form': form})

def remove_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.delete()
    return redirect('assignments')
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save feedback data to the database or send an email
            # For now, we'll just return a simple message
            return HttpResponse("Thank you for your feedback!")
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})





