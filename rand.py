from Crypt import Crypt
import numpy as np

crypter = Crypt()

for i in range(10):
    i = i + 1
    # print()
    data, key = crypter.encrypt(''.join([crypter.dic[int(np.random.rand()*(len(crypter.dic)-1))] for j in range(i*10)]))
    print(len(data)/(i*10))