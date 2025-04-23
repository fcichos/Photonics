
# %% module

isdark = True
from rayoptics.environment import *

# %% Path
root_pth = Path(rayoptics.__file__).resolve().parent


# % optics
opm = open_model(root_pth/"codev/tests/ag_dblgauss.seq")
sm  = opm['seq_model']
osp = opm['optical_spec']
pm = opm['parax_model']
em = opm['ele_model']
pt = opm['part_tree']
ar = opm['analysis_results']



# %% plot
layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, is_dark=isdark).plot()
