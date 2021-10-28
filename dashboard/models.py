from django.db import models

# Create your models here.
class datamodel(models.Model):

        Date= models.CharField(max_length=10)
        ChartType= models.CharField(max_length=30)
        CustomerId= models.IntegerField()
        CustomerName= models.CharField(max_length=30)
        DaysOverdue= models.IntegerField()
        AmountOutstanding= models.IntegerField()
        Recovery= models.IntegerField()
