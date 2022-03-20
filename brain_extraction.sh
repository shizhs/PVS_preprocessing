#!/bin/bash

NUM=$1

echo $rotate
if [ "$rotate" = "T" ]
then
  source_dir=$out_dir
else
  source_dir=$dataset
fi

for id in $(cat $batch_info/id_batch_$NUM)
do
  filename=$(ls $source_dir/*$id*)
  echo "mri_watershed ${filename} $out_dir/${id}_brain.nii"
  mri_watershed ${filename} $out_dir/${id}_brain.nii
done 
