import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
else:
    print('ERROR: DATABASE_URL not set')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

if os.environ.get('BRYLLUP_SECRET_KEY'):
    SECRET_KEY = os.environ.get('BRYLLUP_SECRET_KEY')
else:
    print('ERROR: BRYLLUP_SECRET_KEY not set')
