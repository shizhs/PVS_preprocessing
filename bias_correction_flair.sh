#!/bin/bash

NUM=$1
echo $NUM
for id in $(cat $batch_info/id_batch_${NUM});
do
  echo $id bias_correction
  mri_binarize --i ${id}_T2toT1_CR_RAS.nii.gz --o ${id}_T2toT1_CR_mask_RAS.nii --min 0.1
  python3 N4_bias_correction.py ${id}_T2toT1_CR_RAS.nii.gz ${id}_intensity_flair.nii ${id}_T2toT1_CR_mask_RAS.nii
done
