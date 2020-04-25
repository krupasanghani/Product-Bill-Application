from django.shortcuts import render

from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from .admin import Area, Bills, Company, ProductDetails 
from weasyprint import HTML
from datetime import datetime

# Create your views here.
def downaload_sheet(request, object_id):
    area = Area.objects.all()
    company_name = Company.objects.get(pk=object_id)
    product = ProductDetails.objects.filter(company=company_name)
    sheet = []
    arr_total = []
    for j in ProductDetails.objects.filter(company=company_name):
        total = 0
        for i in Bills.objects.all():
            if str(i.items) == str(j.product):
                sheet.append({'product_name': j.product, 'area': i.area, 'quantity': i.quantity  })
                total += i.quantity 
        arr_total.append({'product': j.product ,'quantity': total})
    html_string = render_to_string('sheet.html', {
        'company_name': company_name,
        'product': sheet,
        'total_quantity': arr_total,
        'area': area,
        })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/sheet.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('sheet.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="sheet.pdf"'
        return response

    return response

def download_bills(request, object_id):
    area = Area.objects.all()
    company_name = Company.objects.get(pk=object_id)
    product = ProductDetails.objects.filter(company=company_name)
    sheet = []
    arr_total = []
    for j in ProductDetails.objects.filter(company=company_name):
        total = 0
        for i in Bills.objects.all():
            if str(i.items) == str(j.product):
                total += i.quantity 
        arr_total.append({'product': j.product, 'unit': j.unit,'quantity': total, 'rate': j.prize, 'total': total*j.prize})
    grand_total = 0
    for i in arr_total:
        grand_total += i['total']

    domain = request.build_absolute_uri('/')[:-1]
    html_string = render_to_string('bills.html', {
        'company_name': company_name,
        'bills': arr_total,
        'grand_total': grand_total,
        'domain': domain,
        'date': company_name.history.last().history_date
        })

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/bills.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('bills.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="bills.pdf"'
        return response

    return response