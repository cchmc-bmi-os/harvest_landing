## This settings files defines the NBSmart projects


HARVEST_SERVER = 'http://lpdr.nbstrn.org'


LDAP = {
    'server_name': 'chmcres.cchmc.org',
    'port': 636,
    'bind_user': 'CN=LINUX AD LOGIN,OU=SERVICEACCTS,OU=RESEARCH,OU=MANAGED,DC=CHMCRES,DC=CCHMC,DC=ORG',
    'bind_password': 'LKLdnPODf13ezZS9BXfW',
    'use_ssl': True,
    'search_base': 'DC=chmcres,DC=cchmc,DC=org'
}


NBSTRN = {
    'display_name': 'NBSTRN LPDR',
    'url': 'https://lpdr.nbstrn.org/harvest/',
    'access_request_link': 'https://register.nbstrn.org/nur-web/registration/input.action'
    }

PROJECTS  = {
    'ibemc': {
        'display_name': 'IBEMC',
        'url': HARVEST_SERVER + '/harvest-ibemc',
        'db' : {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ibemc_inc',
            'USER': 'srv_ibemc',
            'PASSWORD': 'srv_ibemc',
            'HOST': 'localhost'
        },
        'permission_group': 'oA-OPEN-IBEMCHarvTst',
        'version': {
            'data': '2017-03-11',
            'integration': '2017-07-14'
            }
    },
    'krabbe': {
        'display_name': 'Worldwide Krabbe Disease Registry',
        'url': HARVEST_SERVER + '/harvest-krabbe',
        'db' : {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ibemc_inc',
            'USER': 'srv_krabbe',
            'PASSWORD': 'srv_krabbe',
            'HOST': 'localhost'
        },
        'permission_group': 'oA-OPEN-KrabbeHrvTst',
        'version': {
            'data': '2017-07-17',
            'integration': '2018-04-27'
            }
    },
    'sma': {
        'display_name': 'SMA : NHx',
        'url': HARVEST_SERVER + '/harvest-sma',
        'db': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ibemc_inc',
            'USER': 'srv_sma',
            'PASSWORD': 'srv_sma',
            'HOST': 'localhost'
        },
        'permission_group': 'oA-OPEN-SMAHarvTst',
        'version': {
            'data': '2017-12-11',
            'integration': '2017-12-11'
            }
    }
}
