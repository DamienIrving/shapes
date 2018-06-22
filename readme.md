# Notes from packaging workshop

`setup.py` is the brain (describes our package, workhorse for installation)

`__init__.py` is the appendix (typically empty and useless, but it's a hangover from the early days. Good place for global stuff.)

`shapes.py` is the heart (actually does what the package does)

directory structure:
```
shapes/
    setup.py
    shapes/
        __init__.py
        shapes.py
```
