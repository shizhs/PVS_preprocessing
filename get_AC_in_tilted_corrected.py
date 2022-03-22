import numpy as np
import os
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt
def voxel_matmul(id_):
	with open(os.environ['out_dir']+'/'+id_+'_brain_rescaled_FSL.mat', 'r') as f:
	  lines = f.readlines()
	start=0
	for i, sentence in enumerate(lines):
	  if sentence.startswith('#'):
	    start=i
	    break
	lines = lines[start+1:]

	matrix_str = ''.join(lines)

	elems = matrix_str.split()
	data = np.array(elems)

	transform = np.reshape(data, (4, 4)).astype(np.float32)

	with open(os.environ['out_dir']+'/'+id_+'_brain_rescaled_ACPC.txt', 'r') as f:
	  lines = f.readlines()

	AC_li = lines[11].split()
	AC_li.append('1')
	AC_orig = np.reshape(np.array(AC_li), (4, 1)).astype(np.float32)

	return np.rint(transform.dot(AC_orig)).astype(np.int32)

def get_slices(id_, PATH_mri, voxel):
	print(PATH_mri)
	mri = nib.load(PATH_mri)
	mri_np = np.array(mri.get_fdata())
	print(np.shape(mri_np))
	AC_z = int(voxel[2])
	BG = mri_np[:, :, AC_z+2]
	CS = mri_np[:, :, AC_z+37]
	if 'flair' not in PATH_mri:
		plt.imsave(os.environ['out_dir']+'/'+id_+'_BG.png', BG, cmap='gray')
		plt.imsave(os.environ['out_dir']+'/'+id_+'_CS.png', CS, cmap='gray')
	else:
		print("flair : " + PATH_mri)
		plt.imsave(os.environ['out_dir']+'/'+id_+'_BG_flair.png', BG, cmap='gray')
		plt.imsave(os.environ['out_dir']+'/'+id_+'_CS_flair.png', CS, cmap='gray')

visited=set()

ids = []
voxels = []
for filename in sorted(os.listdir(os.environ['out_dir'])):
	if not filename.endswith('_intensity.nii') and not filename.endswith('_intensity_flair.nii'):
		continue
	id_ = filename.split('_')[0]

	voxel = voxel_matmul(id_)
	voxel_li = voxel.reshape((1, 4)).tolist()
	voxel_li = voxel_li[0][:3]
	voxel_li=[str(elem) for elem in voxel_li]
	
	
	if 'T2toT1' not in filename:
		ids.append(id_)
		print(" ".join(voxel_li))	
		voxels.append(" ".join(voxel_li))
	get_slices(id_, os.environ['out_dir']+'/'+filename, voxel_li)
pd.DataFrame(list(zip(ids, voxels)), columns=['SubjID', 'AC_in_MNI']).to_csv(os.environ['out_dir']+'/AC_in_MNI.csv')
