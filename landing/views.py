from django.shortcuts import render
from django.conf import settings
from .ldap import get_permission_groups


USER_KEY = 'HTTP_UID'

def landing(request):
    '''Dynamically display the list of NBSmart project based on user's permissions'''
    projects = settings.PROJECTS
    nbstrn = settings.NBSTRN
    user_key = USER_KEY

    username = request.META[user_key] if user_key in request.META else None
    permission_groups = get_permission_groups(username) if username else []
    user = { 'username': username }

    # print('PERMISSION_GROUPS', permission_groups)

    for project in projects:
        access = False
        if username:
            permission_group = projects[project]['permission_group']
            access = permission_group in permission_groups

        projects[project]['access'] = access

    context = {'PROJECTS': projects, 'NBSTRN': nbstrn, 'USER': user, 'USERNAME': username, 'META': request.META}

    return render(request, 'landing/landing.html', context = context)
