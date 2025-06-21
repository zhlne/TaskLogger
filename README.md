
# ✅ TaskLogger 任務記錄系統

一個簡潔實用的任務管理 Web 應用，支援使用者註冊、登入、每日任務建立與完成追蹤，並以圖表方式統計完成率。

## 📌 功能簡介

- ✅ 使用者註冊 / 登入 / 登出
  - 登入頁面具備錯誤提示功能（如密碼錯誤、查無帳號）
  - 註冊後可立即登入使用任務功能
- 📝 新增任務（分類：學習、工作、其他）
- 📋 任務狀態切換（完成 / 未完成）
- 📊 圓餅圖統計每日任務完成率
- 🔐 Session 控制登入狀態
- 🎨 使用 Bootstrap 美化介面，Chart.js 畫圖表

## 🛠 使用技術

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML + Jinja2
- Bootstrap 5
- Chart.js

## 📂 專案結構

```
├── app.py             # 主程式與所有路由處理
├── extensions.py      # 資料庫初始化模組
├── init_db.py         # 資料庫初始化腳本
├── models.py          # 資料模型 User / Task
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── register.html
│   └── login.html     # 支援錯誤提示的登入畫面
```
