#!/bin/bash

NUM=$1

for id in $(cat $batch_info/id_batch_$NUM)
do
  filename_t1=$(ls $out_dir/*$id*)
  echo $filename_t1
  echo "mri_binarize ${filename_t1} $out_dir/${id}_brain_mask.nii"
  #mri_binarize ${filename_t1} $out_dir/${id}_brain_mask.nii
done
