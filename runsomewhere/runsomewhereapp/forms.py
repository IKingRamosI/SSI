from django import forms

from .utils import decrypt_data, encrypt_data
from .models import Department, Doctor, Patient, Appointment

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class DoctorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        dep_instance = kwargs.pop('dep_instance', None)
        super().__init__(*args, **kwargs)

        if dep_instance:
            self.fields['department'].widget.choices = [(dep.id, decrypt_data(dep.name)) for dep in dep_instance]

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'department', 'specialization', 'email', 'phone']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone', 'address']

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        doc_instance = kwargs.pop('doc_instance', None)
        pat_instance = kwargs.pop('pat_instance', None)
        super().__init__(*args, **kwargs)

        if doc_instance:
            self.fields['doctor'].widget.choices = [(doc.id, (decrypt_data(doc.first_name) + ' ' + decrypt_data(doc.last_name))) for doc in doc_instance]

        if pat_instance:
            self.fields['patient'].widget.choices = [(pat.id, (decrypt_data(pat.first_name) + ' ' + decrypt_data(pat.last_name))) for pat in pat_instance]

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'reason']