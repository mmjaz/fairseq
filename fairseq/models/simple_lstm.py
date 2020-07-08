import torch.nn as nn
from fairseq import utils
from fairseq.models import FairseqEncoder


class SimpleLSTMEncoder(FairseqEncoder):
    def __init__(self, args, dictionary, embed_dim, hidden_dim=128):
        pass

