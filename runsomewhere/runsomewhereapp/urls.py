from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("departments/", views.department_list, name="department_list"),
    path("departments/create/", views.department_create, name="department_create"),
    path("doctors/", views.doctor_list, name="doctor_list"),
    path("doctors/create/", views.doctor_create, name="doctor_create"),
    path("patients/", views.patient_list, name="patient_list"),
    path("patients/create/", views.patient_create, name="patient_create"),
    path("appointments/", views.appointment_list, name="appointment_list"),
    path("appointments/create/", views.appointment_create, name="appointment_create"),
    path("prescriptions/", views.prescription_list, name="prescription_list"),
    path(
        "prescriptions/create/", views.prescription_create, name="prescription_create"
    ),
    path("logout", views.logoutView, name="logout"),
    path("logs/", views.honeypot, name="honeypot"),
]
