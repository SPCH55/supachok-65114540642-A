from django.db import models

# Create your models here.
class course(models.Model):
    course_id = models.IntegerField(unique=True,primary_key=True)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_id},{self.course_name}"