import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'


def get_hash(file_name):
    file = open(blockchain_dir + file_name, 'rb').read()
    return hashlib.md5(file).hexdigest()


def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])


def genesis_create():
    files = os.listdir(blockchain_dir)
    if len(files) == 0:
        data = {'name': '', 'hash': ''}

        with open(blockchain_dir + '1', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        f = open(blockchain_dir + '1')
        h = json.load(f)['hash'] = get_hash('1')
        data['hash'] = h

        with open(blockchain_dir + '1', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        f.close()
        print('Genesis created')
    else:
        print('Genesis exist')


def check_int():
    files = get_files()
    results = []

    for item in files[1:]:
        f = open(blockchain_dir + str(item))
        h = json.load(f)['hash']
        n = json.load(f)['name']

        prev_file = str(item - 1)

        actual_hash = get_hash(prev_file)
        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'
        results.append({'block': prev_file, 'result': res, 'name': n, 'id': h})

    return results


def make_ghost(data):
    files = get_files()
    last_file_name = files[-1]
    next_file_name = str(last_file_name)
    prev_hash = get_hash(str(last_file_name))
    data['hash'] = prev_hash

    ghost_name = str(int(next_file_name) + 1) + 'g'

    with open(blockchain_dir + ghost_name, 'w') as file:
        json.dump(data, file)


def remove_ghost():
    # files = get_files()
    files = os.listdir(blockchain_dir)
    last_file_name = files[-1]
    last_file = str(last_file_name)

    if len(files) > 2:
        os.remove(blockchain_dir + last_file)


def write_block(name, prev_hash=''):
    remove_ghost()

    files = get_files()
    last_file_name = files[-1]

    next_file_name = str(last_file_name + 1)

    prev_hash = get_hash(str(last_file_name))

    data = {'name': name, 'hash': prev_hash}

    with open(blockchain_dir + next_file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    make_ghost(data)



