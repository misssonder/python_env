# FLask

## 虚拟环境管理

> ```linux
> pip freeze --all > requirements.txt
> 
> pip install -r requirements.txt  #安装依赖包
> ```

## 数据库

``` python
设置数据库连接的兼容性
import os,sys
WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

设置数据库URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'lib.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
```

## 登录用户认证

``` python
@login_required #一个页面的用户认证保护

```

``` html
{% if current_user.is_authenticated %}
<li class="li_left"><a class="li_a" href="{{ url_for('logout') }}">登出</a></li>
{% else %}
<li class="li_left"><a class="li_a" href="{{ url_for('login') }}">登录</a></li>
{% endif %}

current_user.is_authenticated 
<!--一个模板内部的用户认证保护-->
```

