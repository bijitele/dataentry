from django.db import models

# Create your models here.
class Citizen(models.Model):
    unique_govt_id = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50) #surname
    state = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    taluk = models.CharField(max_length = 50)
    dob = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    housename = models.CharField(max_length = 50)
    housenumber = models.CharField(max_length = 50)
    street = models.CharField(max_length = 50)
    address1 = models.CharField(max_length = 50)
    address2 = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 50)

    def __str__(self):
        return self.unique_govt_id



class Certificate(models.Model):
    CERT_TYPES = [
        ("DOB", "Date of Birth certificate") ,
        ("DTH", "Death certificate") ,
        ("MC",  "Marriage certificate") ,
    ]
    FILE_TYPES = [
        ("PNG", "PNG"),
        ("PDF", "PDF"),
        ("JPEG",  "JPEG"),
    ]
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    certificate_type = models.CharField(max_length=5, choices=CERT_TYPES, default="DOB")
    certificate_filetype = models.CharField(max_length=5, choices=FILE_TYPES)
    date_of_issue = models.DateField()
    issued_by = models.CharField(max_length=50)
    issued_to = models.CharField(max_length=50)
    issued_to_address = models.CharField(max_length=50)

    def __str__(self):
        return self.certificate_type + self.issued_to
