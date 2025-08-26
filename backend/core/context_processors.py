def default_schema(request):
    """Default schema context processor"""
    return {
        'schema_org': {
            'name': 'Oceanbite Seafood',
            'description': 'Premium wild-caught seafood from the EU',
            'url': request.build_absolute_uri('/'),
        }
    }


def tours_context(request):
    """Tours context processor - placeholder for now"""
    return {
        'contact_info': {
            'email': 'info@oceanbiteseafood.com',
            'phone': '+1 (234) 567-890',
            'location': 'California, USA'
        }
    }