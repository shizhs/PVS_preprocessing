import cv2
import numpy as np
import nibabel as nib
import sys
import os


id_=sys.argv[1]

print(id_,"rescale")
id_ = id_.strip()
mri = nib.load(os.environ['out_dir']+'/'+id_+'_brain.nii')
voxel_data = (np.array(mri.get_fdata())/100).astype(np.int16)
img = nib.Nifti1Image(voxel_data, mri.affine)
nib.save(img, os.environ['out_dir']+'/'+id_+'_brain_rescaled.nii')
