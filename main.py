import pandas as pd
import numpy as np


data = pd.DataFrame(
    np.random.randint(0, 9999, size=(10000, 4)),
    columns=list('ABCD')
)

# Task 1: rename (для красоты кода воспользуемся Dict Comprehension)
data = data.rename(
    columns={column: f'feature_{column.lower()}' for column in data.columns}
)

# Task 2:
# в задании не указано что делать с этими данными после вычисления
# поэтому пускай выводятся в консоль
# можно так:
print(data.describe([0.95, 0.99]))

# если нужно отдельно, то некоторые значения можно достать вот так:
print(data.std())
print(data.min())
print(data.max())
print(data.mean())
print(data.median())

# Task 3: add column `agg_feature` with average
data['agg_feature'] = data.mean(axis=1)

# Task 4: to csv file
data.to_csv(
    "data.csv",
    sep=";"
)

