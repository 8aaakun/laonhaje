from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # 표시할 필드 목록 설정
    list_display = ['username', 'email', 'first_name', 'last_name', 'profile_picture']
    
    # 검색 기능을 사용하여 사용자 검색
    search_fields = ['username', 'email']
    
    # 프로필 이미지 미리 보기
    readonly_fields = ('profile_picture_preview',)
    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return f'<img src="{obj.profile_picture.url}" style="max-height:200px;"/>'
        else:
            return 'No Image'
    profile_picture_preview.allow_tags = True
    profile_picture_preview.short_description = 'Profile Picture Preview'

    # 필드셋 설정 (필요한 경우)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # 필드셋 내 순서 설정 (필요한 경우)
    ordering = ('-date_joined',)

# CustomUser 모델을 등록
admin.site.register(CustomUser, CustomUserAdmin)
