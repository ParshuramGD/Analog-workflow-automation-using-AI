import random
import math

BASE_DESIGN = {
    "W1": 8e-6,
    "W3": 16e-6,
    "W5": 4e-6,
    "W6": 32e-6,
    "W7": 4e-6,
    "Cc": 0.5e-12,
    "Rz": 5000,
    "Lch": 180e-9
}

class ParameterSampler:

    def __init__(self, perturb=0.4):
        self.perturb = perturb

    def perturb_linear(self, base):

        factor = random.uniform(
            1 - self.perturb,
            1 + self.perturb
        )

        return base * factor

    def perturb_log(self, base):

        factor = math.exp(
            random.uniform(-self.perturb, self.perturb)
        )

        return base * factor

    def sample(self):

        params = {}

        # transistor widths
        params["W1"] = self.perturb_linear(BASE_DESIGN["W1"])
        params["W3"] = self.perturb_linear(BASE_DESIGN["W3"])
        params["W5"] = self.perturb_linear(BASE_DESIGN["W5"])
        params["W6"] = self.perturb_linear(BASE_DESIGN["W6"])
        params["W7"] = self.perturb_linear(BASE_DESIGN["W7"])

        # passive components
        params["Cc"] = self.perturb_log(BASE_DESIGN["Cc"])
        params["Rz"] = self.perturb_log(BASE_DESIGN["Rz"])

        # channel length variation
        params["Lch"] = random.uniform(
            180e-9,
            360e-9
        )

        # matching constraints
        params["W2"] = params["W1"]
        params["W4"] = params["W3"]

        return params
