from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .utils import decrypt_data, encrypt_data
from .models import Department, Doctor, Patient, Appointment, Prescription
from .forms import DepartmentForm, DoctorForm, PatientForm, AppointmentForm, PrescriptionForm

def department_list(request):
    departments_list = Department.objects.all()

    departments = []
    for department in departments_list:
        decrypted_department = {
            'id': department.id,
            'name': decrypt_data(department.name),
            'description': decrypt_data(department.description),
        }
        departments.append(decrypted_department)

    return render(request, 'runsomewhereapp/departments/list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.encrypt_sensitive_data()
            department.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'runsomewhereapp/departments/create.html', {'form': form})

def doctor_list(request):
    doctors_list = Doctor.objects.all()

    doctors = []
    for doctor in doctors_list:
        decrypted_doctors = {
            'id': doctor.id,
            'first_name': decrypt_data(doctor.first_name),
            'last_name': decrypt_data(doctor.last_name),
            'department': decrypt_data(doctor.department.name),
            'specialization': decrypt_data(doctor.specialization),
        }
        doctors.append(decrypted_doctors)
    
    return render(request, 'runsomewhereapp/doctors/list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'runsomewhereapp/doctors/create.html', {'form': form})

def patient_list(request):
    patients_list = Patient.objects.all()

    patients = []
    for patient in patients_list:
        decrypted_patient = {
            'id': patient.id,
            'first_name': decrypt_data(patient.first_name),
            'last_name': decrypt_data(patient.last_name),
            'email': decrypt_data(patient.email),
            'phone': decrypt_data(patient.phone),
        }
        patients.append(decrypted_patient)

    return render(request, 'runsomewhereapp/patients/list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'runsomewhereapp/patients/create.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'runsomewhereapp/appointments/list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'runsomewhereapp/appointments/create.html', {'form': form})

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'runsomewhereapp/prescriptions/list.html', {'prescriptions': prescriptions})

def prescription_create(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'runsomewhereapp/prescriptions/create.html', {'form': form})