from django.db import models

# Create your models here.
class todoitem(models.Model):
    task_name=models.CharField(max_length=100)
    choice=(("completed","completed"),("not completed","not completed"))
    status=models.CharField(max_length=20,choices=choice,default="not completed")
    users=models.CharField(max_length=20)

    def __str__(self):
        return self.users


