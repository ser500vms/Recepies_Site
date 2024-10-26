# from django.contrib.auth.models import User
# from django.db import models

# Create your models here.

# можно создать свой класс пользователей на базовом классе, для того чтобы добавить нужные нам поля в него
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     agreement_accepted = models.BooleanField(default=False)