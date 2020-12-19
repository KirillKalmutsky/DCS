import numpy as np
import pandas as pd


if __name__ == '__main__':
    print('\nPrint some numbers:')
    digits = input()
    digits = [int(num) for num in digits.split(' ')]
    print('Median of numbers is:', round(np.median(digits)))
    print('Mean of numbers is:', round(np.mean(digits)))
    df = pd.DataFrame(np.random.randint(1,100,size=(10, 4)), columns=list('ABCD'))
    print('\nAlso show that pandas works well:\n')
    print(df)
    
