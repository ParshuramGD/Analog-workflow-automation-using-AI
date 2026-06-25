from multiprocessing import Pool
import os
from tqdm import tqdm

from parameter_sampler import ParameterSampler
from netlist_builder import NetlistBuilder
from spice_runner import SpiceRunner
from extract_metrics import extract_metrics
from dataset_writer import DatasetWriter
from result_parser import valid_result



sampler = ParameterSampler()
builder = NetlistBuilder("templates/tb_openloop.sp")
runner = SpiceRunner()
writer = DatasetWriter("dataset.csv")

SIM_DIR = "simulations"
os.makedirs(SIM_DIR, exist_ok=True)


    

def run_sim(i):

    params = sampler.sample()

    netlist = builder.build(params)

    filename = os.path.join(SIM_DIR, f"sim_{i}.sp")

    builder.write(netlist, filename)

    log = runner.run(filename)

    #print(f"Simulation {i} finished")

    metrics = extract_metrics(log)
    try:
        os.remove(filename)
    except:
        pass
    if valid_result(metrics):

        writer.write(params, metrics)
        #print("Saved sample:", metrics)

    else:
        pass
        #print("Invalid simulation")

    return i


def run_parallel(n=1000, workers=os.cpu_count()):

    with Pool(workers) as pool:
        list(tqdm(pool.imap_unordered(run_sim, range(n)), total=n))        
