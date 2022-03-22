#!/bin/sh

NUM=$1
echo $NUM

for id in $(cat $batch_info/id_batch_${NUM});
do
  sh registration.sh ${id}
  sh acpc_detect.sh ${id}
  sh bias_correction.sh ${id}
#sh bias_correction_flair.sh ${NUM}
# for i in $(ls $batch_info | cut -d '_' -f 3); do qsub -v NUM="${i}" -v prep_pipeline="/srv/scratch/cheba/NiL/shizuka/PhD/preprocessing/" template.pbs; break; done
#for i in $(ls $batch_info | cut -d '_' -f 3); do qsub -v NUM="${i}" template.pbs; break; done
#for i in $(ls $batch_info | cut -d '_' -f 3); do sh run.sh $i; qsub register_$i.pbs; done
done
