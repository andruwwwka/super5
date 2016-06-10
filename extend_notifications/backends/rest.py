from pinax.notifications.backends.base import BaseBackend
from extend_notifications.models import RestNotification


class RestBackend(BaseBackend):

    spam_sensitivity = 2

    def can_send(self, user, notice_type, scoping):
        """
        Determines whether this backend is allowed to send a notification to
        the given user and notice_type.
        """
        return True

    def deliver(self, recipient, sender, notice_type, extra_context):

        notification = RestNotification(
            user=recipient,
            body=notice_type.description
        )
        notification.save()
