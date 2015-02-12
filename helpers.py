# coding:utf-8

__author__ = 'ChenKai'

from feedgen.feed import FeedGenerator

from project.models import Post
from project import db
import os
import pytz
from datetime import datetime
import time

filename = 'project/static/rss/atom.xml'


def CDATA(str):
    return '<![CDATA[ %s ]]>' % str


# 生成atom.xml 用于Rss
def genAtom(filename):

    if os.path.exists(filename):
        os.remove(filename)

    fg = FeedGenerator()
    fg.title("BONFY")
    fg.link(href='/atom.xml', rel='self')
    fg.link(href='http://www.bonfy.im/')

    fg.id('http://www.bonfy.im/')
    fg.author({
        'name': 'BONFY',
        'email': 'bonfygithub@163.com'
    })

    posts = Post.query.order_by('id desc').limit(10)

    for post in posts:
        fe = fg.add_entry()
        fe.title(post.title)
        fe.link(href='www.bonfy.im/blog/detail/%d' % int(post.id), rel='self')

        local = pytz.timezone("Asia/Shanghai")
        local_dt = local.localize(post.insert_dt, is_dst=None)
        utc_dt = local_dt.astimezone(pytz.utc)

        fe.published(utc_dt)
        fe.id(post.title)
        fe.content(post.content_html, type='html')

    fg.atom_file(filename)


# 将Hexo的.md file 转存进数据库
# 需要将所有的.md file 放进 static/md 文件夹中
def initMd(filePath):
    for file_name in os.listdir(filePath):
        with open(os.path.join(filePath, file_name), 'r') as f:
            lines = f.readlines()

            title = str(lines[0]).strip()[len('title: '):]
            user_id = 1
            insert_date = datetime.strptime(str(lines[1]).strip()[len('date: '):].replace('/', '-'), "%Y-%m-%d %H:%M:%S")
            # tag_id = 1   # tag_id 默认为1 随便说说
            content = ''.join(lines[3:])

            new_message = Post(
                title,
                content,
                user_id,
                insert_dt=insert_date
            )
            db.session.add(new_message)
            db.session.commit()


if __name__ == '__main__':
    # genAtom()
    initMd('project/static/md')