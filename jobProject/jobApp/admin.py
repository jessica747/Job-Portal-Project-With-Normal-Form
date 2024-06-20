from django.contrib import admin
from jobApp.models import *


class Custom_user_model_display(admin.ModelAdmin):
    list_display=['username','display_name','user_type']
    search_fields=['username','display_name']



admin.site.register(Custom_user_model,Custom_user_model_display)
admin.site.register(recruiter_info_model)
admin.site.register(seeker_info_model)





