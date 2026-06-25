


from multiprocessing import Pool, Manager, Process
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


def run_sim(args):

    i, queue = args

    params = sampler.sample()

    netlist = builder.build(params)

    filename = os.path.join(SIM_DIR, f"sim_{i}.sp")

    builder.write(netlist, filename)

    log = runner.run(filename)

    metrics = extract_metrics(log)
    os.remove(filename)

    if valid_result(metrics):

        queue.put((params, metrics))

    return i


def writer_process(queue):

    writer = DatasetWriter("dataset.csv")

    while True:

        item = queue.get()

        if item is None:
            break

        params, metrics = item

        writer.write(params, metrics)


def run_parallel(n=1000, workers=os.cpu_count()):

    manager = Manager()
    queue = manager.Queue()

    writer = Process(target=writer_process, args=(queue,))
    writer.start()

    with Pool(workers) as pool:

        tasks = [(i, queue) for i in range(n)]

        for _ in tqdm(pool.imap_unordered(run_sim, tasks), total=n):
            pass

    queue.put(None)   # stop signal
    writer.join()
