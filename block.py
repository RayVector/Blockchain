import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'


def get_hash(file_name):
    file = open(blockchain_dir + file_name, 'rb').read()
    return hashlib.md5(file).hexdigest()


def check_int():
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    for item in files[1:]:
        f = open(blockchain_dir + str(item))
        h = json.load(f)['hash']

        prev_file = str(item - 1)

        actual_hash = get_hash(prev_file)
        if h == actual_hash:
            res = 'Ok'
        else:
            res = "Corrupted"
        print('Block {} is: {}'.format(prev_file, res))

def write_block(name, amount, to_whom, prev_hash=''):
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    last_file_name = files[-1]

    next_file_name = str(last_file_name + 1)

    prev_hash = get_hash(str(last_file_name))

    data = {'name': name, 'amount': amount, 'to_whom': to_whom, 'hash': prev_hash}

    with open(blockchain_dir + next_file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    check_int()
    # write_block("Oleg", 50, "Petr", )


if __name__ == '__main__':
    main()
