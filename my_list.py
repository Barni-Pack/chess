class MyList(list):
    def __init__(self, *args, **kwargs):
        super(MyList, self).__init__(args[0])

    def __getitem__(self, n):
        return super(MyList, self).__getitem__(n-1)
    
    def __setitem__(self, key, value):
        return super(MyList, self).__setitem__(key-1, value)