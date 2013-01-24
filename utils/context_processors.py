from catalog.models import Category
from ecomstore.settings import *

def main(request):
    return {
#            'active_categories': Category.objects.filter(is_active=True),
            'site_name': SITE_NAME,
            'meta_keywords': META_KEYWORDS,
            'meta_description': META_DESCRIPTION,
            'request': request
            }

