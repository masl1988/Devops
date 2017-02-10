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

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author_id']
    list_filter = ['name']
    search_fields = ['name']

    def get_course_type(self):
        return obj.author.name
    get_course_type.short_description = ' obj.author.name'

class SumAdmin(admin.ModelAdmin):
    list_display = ['id', 'sum1', 'sum2', 'summ']
    list_filter = ['id', 'sum1', 'sum2', 'summ']
    search_fields = ['id', 'sum1', 'sum2', 'summ']

admin.site.register(Author, AuthorAdmin)
admin.site.register(sum, SumAdmin)
admin.site.register(Book, BookAdmin)



#admin.site.register(Book)
#admin.site.register(sum)

