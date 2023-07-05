from Data import GoodCollections


class RecommendationEngine:
    def __init__(self, good_collection: GoodCollections) -> None:
        self.good_collection = good_collection
