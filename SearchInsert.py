
class StringOPS:
    def __init__(self, arrLen=10):
        self.arrLen=arrLen
        self.ct=0
        self.arr={}
        self.counterArr={}
    
    def insert_str(self, key, value):

        if len(self.arr) >= self.arrLen:
            old_val = min(self.counterArr.keys(), key=lambda k: self.counterArr[k])
            self.arr.pop(old_val)
            self.counterArr.pop(old_val)
        self.arr[key]=value
        self.counterArr[key]=self.ct
        self.ct +=1
        return key
    
    def search_str(self, key):
        if key in self.arr:
            self.counterArr[key] = self.ct
            self.ct += 1
            print(self.ct)
            return self.arr[key]
        return -1
    
if __name__ == '__main__':
    sops=StringOPS(2)
    print("1",sops.insert_str(1, "value1"))
    print("2",sops.insert_str(2, "value2"))
    print(sops.search_str(2))
    print(sops.insert_str(3, "value3"))
    print("xxxx")
    print(sops.search_str(1))
    print(sops.search_str(2))
    print("====")
    print(sops.search_str(3))
    print(sops.search_str(3))
    print(sops.search_str(3))
    print(sops.insert_str(4, "value4"))
    print("====")
    print(sops.search_str(2))
    print(sops.insert_str(4, "value4"))
        