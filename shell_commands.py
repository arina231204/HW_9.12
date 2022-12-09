from django.db.models import Q

from employee.models import *


# employee1 = Employee(name='Arina', birth_date='2004-12-23', position='Python student', salary=20500, work_experience='2022-08-05')
# # employee1.save()
# employee2 = Employee(name='Lion', birth_date='2000-12-23', position='Python Senior', salary=10000000, work_experience='2004-01-05')
# # employee2.save()
# employee3 = Employee(name='Mied', birth_date='1993-09-05', position='JS student', salary=150000, work_experience='2017-07-05')
# # employee3.save()
# employee4 = Employee(name='Kolie', birth_date='1991-12-23', position='JS Senior', salary=1500003, work_experience='2012-01-05')
# # employee4.save()
# employee5 = Employee(name='Nophira', birth_date='1999-03-27', position='UxUi student', salary=10000, work_experience='2021-01-05')
# employee5.save()

# passport1 = Passport(employee=employee1, inn="123412321", id_card=11211231)
# passport1.save()
# passport2 = Passport(employee=employee2, inn="777777777", id_card=67777777)
# passport2.save()
# passport3 = Passport(employee=employee3, inn="444433344", id_card=67676767)
# passport3.save()
# passport4 = Passport(employee=employee4, inn="343344444", id_card=22222222)
# passport4.save()

# del_passport = Employee.objects.order_by('-id')[0]
# del_passport.delete()
# print(Employee.objects.all())

# e = list(Employee.objects.all())
# workproject1 = WorkProject(project_name='Ololo')
# workproject1.save()
# workproject1.employee.set(e, through_defaults = {'date_joined':'2022-12-9'})

# del_employee = list(Employee.objects.all())[0]
# del_employee.delete()
# print(Employee.objects.all())

# client1 = Client(name='Onni', birth_date='2004-12-23', address='street 5', phone_number='0555485512')
# client1.save()
# client2 = Client(name='Hopl', birth_date='2000-12-23',address='street 6', phone_number='0558765512')
# client2.save()
client3 = Client(name='Goger', birth_date='1993-09-05', address='street 98', phone_number='+057655412')
client3.save()

# del_employee = list(Client.objects.all())[0]
# del_employee.delete()

# print(Employee.objects.all())
# print(Q(Employee.objects.all()),Q(Passport.objects.all()))
# print(WorkProject.objects.all())
# project = Membership.objects.filter(employee__name__icontains='Lion')
# print(project)
# print(Client.objects.all())
# vipclient = VIPClient(name='Folinasiadia', birth_date='2000-09-05', address='street 202', phone_number=231421421,
#                       donation_amount = 200)
# vipclient.save()
# print(VIPClient.objects.all())



