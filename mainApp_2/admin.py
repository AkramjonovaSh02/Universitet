from django.contrib import admin


from .models import Yonalish, Fan, Ustoz


#4
@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    search_fields = ('ism', )
    search_help_text = ('ism boyicha qidirish')

#5
@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_filter = ('aktiv',)
    search_fields = ('nom',)
    search_help_text = ('nom bo\'yicha qidirish')

#6
@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_filter = ('asosiy', 'yonalish')
    search_fields = ('nom',)
    search_help_text = ('nom bo\'yicha qidirish')

