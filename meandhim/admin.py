from django.contrib import admin


from .models import user, question, response, anwser
# Register your models here.
admin.site.register(user)
admin.site.register(question)
admin.site.register(response)
admin.site.register(anwser)
