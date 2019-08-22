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
    files = get_files()
    if len(files) == 0:
        data = {'name': '', 'amount': 0, 'to_whom': '', 'hash': ''}

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

        prev_file = str(item - 1)

        actual_hash = get_hash(prev_file)
        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'
        results.append({'block': prev_file, 'result': res})

    return results


def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()
    last_file_name = files[-1]
    last_file = str(last_file_name)

    if len(files) > 2:
        os.remove(blockchain_dir + last_file)

    files = get_files()
    last_file_name = files[-1]

    next_file_name = str(last_file_name + 1)

    prev_hash = get_hash(str(last_file_name))

    data = {'name': name, 'amount': amount, 'to_whom': to_whom, 'hash': prev_hash}

    with open(blockchain_dir + next_file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    make_ghost(data)


def make_ghost(data):
    files = get_files()
    last_file_name = files[-1]
    next_file_name = str(last_file_name)
    prev_hash = get_hash(str(last_file_name))
    data['hash'] = prev_hash

    ghost_name = str(int(next_file_name) + 1)

    with open(blockchain_dir + ghost_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
