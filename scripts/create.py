import os
import random
import string

def get_random_ext(extensions):
    return random.sample(extensions, 1)[0]

def get_random_string(k=5):
    # TODO: first letter uppercase
    return ''.join(random.choices(string.ascii_lowercase, k=k))

def get_random_filename(ext):
    if (ext == 'pdf'):
        return f"doc__{get_random_string()}"
    return f"other__{get_random_string()}"

def create_files(root="./output", extensions=['pdf', 'mkv', 'mp3'], count=5):
    # TODO: use built in functionality python
    if not os.path.exists(root):
        os.makedirs(root)
    for _ in range(count):
        ext = get_random_ext(extensions)
        filename = get_random_filename(ext)
        # TODO: use built in functionality python
        # TODO; use path.join
        with open(f'{root}/{filename}.{ext}', 'w') as fp:
            pass
    
    