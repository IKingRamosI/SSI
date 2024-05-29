from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .utils import decrypt_data, encrypt_data
from .models import Department, Doctor, Patient, Appointment
from .forms import DepartmentForm, DoctorForm, PatientForm, AppointmentForm

def department_list(request):
    departments_list = Department.objects.all()

    # Decrypt the data
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

    # Decrypt the data
    doctors = []
    for doctor in doctors_list:
        decrypted_doctor = {
            'id': doctor.id,
            'first_name': decrypt_data(doctor.first_name),
            'last_name': decrypt_data(doctor.last_name),
            'department': doctor.department,
            'specialization': decrypt_data(doctor.specialization),
            'email': decrypt_data(doctor.email),
            'phone': decrypt_data(doctor.phone),
        }
        doctors.append(decrypted_doctor)

    return render(request, 'runsomewhereapp/doctors/list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=None, dep_instance=Department.objects.all())
    return render(request, 'runsomewhereapp/doctors/create.html', {'form': form})

def patient_list(request):
    patients_list = Patient.objects.all()

    # Decrypt the data
    patients = []
    for patient in patients_list:
        decrypted_patient = {
            'id': patient.id,
            'first_name': decrypt_data(patient.first_name),
            'last_name': decrypt_data(patient.last_name),
            'date_of_birth': patient.date_of_birth,
            'gender': decrypt_data(patient.gender),
            'email': decrypt_data(patient.email),
            'phone': decrypt_data(patient.phone),
            'address': decrypt_data(patient.address),
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
    appointments_list = Appointment.objects.all()

    # Decrypt the data
    appointments = []
    for appointment in appointments_list:
        decrypted_appointment = {
            'id': appointment.id,
            'doctor': appointment.doctor,
            'patient': appointment.patient,
            'date': decrypt_data(appointment.date),
            'reason': decrypt_data(appointment.reason),
        }
        appointments.append(decrypted_appointment)

    return render(request, 'runsomewhereapp/appointments/list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.encrypt_sensitive_data()
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=None, doc_instance=Doctor.objects.all(), pat_instance=Patient.objects.all())
    return render(request, 'runsomewhereapp/appointments/create.html', {'form': form})