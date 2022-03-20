import argparse
import sys
import subprocess
import os

PATH_SPM = '/srv/scratch/cheba/NiL/Software/spm/12'
def write_job(batch_num, command):
  with open(os.environ['out_dir']+'/curr_job_batch_'+batch_num, 'a') as f:
    f.write(command+'\n')

def run_rotate_nii(batch_num, qsub):

  new_dir=os.environ['out_dir']
  os.system('mkdir -p '+new_dir)
  
  mris = []
  with open(os.environ['batch_info']+'/id_batch_'+batch_num, 'r') as f:
    lines = f.readlines()
    for line in lines:
      id_ = line.strip()
      output=subprocess.check_output("ls "+os.environ['dataset'] +"/*"+id_+"*", shell=True).decode('utf-8').strip()
      print('cp '+output+' '+new_dir+'/'+id_+'.nii')
      os.system('cp '+output+' '+new_dir+'/'+id_+'.nii')
      mris.append('\''+new_dir+'/'+id_+'.nii\'')
      
  imgList = ', '.join(mris)
  imgList = '{'+imgList+'}'
  print(imgList)
  print("matlab -nodisplay -nosplash -r \"run_rotate('"+PATH_SPM+"', "+imgList+")\"")
  
  command = "matlab -nodisplay -nosplash -r \"run_rotate('"+PATH_SPM+"', "+imgList+")\""
  if qsub:
    write_job(batch_num, command)
    print(qsub)
  else:
    # os.system("matlab -nodisplay -nosplash -r \"run_rotate({'"+PATH_SPM+"', '"+new_dir+"/"+imgList+"'})\"")
    print(qsub)
  return 

def run_brain_extraction(batch_num, qsub):
  command = "sh "+os.environ['prep_pipeline']+'/brain_extraction.sh '+batch_num
  if qsub:
    #os.system("cp "+os.environ['prep_pipeline']+'/template.pbs '+os.environ['out_dir']+'/curr_job_batch_'+batch_num)
    write_job(batch_num, command)    
  else:
    print('hi')
    #os.system(command)
  return

def run_intensity_correction(batch_num, qsub):
  
  command = "sh "+os.environ['prep_pipeline']+'/intensity_correction.sh '+batch_num
  if qsub:
    write_job(batch_num, command)

  else:
    print('hi')
    #os.system(command)
  return

def run_acpc_detection(batch_num, qsub):
  command = "sh "+os.environ['prep_pipeline']+'/acpc_detection.sh '+batch_num
  if qsub:
   write_job(batch_num, command)
  else:
    print('hi')
    #os.system(command)
  return

def run_get_slices(batch_num, qsub):
  command = "python3 "+os.environ['prep_pipeline']+'/get_slices.py '+batch_num
  if qsub:
   write_job(batch_num, command)
  else:
    print('hi')
    #os.system(command)
  return

parser = argparse.ArgumentParser(description="RUN pre-processing steps (from brain extraction to slices extraction")

parser.add_argument('--rotate', type=str, help="Rotate to MNI space (optional)")

#parser.add_argument('--rotated_dir', type=str, help="define the output dir for rotated MRI")

parser.add_argument('--qsub', default=False, action='store_true', help="Submit to HPC")

parser.add_argument('--all', default=False, action='store_true', help="Run all batches")

parser.add_argument('--batch', type=str, help="Select which batch to process (this argument will be ignored when --all is set")


def check_parser(args):
  if not (args.all or args.batch):
     parser.error('Please indicate batch number or --all if required to process on all the batches')
  #if args.rotate:
  #  if args.rotated_dir is None:
  #   parser.error('Please define output dir for rotated MRI')

if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    check_parser(args) 
    batch_nums = []
    if args.all:
      for filename in os.listdir(os.environ['batch_info']):
        batch_nums.append(filename.split('_')[-1])
    else:
      batch_nums.append(args.batch)
    print('batch_nums', batch_nums)   
    for batch_num in batch_nums:
      os.system("cp "+os.environ['prep_pipeline']+'/template.pbs '+os.environ['out_dir']+'/curr_job_batch_'+batch_num) 
      if args.rotate == 'T':
        run_rotate_nii(batch_num, args.qsub)
          
      run_brain_extraction(batch_num, args.qsub)
#      run_intensity_correction(batch_num, args.qsub)
#      run_acpc_detection(batch_num, args.qsub)
#      run_get_slices(batch_num, args.qsub)
