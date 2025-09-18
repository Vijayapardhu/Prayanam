from django.conf import settings

def get_site_domain():
    """Get the current site domain"""
    return getattr(settings, 'SITE_DOMAIN', 'https://prayanam-91p7.onrender.com')

def get_site_name():
    """Get the current site name"""
    return getattr(settings, 'SITE_NAME', 'Prayanam')

def get_full_url(path=''):
    """Get full URL for a given path"""
    domain = get_site_domain()
    if path.startswith('/'):
        path = path[1:]
    return f"{domain}/{path}" if path else domain
