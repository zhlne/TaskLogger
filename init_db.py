from app import app
from extensions import db
from models import User, Task

with app.app_context():
    db.drop_all()      # 可選：先清空所有表格（如果有）
    db.create_all()    # ✅ 這會建立 User 和 Task 兩張表

print("✅ 資料庫初始化完成")

