import pandas as pd
import numpy as np


data = pd.DataFrame(
    np.random.randint(0, 9999, size=(10000, 4)),
    columns=list('ABCD')
)

# Task 1: rename
data = data.rename(
    columns={column: f'feature_{column.lower()}' for column in data.columns}
)

# Task 2:
# стандартное отклонение,
# экстремумы (мин, макс),
# среднее и медиану,
# 95, 99 перцентили
print(data.mean())
print(data.median())

# Task 3: add column `agg_feature` with average

# Task 4: to csv file
data.to_csv(
    "data.csv",
    sep=";"
)

print(data.head())
