import numpy as np


if __name__ == '__main__':
    print('Print some numbers:')
    digits = input()
    digits = [int(num) for num in digits.split(' ')]
    print('Median of numbers is:', np.median(digits))
    print('Mean of numbers is:', np.mean(digits))
