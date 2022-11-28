import transforms3d
import numpy as np
q = [-0.286054, 0.412, 0.534103, 0.680561]
t = np.array([[1.51834], [-1.12397], [3.17068]])
R = transforms3d.quaternions.quat2mat(q)
Rt = np.matrix.transpose(R)
minusRt = -Rt
P = np.matmul(minusRt,t)

# print('\nQuaternion:\n{}\n \
#     \nTranslation:\n{}\n \
#     \nRotation_matrix from Quaternion:\n{}\n \
#     \nTranspose of Rotation Matrix:\n{}\n \
#     \nTranslation:\n{}\n \
#     \nPosition:\n{}\n'.format(q, t, R, Rt, t, P))
print("5: " + str(P))
