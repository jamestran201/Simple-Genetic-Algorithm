import matplotlib.pyplot as plt
import os
from datetime import datetime

RESULTS_DIR = "results/"

TEST_FUNCTIONS = [
    "Ackley", "De Jong Sphere", "Easom", "Griewank", "Himmelblau", "Rastrigin", "Rosenbrock",
    "Rosenbrock", "Schwefel", "Six Hump Camel Back", "Xin She Yang", "Zakharov", "f10", "f11",
    "f12", "f13", "f14", "f15", "f16", "f17", "f18", "f19", "f20", "f21", "f22", "f23", "f24",
    "f25", "f26", "f27"
]

def plot_line_graph(x, y, xlabel, ylabel, plot_title, timestamp):
    plt.plot(x, y)
    plt.title(plot_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    output_dir = RESULTS_DIR + timestamp.strftime("%Y%m%d-%H%M%S")
    try:
        os.mkdir(output_dir)
    except:
        pass

    outfile = plot_title.replace(" ", "-").replace("(","").replace(")","") + ".png"
    plt.savefig(output_dir + "/" + outfile)
    
    plt.show()

def save_result_to_file(result_dict, timestamp):
    """
    Save the results to a text file.
    The input "result_dict" is a dictionary that must include all fields below:
    {
        "obj_func" : int,
        "obj_dimen" : int,
        "pool_size" : int,
        "mutate_prob" : float,
        "max_iter" : int,
        "best_obj_value" : float,
        "best_gene": list,
        "stop_iter" : int,
        "stop_reason" : str
    }
    """

    output_dir = RESULTS_DIR + timestamp.strftime("%Y%m%d-%H%M%S")
    try:
        os.mkdir(output_dir)
    except:
        pass

    with open(output_dir + "/" + "summary.txt", "w") as f:
        f.write("Objective function: {}\n".format(TEST_FUNCTIONS[result_dict["obj_func"] - 1]))
        f.write("Dimension of objective function: {}\n".format(result_dict["obj_dimen"]))
        f.write("Pool size: {}\n".format(result_dict["pool_size"]))
        f.write("Mutation probability: {}\n".format(result_dict["mutate_prob"]))
        f.write("Maximum number of iterations: {}\n".format(result_dict["max_iter"]))
        f.write("Stopped at iteration: {}\n".format(result_dict["stop_iter"]))
        f.write("Reason for stopping: {}\n".format(result_dict["stop_reason"]))
        f.write("Best fitness value: {:.3f}\n".format(result_dict["best_obj_value"]))
        f.write("Best gene:\n")
        f.write("{}\n".format(result_dict["best_gene"]))