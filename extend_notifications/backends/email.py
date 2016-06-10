from django.conf import settings
from django.template import Context


from pinax.notifications.backends.email import EmailBackend


class ExtendEmailBackend(EmailBackend):

    def default_context(self):
        # FixMe временно перекрыл. Надо будет ввести родную модель Sites, если необходимо в уведомлении
        # FixMe указывать ссылку на источник откуда пришло уведомление. На обдумать.
        use_ssl = getattr(settings, "PINAX_USE_SSL", False)
        default_http_protocol = "https" if use_ssl else "http"
        return Context({
            "default_http_protocol": default_http_protocol,
        })

    def can_send(self, user, notice_type, scoping):
        if user.email:
            return True
        return False
