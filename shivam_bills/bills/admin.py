from django.contrib import admin
import nested_admin
from .models import Company, Area, Products, ProductDetails, Bills, CompanySetting
from solo.admin import SingletonModelAdmin
from django.utils.html import format_html
from django.urls import reverse

class ProductInline(nested_admin.NestedTabularInline): # or StackedInline
    model = Bills
    extra = 0

class BillInline(nested_admin.NestedStackedInline): # or StackedInline
    model = ProductDetails
    template = 'admin/bills/stacked.html'
    extra = 0
    inlines = [ProductInline]

class BillAdmin(nested_admin.NestedModelAdmin):
    inlines = [BillInline]
    list_display = (
        'company',
        'account_actions',
    )
    change_form_template = 'admin/bills/change_view.html'
    def get_total(self, object_id):
        arr_total = []
        for j in self.inlines[0].model.objects.all():
            total = 0
            for i in self.inlines[0].inlines[0].model.objects.all():
                if j == i.items and Company.objects.get(pk=object_id) == j.company:
                    total += i.quantity
            arr_total.append({'product': j ,'quantity': total, 'prize': total*j.prize})
        return arr_total
    
    def grand_total(self, object_id):
        total = self.get_total(object_id)
        grand_total = 0
        for i in total:
            grand_total += i['prize']
        return grand_total

    def change_view(self, request, object_id, form_url='', extra_context=None):
        my_context = {
            'order_total': self.get_total(object_id),
            'grand_total': self.grand_total(object_id),
        }
        return super(BillAdmin, self).change_view(request, object_id, form_url,
            extra_context=my_context)
    
    def account_actions(self, obj):
        return format_html(
            '<a class="button" target="_blank" href="{}">Download Sheet</a>&nbsp;'
            '<a class="button" target="_blank" href="{}">Download Bill</a>',
            reverse('pdf_generate', args=[obj.pk]),
            reverse('download_bills', args=[obj.pk]),
        )
    account_actions.short_description = 'Actions'
    account_actions.allow_tags = True

# Register your models here.
admin.site.register(Area)
admin.site.register(Products)
admin.site.register(Company, BillAdmin)
admin.site.register(CompanySetting, SingletonModelAdmin)
