#!/bin/sh

cd $out_dir
NUM=$1

for id in $(cat $batch_info/id_batch_$NUM); 
do 
	echo ${id}_brain.nii;
	gunzip -f ${id}_brain_restore.nii.gz	 
done

for id in $(cat $batch_info/id_batch_$NUM);
do
        echo $filename;
	mri_convert -odt short ${id}_brain_restore.nii ${id}_brain_short.nii
        acpcdetect -i ${id}_brain_short.nii
done

