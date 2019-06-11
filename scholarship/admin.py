from django.contrib import admin
from .models import Scholar_content,Scholar_filter,Uniqueness
# Register your models here.


class FilterAdmin(admin.ModelAdmin):
    model = Scholar_filter
    list_display=['get_name']
    def get_name(self,obj):
        return obj.filter_id.scholar_name+'  필터링 추가'


class UniquenessAdmin(admin.ModelAdmin):
    model = Uniqueness
    list_display=['get_name']
    def get_name(self,obj):
        return obj.u_ID.filter_id.scholar_name+'  특이사항'


admin.site.register(Scholar_content)
admin.site.register(Scholar_filter,FilterAdmin)
admin.site.register(Uniqueness,UniquenessAdmin)