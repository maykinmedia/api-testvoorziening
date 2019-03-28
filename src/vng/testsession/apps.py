from django.apps import AppConfig

from ..utils.choices import StatusChoices


class TestsessionConfig(AppConfig):
    name = 'vng.testsession'

    def ready(self):
        from .models import Session, SessionType
        from .task import bootstrap_session, create_latent_session
        sleep = Session.objects.filter(status=StatusChoices.sleeping)
        session_types = SessionType.objects.all()
        for st in session_types:
            present = False
            for session in sleep:
                if session.session_type == st:
                    present = True
            if not present:
                create_latent_session.delay(st)
