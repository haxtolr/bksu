from django.apps import AppConfig
from django.db.models.signals import post_save

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # 앱이 로드될 때 호출되는 메서드를 오버라이드
        # 여기에서 신호 함수를 등록합니다.
        from . import signals  # 신호 함수가 정의된 파일을 임포트합니다.
