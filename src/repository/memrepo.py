from src.domain.model import Converted


class MemRepo:

    def __init__(self, data):
        self.data = data

    def list(self):
        return [Converted.from_dict(dict_) for dict_ in self.data]