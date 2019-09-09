from django.db import models
from django.utils import timezone


class Travel(models.Model):
    destination = models.CharField(max_length=200)
    destination_title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    destination_description = models.TextField()
    type_category = models.CharField(max_length=200, null=True)
    destination_images = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    def create_author(sender, instance, **kwargs):
        print("instance")
        print("Authoe is saved")

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

#pre_save.connect(receiver=create_author, sender=Author)
#post_save.connect(receiver=create_author, sender=Author)


class Food(models.Model):
    food_title = models.CharField(max_length=200)
    food_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    type_category = models.CharField(max_length=200)
    food_picture = models.ImageField(upload_to='images/%Y/%m/%d', null=True)


class BlogManager(models.Manager):
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(author=True)

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    blog_title = models.CharField(max_length=200)
    blog_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    blog_picture = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    #all_blogs = models.Manager()
    #varsha_blog = BlogManager()


    # class Meta:
    #     def



class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    travel_category = models.ManyToManyField(Travel)
    food_category = models.ManyToManyField(Food)

    all_posts = models.Manager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class About(models.Model):
    full_name = models.CharField(max_length=200)
    introduction = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    def __str__(self):
        return self.full_name



class NluUserAnalyticsTesting(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    #assigned_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='assigned_by')
    assigned_at = models.DateTimeField(blank=True, null=True)
    #deleted_by = models.ForeignKey(Account, models.DO_NOTHING, db_column='deleted_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    masked = models.BooleanField(blank=True, null=True)
    is_greeting = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nlu_user_analytics_testing'


class Contribute(models.Model):
    blog_title = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    blog_content = models.TextField(blank=True, null=True)
    your_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    about_yourself = models.TextField(blank=True, null=True)
    facebook_profile_link = models.URLField(max_length=150, unique=True, blank=True)





