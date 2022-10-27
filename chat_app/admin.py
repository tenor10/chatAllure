from django.contrib import admin

from chat_app.models import Message, User


# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "receiver", "date_time", "message")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "date_joined")


from django.contrib import admin

# Register your models here.
