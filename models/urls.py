from django.urls import path, register_converter
from .views import *
class TelegramIDConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
register_converter(TelegramIDConverter, 'tg_id')


urlpatterns = [
    path('contact-us/', ContactCreateView.as_view()),
    path('tg-contact-us/', TgContactCreateView),
    path('tg-contact-us/<tg_id:tg_id>/', TgContactDetailView),
]