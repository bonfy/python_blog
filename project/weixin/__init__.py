from project import weixin
from project.models import Post

jing_music = (
    'http://cc.cdn.jing.fm/201310171130/19e715ce8223efd159559c15de175ab6/'
    '2012/0428/11/AT/2012042811ATk.m4a'
)


@weixin('*')
def reply_all(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    message_type = kwargs.get('type')
    content = kwargs.get('content', message_type)

    if content == 'M':
        return weixin.reply(
            username, type='music', sender=sender,
            title='Weixin Music',
            description='weixin description',
            music_url=jing_music,
            hq_music_url=jing_music,
        )
    elif content == 'N':

        posts = Post.query.order_by('id desc').limit(5)
        articles = [{
                    'title': post.title,
                    'description': post.title,
                    'picurl': '',
                    'url': 'http://www.bonfy.im/details/'+str(post.id),
                } for post in posts]
        return weixin.reply(
            username, type='news', sender=sender,
            articles=articles
        )
    else:
        return weixin.reply(
            username, sender=sender, content=content
        )