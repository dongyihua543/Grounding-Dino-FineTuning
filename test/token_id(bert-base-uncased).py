# -*- coding: utf-8 -*-
# ModuleName: token_id(bert-base-uncased)
# Author: dongyihua543
# Time: 2023/10/16 15:37

from collections import defaultdict

"""
bert-base-uncased 模型
token id
"""

# 词表共30522行数据
path = "./data/bert-base-uncased_vocab.txt"
hash_table = defaultdict()

with open(path, mode='r', encoding='utf-8') as reader:
    for i, line in enumerate(reader):
        token = line.strip()
        if token:
            hash_table[i] = token
print("hash_table size: {}".format(len(hash_table)), end="\n\n")

# token_ids = [101, 5909, 15415, 102]
token_ids = [101, 5909, 1012, 21877, 27584, 14321, 1012, 102]
for token_id in token_ids:
    token = hash_table[token_id]
    print("token_id: {}, token: {}".format(token_id, token))
