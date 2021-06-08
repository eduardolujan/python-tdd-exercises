class TempRecord:
    def __init__(self, dy: int = None, mxt: int = None, mnt: int = None):
        if not isinstance(dy, int):
            raise ValueError("Error dy is not int")

        if not isinstance(mxt, int):
            raise ValueError("Error mxt is not int")

        if not isinstance(mnt, int):
            raise ValueError("Error mnt is not int")

        self.dy = dy
        self.mxt = mxt
        self.mnt = mnt


class TempDisp:
    def __init__(self, temp_record: TempRecord):
        self.temp_record = temp_record

    def __call__(self):
        self.temp_disp()

    def temp_disp(self):
        return self.temp_record.mxt - self.temp_record.mnt


class TempCollection:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def append(self, element: TempRecord):
        if not isinstance(element, TempRecord):
            raise ValueError(
                f"Error element:{element} is not instance of {TempRecord}"
            )

        self.elements.append(element)

    def __iter__(self):
        return self

    def __next__(self):
        for record in self.elements:
            return record


class CollectionFilter:
    def __init__(self, temp_collection: TempCollection):
        self.temp_collection = temp_collection

    def max(self) -> TempRecord:

        return max(
            [TempDisp(record) for record in self.temp_collection],
            key=lambda record: record.temp_disp(),
        )
