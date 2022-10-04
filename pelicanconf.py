AUTHOR = '牛思宇'
SITENAME = '平舆一高书法协会'
SITEURL = 'https://ygsfxh.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = './pelican-theme/backdrop'
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# 下面自己看着改
BACKDROP_IMAGE = "https://pic2.zhimg.com/80/v2-892af670f6d0ad7b46564dfa8c3858b0_720w.jpg?source=1940ef5c"  # 背景图片
EMAIL = 'metalstorm15@163.com'  # 你的邮箱
