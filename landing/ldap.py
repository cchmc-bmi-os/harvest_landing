##from django.conf import settings
from ldap3 import (Server, Connection)

##LDAP = settings.LDAP

LDAP = {
    'server_name': 'chmcres.cchmc.org',
    'port': 636,
    'bind_user': 'CN=LINUX AD LOGIN,OU=SERVICEACCTS,OU=RESEARCH,OU=MANAGED,DC=CHMCRES,DC=CCHMC,DC=ORG',
    'bind_password': 'LKLdnPODf13ezZS9BXfW',
    'use_ssl': True,
    'search_base': 'DC=chmcres,DC=cchmc,DC=org'
}



# LDAP = {
#     'server_name': 'chmccorp.cchmc.org',
#     'port': 636,
#     'bind_user': 'CN=srv-bmistore,OU=Service Accts,OU=Specialized Accts,DC=chmccorp,DC=cchmc,DC=org',
#     'bind_password': '(lq|QV+dqXT6',
#     'use_ssl': True,
#     'search_base': 'dc=CHMCCORP,DC=CCHMC,DC=ORG'
# }


## ldapsearch -h chmccorp.cchmc.org -D "CN=srv-bmistore,OU=Service Accts,OU=Specialized Accts,DC=chmccorp,DC=cchmc,DC=org" -x -W -b "ou=main,dc=CHMCCORP,DC=CCHMC,DC=ORG" -s sub "(sAMAccountName=labs9y)"
## (lq|QV+dqXT6

## ldapsearch -h chmcres.cchmc.org -D "CN=LINUX AD LOGIN,OU=SERVICEACCTS,OU=RESEARCH,OU=MANAGED,DC=CHMCRES,DC=CCHMC,DC=ORG" -x -W -b "DC=chmcres,DC=cchmc,DC=org" -s sub "(sAMAccountName=labs9y)"
## LKLdnPODf13ezZS9BXfW


def get_permission_groups(username):
    server_name = LDAP['server_name']
    bind_user = LDAP['bind_user']
    password = LDAP['bind_password']
    search_base = LDAP['search_base']
    use_ssl = LDAP['use_ssl']

    search_filter = '(sAMAccountName={})'.format(username)
    search_attributes = ['memberOf', ]

    c =  Connection(Server(server_name, connect_timeout = 3, use_ssl=use_ssl),
                    user = bind_user,
                    password = password,
                    auto_bind = True,
                    raise_exceptions = True)

    c.search(search_base, search_filter, attributes = search_attributes)

    result = c.result
    response = c.response
    c.unbind()

    resp = response[0]['attributes']['memberOf']
    groups = []

    for g in resp:
        groups.append(g.split(',')[0].split('=')[1])

    return groups
