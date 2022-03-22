import SimpleITK as sitk
import sys
import os

if len(sys.argv) < 2:
    print("Usage: N4BiasFieldCorrection inputImage " +
          "outputImage maskImage [shrinkFactor] [numberOfIterations] " +
          "[numberOfFittingLevels]")
    sys.exit(1)

inputImage = sitk.ReadImage(os.environ['out_dir']+'/'+sys.argv[1],sitk.sitkFloat32)
image = inputImage

if len(sys.argv) > 3:
    maskImage = sitk.ReadImage(os.environ['out_dir']+'/'+sys.argv[3],sitk.sitkUInt8)
else:
  print("Usage: N4BiasFieldCorrection inputImage " +
          "outputImage maskImage [shrinkFactor] [numberOfIterations] " +
          "[numberOfFittingLevels]")
  sys.exit(1)

corrector = sitk.N4BiasFieldCorrectionImageFilter()

numberFittingLevels = 4

if len(sys.argv) > 6:
    numberFittingLevels = int(sys.argv[6])

if len(sys.argv) > 5:
    corrector.SetMaximumNumberOfIterations([int(sys.argv[5])]
                                           * numberFittingLevels)

corrected_image = corrector.Execute(image, maskImage)


log_bias_field = corrector.GetLogBiasFieldAsImage(inputImage)

corrected_image_full_resolution = inputImage / sitk.Exp( log_bias_field )

sitk.WriteImage(corrected_image, os.environ['out_dir']+'/'+sys.argv[2])
