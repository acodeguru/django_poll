class AppUtil:

    def get_client_ip(self, request):
        remote_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        ip = remote_address
        return ip
