from django.contrib import admin
from olcha.models import (Category,
                          Group,
                          Product,
                          Image,
                          Comment,
                          Attribute,
                          AttributeValue,
                          PraductAttribute)
# Register your models here.
admin.site.register(Image)
# admin.site.register(Group)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(PraductAttribute)
@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(Group)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'slug']
    prepopulated_fields = {'slug': ('group_name',)}

# @admin.register(Product)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = ['group_name', 'slug']
#     prepopulated_fields = {'slug': ('group_name',)}
