
def logger(type, message, error=None, exception=None):
    model = '[{level}]: {message}'
    if type == 'l':
        print(model.format(level='LOG', message=message))
    elif type == 'e':
        print(model.format(level='ERROR', message='Causa: {0} - Error: {1} - Exception: {2}'.format(message, error, exception)))
    else:
        logger('e', 'Tipo ({0}) no válido para mostrar el mensaje {1}'.format(type, message))