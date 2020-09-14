import matplotlib as mpl
mpl.use('Agg')
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
sns.set()

def plot_w(np_arr, filename):
    #ax = plt.axes()

    f, ax = plt.subplots(figsize=(100,100), nrows=1)
    ax = sns.heatmap(np_arr, annot=True, center=0, ax=ax)
    ax.set_title("%s" % filename)
    #plt.savefig("%s.png" % filename, dpi='figure')
    f.savefig("%s.png" % filename, dpi='figure')

def load_data(filein):
    x = np.loadtxt(filein, delimiter="\t", comments="\t\n")
    return x

if __name__ == '__main__':
    print("init plot heatmap....")
    a_mat = load_data(sys.argv[1])
    a_mat = np.random.rand(100, 100)
    for i in range(a_mat.shape[0]):
        a_mat[i][i] = 0.0
    print("load mat shape (%d, %d)" % (a_mat.shape[0], a_mat.shape[1]))
    plot_w(a_mat, sys.argv[1])

    #os.system("/home/zangqiguang/bin/imgcat/bin/imgcat --width=60 --height=20 --depth iterm2 %s.png" % sys.argv[1])
    print("gen a_mat  %s.png success!" % sys.argv[1])
