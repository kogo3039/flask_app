import os

# 현재 파일의 위치 ./flask_app
BASE_DIR = os.path.dirname(__file__)

# 현재 파일의 위치에 flask_app.db 파일 만들기
DATABASE = os.path.join(BASE_DIR, 'flask_app.db')

# 데이터 베이스 주소 등록하고 데이터베이스 이름 등록
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE}"

# SQLALCHEMY 이벤트 처리 안함
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "KOGO1490"