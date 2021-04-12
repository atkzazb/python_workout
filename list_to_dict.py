def list_to_dict(*dicts):
    out = {}
    for d in dicts:
        for k, v in d.items():
            if k in out:
                try:
                    out[k].append(v)
                except AttributeError:
                    out[k] = [out[k], v]
            else:
                out[k] = v
    return out


print(list_to_dict({'a':1, 'b':2, 'c':3}, {'a':4, 'e':5}))