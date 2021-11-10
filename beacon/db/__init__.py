# TODO: to be deleted 

class FieldMock:
    def __init__(self):
        self.find = lambda _: FieldMock()
        self.skip = lambda _: FieldMock()
        self.limit = lambda _: FieldMock()
class BeaconMock:
    def __init__(self):
        self.datasets = FieldMock()
class DBMock:
    def __init__(self):
        self.beacon = BeaconMock()

client = DBMock()
