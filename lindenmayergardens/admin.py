from django.contrib import admin

from .models import Lsystem, Lrule

# Register your models here.


class LrulesInLine(admin.StackedInline):
    model = Lrule

class LsystemAdmin(admin.ModelAdmin):
    list_display = ['init_text']
    inlines = [LrulesInLine]
    search_fields = ['init_text']

class LruleAdmin(admin.ModelAdmin):
    list_display = ['str_in', 'str_out', 'rule_priority', 'lsys']
    search_fields = ['question_text']

admin.site.register(Lsystem, LsystemAdmin)
admin.site.register(Lrule, LruleAdmin)