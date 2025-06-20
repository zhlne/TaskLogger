from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
from extensions import db
from models import User, Task

app = Flask(__name__)

# 設定密鑰用於 session 加密
app.secret_key = 'your_secret_key'

# 設定資料庫路徑（SQLite 檔案）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasklogger.db'

# 初始化資料庫
db.init_app(app)

# 首頁：根據登入狀態導向對應頁面
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# 使用者註冊頁面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# 使用者登入頁面
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None  # 預設沒有錯誤
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user:
            if user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('dashboard'))
            else:
                error = "密碼錯誤，請再試一次"
        else:
            error = "查無此帳號，請註冊新帳號"

    return render_template('login.html', error=error)

# 任務主畫面（新增任務、顯示清單、任務統計）
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    tasks = Task.query.filter_by(user_id=user_id, date=date.today()).all()

    if request.method == 'POST':
        content = request.form['content']
        category = request.form['category']
        task = Task(
            user_id=user_id,
            content=content,
            category=category,
            date=date.today(),
            is_done=False
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('dashboard'))

    # 計算完成與未完成任務數量，提供圖表使用
    completed = sum(1 for t in tasks if t.is_done)
    pending = sum(1 for t in tasks if not t.is_done)

    return render_template('dashboard.html', tasks=tasks, completed=completed, pending=pending)

# 切換任務完成狀態（按鈕觸發）
@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get(task_id)
    task.is_done = not task.is_done
    db.session.commit()
    return redirect(url_for('dashboard'))

# 使用者登出
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# 啟動 Flask 開發伺服器
if __name__ == '__main__':
    app.run(debug=True)


