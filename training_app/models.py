from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        managed = False   #  Don't let Django create or modify the table
        db_table = 'user' # Use your existing MySQL table name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
