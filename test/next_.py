# -*- coding: utf-8 -*-
# ModuleName: next_
# Author: dongyihua543
# Time: 2023/10/23 18:38

import os

"""
next(iterator[, default])

Return the next item from the iterator.
If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.
"""

token_ids = (i for i in range(1, 4))

token_id = next(token_ids)
print(token_id)

token_id = next(token_ids)
print(token_id)

token_id = next(token_ids)
print(token_id)

# if default is given and the iterator is exhausted.
token_id = next(token_ids, None)
print(token_id)
