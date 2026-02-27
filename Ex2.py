def check_url(url):

    if " " in url:
        return False

    has_protocol = url.startswith("http://") or url.startswith("https://")

    if not has_protocol:
        return False

    if "." not in url:
        return False

    if url == "https://" or url == "http://":
        return False

    return True

print("Is 'https://google.com' valid?", check_url("https://google.com"))
print("Is 'google.com' valid?", check_url("google.com"))
print("Is 'https://my site.com' valid?", check_url("https://my site.com"))