from django.utils.deprecation import MiddlewareMixin
from django.utils import translation

class LanguageMiddleware(MiddlewareMixin):
    """
    Middleware to handle user language preferences
    """
    
    def process_request(self, request):
        try:
            # Check if user has a language preference
            if request.user.is_authenticated and hasattr(request.user, 'language_preference'):
                language = request.user.language_preference
                if language in ['en', 'te', 'hi']:
                    translation.activate(language)
                    request.LANGUAGE_CODE = language
                    return
            
            # Check session for language preference
            language = request.session.get('django_language')
            if language and language in ['en', 'te', 'hi']:
                translation.activate(language)
                request.LANGUAGE_CODE = language
                return
            
            # Use default language
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'
            
        except Exception as e:
            # Fallback to default language if any error occurs
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'
