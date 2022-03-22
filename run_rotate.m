function run_rotate (varargin)
start="starting rotation"
SPM_PATH = varargin{1};
imgList = varargin{2};
addpath(SPM_PATH);
future_spm12_autoReorient(imgList);

finish = "finishing rotation"

