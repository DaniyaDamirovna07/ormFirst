from django.contrib import admin
from phones.models import Phone
from django.template.defaultfilters import slugify

# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'image','price','release_date', 'lte_exists', 'slug']
    list_filter = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}

def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        super(Phone, self).save(*args, **kwargs)