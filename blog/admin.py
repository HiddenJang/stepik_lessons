from django.contrib import admin
from .models import Post, Comment
# Register your models here.


#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # перечень полей для отображения в админке
    list_filter = ['status', 'created', 'publish', 'author'] # добавляет боковую панель с настройками фильтрации
    search_fields = ['title', 'body'] # добавляет поле для поиска и указываем список полей, по которым можно выполнять поиск
    prepopulated_fields = {'slug': ('title',)} # при вводе заголовка нового поста поле slug заполняется автоматически.Вы сообщили Django, что нужно предзаполнять поле slug данными, вводимыми в поле title
    raw_id_fields = ['author'] # поле author отображается поисковым виджетом, который будет более приемлемым, чем выбор из выпадающего списка, когда у вас тысячи пользователей
    autocomplete_fields = ['author'] #  заменяет выпадающий список на поле с автозаполнением, которое автоматически фильтрует результаты по введенным символам пользователем
    date_hierarchy = 'publish'  #  навигационные ссылки для навигации по иерархии дат ниже поиска
    ordering = ['status', 'publish'] #  задает критерии сортировки, которые будут использоваться по умолчанию


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']