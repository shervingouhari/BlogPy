from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Category, Article
from .forms import UserCreationForm, UserChangeForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    fieldsets = (
        ('General Info', {'fields': ('avatar', 'username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'description')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Additional Info', {'fields': ('date_joined', 'last_login')})
    )
    add_form = UserCreationForm
    add_fieldsets = (
        ('Mandatory Fields', {'fields': ('username', 'password1', 'password2')}),
    )
    list_display = ['id', 'username', 'email', 'is_active', 'is_staff']
    list_filter = ['is_staff', 'is_active']
    readonly_fields = ['date_joined', 'last_login']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

    def get_title(self, obj):
        return obj


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'author', 'title', 'created', 'updated', 'promoted']
    list_filter = ['promoted']
    search_fields = ['title']

    def get_title(self, obj):
        return obj
