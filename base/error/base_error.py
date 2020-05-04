class BaseError(Exception):
    def __init__(self):
        super(BaseError, self).__init__()

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        # print("水电费")
        return "Sdsafs"

class Assertion(Exception):
    def __init__(self):
        super(Assertion, self).__init__()

    def check_assert(self, a, b, type='length'):
        try:
            if type=='length':
                assert len(a) == len(b)
        except Exception as e:
            print(e)







raise BaseError()