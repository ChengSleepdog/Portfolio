# 引入 Python 3.9 基礎鏡像
FROM python:3.9
LABEL maintainer sleepdog

ENV PYTHONUNBUFFRED 1

# 更新與安裝 OS 套件， --no-install-recommends 讓套件安裝必要依賴即可
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  --no-install-recommends \ 
        git \
        libpq-dev \
        make

# 移動或創建到工作目錄/web
RUN mkdir /web
WORKDIR /web

# 將環境依賴複製
COPY requirements.txt .

# 安裝環境依賴
RUN pip install -r requirements.txt

# 複製正個目錄到容器中
COPY . .
COPY .env .env

# set API_ENVIRONMENT，./setting 才能引入正確的 config 檔案
RUN export API_ENVIRONMENT=dev

# 持久化路徑點
EXPOSE 8000
# 運行 Django 服務
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]