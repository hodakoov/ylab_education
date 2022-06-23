"""
Написать метод domain_name, который вернет домен из url адреса:
url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = "cnet"
"""


def domain_name(url: str):
    if 'www' in url:
        url = url[(url.find('.')) + 1:]
        return url[:(url.rfind('.'))]

    else:
        while '.' in url:
            url = url[:url.rfind('.')]
        return url[url.find('/') + 2:]


"""
Для проверки:

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
"""
