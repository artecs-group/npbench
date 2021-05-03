import argparse

from npbench.infrastructure import (Benchmark, generate_framework, LineCount,
                                    Test, utilities as util)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p",
                        "--preset",
                        choices=['S', 'M', 'L', 'paper'],
                        nargs="?",
                        default='S')
    parser.add_argument("-m", "--mode", type=str, nargs="?", default="main")
    parser.add_argument("-v",
                        "--validate",
                        type=util.str2bool,
                        nargs="?",
                        default=True)
    parser.add_argument("-r", "--repeat", type=int, nargs="?", default=10)
    parser.add_argument("-t", "--timeout", type=float, nargs="?", default=10.0)
    args = vars(parser.parse_args())

    # print(args)

    benchmarks = [
        'adi', 'arc_distance', 'atax', 'azimint_hist', 'bicg', 'cavity_flow',
        'cholesky2', 'compute', 'doitgen', 'floyd_warshall', 'gemm', 'gemver',
        'gesummv', 'go_fast', 'hdiff', 'jacobi_2d', 'lenet', 'syr2k', 'trmm',
        'vadv'
    ]
    numpy = generate_framework("numpy")
    numba = generate_framework("numba")

    for benchname in benchmarks:
        bench = Benchmark(benchname)
        for frmwrk in [numpy, numba]:
            lcount = LineCount(bench, frmwrk, numpy)
            lcount.count()
            test = Test(bench, frmwrk, numpy)
            try:
                test.run(args["preset"], args["validate"], args["repeat"],
                         args["timeout"])
            except:
                continue
