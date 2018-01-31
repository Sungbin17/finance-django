from django.db import models


class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=120)
    index1 = models.CharField(max_length=20)
    sector = models.CharField(max_length=120)
    major_product = models.CharField(max_length=120)
    listed_day = models.CharField(max_length=120)
    account_day = models.CharField(max_length=120)
    representative = models.CharField(max_length=120)
    homepage = models.CharField(max_length=500)
    province = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = '상장법인목록2'

    def __str__(self):
        return self.company_name