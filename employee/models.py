import datetime

from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        birth_date = self.birth_date.year - datetime.today.year
        return birth_date

    def __str__(self):
        return self.name


class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField()
    work_experience = models.DateField()

    def __str__(self):
        return self.name


class WorkProject(models.Model):
    project_name = models.CharField(max_length=20)
    employee = models.ManyToManyField(Employee, related_name='employees', through='Membership')

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.project.project_name} - {self.employee.name}'


class Passport(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    inn = models.CharField(max_length=20)
    id_card = models.IntegerField()

    def get_gender(self):
        if self.inn[0] == '1':
            self.inn = 'Male'
        elif self.inn[0] == '2':
            self.inn = 'Female'
            return self.inn

    def __str__(self):
        return self.inn


class Client(AbstractPerson):
    address = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name


class VIPClient(Client):
    vip_status_start = models.DateField(auto_now_add=True)
    donation_amount = models.IntegerField()



