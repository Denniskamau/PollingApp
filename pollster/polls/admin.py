from django.contrib import admin

# Register your models here.
from .models import Questions,Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to Pollster admin Area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
    ('Date Information', {'fields':['pub_date'],'classes':['collapse']}),]
    inlines = [ChoiceInline]
# admin.site.register(Questions)
# admin.site.register(Choice)
admin.site.register(Questions,QuestionAdmin)
