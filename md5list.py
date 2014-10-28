# encoding=utf-8
import os, hashlib
import hurry.filesize

def get_md5_for_file(filepath, block_size=2**20):
    md5 = hashlib.md5()
    filepath = open(filepath, 'rb')
    while True:
        data = filepath.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def md5_list(dir):
    tot_repeated = 0
    tot_bytes = 0
    hash_list = {}
    try:
        for root, dirs, files in os.walk(dir):
            for file in files:
                filepath = os.path.join(root, file)
                hash = get_md5_for_file(filepath, 8192)
                if hash not in hash_list:
                    hash_list[hash] = filepath
                else:
                    print "{0} ; {1} ; {2}; {3}".format(hash, filepath, hash_list[hash], os.path.getsize(filepath))
                    tot_repeated += 1
                    tot_bytes += os.path.getsize(filepath)
    except KeyboardInterrupt:
        print "You cancelled!"
    finally:
        print "Total of repeated files: {}".format(tot_repeated)
        print "Total size of duplicated files: {}".format(hurry.filesize.size(tot_bytes))
            #print hash_list

def add_duplicate(hash, filename):
    pass

def run():
    md5_list('/home/lborda/dev')

if __name__ == '__main__':
    run()
