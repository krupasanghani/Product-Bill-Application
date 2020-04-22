from django.db import models

UNIT_NAME = [
    ('nos', 'NOS'),
    ('meter', 'MTRS'),
    ('feet', 'FEET')
]

# Create your models here.

class CompanyBill(models.Model):
    company_name = models.CharField(max_length=500)

    def __str__(self):
        return self.company_name

class ProductItem(models.Model):
    '''
        This model stores product item name
    '''
    company = models.ForeignKey(CompanyBill, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)
    unit = models.CharField(max_length=5, choices=UNIT_NAME)
    prize = models.IntegerField()

    def __str__(self):
        return self.item_name

class AreaName(models.Model):
    '''
        This model stores area name
    '''
    area_name = models.CharField(max_length=500)

    def __str__(self):
        return self.area_name

class BillModel(models.Model):
    items = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    area = models.ForeignKey(AreaName, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return ''
