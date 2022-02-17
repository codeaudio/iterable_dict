class IterableDict(dict):
    def __init__(self, *args, **kwargs):
        if args:
            args = tuple(map(str, args))
            if len(args) == 1:
                super().__init__(
                    {x: x for i in args for x in i}
                )
            else:
                super().__init__(
                    {i: {x: x for x in args[i]} for i in range(0, len(args))}
                )
        else:
            super(IterableDict, self).__init__(**kwargs)
