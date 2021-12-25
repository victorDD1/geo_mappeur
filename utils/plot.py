from matplotlib.pyplot import figure, show

def plot_3d_from_txt(file_path):
    '''
    3d plots from a processed data file (.txt)
    '''
    xs, ys, zs = [], [], []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            x,y,z = line.replace('{', '').replace('}', '').split(',')
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
    fig = figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs, ys, zs)
    show()
    return fig