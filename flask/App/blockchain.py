import json
import os
import hashlib
import datetime

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
        data = {'name': 'Core'}

        with open(blockchain_dir + '1', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        # hashing genesis self
        # f = open(blockchain_dir + '1')
        # h = json.load(f)['hash'] = get_hash('1')
        # data['hash'] = h
        #
        # with open(blockchain_dir + '1', 'w') as file:
        #     json.dump(data, file, indent=4, ensure_ascii=False)
        # f.close()
        print('Genesis created')
        now = datetime.datetime.now()
        print(str(now))
    else:
        print('Genesis exist')
        now = datetime.datetime.now()
        print(str(now))


def check_int():
    files = get_files()
    results = []

    if len(files) < 2:
        results.append({'block': 'empty', 'result': 'empty', 'name': 'system', 'id': 'empty'})
    else:
        for item in files[1:]:
            f = open(blockchain_dir + str(item))
            h = json.load(f)['hash']

            prev_file = str(item - 1)

            f2 = open(blockchain_dir + prev_file)
            n = json.load(f2)['name']

            actual_hash = get_hash(prev_file)
            if h == actual_hash:
                res = 'Correct'
            else:
                res = 'Damaged'
            results.append({'block': prev_file, 'result': res, 'name': n, 'id': h})
    return results


def make_ghost(data):
    files = get_files()
    last_file_name = files[-1]
    next_file_name = str(last_file_name)
    prev_hash = get_hash(str(last_file_name))
    data['hash'] = prev_hash

    ghost_name = str(int(next_file_name) + 1)

    with open(blockchain_dir + ghost_name, 'w') as file:
        json.dump(data, file)


def remove_ghost():
    files = os.listdir(blockchain_dir)
    last_file_name = files[-1]
    last_file = str(last_file_name)

    if len(files) > 2:
        os.remove(blockchain_dir + last_file)


def write_block(name, prev_hash=''):
    now = datetime.datetime.now()
    print(str(now))

    remove_ghost()

    files = get_files()
    last_file_name = files[-1]

    next_file_name = str(last_file_name + 1)

    prev_hash = get_hash(str(last_file_name))

    data = {'name': name, 'hash': prev_hash}

    with open(blockchain_dir + next_file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    make_ghost(data)
