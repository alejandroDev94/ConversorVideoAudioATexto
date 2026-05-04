from urllib.parse import urlparse

def is_url(path):
    """
    Check if the given path is a URL.
    """
    parsed = urlparse(path)
    return parsed.scheme and parsed.netloc
