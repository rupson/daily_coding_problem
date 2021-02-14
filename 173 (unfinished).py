#rob upson 20/5/19 daily coding problem 173

def flatten(d):

    if d.isdigit():
        return d
    return flatten(d)

    for each in d:
        if each.isIterable():
            flatten(each)

    return newDictionary

if __name__ == "__main__":

    dictionary = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "bar": {
                    "baz": 8
                    }
                }
            }
        }
    
    print(flatten(dictionary))
