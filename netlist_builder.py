import os

class NetlistBuilder:

    def __init__(self, template_tb):

        with open(template_tb) as f:
            self.template = f.read()

    def build(self, params):

        netlist = self.template

        for k, v in params.items():
            netlist = netlist.replace("{" + k + "}", str(v))

        return netlist

    def write(self, text, path):

        with open(path, "w") as f:
            f.write(text)

        return path