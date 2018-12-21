class Utility(object):
    HTTP_PREFIX = 'http://'

    HTTPS_PREFIX = 'https://'

    @staticmethod
    def convertToValidUrl(url):
        if not url.startswith(Utility.HTTP_PREFIX) and not url.startswith(Utility.HTTPS_PREFIX):
            return ''.join([Utility.HTTP_PREFIX, url])
        return url