from django.apps import AppConfig


class SocialConfig(AppConfig):
    name = 'social'

    def ready(self):
    	import social.signals

class VideoConfig(AppConfig):
    name = 'video'
