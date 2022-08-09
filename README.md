# 中文暗网爬虫

## 运行环境
```
root# wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
root# tar xzf geckodriver-v0.31.0-linux64.tar.gz
root# mv geckodriver /usr/local/bin/
```

## 运行方式
```
没有什么特殊的库，缺啥直接pip安装就行
root# cd /ChineseDarkWebCrawler/DrakWeb/Crawler
root# pipenv install
root# pipenv shell
(ChineseDarkWebCrawler-AEMMb0hY) # pip install django
(ChineseDarkWebCrawler-AEMMb0hY) # pipenv run python manage.py runserver 0.0.0.0:8080 &
```

#### 页面爬取
```
darkweb.py 页面爬取保存及图片id保存脚本
python darkweb.py keyword pagenum
keyword必须是其中一个：'sex','data','service','material','virtual_source','teach','cvv','other','basic','private'
pagenum是页数，随意
(ChineseDarkWebCrawler-AEMMb0hY) # python darkweb.py private 1
your keyword must be in 'sex','data','service','material','virtual_source','teach','cvv','other','basic','private'
```
#### 图片爬取
```
get_darkweb_pic_auto.py 根据保存的图片id进行图片定时爬取
python get_darkweb_pic_auto.py
时间间隔自行设定
```
#### 前台显示
```
使用nginx.conf启动nginx
python manage.py runserver 127.0.0.1 port
修改配置文件连对应的端口号
```
## 预览
![1](1.png "1")

![2](2.png "2")

## PS
如果要用前台展示，换个好看的前端，没空改，所以太丑了，顺便帮我更新下
