from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .decorators import session_check
from .utils import decrypt_data
from .models import Department, Doctor, Patient, Appointment, Prescription
from .forms import (
    DepartmentForm,
    DoctorForm,
    PatientForm,
    AppointmentForm,
    PrescriptionForm,
)
from runsomewhereapp.middleware import RequestResponseLoggingMiddleware
import logging
from django.contrib.auth.decorators import login_required, user_passes_test

logger = logging.getLogger("user_events")


def isSuperUser(user):
    return user.is_superuser


def honeypot(request):
    middleware = RequestResponseLoggingMiddleware(request)
    logger.warning("-- Honey reached --")
    middleware.process_request(request)
    return render(request, "runsomewhereapp/accounts/login.html")


def login_view(request):
    middleware = RequestResponseLoggingMiddleware(request)

    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
        except KeyError:
            return render(request, "runsomewhereapp/login.html")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("department_list"))
        else:
            logger.warning("-- Invalid Crendentials --")
            middleware.process_request(request)
    return render(request, "runsomewhereapp/accounts/login.html")


def logoutView(request):
    request.session.flush()
    return redirect("login_view")


@login_required(login_url="login_view")
def department_list(request):
    departments_list = Department.objects.all()

    departments = []
    for department in departments_list:
        decrypted_department = {
            "id": department.id,
            "name": decrypt_data(department.name),
            "description": decrypt_data(department.description),
        }
        departments.append(decrypted_department)

    return render(
        request, "runsomewhereapp/departments/list.html", {"departments": departments}
    )


@login_required(login_url="login_view")
@user_passes_test(isSuperUser, login_url="login_view")
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.encrypt_sensitive_data()
            department.save()
            return redirect("department_list")
    else:
        form = DepartmentForm()
    return render(request, "runsomewhereapp/departments/create.html", {"form": form})


@login_required(login_url="login_view")
def doctor_list(request):
    doctors_list = Doctor.objects.all()

    doctors = []
    for doctor in doctors_list:
        decrypted_doctors = {
            "id": doctor.id,
            "first_name": decrypt_data(doctor.first_name),
            "last_name": decrypt_data(doctor.last_name),
            "department": decrypt_data(doctor.department.name),
            "specialization": decrypt_data(doctor.specialization),
        }
        doctors.append(decrypted_doctors)

    return render(request, "runsomewhereapp/doctors/list.html", {"doctors": doctors})


@login_required(login_url="login_view")
@user_passes_test(isSuperUser, login_url="login_view")
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = User.objects.create_user(
                form.cleaned_data["email"],
                form.cleaned_data["email"],
                request.POST["password"],
            )
            doctor.encrypt_sensitive_data()
            doctor.save()
            return redirect("doctor_list")
    else:
        form = DoctorForm()
    return render(request, "runsomewhereapp/doctors/create.html", {"form": form})


@login_required(login_url="login_view")
def patient_list(request):
    patients_list = Patient.objects.all()

    patients = []
    for patient in patients_list:
        decrypted_patient = {
            "id": patient.id,
            "first_name": decrypt_data(patient.first_name),
            "last_name": decrypt_data(patient.last_name),
            "email": decrypt_data(patient.email),
            "phone": decrypt_data(patient.phone),
        }
        patients.append(decrypted_patient)

    return render(request, "runsomewhereapp/patients/list.html", {"patients": patients})


@login_required(login_url="login_view")
def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = User.objects.create_user(
                form.cleaned_data["email"],
                form.cleaned_data["email"],
                request.POST["password"],
            )
            patient.encrypt_sensitive_data()
            patient.save()
            return redirect("patient_list")
    else:
        form = PatientForm()
    return render(request, "runsomewhereapp/patients/create.html", {"form": form})


@login_required(login_url="login_view")
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(
        request,
        "runsomewhereapp/appointments/list.html",
        {"appointments": appointments},
    )


@login_required(login_url="login_view")
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm()
    return render(request, "runsomewhereapp/appointments/create.html", {"form": form})


@login_required(login_url="login_view")
def prescription_list(request):
    prescriptions_list = Prescription.objects.all()

    prescriptions = []
    for prescription in prescriptions_list:
        decrypted_prescription = {
            "id": prescription.id,
            "appointment": prescription.appointment,
            "medication": decrypt_data(prescription.medication),
            "instructions": decrypt_data(prescription.instructions),
        }
        prescriptions.append(decrypted_prescription)

    return render(
        request,
        "runsomewhereapp/prescriptions/list.html",
        {"prescriptions": prescriptions},
    )


@login_required(login_url="login_view")
def prescription_create(request):
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect("prescription_list")
    else:
        form = PrescriptionForm()
    return render(request, "runsomewhereapp/prescriptions/create.html", {"form": form})
