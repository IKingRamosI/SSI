from django.db import models

from .utils import decrypt_data, encrypt_data

class Department(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return decrypt_data(self.name)
    
    def encrypt_sensitive_data(self):
        self.name = encrypt_data(self.name)
        self.description = encrypt_data(self.description)

class Doctor(models.Model):
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=1024)
    email = models.EmailField(unique=True, max_length=1024)
    phone = models.CharField(max_length=1024)

    def __str__(self):
        return f"Dr. {decrypt_data(self.first_name)} {decrypt_data(self.last_name)}"
    
    def encrypt_sensitive_data(self):
        self.first_name = encrypt_data(self.first_name)
        self.last_name = encrypt_data(self.last_name)
        self.specialization = encrypt_data(self.specialization)
        self.email = encrypt_data(self.email)
        self.phone = encrypt_data(self.phone)

class Patient(models.Model):
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1024, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    email = models.EmailField(unique=True, max_length=1024)
    phone = models.CharField(max_length=1024)
    address = models.TextField(max_length=1024)

    def __str__(self):
        return f"{decrypt_data(self.first_name)} {decrypt_data(self.last_name)}"
    
    def encrypt_sensitive_data(self):
        self.first_name = encrypt_data(self.first_name)
        self.last_name = encrypt_data(self.last_name)
        self.date_of_birth = self.date_of_birth
        self.gender = encrypt_data(self.gender)
        self.email = encrypt_data(self.email)
        self.phone = encrypt_data(self.phone)
        self.address = encrypt_data(self.address)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField(max_length=1024)

    def __str__(self):
        return f"Appointment with {self.doctor} for {self.patient} on {self.date}"
    
    def encrypt_sensitive_data(self):
        self.date = self.date
        self.reason = encrypt_data(self.reason)

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    medication = models.TextField(max_length=1024)
    instructions = models.TextField(max_length=1024)

    def __str__(self):
        return f"Prescription for {self.appointment.patient} by {self.appointment.doctor}"
    
    def encrypt_sensitive_data(self):
        self.medication = encrypt_data(self.medication)
        self.instructions = encrypt_data(self.instructions)
