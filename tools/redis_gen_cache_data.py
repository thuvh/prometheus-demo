import random
import sys

from walrus import *

DEFAULT_N = 10
HOST = '192.168.10.88'
DB = 2
KEY_NOT_EXPIRED = 'non_expired_key_{}'
KEY_EXPIRED = 'expired_key_{}'
KEY_HASH = 'hash_{}'
CMD_GEN = 'gen'
CMD_CLEAN = 'clean'
CACHE_NAME = 'prometheus_demo_cache'
HASH_NAME = 'prometheus_demo_hash'
KEY = 'prometheus_demo_key_{}'

redis_db = Database(host=HOST, db=DB)


def main():
    num_of_argv = len(sys.argv)
    cmd = None
    if num_of_argv == 1:
        n = DEFAULT_N
        cmd = CMD_GEN
    else:
        cmd = sys.argv[1]
        if cmd == CMD_GEN:
            if num_of_argv <= 2:
                n = DEFAULT_N
            else:
                try:
                    n = int(sys.argv[2])
                except ValueError:
                    n = DEFAULT_N
        elif cmd == CMD_CLEAN:
            if num_of_argv <= 2:
                n = DEFAULT_N
            else:
                try:
                    n = int(sys.argv[2])
                except ValueError:
                    n = DEFAULT_N
        else:
            cmd = CMD_GEN
            n = DEFAULT_N
    print(f'n={n}')

    if cmd == CMD_CLEAN:
        clean(n)
    elif cmd == CMD_GEN:
        gen(n)
    print('Done!')


def gen(n):
    min_exp_time = 30  # 30 second
    max_exp_time = 2 * 60  # 2 minute
    redis_cache = redis_db.cache(CACHE_NAME)
    redis_hash = redis_db.Hash(HASH_NAME)
    for i in range(n):
        exp = random.randint(min_exp_time, max_exp_time)
        redis_cache.set(KEY_EXPIRED.format(i), exp, exp)
        redis_hash[KEY_HASH.format(i)] = exp
        redis_db.set(KEY.format(i), exp)


def clean(n):
    redis_cache = redis_db.cache(CACHE_NAME)
    redis_hash = redis_db.Hash(HASH_NAME)
    for i in range(n):
        redis_cache.delete(KEY_EXPIRED.format(i))
        redis_db.delete(KEY.format(i))
    redis_hash.clear()


if __name__ == '__main__':
    main()

