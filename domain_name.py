def domain_name(url):
    if 'www' in url:
        url = url[(url.find('.')) + 1:]
        return url[:(url.rfind('.'))]

    else:
        while '.' in url:
            url = url[:url.rfind('.')]
        return url[url.find('/') + 2:]
