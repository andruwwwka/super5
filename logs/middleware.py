from logs.models import AccessLog


class LoggingMiddleware:

    def process_template_response(self, request, response):
        user = request.user
        if response.context_data:
            response.context_data.update(
                {
                    'user_pk': None
                }
            )
            if user and user.pk:
                response.context_data.update(
                    {
                        'user_pk': user.pk
                    }
                )
        self.save_data_to_logs(request, response.context_data)
        return response

    def save_data_to_logs(self, request, ctx):
        user = request.user.email if hasattr(request.user, 'email') else 'anonymous'
        log_data = {
            'ip': request.META.get('REMOTE_ADDR', None),
            'user_agent': request.META.get('HTTP_USER_AGENT', None),
            'user': user,
            'method': request.method,
            'to_server_data': request.POST,
            'to_client_data': ctx
        }
        a_l = AccessLog(
            data=str(log_data)
        )
        a_l.save()
