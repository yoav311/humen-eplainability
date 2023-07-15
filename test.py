from utils.align_data import pre_process_images
from scripts.run_pti import run_PTI

image_path = 'C:/personal/Technion/pain-GAN/PTI/docs/'
# pre_process_images(image_path)

run_PTI(run_name='test1', use_wandb=False, use_multi_id_training=False)
