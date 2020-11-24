# 小猴子

= = ...

![猫猫哭泣](https://raw.githubusercontent.com/tonicbupt/xiaohouzi/master/images/cry.jpg)

打黑工啊... 写一些烂脚本...

0. 先 `pip install pillow --index-url https://pypi.doubanio.com/simple/`
1. 把图片都丢到一个目录, 脚本也丢到一个目录
2. terminal 里 cd 到这个目录, 然后 `python xiaohouzi.py` 或者 `./xiaohouzi.py`
3. done...

# Usage

```
➜ ./xiaohouzi.py -h
usage: xiaohouzi.py [-h] [source] [target]

positional arguments:
  source      source dir for pictures, default current dir
  target      target dir name for pictures, default pictures_4_3

optional arguments:
  -h, --help  show this help message and exit
```

唉又升级了... 要用 macOS 啊... 得有 `sips`

```
$ gunicorn app:app --bind 0.0.0.0:5000 --workers 4
```
