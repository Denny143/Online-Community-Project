from django.contrib import admin

# Register your models here.

from .models import Place,Teacher,StudioUser


admin.site.register(Place)

admin.site.register(StudioUser)

admin.site.register(Teacher)

#@admin.register(Teacher)
#class TeacherAdmin(admin.ModelAdmin):
#    def get_form(self, request, obj=None, **kwargs):
#        if not request.user.is_superuser:
#            self.exclude = ['authorized']
#        return super(DocumentModelAdmin, self).get_form(request, obj, **kwargs)
