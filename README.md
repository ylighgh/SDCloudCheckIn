# SD Cloud自动签到脚本

原`66yun`机场

机场地址:[https://shidongli148.xyz/](https://shidongli148.xyz/)

注意： **机场地址会经常变动，如果签到失败，请修改config.py中的URL地址**

使用Python的`requests`库进行每日自动签到，白嫖流量

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用

```bash
1. 重命名config.py文件
mv config.py.sample config.py

2. 修改`config.py`中的用户信息

3. 执行脚本
python app.py
```

## 示例

```
python app.py
2022-11-03 19:39:10 4003 [INFO] 用户aaa@qq.com签到成功！
2022-11-03 19:39:13 4003 [INFO] 用户bbb@qq.com签到成功！
```
