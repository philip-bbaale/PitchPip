from flask import render_template, url_for, flash, redirect, request, abort
from Pitching import app, db, bcrypt, photos
from Pitching.forms import RegistrationForm, LoginForm, UpdateProfile, PostForm, CommentForm
from Pitching.models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
from Pitching.email import mail_message


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template('home.html', posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to postPip","email/welcome_user",user.email,user=user)

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(request.args.get('next') or url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account/<uname>")
@login_required
def account(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('account.html', title='Account', user = user, posts=posts)


@app.route('/account/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('account',uname=user.username, title='Update Profile'))

    return render_template('update.html',form =form)

@app.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.image_file = path
        db.session.commit()
    return redirect(url_for('account',uname=uname))

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, category=form.category.data, author=current_user, upvotes=0, downvotes=0)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.args.get("upvote"):
        post.upvotes += 1
        db.session.add(post)
        db.session.commit()
        return redirect("/post/{post_id}".format(post_id=post.id))

    elif request.args.get("downvote"):
        post.downvotes += 1
        db.session.add(post)
        db.session.commit()
        return redirect("/post/{post_id}".format(post_id=post.id))

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.text.data

        new_comment = Comment(content = comment, post_id = post.id)

        new_comment.save_comment()
    comments = Post.get_comments(post)

    return render_template('post.html', title=post.title, post=post, comments=comments, form=form)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/posts_by_category/<uname>")
def posts_by_category(uname):
    posts = Post.query.filter_by(category=uname).all()
    return render_template('posts_by_category', title='Posts By Category',  posts=posts)

