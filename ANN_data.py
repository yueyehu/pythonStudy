from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import SoftmaxLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

net = buildNetwork(36, 50, 7, hiddenclass=TanhLayer,bias=True)
ds = SupervisedDataSet(36, 7)
file_read = open("data_bin.txt")
for line in file_read:
    line = line.strip().split()
    input_d = tuple([int(c) for c in line[1]])
    output_d = tuple([int(c) for c in line[0]])
    ds.addSample(input_d,output_d)
trainer = BackpropTrainer(net, ds)
trainer.trainUntilConvergence()

test = [int(c) for c in '100001101000010011000110001000100011']
print sum([(1 if c > 0.5 else 0)*2**(6-i) for i,c in enumerate(net.activate(test))])
