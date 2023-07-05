from collections import defaultdict

from Data.DataCollections import DataCollections
from Schema.Good import Good


class GoodCollections(DataCollections):
    def __init__(self):
        # another extract dict with property
        self.category4_map = defaultdict(set)
        self.city_map = defaultdict(set)

    def update_data(self, good: Good):
        self.remove_data(good)
        self[good.id] = good
        self.category4_map[good.cat4].add(good)
        self.city_map[good.city].add(good)

    def remove_data(self, good: Good):
        if good.id in self:
            self.pop(good.id)

        self.category4_map.get(good.cat4, set()).discard(good)
        self.city_map.get(good.city, set()).discard(good)

    def __repr__(self) -> str:
        return "\n".join([str(good) for good in self.values()])

    def __str__(self) -> str:
        return self.__repr__()
