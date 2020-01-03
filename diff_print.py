import difflib
import datetime
from config import DATABASE_CONFIG


def diff_writer():
    try:
        config = DATABASE_CONFIG
        old = open(config['old']).readlines()
        new = open(config['new']).readlines()

        now = datetime.datetime.now()

        f_diff = open(config['diff'], 'w')
        f_diff.write("WhenCreated : " + str(now) + '\n')

        for line in difflib.unified_diff(old, new, n=0):
            f_diff.write(line)

        print(f_diff.read().count("\n") + 1)

        f_diff.close()
        return True
    except:
        return False


def diff_count():
    config = DATABASE_CONFIG

    f_diff = open(config['diff'], 'r')
    line_count = f_diff.read().count("\n")
    f_diff.close()

    return line_count
