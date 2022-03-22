#!/bin/bash

id=$1
echo $id bias_correction
mri_binarize --i $out_dir/${id}_brain_rescaled_RAS.nii --o $out_dir/${id}_brain_mask_RAS.nii --min 0.1
python3 N4_bias_correction.py ${id}_brain_rescaled_RAS.nii ${id}_intensity.nii ${id}_brain_mask_RAS.nii

mri_binarize --i $out_dir/${id}_T2toT1_CR_RAS.nii.gz --o $out_dir/${id}_T2toT1_CR_mask_RAS.nii --min 0.1
python3 N4_bias_correction.py ${id}_T2toT1_CR_RAS.nii.gz ${id}_intensity_flair.nii ${id}_T2toT1_CR_mask_RAS.nii
