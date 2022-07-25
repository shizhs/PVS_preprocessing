## Old version of MRIbrain preprocessing
# left the repo for referencing

## Steps 

1. open env.sh file and set the environmental variable accordingly
2. command: source env.sh
3. command: python3 create_batch.py
4. TODO: create a scripts that runs rotation(optional) + mri-watershed + FSL fast for intensity correction + ACPC detection + BG, CS extraction


 flirt -in 0042_brain.nii -ref 0042_brain_short_RAS.nii -out testing.nii -applyxfm -init 0042_brain_short_FSL.mat 
