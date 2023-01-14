import base64

def shorten_url(long_url):
    # Encode the URL using base64
    short_url = base64.urlsafe_b64encode(long_url.encode('utf-8')).decode('utf-8')
    # Return the shortened URL
    return short_url

def restore_url(short_url):
    # Decode the short URL using base64
    long_url = base64.urlsafe_b64decode(short_url.encode('utf-8')).decode('utf-8')
    # Return the original URL
    return long_url

long_url = 'https://replit.com/@anirban-oss/url-shortener#main.py'#"https://www.example.com/some-very-long-path/to-a-page"
short_url = shorten_url(long_url)

print(short_url) # b'aHR0cHM6Ly93d3cueW91dHViZS5jb20='
print(restore_url(short_url)) # "https://www.youtube.com"
