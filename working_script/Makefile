#Makefile
.PHONY: reset_all_db, reset_db, db_init, clear_whole_progrme, venv_build, output_venv, remove_all_imag, rebuild_code, generate_ca, oneline_create_super_user
# 解釋器設定為 /bin/bash 默認為 /bin/sh
SHELL := /bin/bash

# === 預設常數 ===
Dockerfile_fastapi = Dockerfile
TESTING_PROGRAME = test_db
# SETTING_FILE = docker-deploy-database-redis.yml # 本地
SETTING_FILE = docker-deploy.yml # docker 
# === SSL Scripts ===
CA_KEY = SSL/ca.key
CA_CRT = SSL/ca.crt

# 單純下 make 時會執行的功能 
all: clear_whole_progrme remove_all_image docker_init

docker_build:
	@docker build -f $(Dockerfile_fastapi) .
docker_init: docker_build
	@docker-compose -f $(SETTING_FILE) up -d

# 只有再本地測試才會用到
# -------------------------
db_init: 
	@sh initinal_db.sh
	@sh initinal_seed.sh
db_init_singal:
	@python3 manage.py makemigrations $(TESTING_PROGRAME)
	@python3 manage.py migrate
# -------------------------

rebuild_code:
	@docker-compose -f $(SETTING_FILE) up -d --build

# 關閉後刪除所有當前的 docker 
docker_clean:
	@docker ps -aq | xargs docker stop | xargs docker rm
# 刪除未被使用的數據卷宗 
docker_volume_clean:
	@docker volume prune
# 刪除所有未使用image
docekr_image_clean:
	@docker image prune
clear_whole_progrme: docker_clean docker_volume_clean docekr_image_clean
	@python3 clean_all_apps_migrations_folders.py 

# 
remove_all_image:
	@read -p "警告：執行 'docker rmi -f $$(docker images -aq)' 將刪除所有 Docker 映像檔。這個操作無法還原。您確定要繼續嗎？ [y/N] " choice; \
	if [[ $$choice =~ ^[Yy]$$ ]]; then \
		echo "繼續執行 'docker rmi -f $$(docker images -aq)'..."; \
		docker rmi -f $$(docker images -aq); \
	else \
		echo "操作已取消。"; \
		exit 1; \
	fi

reset_db: 
	@python3 manage.py migrate $(TESTING_PROGRAME) zero
	@python3 manage.py makemigrations $(TESTING_PROGRAME)
	@python3 manage.py migrate $(TESTING_PROGRAME)

# 開發環境常用 
remove_poetry_venv:
	@rm -f pyproject.toml
	@rm -f poetry.lock
	@rm -rf .venv
venv_build: remove_poetry_venv
	@poetry init 
	@poetry add $$(cat requirements.txt)
	@poetry shell

# 快速建立資料庫admin使用者 
oneline_create_super_user:
	@echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gamil.com', 'admin123')" | python manage.py shell

# 快速導出環境 
output_venv:
	@poetry export -o requirements_test.txt --without-hashes

generate_ca:
# 生成 .key 私鑰文件
	@openssl genrsa -out $(CA_KEY) 2048
# 自簽名生成 .crt 證書文件
	@openssl req -new -x509 -days 3650 \
    -key $(CA_KEY) -out $(CA_CRT) \
    -subj "/C=TW/ST=Taiwan/L=Taipei/O=TEST INC./OU=Test/CN=gRPC_CA"
