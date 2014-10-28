import sys, re
re.IGNORECASE

# get system arguments
filename = sys.argv [1]
db = sys.argv [2]

# read from file
f = open (filename, 'r')
settings = f.read ()
f.close ()

# set up database settings
pattern = re.compile (r'postgres://(?P<username>[\w]+):(?P<password>[-_\w]+)@(?P<host>[-\w\.]+):[\d]+/(?P<database>[\w]+)')
mo = re.search (pattern, db)
to_replace = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '""" + mo.group ('database') + """',
        'USER': '""" + mo.group ('username') + """',
        'PASSWORD': '""" + mo.group ('password') + """',
        'HOST': '""" + mo.group ('host') + """',
        'PORT': '5432',
    }
}"""

# sub in new database values
settings = re.sub ('DATABASES = {[^{]+{[^}]+}[^}]+}', to_replace, settings)

# write to file
f = open (filename, 'w')
f.write (settings)
f.close ()