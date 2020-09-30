from django.contrib import admin
from orm.models import arm, CPU, x86, Language, Framework, Shoes_Brand, Shoe
# Register your models here.
# admin.site.register(arm)


class cpu_arch(admin.ModelAdmin):
    list_display = ('name', 'platform', 'status')


admin.site.register(CPU, cpu_arch)
# admin.site.register(x86)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Shoe)
admin.site.register(Shoes_Brand)
