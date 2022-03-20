import numpy as np
import os
import nibabel as nib
import matplotlib.pyplot as plt
import sys


def voxel_matmul(id_):
    with open(os.environ['out_dir']+'/'+id_+'_brain_short_FSL.mat', 'r') as f:
        lines = f.readlines()
    start = 0
    for i, sentence in enumerate(lines):
        if sentence.startswith('#'):
            start = i
            break
    lines = lines[start+1:]

    matrix_str = ''.join(lines)

    elems = matrix_str.split()
    data = np.array(elems)

    transform = np.reshape(data, (4, 4)).astype(np.float32)

    with open(os.environ['out_dir']+'/'+id_+'_brain_short_ACPC.txt', 'r') as f:
        lines = f.readlines()

    AC_li = lines[11].split()
    AC_li.append('1')
    AC_orig = np.reshape(np.array(AC_li), (4, 1)).astype(np.float32)

    return np.rint(transform.dot(AC_orig)).astype(np.int32)


def get_slices(id_, PATH_mri, voxel):
    mri = nib.load(PATH_mri)
    mri_np = np.array(mri.get_fdata())
    AC_z = int(voxel[2])
    BG = mri_np[:, :, AC_z+2, 0]
    CS = mri_np[:, :, AC_z+37, 0]
    plt.imsave(os.environ['out_dir']+'/'+id_+'_BG.png', BG, cmap='gray')
    plt.imsave(os.environ['out_dir']+'/'+id_+'_CS.png', CS, cmap='gray')


args = sys.argv
batch_num = args[1]
print(args[1])
with open(os.environ['batch_info']+'/id_batch_'+batch_num, 'r') as f:
    lines = f.readlines()

for id_ in lines:
    id_ = id_.strip()
    voxel = voxel_matmul(id_)
    voxel_li = voxel.reshape((1, 4)).tolist()
    voxel_li = voxel_li[0][:3]
    voxel_li = [str(elem) for elem in voxel_li]
    get_slices(id_, os.environ['out_dir']+'/' +
               id_+'_brain_short_RAS.nii', voxel_li)
