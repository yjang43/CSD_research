from load_mat import MAT_DATA
from typing import List
import matplotlib.pyplot as plt


def visualize_reps(rep_list: List, title: str = "REPS"):
    if rep_list.__len__() > 9:
        print("size of the list should be bound to 9")
    fig, axes = plt.subplots(3, 3)
    fig.suptitle(title)
    for rep_index in range(rep_list.__len__()):
        axes[int(rep_index / 3)][int(rep_index % 3)].plot(rep_list[rep_index])
    plt.show()


def set_rep_list(start, end):
    rep_list = list()
    for row in range(start, end):
        rep_list.append(MAT_DATA[row, :])
    return rep_list


rep_list = set_rep_list(150, 159)   # gradual right shift of spike
rep_list = set_rep_list(300, 309)   # not gradual but right shift of spikes
                                    # make sure if the spike is something that happens due to stimulus, not natural sig

visualize_reps(rep_list, "rep_151~rep_159")
