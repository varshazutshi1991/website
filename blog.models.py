base /home/xen-478/my_workspace/website
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=1000)
    org = models.ForeignKey('Org', models.DO_NOTHING)
    role = models.CharField(max_length=200)
    active = models.BooleanField()
    created = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account'


class Attribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    scope = models.CharField(max_length=200)
    typ = models.CharField(max_length=200)
    ix = models.ForeignKey('Interaction', models.DO_NOTHING)
    tpl = models.ForeignKey('Tpl', models.DO_NOTHING)
    created = models.DateTimeField()
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')

    class Meta:
        managed = False
        db_table = 'attribute'
        unique_together = (('ix', 'name', 'scope', 'typ'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogAbout(models.Model):
    full_name = models.CharField(max_length=200)
    introduction = models.TextField()
    created_date = models.DateTimeField()
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_about'


class BlogAuthor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'blog_author'


class BlogFood(models.Model):
    food_title = models.CharField(max_length=200)
    food_description = models.TextField()
    created_date = models.DateTimeField()
    type_category = models.CharField(max_length=200)
    food_picture = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_food'


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(BlogAuthor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_post'


class BlogPostFoodCategory(models.Model):
    post = models.ForeignKey(BlogPost, models.DO_NOTHING)
    food = models.ForeignKey(BlogFood, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post_food_category'
        unique_together = (('post', 'food'),)


class BlogPostTravelCategory(models.Model):
    post = models.ForeignKey(BlogPost, models.DO_NOTHING)
    travel = models.ForeignKey('BlogTravel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post_travel_category'
        unique_together = (('post', 'travel'),)


class BlogTravel(models.Model):
    destination = models.CharField(max_length=200)
    destination_title = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    destination_description = models.TextField()
    destination_images = models.CharField(max_length=100, blank=True, null=True)
    type_category = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_travel'


class Bot(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    name = models.CharField(unique=True, max_length=200)
    note = models.CharField(max_length=1024)
    org = models.ForeignKey('Org', models.DO_NOTHING)
    wlcm_msg = models.CharField(max_length=1024)
    active = models.BooleanField()
    created = models.DateTimeField()
    timezone = models.CharField(max_length=200)
    confidence = models.SmallIntegerField()
    life_span = models.SmallIntegerField()
    avatar = models.CharField(max_length=1024)
    bg_img = models.CharField(max_length=1024)
    theme = models.CharField(max_length=200)
    btn_theme = models.CharField(max_length=200)
    theme_colour = models.CharField(max_length=200)
    vhost = models.CharField(max_length=200)
    jid = models.CharField(max_length=200)
    broker = models.CharField(max_length=200)
    language = models.TextField(blank=True, null=True)  # This field type is a guess.
    auto_reply = models.BooleanField()
    auto_reply_count = models.IntegerField()
    nlubackend = models.TextField()
    enable_nps = models.BooleanField()
    enable_avatar = models.BooleanField()
    email_conv = models.BooleanField()
    auto_reply_msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    feedback_msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    flat_nlu = models.BooleanField()
    p_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'bot'


class BotCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    org = models.ForeignKey('Org', models.DO_NOTHING)
    bot = models.ForeignKey(Bot, models.DO_NOTHING)
    active = models.BooleanField()
    path = models.TextField()  # This field type is a guess.
    typ = models.TextField()

    class Meta:
        managed = False
        db_table = 'bot_category'


class BotSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=200)
    org = models.ForeignKey('Org', models.DO_NOTHING)
    bot = models.ForeignKey(Bot, models.DO_NOTHING)
    active = models.BooleanField()
    bg_img = models.CharField(max_length=1024)
    theme = models.CharField(max_length=200)
    btn_theme = models.CharField(max_length=200)
    theme_colour = models.CharField(max_length=200)
    response_bubble = models.CharField(max_length=200)
    sender_bubble = models.CharField(max_length=200)
    carousel_color = models.CharField(max_length=200)
    header_logo = models.CharField(max_length=1024)
    header_enable = models.BooleanField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bot_settings'


class BotSnapshot(models.Model):
    id = models.BigAutoField(primary_key=True)
    bot = models.ForeignKey(Bot, models.DO_NOTHING)
    tpl = models.ForeignKey('Tpl', models.DO_NOTHING)
    tpl_uid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=100)
    data = models.TextField()  # This field type is a guess.
    version = models.IntegerField()
    interactions = models.TextField()  # This field type is a guess.
    synced_at = models.DateTimeField()
    typ = models.TextField()
    entities = models.TextField()  # This field type is a guess.
    updated_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='updated_by')
    imported_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='imported_by')
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bot_snapshot'
        unique_together = (('bot', 'tpl'),)


class BotTpl(models.Model):
    bot = models.ForeignKey(Bot, models.DO_NOTHING)
    tpl = models.ForeignKey('Tpl', models.DO_NOTHING)
    category = models.ForeignKey(BotCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_tpl'
        unique_together = (('bot', 'tpl'),)


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    org = models.ForeignKey('Org', models.DO_NOTHING)
    repo = models.ForeignKey('Repository', models.DO_NOTHING)
    active = models.BooleanField()
    path = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'category'


class Changelog(models.Model):
    id = models.BigAutoField(primary_key=True)
    content_type = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'changelog'


class Demo(models.Model):

    class Meta:
        managed = False
        db_table = 'demo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.ForeignKey(EasyThumbnailsThumbnail, models.DO_NOTHING, unique=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class Entity(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=200)
    org = models.ForeignKey('Org', models.DO_NOTHING)
    name = models.CharField(max_length=250)
    language = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    created = models.DateTimeField()
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')
    updated = models.DateTimeField()
    updated_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='updated_by')

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'entity'
        unique_together = (('org', 'language'),)


class EntityItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=200)
    entity = models.ForeignKey(Entity, models.DO_NOTHING)
    name = models.CharField(max_length=250)
    synonyms = models.TextField()  # This field type is a guess.
    created = models.DateTimeField()
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')
    updated = models.DateTimeField()
    updated_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='updated_by')

    class Meta:
        managed = False
        db_table = 'entity_item'
        unique_together = (('entity', 'name'),)


class EntityReference(models.Model):
    ix_id = models.BigIntegerField()
    entity_id = models.BigIntegerField()
    tpl_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_reference'
