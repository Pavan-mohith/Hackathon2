from django.urls import path
from . import views
from .views import home_view, login_view, logout_view, MaterialsView, MaterialsView2, Quiz
from .views import CoursesView

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home page
    path('login/', views.login_view, name='login'),  # Route for the login page
    path('register/', views.register_view, name='register'),  # Route for the register page
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home_view/', views.home_view, name='home_view'),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('course/<int:course_id>/', CoursesView.as_view(), name='course'),
    path('course1/', CoursesView.as_view(), name='course1'),
    path('course2/', CoursesView.as_view(), name='course2'),
    path('course3/', CoursesView.as_view(), name='course3'),
    path('course4/', CoursesView.as_view(), name='course4'),
    path('course5/', CoursesView.as_view(), name='course5'),
    path('MaterialsView/', MaterialsView.as_view(), name='MaterialsView'),
    path('buy_courses/', views.buy_courses_view, name='buy_courses'),
    path('MaterialsView/notes/', views.notes_view, name='notes'),
    path('schedule/', views.schedule_view, name='schedule'),

    path('add_student/', views.add_student, name='add_student'),
    path('faculty/', views.faculty_view, name='faculty_view'),
    path('MaterialsView2/', MaterialsView2.as_view(), name='MaterialsView2'),
    path('office_hours/', views.office_hours, name='office_hours'),  # URL to view office hours
    path('add_office_hour/', views.add_office_hour, name='add_office_hour'),
    path('quiz/', Quiz.as_view(), name='quiz'),
    path('assignments/', views.assignments_view, name='assignments'),
    path('assignments/add/', views.add_assignment, name='add_assignment'),
    path('assignments/remove/<int:pk>/', views.remove_assignment, name='remove_assignment'),
    path('feedback/', views.feedback_view, name='feedback'),







    # ... other URL patterns ...
]





    # Add other routes here as needed

