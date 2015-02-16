from project import weixin
from project.models import Post
import random

songs = [
    {
        'title':'Touch My body',
        'description':'SISTAR',
        'music_url':'http://bonfy.qiniudn.com/Touch%20My%20Body.mp3',
        'hq_music_url':'http://bonfy.qiniudn.com/Touch%20My%20Body.mp3',
    },
    {
        'title':'Gin Iro no sora',
        'description':'银魂',
        'music_url':'http://bonfy.qiniudn.com/gin%20iro%20no%20sora.mp3',
        'hq_music_url':'http://bonfy.qiniudn.com/gin%20iro%20no%20sora.mp3',
    },
    {
        'title':'Mr.Raindrop',
        'description':'银魂',
        'music_url':'http://bonfy.qiniudn.com/Mr.Raindrop.mp3',
        'hq_music_url':'http://bonfy.qiniudn.com/Mr.Raindrop.mp3',
    },
    {
        'title':'勇气100%',
        'description':'NYC 忍者乱太郎',
        'music_url':'http://bonfy.qiniudn.com/%E5%8B%87%E6%B0%97100%25.mp3',
        'hq_music_url':'http://bonfy.qiniudn.com/%E5%8B%87%E6%B0%97100%25.mp3',
    },
    {
        'title':'泡沫',
        'description':'邓紫棋',
        'music_url':'http://bonfy.qiniudn.com/%E6%B3%A1%E6%B2%AB.mp3',
        'hq_music_url':'http://bonfy.qiniudn.com/%E6%B3%A1%E6%B2%AB.mp3',
    }
]


@weixin('*')
def reply_all(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    message_type = kwargs.get('type')
    content = kwargs.get('content', message_type)

    eventType = kwargs.get('event', '')

    if content == 'event' and eventType == 'subscribe':
        WelcomeMsg = '欢迎关注Shrimp，你老婆也爱吃虾?\n回复：M 收听音乐\n回复：N 查看新闻'
        return weixin.reply(
            username, sender=sender, content=WelcomeMsg
        )

    elif content == 'M':
        music = songs[random.randrange(0,4)]
        return weixin.reply(
            username, type='music', sender=sender,
            title=music['title'],
            description=music['description'],
            music_url=music['music_url'],
            hq_music_url=music['hq_music_url'],
        )
    elif content == 'N':

        posts = Post.query.order_by('id desc').limit(5)
        articles = [{
                    'title': post.title,
                    'description': post.title,
                    'picurl': 'http://bonfy.qiniudn.com/back.jpg',
                    'url': 'http://www.bonfy.im/blog/detail/'+str(post.id),
                } for post in posts]
        return weixin.reply(
            username, type='news', sender=sender,
            articles=articles
        )
    else:
        return weixin.reply(
            username, sender=sender, content=content
        )