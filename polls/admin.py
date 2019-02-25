from django.contrib import admin

from .models import Choice, Question

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]
    # fields = ['pub_date', 'question_text']


# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
# End of File
