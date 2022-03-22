#!/bin/sh

id=$1

python3 rescale.py ${id}

echo $id acpc
cd $out_dir
acpcdetect -i ${id}_brain_rescaled.nii
cd $prep_pipeline
cost="-cost corratio -omat $out_dir/${id}_T2toT1_CR_RAS.mat -out $out_dir/${id}_T2toT1_CR_RAS"
flirt -in $out_dir/${id}_t2_brain.nii -ref $out_dir/${id}_brain_rescaled_RAS.nii -dof 6 $cost -searchrx -180 180 -searchry -180 180 -searchrz -180 180 

#for i in $(ls $batch_info | cut -d '_' -f 3); do sh run.sh $i; qsub register_$i.pbs; done
