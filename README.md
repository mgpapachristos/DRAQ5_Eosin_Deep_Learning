Code Files Description:

Retrieve_masks.ipynb: Code that extracts annotations from CZI file into a numpy python file.

PANDA_heroimage.ipynb: Code that developes models for transfer learning based on the PANDA dataset. The H&E image crops are converted to synthetic DRAQ5&Eosin and then used for training the models.

Epithelial_Segmentation: Code that develops an epithelial segmentation algorithm based on the data by Bulten et al., and applies it to the DRAQ5&Eosin images, providing corresponding epithelial masks.

H&E_simulation: Code that converts DRAQ5&Eosin CZI images to a synthetic H&E image for expert pathology Gleason annotation.

HealthyvsGleason45_Final.ipynb: Code that trains and develops the High Grade Cancer vs Healthy classification model based on DRAQ5&Eosin data (using transfer learning on pretrained model developed in PANDA_heroimage.ipynb).

HealthyvsGleason3_Final.ipynb: Code that trains and develops the Low Grade Cancer vs Healthy classification model based on DRAQ5&Eosin data (using transfer learning on pretrained model developed in PANDA_heroimage.ipynb).

Gleason3vsGleason45_Final.ipynb: Code that trains and develops the High Grade Cancer vs Low Grade Cancer classification model based on DRAQ5&Eosin data (using transfer learning on pretrained model developed in PANDA_heroimage.ipynb).

CancerSegmentation_Final.ipynb: Code that trains and develops the Cancer Detection segmentation model based on DRAQ5&Eosin data (using transfer learning on pretrained model developed in PANDA_heroimage.ipynb).

Deep_Learning_Results.ipynb: Code that validates the trained models on the External Standardization Dataset which was collected under different microscopy configurations.

background_correctio.py: Code used on Fiji software for performing background correction on the Commercial Tissue MicroArray A data.

background_correction2.py: Code used on Fiji software for performing background correction on the Commercial Tissue MicroArray B data.

background_correction3.py: Code used on Fiji software for performing background correction on the WCB Tissue MicroArray data.

background_correction_stand.py: Code used on Fiji software for performing background correction on the WCB Tissue Slide Cores data.
