# encoding=utf-8
import os, hashlib

def get_file_descriptor(filepath, mode='rb'):
    fd = None
    try:
        fd = open(filepath, mode)
        return fd
    except IOError:
        return fd

def get_md5_for_file(fd, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = fd.read(block_size)
        if not data:
            break
        md5.update(data)
    fd.close
    return md5.hexdigest()


def bytestomegabytes(bytes):
    return (bytes / 1024) / 1024

def md5_list(dir):
    tot_repeated = 0
    tot_bytes = 0
    hash_list = {}
    try:
        for root, dirs, files in os.walk(dir):
            for file in files:
                    filepath = os.path.join(root, file)
                    if get_file_descriptor(filepath):
                        fd = get_file_descriptor(filepath)
                        hash = get_md5_for_file(fd, 8192)
                        if hash not in hash_list:
                            hash_list[hash] = filepath
                        else:
                            print "{0} ; {1} ; {2}; {3}".format(hash, filepath, hash_list[hash], os.path.getsize(filepath))
                            tot_repeated += 1
                            tot_bytes += os.path.getsize(filepath)
    except KeyboardInterrupt:
        print "You cancelled!"
    finally:
        print "Total of dup files: {}".format(tot_repeated)
        print "Total size of duplicated files: {} Mbytes".format(bytestomegabytes(tot_bytes))
            #print hash_list

def add_duplicate(hash, filename):
    pass

def run():
    #md5_list('/home/lborda/Pictures')
    md5_list('/media/lborda/data')

if __name__ == '__main__':
    run()
