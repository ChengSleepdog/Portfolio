## Django 功能展示
### 前言 
這裡主要展示使用 Django 所接觸到的操作或服務
> 因原程式碼不方便直接展示，因此會慢慢過濾後丟上來補充 

### 07/17
- 撰寫並使用 docker 啟動伺服器

### 07/18
- 重構 Django 架構，並新增 nmap 功能 API 範例

### 07/26
- 建立與設定 Postgres 連線 
  - 問題：使用 docker 建立 postgres 時，不能設定 DB_HOST 為 localhost，Django 會找尋本機而不是容器 DB 導致錯誤
