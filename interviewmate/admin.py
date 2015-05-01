from django.contrib import admin
from interviewmate.models import Category, Question, UserProfile
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','category','content')

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile)
