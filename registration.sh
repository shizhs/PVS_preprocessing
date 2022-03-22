#!/bin/sh

id=$1

echo $id registration
cost="-cost corratio -omat $out_dir/${id}_T2toT1_CR.mat -out $out_dir/${id}_T2toT1_CR"

t1_filename=$(ls ${dataset_t1}/ | grep ${id})
flair_filename=$(ls ${dataset_flair}/ | grep ${id})
flirt -in ${dataset_flair}/${flair_filename} -ref ${dataset_t1}/${t1_filename} -dof 6 $cost -searchrx -180 180 -searchry -180 180 -searchrz -180 180 

mri_watershed ${dataset_t1}/${t1_filename} $out_dir/${id}_brain.nii
mri_binarize --i $out_dir/${id}_brain.nii --o $out_dir/${id}_brain_mask.nii --min 0.1
mri_mask $out_dir/${id}_T2toT1_CR.nii.gz  $out_dir/${id}_brain_mask.nii $out_dir/${id}_t2_brain.nii


