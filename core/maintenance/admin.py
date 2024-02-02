from django.contrib import admin

from .models import Answer, FormType, Maintenance, Question
# Register your models here.


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'maintenance', 'answer']
    search_fields = ['maintenance']


class FormTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'station', 'user', 'created_at']
    search_fields = ['station']

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'form_type', 'question', 'is_active']
    search_fields = ['form_type', 'is_active', 'question']


admin.site.register(Answer, AnswerAdmin)
admin.site.register(FormType, FormTypeAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Question, QuestionsAdmin)