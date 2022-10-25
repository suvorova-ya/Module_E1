from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from.models import Post,Contact

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'created')
    list_filter = ('created',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['created']
    summernote_fields = ('body',)


admin.site.register(Post,PostAdmin)
admin.site.register(Contact)