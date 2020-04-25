from django.db import models
from django.core.validators import RegexValidator
from solo.models import SingletonModel
from simple_history.models import HistoricalRecords

UNIT_NAME = [
    ('NOS', 'NOS'),
    ('MTRS', 'MTRS'),
    ('FEET', 'FEET')
]

# Create your models here.
class CompanySetting(SingletonModel):
    '''
        This model store compant settings like - Name, Email, Contact, Address, Logo
    '''
    name = models.CharField(max_length=500)
    logo = models.ImageField(upload_to = 'pic_folder/')
    email = models.EmailField()
    contact = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='[0-9]{10,13}$',
            message='Invalid contact number. Maximum 10-13 digits are allowed.',
            code='invalid_username'
        ),
    ])
    address = models.TextField()

    def __str__(self):
        return "Company Settings"

    class Meta:
        verbose_name = "Company Settings"
        verbose_name_plural = "Company Settings"

class Company(models.Model):
    '''
        This model stores company name
    '''
    company = models.CharField(max_length=500)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Final Bill'
        verbose_name_plural = 'Final Bills'

class Area(models.Model):
    '''
        This model stores area name
    '''
    area = models.CharField(max_length=500)

    def __str__(self):
        return self.area

class Products(models.Model):
    '''
        This model stores product name
    '''
    product_name = models.CharField(max_length=500)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductDetails(models.Model):
    '''
        This model stores product details
    '''
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    unit = models.CharField(max_length=5, choices=UNIT_NAME)
    prize = models.IntegerField()

    def __str__(self):
        return self.product.product_name
            
    class Meta:
        verbose_name = 'Bill Details'
        verbose_name_plural = 'Bill Details'

class Bills(models.Model):
    items = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return ''
    
    class Meta:
        verbose_name = 'Sheet Details'
        verbose_name_plural = 'Sheet Details'