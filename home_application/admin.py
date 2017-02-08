# -*- coding: utf-8 -*-

# import from apps here


# import from lib
# ===============================================================================
# from django.contrib import admin
# from apps.__.models import aaaa
#
# admin.site.register(aaaa)
# ===============================================================================
from django.contrib import admin

from .models import Author, Book
from .models import sum


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(sum)