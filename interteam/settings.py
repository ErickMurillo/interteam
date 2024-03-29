"""
Django settings for interteam project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
from .local_settings import *

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'notas',
    'contrapartes',
    'foros',
    'agendas',
    'publicaciones',
    'galerias',
    'opiniones',
    'biblioteca',
    'configuracion',
    'informes',
    'catalogo',

    'ckeditor',
    'ckeditor_uploader',
    'sorl.thumbnail',
    'taggit',
    'taggit_autosuggest',
    'el_pagination',
    'embed_video',
    'disqus',
    'crispy_forms',
    'crispy_bootstrap4',
    'nested_admin',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'interteam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'interteam.context.global_vars'
            ],
        },
    },
]

WSGI_APPLICATION = 'interteam.wsgi.application'

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_media"),
]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-ni'

TIME_ZONE = 'America/Managua'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_MEDIA_PREFIX = '/files/media/ckeditor/'

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 650,
    },
}

CKEDITOR_CONFIGS = {
    'default': {
        'extraPlugins': ','.join([
            # 'image2',
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'embed',
            'autoembed',

            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        'toolbar': [
            { 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ], 'items': [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ] },
            { 'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ], 'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
            { 'name': 'editing', 'groups': [ 'find', 'selection', 'spellchecker' ], 'items': [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
            #{ 'name': 'forms', 'items': [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ] },
            '/',
            { 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ], 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ] },
            { 'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ], 'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ] },
            { 'name': 'links', 'items': [ 'Link', 'Unlink', 'Anchor' ] },
            { 'name': 'insert', 'items': [ 'Image', 'Youtube', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ] },
            '/',
            { 'name': 'styles', 'items': [ 'Styles', 'Format', 'Font', 'FontSize' ] },
            { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
            { 'name': 'tools', 'items': [ 'Maximize', 'ShowBlocks', ] },
             {
    }

        ],
        'height': '300px',
        'width': 'auto',
    },

}

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

DISQUS_API_KEY = 'rZ2AINHqiAOGEAkPOnH3i91zOzLGw8mP38SUY2hIQezO8h60XbkYM0pe4rCyCHWT'
DISQUS_WEBSITE_SHORTNAME = 'http-cluster-nicaragua-net'

FILE_UPLOAD_PERMISSIONS = 0o644

CELERY_broker_url = 'redis://localhost'

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"


# set the celery timezone
timezone = 'America/Managua'