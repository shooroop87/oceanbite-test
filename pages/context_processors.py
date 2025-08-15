from django.templatetags.static import static

def site_info(request):
    return {
        "SITE_NAME": "Oceanbite Seafood",
        "SITE_EMAIL": "contact@oceanbiteseafood.com",
        "SITE_PHONE": "(818)-454-8765",
        "SITE_ADDRESS": "4695 MacArthur Ct, FL 11, Newport Beach, CA 92660, United States",
        "LOGO_URL": static('img/placeholders/logo.svg'),
    }
