from django.contrib import admin
import models


class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryToPostInline(admin.TabularInline):
    model = models.CategoryToPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    '''
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['body']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    '''
    #inlines = [CommentInline, CategoryToPostInline]
    inlines = [CategoryToPostInline]
    list_display = ('title', 'pub_date')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Comment)