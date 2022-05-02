url = input()
if 'https://youtu.be/' in url:
    shorturl_split = url.split('https://youtu.be/')
    print(shorturl_split[1])
elif 'https://www.youtube.com/watch?v=' in url:
    longurl_split = url.split('https://www.youtube.com/watch?v=')
    print(longurl_split[1])