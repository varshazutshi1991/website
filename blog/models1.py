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


class ExtraSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    key = models.CharField(max_length=500)
    extra_value = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'extra_settings'


class FileStore(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=500)
    ns = models.CharField(max_length=500)
    filename = models.CharField(max_length=500)
    path = models.CharField(max_length=2000)
    mimetype = models.CharField(max_length=500)
    kind = models.CharField(max_length=500)
    size = models.BigIntegerField()
    storage = models.CharField(max_length=500)
    thumb = models.CharField(max_length=2000)
    uploader = models.BigIntegerField()
    active = models.BooleanField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'file_store'


class FilerClipboard(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboard'


class FilerClipboarditem(models.Model):
    clipboard = models.ForeignKey(FilerClipboard, models.DO_NOTHING)
    file = models.ForeignKey('FilerFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboarditem'


class FilerFile(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)
    field_file_size = models.BigIntegerField(db_column='_file_size', blank=True, null=True)  # Field renamed because it started with '_'.
    sha1 = models.CharField(max_length=40)
    has_all_mandatory_data = models.BooleanField()
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    is_public = models.BooleanField()
    folder = models.ForeignKey('FilerFolder', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    polymorphic_ctype = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_file'


class FilerFolder(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folder'
        unique_together = (('parent', 'name'),)


class FilerFolderpermission(models.Model):
    type = models.SmallIntegerField()
    everybody = models.BooleanField()
    can_edit = models.SmallIntegerField(blank=True, null=True)
    can_read = models.SmallIntegerField(blank=True, null=True)
    can_add_children = models.SmallIntegerField(blank=True, null=True)
    folder = models.ForeignKey(FilerFolder, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folderpermission'


class FilerImage(models.Model):
    file_ptr = models.ForeignKey(FilerFile, models.DO_NOTHING, primary_key=True)
    field_height = models.IntegerField(db_column='_height', blank=True, null=True)  # Field renamed because it started with '_'.
    field_width = models.IntegerField(db_column='_width', blank=True, null=True)  # Field renamed because it started with '_'.
    date_taken = models.DateTimeField(blank=True, null=True)
    default_alt_text = models.CharField(max_length=255, blank=True, null=True)
    default_caption = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    must_always_publish_author_credit = models.BooleanField()
    must_always_publish_copyright = models.BooleanField()
    subject_location = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filer_image'


class FilerThumbnailoption(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    crop = models.BooleanField()
    upscale = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'filer_thumbnailoption'


class Interaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    tpl = models.ForeignKey('Tpl', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200)
    queries = models.TextField()  # This field type is a guess.
    replies = models.TextField()  # This field type is a guess.
    props = models.TextField(blank=True, null=True)  # This field type is a guess.
    intent = models.CharField(max_length=-1)
    version = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    auto_reply_toggle = models.BooleanField()
    auto_reply = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')
    updated_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='updated_by')
    is_global = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'interaction'


class InteractionRef(models.Model):
    itx = models.ForeignKey(Interaction, models.DO_NOTHING)
    qr_uid = models.CharField(max_length=200, blank=True, null=True)
    typ = models.CharField(max_length=200, blank=True, null=True)
    tpl = models.ForeignKey('Tpl', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'interaction_ref'


class InteractionTags(models.Model):
    interaction = models.ForeignKey(Interaction, models.DO_NOTHING)
    tag = models.ForeignKey('Tag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'interaction_tags'
        unique_together = (('interaction', 'tag'),)


class InviteUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=200)
    org_id = models.BigIntegerField()
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    completed = models.BooleanField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    expires_at = models.DateTimeField()
    invited_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'invite_user'


class Kv(models.Model):
    id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey('Org', models.DO_NOTHING, blank=True, null=True)
    k = models.CharField(max_length=200)
    v = models.CharField(max_length=-1)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kv'


class Launcher(models.Model):
    id = models.UUIDField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    prod_id = models.CharField(max_length=300, blank=True, null=True)
    asset_tag = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'launcher'


class LoginUserData(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    user_session_id = models.CharField(max_length=255, blank=True, null=True)
    msg_payload = models.TextField(blank=True, null=True)
    jid = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    tid = models.CharField(max_length=-1, blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    msg_payload_json = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'login_user_data'


class NluBot(models.Model):
    bot_uid = models.TextField(blank=True, null=True)
    name = models.TextField()
    languages = models.TextField(blank=True, null=True)  # This field type is a guess.
    greeting_msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    fall_back_msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    external_bot_type = models.TextField(blank=True, null=True)
    external_bot_id = models.TextField(blank=True, null=True)
    confidence = models.IntegerField()
    auto_replies = models.BooleanField()
    auto_replies_count = models.IntegerField()
    welcome_template_id = models.IntegerField(blank=True, null=True)
    fallback_template_id = models.IntegerField(blank=True, null=True)
    linked_entities_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_feedback_message = models.TextField(blank=True, null=True)  # This field type is a guess.
    auto_reply_message = models.TextField(blank=True, null=True)  # This field type is a guess.
    pos_feedback_id = models.IntegerField(blank=True, null=True)
    neg_feedback_id = models.IntegerField(blank=True, null=True)
    acknowledge_feedback_id = models.IntegerField(blank=True, null=True)
    enable_context = models.BooleanField()
    context_life_span = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nlu_bot'


class NluBotTrained(models.Model):
    id = models.IntegerField()
    bot_uid = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)  # This field type is a guess.
    greeting_msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    fall_back_msg = models.TextField(blank=True, null=True)  # This field type is a guess.
    external_bot_type = models.TextField(blank=True, null=True)
    external_bot_id = models.TextField(blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    auto_replies = models.BooleanField(blank=True, null=True)
    auto_replies_count = models.IntegerField(blank=True, null=True)
    welcome_template_id = models.IntegerField(blank=True, null=True)
    fallback_template_id = models.IntegerField(blank=True, null=True)
    linked_entities_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_feedback_message = models.TextField(blank=True, null=True)  # This field type is a guess.
    auto_reply_message = models.TextField(blank=True, null=True)  # This field type is a guess.
    pos_feedback_id = models.IntegerField(blank=True, null=True)
    neg_feedback_id = models.IntegerField(blank=True, null=True)
    acknowledge_feedback_id = models.IntegerField(blank=True, null=True)
    enable_context = models.BooleanField(blank=True, null=True)
    context_life_span = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_bot_trained'


class NluConfig(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_config'


class NluEntities(models.Model):
    uid = models.UUIDField(primary_key=True)
    entity_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    keyword = models.CharField(max_length=50, blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nlu_entities'


class NluEntitiesTrained(models.Model):
    bot_id = models.IntegerField()
    entity_name = models.CharField(max_length=50)
    language = models.CharField(max_length=5)
    item = models.CharField(max_length=50, blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)  # This field type is a guess.
    uid = models.CharField(max_length=200, blank=True, null=True)
    keyword = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_entities_trained'


class NluFilters(models.Model):
    filter_id = models.BigIntegerField(primary_key=True)
    uid = models.CharField(max_length=200)
    bot_id = models.BigIntegerField()
    bot_uid = models.TextField(blank=True, null=True)
    language_id = models.CharField(max_length=2, blank=True, null=True)
    template_id = models.IntegerField()
    attribute_name = models.CharField(max_length=250)
    rule = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_filters'
        unique_together = (('filter_id', 'bot_id'),)


class NluFiltersTrained(models.Model):
    filter_id = models.IntegerField()
    uid = models.CharField(max_length=200)
    bot_id = models.BigIntegerField()
    bot_uid = models.TextField()
    language_id = models.CharField(max_length=2, blank=True, null=True)
    template_id = models.IntegerField()
    attribute_name = models.CharField(max_length=250)
    rule = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_filters_trained'


class NluLangProp(models.Model):
    language = models.CharField(primary_key=True, max_length=10)
    contractions_dict = models.TextField(blank=True, null=True)  # This field type is a guess.
    leftovers_dict = models.TextField(blank=True, null=True)  # This field type is a guess.
    slang = models.TextField(blank=True, null=True)  # This field type is a guess.
    safety_keys = models.TextField(blank=True, null=True)  # This field type is a guess.
    stopwords = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nlu_lang_prop'


class NluLanguages(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    language = models.CharField(unique=True, max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_languages'


class NluLoginUserData(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    user_session_id = models.CharField(max_length=255)
    msg_payload = models.TextField(blank=True, null=True)
    jid = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_login_user_data'


class NluServerEntries(models.Model):
    server_ip = models.CharField(primary_key=True, max_length=200)
    port = models.IntegerField()
    bot_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nlu_server_entries'
        unique_together = (('server_ip', 'bot_id'),)


class NluSlotValidationMapping(models.Model):
    slot_validation_id = models.BigIntegerField(primary_key=True)
    display_name = models.CharField(max_length=50)
    nlu_slot_name = models.CharField(max_length=50)
    slot_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'nlu_slot_validation_mapping'


class NluStopwords(models.Model):
    language_id = models.CharField(max_length=20)
    stop_words = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nlu_stopwords'


class NluSynonymsTrained(models.Model):
    item = models.CharField(max_length=250)
    synonyms = models.TextField()  # This field type is a guess.
    bot_id = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=5, blank=True, null=True)
    bot_uid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_synonyms_trained'


class NluTemplate(models.Model):
    bot_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    intent = models.CharField(max_length=50, blank=True, null=True)
    auto_replies_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    bot_uid = models.TextField(blank=True, null=True)
    is_global = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nlu_template'
        unique_together = (('id', 'bot_id'),)


class NluTemplateQueries(models.Model):
    query_id = models.CharField(primary_key=True, max_length=100)
    bot = models.ForeignKey(NluTemplate, models.DO_NOTHING, blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(NluLanguages, models.DO_NOTHING, blank=True, null=True)
    query = models.CharField(max_length=1200)
    tag = models.TextField(blank=True, null=True)  # This field type is a guess.
    slots = models.TextField(blank=True, null=True)  # This field type is a guess.
    prediction_enable = models.BooleanField()
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'nlu_template_queries'


class NluTemplateQueriesTrained(models.Model):
    query_id = models.CharField(max_length=100)
    bot_id = models.IntegerField(blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    language_id = models.CharField(max_length=2, blank=True, null=True)
    query = models.CharField(max_length=1200)
    tag = models.TextField(blank=True, null=True)  # This field type is a guess.
    slots = models.TextField(blank=True, null=True)  # This field type is a guess.
    prediction_enable = models.BooleanField()
    bot_uid = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'nlu_template_queries_trained'


class NluTemplateReplies(models.Model):
    reply_id = models.CharField(primary_key=True, max_length=100)
    reply_index = models.IntegerField(blank=True, null=True)
    bot = models.ForeignKey(NluTemplate, models.DO_NOTHING, blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(NluLanguages, models.DO_NOTHING, blank=True, null=True)
    reply_type = models.CharField(max_length=25)
    response = models.TextField()  # This field type is a guess.
    delay = models.IntegerField()
    bot_uid = models.TextField(blank=True, null=True)
    filter = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nlu_template_replies'


class NluTemplateRepliesTrained(models.Model):
    reply_id = models.CharField(max_length=100)
    reply_index = models.IntegerField(blank=True, null=True)
    bot_id = models.IntegerField(blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    language_id = models.CharField(max_length=2, blank=True, null=True)
    reply_type = models.CharField(max_length=25)
    response = models.TextField()  # This field type is a guess.
    delay = models.IntegerField()
    bot_uid = models.TextField(blank=True, null=True)
    filter = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nlu_template_replies_trained'


class NluTemplateTrained(models.Model):
    id = models.IntegerField(primary_key=True)
    bot_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    intent = models.CharField(max_length=50, blank=True, null=True)
    auto_replies_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    bot_uid = models.TextField(blank=True, null=True)
    is_global = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_template_trained'
        unique_together = (('id', 'bot_id'),)


class NluUserAnalytics(models.Model):
    id = models.BigAutoField(primary_key=True)
    jid = models.CharField(max_length=255)
    message_id = models.BigIntegerField()
    query = models.TextField()
    bot_id = models.BigIntegerField()
    language = models.CharField(max_length=5)
    sentiment = models.IntegerField()
    intent = models.CharField(max_length=255)
    user_feedback = models.CharField(max_length=50, blank=True, null=True)
    unhandled = models.BooleanField()
    assigned = models.BooleanField()
    assigned_to = models.BigIntegerField()
    agent_transfer = models.BooleanField()
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)
    intent_id = models.IntegerField()
    user_id = models.CharField(max_length=50, blank=True, null=True)
    login_id = models.TextField(blank=True, null=True)
    uid = models.CharField(max_length=200, blank=True, null=True)
    user_input_feedback = models.TextField(blank=True, null=True)
    bot_uid = models.TextField(blank=True, null=True)
    assigned_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='assigned_by')
    assigned_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='deleted_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    masked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_user_analytics'


class NluUserAnalyticsTesting(models.Model):
    #id = models.BigAutoField(primary_key=True)
    jid = models.CharField(max_length=255, blank=True, null=True)
    message_id = models.BigIntegerField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    bot_id = models.BigIntegerField(blank=True, null=True)
    language = models.CharField(max_length=5, blank=True, null=True)
    sentiment = models.IntegerField(blank=True, null=True)
    intent = models.CharField(max_length=255, blank=True, null=True)
    user_feedback = models.CharField(max_length=50, blank=True, null=True)
    unhandled = models.BooleanField(blank=True, null=True)
    assigned = models.BooleanField(blank=True, null=True)
    assigned_to = models.BigIntegerField(blank=True, null=True)
    agent_transfer = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)
    intent_id = models.IntegerField()
    user_id = models.CharField(max_length=50, blank=True, null=True)
    login_id = models.TextField(blank=True, null=True)
    uid = models.CharField(max_length=200, blank=True, null=True)
    user_input_feedback = models.TextField(blank=True, null=True)
    bot_uid = models.TextField(blank=True, null=True)
    assigned_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='assigned_by')
    assigned_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='deleted_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    masked = models.BooleanField(blank=True, null=True)
    is_greeting = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nlu_user_analytics_testing'


class NluUserPrompt(models.Model):
    bot_id = models.BigIntegerField()
    language_id = models.CharField(max_length=2, blank=True, null=True)
    template_id = models.IntegerField()
    prompt_id = models.IntegerField()
    query = models.TextField(blank=True, null=True)  # This field type is a guess.
    slot_name = models.CharField(max_length=50)
    validation_type = models.CharField(max_length=50)
    retries = models.IntegerField()
    fallback_action = models.CharField(max_length=10)
    masked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nlu_user_prompt'


class NluUserPromptTrained(models.Model):
    bot_id = models.BigIntegerField()
    language_id = models.CharField(max_length=2, blank=True, null=True)
    template_id = models.IntegerField()
    prompt_id = models.IntegerField()
    query = models.TextField(blank=True, null=True)  # This field type is a guess.
    slot_name = models.CharField(max_length=50)
    validation_type = models.CharField(max_length=50)
    retries = models.IntegerField()
    fallback_action = models.CharField(max_length=10)
    masked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nlu_user_prompt_trained'


class NluUserdata(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    admin_flag = models.BooleanField(blank=True, null=True)
    public_id = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nlu_userdata'


class NluValidation(models.Model):
    nlu_validation_id = models.BigIntegerField(primary_key=True)
    display_name = models.CharField(max_length=50)
    validation_name = models.CharField(max_length=50)
    validation_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'nlu_validation'


class Org(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=200)
    plan = models.CharField(max_length=100)
    active = models.BooleanField()
    op_mode = models.CharField(max_length=100)
    created = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'org'


class Provider(models.Model):
    uid = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    settings = models.TextField()  # This field type is a guess.
    active = models.BooleanField()
    created_at = models.DateTimeField()
    name = models.CharField(max_length=500, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'provider'


class RepliesTrained(models.Model):
    reply_id = models.CharField(max_length=100, blank=True, null=True)
    reply_index = models.IntegerField(blank=True, null=True)
    bot_id = models.IntegerField(blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    language_id = models.CharField(max_length=2, blank=True, null=True)
    reply_type = models.CharField(max_length=25, blank=True, null=True)
    response = models.TextField(blank=True, null=True)  # This field type is a guess.
    delay = models.IntegerField(blank=True, null=True)
    bot_uid = models.TextField(blank=True, null=True)
    filter = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'replies_trained'


class Repository(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    supported_types = models.TextField()  # This field type is a guess.
    org = models.ForeignKey(Org, models.DO_NOTHING)
    active = models.BooleanField()
    created = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'repository'


class ResetPswd(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    org = models.ForeignKey(Org, models.DO_NOTHING)
    email = models.CharField(max_length=200)
    completed = models.BooleanField()
    created = models.DateTimeField()
    expires_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reset_pswd'
        unique_together = (('uid', 'email'),)


class SsoAdapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    client_id = models.CharField(max_length=2000)
    client_secret = models.CharField(max_length=2000)
    app_id = models.CharField(max_length=2000)
    cert = models.CharField(max_length=2000)
    ckey = models.CharField(max_length=2000)
    sso_toggle = models.BooleanField()
    auth_url = models.CharField(max_length=2000)
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')
    active = models.BooleanField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sso_adapter'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(Org, models.DO_NOTHING)
    uid = models.CharField(max_length=200)
    name = models.CharField(unique=True, max_length=200)
    active = models.BooleanField()
    created = models.DateTimeField()

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'tag'


class Tpl(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=200)
    org = models.ForeignKey(Org, models.DO_NOTHING)
    repo = models.ForeignKey(Repository, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=100)
    data = models.TextField()  # This field type is a guess.
    active = models.BooleanField()
    version = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    updated_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='updated_by')
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')

    class Meta:
        managed = False
        db_table = 'tpl'


class TplRef(models.Model):
    tmpl = models.ForeignKey(Tpl, models.DO_NOTHING, db_column='tmpl')
    ref = models.ForeignKey(Tpl, models.DO_NOTHING, db_column='ref')
    ref_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'tpl_ref'


class TrainJob(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    bot = models.ForeignKey(Bot, models.DO_NOTHING)
    state = models.CharField(max_length=100)
    created = models.DateTimeField()
    completed = models.DateTimeField()
    current_stage = models.CharField(max_length=200)
    status_msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_job'


class UnhandledChat(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    bot = models.ForeignKey(Bot, models.DO_NOTHING)
    bot_name = models.CharField(max_length=500)
    msg = models.CharField(max_length=1500)
    ts = models.DateTimeField()
    c_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'unhandled_chat'


class UserAgentAnalytics(models.Model):
    id = models.AutoField()
    msg_id = models.IntegerField()
    user_id = models.CharField(max_length=100)
    fallback_msg = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_agent_analytics'


class UserDataSet(models.Model):
    wdid = models.CharField(primary_key=True, max_length=30)
    bot_id = models.IntegerField()
    region = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    confidence = models.IntegerField()
    userid = models.CharField(max_length=50, blank=True, null=True)
    bot_uid = models.TextField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_data_set'


class UserSurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    kind = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    score = models.IntegerField()
    reason = models.TextField()
    segment = models.CharField(max_length=200)
    created = models.DateTimeField()
    org_id = models.BigIntegerField()
    bot_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_survey'


class Version(models.Model):
    id = models.BigAutoField(primary_key=True)
    content_type = models.CharField(max_length=200)
    ref = models.BigIntegerField()
    ver = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'version'
        unique_together = (('ref', 'content_type'),)


class Vocabulary(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(unique=True, max_length=200)
    bot = models.ForeignKey(Bot, models.DO_NOTHING)
    root = models.CharField(max_length=250)
    synonyms = models.TextField()  # This field type is a guess.
    language = models.CharField(max_length=200)
    created = models.DateTimeField()
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')
    updated = models.DateTimeField()
    updated_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='updated_by')

    class Meta:
        managed = False
        db_table = 'vocabulary'
        unique_together = (('bot', 'root', 'language'),)


class WebSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    session_id = models.TextField(unique=True)
    org_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    ip = models.TextField()
    ua = models.TextField()
    created = models.DateTimeField()
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_session'


class Webhooks(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=200)
    org = models.ForeignKey(Org, models.DO_NOTHING)
    title = models.CharField(max_length=200)
    url = models.TextField()
    method = models.CharField(max_length=10)
    payload = models.TextField()  # This field type is a guess.
    headers = models.TextField()  # This field type is a guess.
    active = models.BooleanField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    created_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='created_by')
    updated_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='updated_by')
    p_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'webhooks'
        unique_together = (('title', 'active'),)


class WebhooksRef(models.Model):
    id = models.BigAutoField(primary_key=True)
    wh = models.ForeignKey(Webhooks, models.DO_NOTHING)
    r_uid = models.CharField(max_length=200, blank=True, null=True)
    ix = models.ForeignKey(Interaction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'webhooks_ref'
        unique_together = (('wh', 'r_uid', 'ix'),)
