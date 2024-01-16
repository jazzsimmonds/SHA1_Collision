import hashlib

def get_sha1(text):
    hashed = hashlib.sha1(text)
    sha1 = hashed.hexdigest()
    return sha1

def get_dict_value(text, d):
    keys = d.keys()
    for i in keys:
        if d[i] == text:
            return i
ptext = 'c'
text = ptext
hashed = get_sha1(bytes(text,'utf-8'))
hf = hashed[0:6]
count = 0
right = text

all_hashes = {}
a=1
while count != 1:
    print("COUNT: ",a)
    #+1 each time on left
    lo = get_sha1(bytes(text,'utf-8'))
    #+2 each time on right
    ro = get_sha1(bytes(right,'utf-8'))
    rl = get_sha1(bytes(ro,'utf-8'))
    lf = lo[0:6]
    rf = rl[0:6]
    if lf != rf:
        if len(all_hashes) != 0:
            vals = all_hashes.values()
            for i in vals:
                if rf == i:
                    v = get_dict_value(i, all_hashes)
                    if v == ro:
                        pass
                    else:
                        print("Same value found")
                        print(v, " and ", ro)
                        print(i, " and ", rf)
                        count = 1
                        break
                elif lf == i:
                    v = get_dict_value(i, all_hashes)
                    if v == text:
                        pass
                    else:
                        print("Same value found")
                        print(v, " and ", text)
                        print(i, " and ", rlf)
                        count = 1
                        break
            all_hashes[text]=lf
            all_hashes[ro]=rf
            text = lo
            right = rl
        else:
            all_hashes[text]=lf
            all_hashes[ro]=rf
            text = lo
            right = rl
    elif lf == rf:
        print("Same value found")
        print(text, " and ", ro)
        print(lf, " and ", rf)
    a+=1

                        
    
