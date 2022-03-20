#!/bin/bash

NUM=$1
for id in $(cat $batch_info/id_batch_$NUM)
do
  echo $out_dir/${id}_brain.nii
  fast -n 1 -B -v 2 $out_dir/${id}_brain.nii
done 
