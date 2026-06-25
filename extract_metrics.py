import re

def extract_metrics(output):

    gain = None
    ugf = None
    pm = None

    for line in output.splitlines():

        if "dc_gain" in line and "=" in line:
            try:
                gain = float(line.split("=")[1])
            except:
                pass

        if "ugf" in line and "=" in line:
            try:
                ugf = float(line.split("=")[1])
            except:
                pass

        if "phase_margin_val" in line and "=" in line:
            try:
                pm = float(line.split("=")[1])
            except:
                pass

    return {
        "gain": gain,
        "ugf": ugf,
        "pm": pm
    }
