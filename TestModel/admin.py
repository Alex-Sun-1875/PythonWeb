from django.contrib import admin

from TestModel.models import Test, Contact, Tag

"""
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse', ), # CSS
            'fields': ('age', ),
        }]
    )
"""

class TagInLine(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    inlines = [TagInLine]   # inline
    search_fields = ('name', 'age')
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse'), # CSS
            'fields': ('age', ),
        }]
    )

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
