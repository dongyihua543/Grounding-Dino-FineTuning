# -*- coding: utf-8 -*-
# ModuleName: grounding_dino分词器
# Author: dongyihua543
# Time: 2023/10/16 14:56

import torch
from utils.train import load_model, load_image, train_image, annotate

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = load_model(model_config_path="D:/PycharmProjects/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py",
                   model_checkpoint_path="D:/PycharmProjects/GroundingDINO/weights/groundingdino_swint_ogc.pth",
                   device=device)
print("实例类型: {}".format(type(model)))

# text = 'fruit vegetable'
# text = 'fruit.peduncle.'
text = 'fruit.'
tokenizer = model.tokenizer
tokenized = tokenizer(text)
print(tokenized)
