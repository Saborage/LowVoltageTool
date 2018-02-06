# LowVoltageTool
---------------------------------------------------------------
**Low Voltage Tool** is the project I made for my Bachelor's thesis at Haute Ecole Louvain en Hainaut - Mons. This project is being built
under the watch of Electrical Engineering Service of Mons' Polytechnic Faculty (GELE). All the rights of the project are reserved to GELE.

## Overview
---------------------------------------------------------------

### Libraries

python==3.6.0
anytree==2.0.0
openpyxl==2.4.4
wxPython==4.0.0b2
numpy==1.13.1
scipy==0.19.1

Be careful that numpy, scipy and wxPython versions are subject to changes as those are still in development.

------
### Tasks 
- [x] Build a model structure
- [x] Translate load-flow algorithm from Matlab to Python
- [x] Build a basis for implementing a Graphical User Inteface
- [ ] Finish the GUI

See more on this [Trello](https://trello.com/b/EAq94Q1x/outil-basse-tension-gui)
-----

### Contribute

#### On Windows

1. Install [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) globally
``` pip install virtualenv ```
2. Create a virtual environment for this project and then activate it.
3. Install the requirements.
4. run ``` pip install -r requirements-win.txt ```
5. Install the dependencies except Numpy and Scipy.
6. Download [numpy+mkl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) (Choose depending on your platform).
7. Download [scipy](https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy) (Choose depending on your platform).
8. Install them ```pip install numpy*.whl && pip install scipy*.whl```

#### On Debian

1. Before installing the requirements, I suggest to use (if you don't use it yet) [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
2. Install the requirements for debian: ```pip install -r requirements-debian.txt```
3. Install wxPython:
    pip install -U --pre \
        -f https://wxpython.org/Phoenix/snapshot-builds/linux/gtk3/ubuntu-16.04 \
        wxPython
4. You're now good to go.
N.B.: The projet uses some libraries that depends on Windows. It should behave differently on a Linux distribution (or some features will just be missing).
