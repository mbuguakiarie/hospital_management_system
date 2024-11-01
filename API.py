class Patient:
    def __init__(self, name, age, medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history

    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}"

class Doctor:
    def __init__(self, name, specialization, patients):
        self.name = name
        self.specialization = specialization
        self.patients = patients

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient):
        self.patients.remove(patient)

class Appointment:
    def __init__(self, date, time, reason, patient, doctor):
        self.date = date
        self.time = time
        self.reason = reason
        self.patient = patient
        self.doctor = doctor

    def __str__(self):
        return f"Appointment: {self.date} {self.time}, Reason: {self.reason}, Patient: {self.patient.name}, Doctor: {self.doctor.name}"

# Example usage:
patient1 = Patient("John Doe", 30, "None")
doctor1 = Doctor("Dr. Smith", "General Practice", [])
appointment1 = Appointment("2023-11-25", "10:00 AM", "Checkup", patient1, doctor1)

doctor1.add_patient(patient1)
print(appointment1)