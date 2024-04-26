from django.db import models
import environ
env = environ.Env()
environ.Env.read_env()

Boglanildi = "Bog'lanildi"
Boglanilmadi = "Bog'lanilmadi"


class ContactModel(models.Model):
    Call = (
        (Boglanildi, Boglanildi),
        (Boglanilmadi, Boglanilmadi),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    course_1 = models.CharField(max_length=255)
    course_2 = models.CharField(max_length=255, null=True, blank=True)
    course_3 = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    called = models.CharField(max_length=100, choices=Call, default=Boglanilmadi)
    is_site = models.BooleanField(default=True)
    tg_id = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def check_address(self):
        if self.address:
            normalize_email = self.address.lower()
            self.address = normalize_email

    def check_firstName(self):
        if self.first_name:
            normalize_email = self.first_name.lower()
            self.first_name = normalize_email

    def check_lastName(self):
        if self.last_name:
            normalize_email = self.last_name.lower()
            self.last_name = normalize_email

    def save(self, *args, **kwargs):
        self.clean()
        super(ContactModel, self).save(*args, **kwargs)
    def clean(self):
        self.check_address()
        self.check_firstName()
        self.check_lastName()


# class MyContactModel(ContactModel):
#     class Meta:
#         proxy = True
#     class Manager(models.Manager):
#         def get_queryset(self) -> models.QuerySet:
#             return super().get_queryset().filter(called=Boglanilmadi)
#
#     objects = Manager()s