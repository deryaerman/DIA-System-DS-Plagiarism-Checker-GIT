'''
MIT License

Copyright (c) 2021 Intel Labs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import torch
import torch.nn as nn
from torch_scatter import scatter_mean


class BagOfFeaturesModel(nn.Module):
    def __init__(self, feature_emb_size, feature_vocab_size, output_size):
        super().__init__()
        self.feature_emb = nn.Sequential(
            nn.Embedding(feature_vocab_size, feature_emb_size),
            nn.Dropout(0.5)
        )
        self.out = nn.Sequential(
            nn.Linear(feature_emb_size, output_size)
        )

    def forward(self, features, indices):
        feature_emb = self.feature_emb(features)
        return self.out(scatter_mean(feature_emb, indices, dim=0))
