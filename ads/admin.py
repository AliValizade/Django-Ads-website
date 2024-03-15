from django.contrib import admin
from django.contrib import admin, messages
from django.db.models import Count, Sum, F
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.http import urlencode 

from . import models


class AdImageInline(admin.TabularInline): # یا StackedInline
    model = models.AdImage
    extra = 5  # تعداد فیلدهای خالی برای آپلود تصاویر اضافی


@admin.register(models.Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'advertiser_name', 'city', 'main_image', ]
    list_per_page = 10
    search_fields = ['title', ]
    inlines = [AdImageInline]  


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'top_ad', ]
