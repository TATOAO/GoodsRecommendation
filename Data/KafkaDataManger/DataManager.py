from Data.DataCollections import DataCollections


class DataManager(dict):
    """
    Provides update, extracting methods to updat data
    """

    def update_data(self, data_collection: DataCollections, data_inst):
        data_collection.update_data(data_inst)

    def remove_data(self, data_collection: DataCollections, data_inst):
        data_collection.remove_data(data_inst)
