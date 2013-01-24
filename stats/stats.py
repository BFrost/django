#import os
#import base64
import random
import string

def _generate_tracking_id():
    tracking_id = ''
    characters = string.uppercase + string.lowercase + string.digits + '!@#$%^&*()'
    id_length = 50
    for y in range(id_length):
        tracking_id += characters[random.randint(0, len(characters)-1)]
    return tracking_id

def tracking_id(request):
    try:
        return request.session['tracking_id']
    except KeyError:
#        request.session['tracking_id'] = base64.b64encode(os.urandom(36))
        request.session['tracking_id'] = _generate_tracking_id()
        return request.session['tracking_id']