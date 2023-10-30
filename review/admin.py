from django.contrib import admin
from .models import Game, Review, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Review)
class ReviewAdmin (SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'username', 'game', 'created_on')
    search_fields = ['title', 'game', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')   
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'review', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('username', 'email', 'body')
    actions = ['approve_comments']                      
                                                        
    def approve_comments(self, request, queryset):      
        queryset.update(approved=True)                  



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'genre', 'year', 'platform',)
    search_fields = ['title', 'game', 'gerne', 'year', 'platform',]
    prepopulated_fields = {'slug': ('title',)}
