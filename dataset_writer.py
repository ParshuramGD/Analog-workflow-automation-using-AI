import csv
import os

class DatasetWriter:

    def __init__(self, filename):

        self.filename = filename

        self.fieldnames = [
            "W1","W2","W3","W4","W5","W6","W7",
            "Cc","Rz","Lch",
            "gain","ugf","pm"
        ]

        self.header_written = os.path.exists(filename)

    def write(self, params, metrics):

        row = {**params, **metrics}

        with open(self.filename, "a", newline="") as f:

            writer = csv.DictWriter(f, fieldnames=self.fieldnames)

            if not self.header_written:
                writer.writeheader()
                self.header_written = True

            writer.writerow(row)
