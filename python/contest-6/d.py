import re

# спёртая с интернета штука и чутка модифицированная
PATTERN = '(?:(?:http|https):\/\/)?[a-z0-9.\/?:@-_=#]+\.(?:[a-z]){2,6}(?:[a-z0-9а-я+.&\/?:@-_=#])*'

def get_urls(text):
    temp = " ".join(text.lower().split())
    return re.findall(PATTERN, text)

print(*get_urls("""По результатам семестра ваша скидка понижена. 
Для подробностей обратитесь к https://hse/rating/fcn/pmi.html 
и по возникшим вопросам оставьте 
обращение на https://anime.com"""))
