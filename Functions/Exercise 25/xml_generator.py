def myxml(tag, text='', **kwargs):
    attributes = ' '.join([f'{key}="{value}"' for key, value in kwargs.items()])
    return f'<{tag} {attributes}>{text}</{tag}>'


print(myxml('foo', 'bar', a=1, b=2))