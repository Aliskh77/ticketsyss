# tickets/admin.py
from django.contrib import admin
from .models import User, Ticket, Comment

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'created_at')
    list_filter = ('ticket',)

admin.site.register(User)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
