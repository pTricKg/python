from hashlib import md5
import sys

def crack_pass(pass_hash):
    for i in range(1001): #1000 times
        m = md5()         
        m.update(str(i))
        test_hash = m.hexdigest()
        if(test_hash != pass_hash):
            print("Failed: %s\t%s" % (test_hash, pass_hash))
        else:
            print("Success: %d" % i)
            return

m = md5()
m.update(str(sys.argv[1]))
crack_pass(m.hexdigest())

