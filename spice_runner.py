import subprocess

class SpiceRunner:

    def run(self, netlist_path):

        cmd = ["ngspice", "-b", netlist_path]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        return result.stdout