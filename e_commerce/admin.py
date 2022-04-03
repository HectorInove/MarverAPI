from django.contrib import admin

from e_commerce.models import Comic, WishList, UserDetail

admin.site.register(Comic)
admin.site.register(UserDetail)

class ComicAdmin(admin.ModelAdmin):
    list_display = ('marvel_id', 'title', 'stock_qty', 'price')
    list_filter= ('marvel_id','title')
    search_fields = ['title']
    
    fieldsets = (
        (None, {
            'fields': ('marvel_id', 'title', 'stock_qty')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description','price', 'picture'),
        }),
    )


admin.site.register(WishList)

class wish_listAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'comic_id', 'favorite', 'cart')
    list_display_links = ('user_id', 'comic_id')
    list_filter= ('favorite','cart')
