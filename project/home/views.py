# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#################
#### imports ####
#################

from flask import render_template, Blueprint, \
    request, flash, redirect, url_for, jsonify, abort
from flask.ext.login import login_required, current_user
from config import PAGE_SIZE

from .forms import MessageForm
from project import db
from project.models import Post, Tag
from project.helpers import genAtom

import mistune

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
@home_blueprint.route('/index')
@home_blueprint.route('/index/<int:page>')
def home(page=1):
    error = None

    # posts = db.session.query(Post).all()

    posts = Post.query.order_by('insert_dt desc').paginate(page, PAGE_SIZE, False)

    # print posts[5].content_html
    return render_template(
        'index.html', posts=posts, error=error)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


@home_blueprint.route('/blog/add', methods=['GET', 'POST'])
@login_required
def blog_add():
    error = None
    form = MessageForm(request.form)
    form.tag_id.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('id')]

    if form.validate_on_submit():

        # print form.title.data
        # print form.content.data
        # print form.insert_dt.data
        # print current_user.id

        new_message = Post(
            form.title.data,
            form.content.data,
            current_user.id,
            insert_dt=form.insert_dt.data,
            tag_id=form.tag_id.data
        )
        db.session.add(new_message)
        db.session.commit()

        # update rss
        genAtom('project/static/rss/atom.xml')

        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        return render_template(
            'blog_add.html', form=form, error=error)


@home_blueprint.route('/blog/detail/<int:id>')
def blog_detail(id):
    # 通过主键 用  get  如果是查询 用 filter_by
    post = Post.query.get(id)

    return render_template('blog_detail.html', post=post)


@home_blueprint.route('/blog/add/ajax')
def blog_add_ajax():
    return render_template('blog_add_ajax.html')


#########
#   Json From Here
#########

@home_blueprint.route('/json/web/content', methods=['POST'])
def json_content():
    # print request
    # print request.form

    if not request.json or not 'content' in request.json:
        abort(400)

    content = request.json.get('content', '')
    return jsonify(result=mistune.markdown(content))

@home_blueprint.route('/json/list/tag', methods=['GET'])
def json_list_tag():
    tags = Tag.query.order_by('id')
    return jsonify(result=[{'name':tag.name,'id':tag.id} for tag in tags])


@home_blueprint.route('/json/blog/add', methods=['POST'])
@login_required
def json_blog_add():

    if not request.json or not 'title' in request.json:
        abort(400)

    try:
        title = request.json.get('title', '')
        content = request.json.get('content', '')
        insert_dt = request.json.get('insert_dt', '')
        tag_id = request.json.get('tag_id', '')

        new_message = Post(
                title,
                content,
                current_user.id,
                insert_dt=insert_dt,
                tag_id = tag_id
        )
        db.session.add(new_message)
        db.session.commit()

        # update rss
        # print os.getcwd()
        genAtom('project/static/rss/atom.xml')

    except Exception as e:
        print e
        return jsonify(result=u'出错啦！')

    return jsonify(result=u'成功添加！')

#########
#   Rss
#########
@home_blueprint.route('/rss')
def rss():
    return redirect(url_for('static', filename='rss/atom.xml'))