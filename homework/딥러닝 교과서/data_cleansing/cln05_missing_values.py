import numpy as np
from numpy import nan as NA
import pandas as pd

sample_data_frame = pd.DataFrame(np.random.rand(10, 4))

# 일부 데이터를 누락 시킵니다.
sample_data_frame.iloc[1, 0] = NA
sample_data_frame.iloc[2, 2] = NA
sample_data_frame.iloc[5:, 3] = NA

print(sample_data_frame)
#           0         1         2         3
# 0  0.325538  0.528041  0.634729  0.755322
# 1       NaN  0.872643  0.507700  0.333328
# 2  0.898748  0.964324       NaN  0.963705
# 3  0.178094  0.517255  0.477483  0.044298
# 4  0.600127  0.147818  0.257669  0.290597
# 5  0.337104  0.331577  0.964237       NaN
# 6  0.769419  0.426936  0.889084       NaN
# 7  0.437038  0.326573  0.232447       NaN
# 8  0.544041  0.231620  0.806235       NaN
# 9  0.923168  0.593689  0.357183       NaN


'''
# 리스트와이즈 삭제 ( listwise delection)
: 데이터가 누락된 행(NaN을 가진 행)을 통째로 지우는 것
'''
print(sample_data_frame.dropna())
#           0         1         2         3
# 0  0.639910  0.590755  0.621288  0.472937
# 3  0.391421  0.175547  0.760504  0.499116
# 4  0.786901  0.154435  0.673574  0.146318

'''
#  페어와이즈 삭제 (pairwise delection)
: 결손이 적은 열만 남기는 것
'''
print(sample_data_frame[[0, 1, 2]].dropna())
#           0         1         2
# 0  0.331314  0.510333  0.296017
# 3  0.573541  0.037328  0.077334
# 4  0.936057  0.501714  0.265234
# 5  0.139453  0.853888  0.589892
# 6  0.514939  0.481430  0.386608
# 7  0.612340  0.307514  0.771854
# 8  0.793148  0.822876  0.622429
# 9  0.945902  0.531969  0.306064


# 문제 
print(sample_data_frame[[0, 2]].dropna())   # 해당 열만 남기고 버림
#           0         2
# 0  0.480231  0.506938
# 3  0.195454  0.602821
# 4  0.584765  0.052796
# 5  0.895301  0.380775
# 6  0.402695  0.852949
# 7  0.738165  0.913220
# 8  0.538291  0.256736
# 9  0.855331  0.178076

