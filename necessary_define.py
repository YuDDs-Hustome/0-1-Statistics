import numpy as np

def dice():
    random_tx_1  = np.random.randint(1, 7)
    random_tx_2  = np.random.randint(1, 7)
    random_tx_3  = np.random.randint(1, 7)
    random_tx = random_tx_1 + random_tx_2 + random_tx_3

    if 4 <= random_tx <= 10:
        return 0
    elif 11 <= random_tx <= 17:
        return 1
    elif random_tx_1 == random_tx_2 == random_tx_3:
        return -1
