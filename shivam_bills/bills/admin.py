from django.contrib import admin
import nested_admin
from .models import Company, Area, Products, ProductDetails, Bills

class ProductInline(nested_admin.NestedTabularInline): # or StackedInline
    model = Bills
    template = 'admin/bills/table.html'
    extra = 0

class BillInline(nested_admin.NestedStackedInline): # or StackedInline
    model = ProductDetails
    template = 'admin/bills/stacked.html'
    extra = 0
    inlines = [ProductInline]

class BillAdmin(nested_admin.NestedModelAdmin):
    inlines = [BillInline]
    change_form_template = 'admin/bills/change_view.html'
    def get_total(self):
        arr_total = []
        for j in self.inlines[0].model.objects.all():
            total = 0
            print(j.prize)
            for i in self.inlines[0].inlines[0].model.objects.all():
                if j == i.items:
                    total += i.quantity
            arr_total.append({'product': j ,'quantity': total, 'prize': total*j.prize})
        return arr_total
    
    def grand_total(self):
        total = self.get_total()
        grand_total = 0
        for i in total:
            grand_total += i['prize']
        print(grand_total)
        return grand_total

    def change_view(self, request, object_id, form_url='', extra_context=None):
        my_context = {
            'order_total': self.get_total(),
            'grand_total': self.grand_total(),
        }
        return super(BillAdmin, self).change_view(request, object_id, form_url,
            extra_context=my_context)

# Register your models here.
admin.site.register(Area)
admin.site.register(Products)
admin.site.register(Company, BillAdmin)
