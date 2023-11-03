# -*- coding: utf-8 -*-
# ModuleName: 111
# Author: dongyihua543
# Time: 2023/10/11 18:01

import warnings
# import groundingdino.datasets.transforms as T
from groundingdino.util.inference import load_model, load_image, predict, annotate

try:
    from groundingdino import _C
except BaseException as e:
    print("Exception: {}".format(e))
    warnings.warn("Failed to load custom C++ ops. Running on CPU mode Only!")
else:
    print("import _C success")
