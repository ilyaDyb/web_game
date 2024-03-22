from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    groups = models.ManyToManyField("auth.Group", related_name="custom_user_set")
    user_permissions = models.ManyToManyField("auth.Permission", related_name="custom_user_set")
    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username
    