from Schema.Good import Good


class GoodCollections:
    def __init__(self):
        self.good_collections = {}

    def get_collections(self):
        return self.good_collections

    def update_good(self, good: Good):
        self.good_collections[good.id] = good

    def remove_good(self, good: Good):
        self.good_collections.pop(good.id)

    def __repr__(self) -> str:
        return "\n".join([good for good in self.good_collections.values()])

    def __str__(self) -> str:
        return self.__repr__()

    def __getitem__(self, key):
        return self.good_collections[key]
