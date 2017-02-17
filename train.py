import tensorflow as tf
import numpy as np
import math
from model import Seq2Seq
from batherize import batherize
from data.data import load_data_as_array
from data.data import VOCAB_SIZE
from data.data import decode
print tf.__version__

metadata, idx_q, idx_a = load_data_as_array(PATH='data/')
batch = batherize(train_x=idx_q, train_y=idx_a, batch_size=50)

def decoder(seq):
    return decode(seq, metadata['idx2w'])
print "Total number of lines %d and batches %f" % (batch.n, batch.b)
with tf.Session() as session:
    model = Seq2Seq(vocab_size=VOCAB_SIZE)
    session.run(tf.global_variables_initializer())
    model.train(session, batch, decoder=decoder)