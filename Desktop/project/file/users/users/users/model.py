import uuid
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # set_password()
    nickname = models.CharField(max_length=50, validators=[MinLengthValidator(3, '닉네임은 최소 3자 이상이어야 합니다.')])
    name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="전화번호는 '+8201012345678' 형식으로 입력해야 하며, 최대 15자리까지 가능합니다."
            )
        ]
    )
    last_login = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        """비밀번호를 해싱하여 안전하게 저장합니다."""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    class Meta:
        db_table = 'user'
        ordering = ['-created_at']
