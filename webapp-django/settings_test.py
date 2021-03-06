## This is automatically imported by test-utils to make sure tests are run in
## a consistent way across different platforms and different developers.

CACHE_MIDDLEWARE = True
CACHE_MIDDLEWARE_FILES = False

import os
os.environ['FORCE_DB'] = 'true'

DEFAULT_PRODUCT = 'WaterWolf'

# here we deliberately "destroy" the BZAPI URL so running tests that are
# badly mocked never accidentally actually use a real working network address
BZAPI_BASE_URL = 'https://bugzilla.testrunner/rest'

# by scrubbing this to something unreal, we can be certain the tests never
# actually go out on the internet when `request.get` should always be mocked
MWARE_BASE_URL = 'http://shouldnotactuallybeused'

STATSD_CLIENT = 'django_statsd.clients.null'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# see ("https://docs.djangoproject.com/en/1.4/topics/auth/",
#      "#how-django-stores-passwords")
# for how django stores passwords,
# To avoid depending on django_sha2 which requires bcrypt to be installed,
# we override whatever funfactory sets up.
# And because this is for running tests, we use the simplest hasher possible.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


# don't accidentally send anything to sentry whilst running tests
RAVEN_CONFIG = {}
SENTRY_DSN = None


BROWSERID_AUDIENCES = ['http://testserver']

# Make sure these have something but something not right
# so the tests never accidentally manage to connect to AWS
# for realz.
AWS_ACCESS_KEY = 'something'
AWS_SECRET_ACCESS_KEY = 'anything'
SYMBOLS_BUCKET_DEFAULT_NAME = 'my-lovely-bucket'
SYMBOLS_FILE_PREFIX = 'v99'
SYMBOLS_BUCKET_DEFAULT_LOCATION = 'us-west-2'


# So it never ever actually uses a real ElasticSearch server
SOCORRO_IMPLEMENTATIONS_CONFIG = {
    'elasticsearch': {
        'elasticsearch_urls': ['http://example:9123'],
    },
}
