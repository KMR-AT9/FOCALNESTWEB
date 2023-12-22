from django.contrib import admin
from .models import BlogPost, ServicePost, Gallery, GalleryImage,Enquiry
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.html import format_html

class BlogPostAdmin(admin.ModelAdmin):
    actions = None
    prepopulated_fields = {'Title_url': ('Blog_title',)}
    def has_add_permission(self, request, obj=None):
        return False

class ServicePostAdmin(admin.ModelAdmin):
    actions = None
    prepopulated_fields = {'Title_Url': ('title',)}
    def has_add_permission(self, request, obj=None):
        return False

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1 

class GalleryAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('Gallery_Title', 'service')
    search_fields = ['Gallery_Title']
    list_filter = ['service']
    inlines = [GalleryImageInline]
    def has_add_permission(self, request, obj=None):
        return False
    
class EnquiryAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone', 'interested_in', 'message')
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        # Disable delete permission
        return False

    def get_actions(self, request):
        # Remove the default delete action from the list
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_list_display(self, request):
        # Add custom button to the list display
        return ('name', 'email', 'phone', 'interested_in', 'custom_button')

    def custom_button(self, obj):
        delete_url = reverse('admin:FocalNest_enquiry_delete', args=[obj.id])
        return format_html('<a class="button" href="{}" onclick="return confirm(\'Are you sure you want to delete?\')">Delete</a>', delete_url)

    custom_button.short_description = 'Delete'

    def response_add(self, request, obj, post_url_continue=None):
        return super().response_add(request, obj, post_url_continue='.')

    def delete_view(self, request, object_id, extra_context=None):
        # Custom delete view logic
        obj = self.get_object(request, object_id)
        if obj:
            obj.delete()
            self.message_user(request, 'The object was successfully deleted.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


admin.site.register(BlogPost, BlogPostAdmin )
admin.site.register(ServicePost, ServicePostAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Enquiry, EnquiryAdmin)

