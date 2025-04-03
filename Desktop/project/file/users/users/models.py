import uuid # 사용자 ID를 고유 UUID로 만들기 위해 사용
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator 
# validators 필드값 검증 도구 / min 은 문자열 길이 / 입력받을 때 형식을 검사

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    # 사용자 고유 식별자 / UUID 형태
    # 자동으로 생성, 수정 불가 (editable=False) / 기본 키로 사용 (Primary_key=ture)
    
    email = models.EmailField(max_length=255, unique=True)
    # 이메일 주소 저장 / EmailField: 이메일 형식 자동 검증
    # unique = true 같은 이멜 중복 가입 불가
    
    password = models.CharField(max_length=255)  # set_password()를 사용하여 해시 저장 / 해시된 비밀번호 저장 필드
    
    nickname = models.CharField(max_length=50, validators=[MinLengthValidator(3, '닉네임은 최소 3자 이상이어야 합니다.')]) # 최소 3자 이상 검증
    
    name = models.CharField(max_length=50) # 사용자 이름
    
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$', # 전화번호 정규표현식
                message="전화번호는 '+8201012345678' 형식으로 입력, 최대 15자리까지 가능합니다."
            )
        ]
    )
    
    last_login = models.DateTimeField(null=True, blank=True) # 마지막 로그인 / DB null 허용 / 폼에서 공란 허용
    
    is_staff = models.BooleanField(default=False) # 관리자 접근 가능여부
    is_admin = models.BooleanField(default=False) # 관리자 권한 여부
    is_active = models.BooleanField(default=True) # 비활성 계정 여부
    
    created_at = models.DateTimeField(auto_now_add=True) # 처음 객체 생성된 시간 기록
    updated_at = models.DateTimeField(auto_now=True) # 수정될때 시간 갱신

# 객체를 문자열로 출력할때 이메일 보이도록 
    def __str__(self):
        return self.email

# 비밀번호 해시 저장 예: "1234" → "pbkdf2_sha256$260000$...."
    def set_password(self, raw_password):
        """비밀번호를 해싱하여 안전하게 저장합니다."""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    class Meta:
        db_table = 'user' # 실제 DB에 저장될 테이블 이름
        ordering = ['-created_at'] # 생성일 역순(최신 사용자 먼저)
