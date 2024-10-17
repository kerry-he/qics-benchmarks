import argparse
import csv
import os
import qics


parser = argparse.ArgumentParser(description="Runs benchmarks for QICS.")

parser.add_argument("-d", "--directory", type=str, required=True,
                    help="input directory to read problems from")
parser.add_argument("-o", "--output", type=str,
                    help="name of file to output logs to")
parser.add_argument("--lowaccuracy", action="store_true",
                    help="solve problems to low accuracy, i.e., tol=1e-5 "
                    "(default: tol=1e-8)")

args = parser.parse_args()

folder = args.directory.strip()
fin_names = os.listdir(folder)

if args.output is None:
    import time
    time_str = time.strftime("%Y-%m-%d_%H-%M-%S")
    fout_name = "qics_benchmarks_" + time_str + ".csv"

tol_gap = 1e-5 if args.lowaccuracy else 1e-8
tol_feas = 1e-5 if args.lowaccuracy else 1e-8

with open(fout_name, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["problem", "solver", "status", "optval", "time",
                     "iter", "gap", "pfeas", "dfeas"])

for fname in fin_names:
    # Read and solve a conic program
    model = qics.io.read_file(folder + "/" + fname)
    solver = qics.Solver(model, 
                         max_iter=500, tol_gap=tol_gap, tol_feas=tol_feas)
    info = solver.solve()

    # Write solver summary to file
    with open(fout_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([fname, "ours", info["sol_status"],  info["p_obj"],
                         info["solve_time"], info["num_iter"], 
                         info["opt_gap"], info["p_feas"], info["d_feas"]])
