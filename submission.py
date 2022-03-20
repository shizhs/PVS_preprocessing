import os

MAS_DIR="/srv/scratch/cheba/NiL/shizuka/PhD/Data/MAS_w2/MAS_t1_w2_rotated/"
for filename in sorted(os.listdir(MAS_DIR)):
  if filename.startswith('id_batch'):
    num = int(filename.split('_')[-1])
    os.system('qsub -v NUM='+"{:02d}".format(num)+" T1.pbs")
    print('qsub -v NUM='+"{:02d}".format(num)+" T1.pbs")
