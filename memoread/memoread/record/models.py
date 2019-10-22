from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
import uuid as uuid_lib
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.conf import settings

GENRE = (('1', '文学・評論'), ('2','人文・思想'),('3','社会・政治・法律'),('4','ノンフィクション'),
        ('5','歴史・地理'),('6','ビジネス・経済'),('7','投資・金融'),('8','科学・テクノロジー'),('9','医学・薬学'),
        ('10','コンピュータ・IT'),('11','アート・建築・デザイン'),('12','趣味・実用'),('13','スポーツ・アウトドア'),
        ('14','暮らし・健康・子育て'),('15','その他'))

class Record(models.Model):
    title = models.CharField(max_length=50, verbose_name='タイトル')
    image = models.ImageField(
            upload_to = 'images/',
            verbose_name = '画像',
            height_field = 'url_height',
            width_field = 'url_width',
            null=True,
            blank=True,
    )
    url_height = models.IntegerField(
        editable=False,
        null=True,
        blank=True,
    )
    url_width = models.IntegerField(
        editable=False,
        null=True,
        blank=True,
    )
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    author = models.CharField(max_length=30, verbose_name='著者', null=True, blank=True)
    genre = models.CharField(
        max_length = 30,
        choices = GENRE,
        verbose_name = 'ジャンル',
        null = True,
        blank = True
    )
    summary = models.CharField(max_length=800, verbose_name='要約', null=True, blank=True)
    impressions = models.CharField(max_length=800, verbose_name='感想', null=True, blank=True)
    learn = models.CharField(max_length=800, verbose_name='学び', null=True, blank=True)
    story = models.CharField(max_length=800, verbose_name='進め方', null=True, blank=True)
    difference = models.CharField(max_length=800, verbose_name='違い', null=True, blank=True)
    importance = models.CharField(max_length=800, verbose_name='重要な文', null=True, blank=True)
    agree = models.CharField(max_length=800, verbose_name='賛成', null=True, blank=True)
    opposition = models.CharField(max_length=800, verbose_name='反対', null=True, blank=True)
    unkown = models.CharField(max_length=800, verbose_name='不明点', null=True, blank=True)
    example = models.CharField(max_length=800, verbose_name='事例', null=True, blank=True)
    inspiration = models.CharField(max_length=800, verbose_name='感銘', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('index')

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            primary_key=True, editable=False)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    full_name = models.CharField(_('氏名'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    #date_of_birth = models.DateField(_('生年月日'), blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name
