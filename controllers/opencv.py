from mediaBase.controllers.media_base import media_prod
# from controllers.functions import 
from logconf import mylogger

from cv2_interface.fourpoint_algorithm import cv2_fourpoint_algorithm
logger = mylogger(__name__)
print('__name__', __name__)

class opencv_controller(media_prod):
    def __init__(self, _config):

        super().__init__(_config)

    def draw_info2image(self, fpath: str, fpath_dst: str, **kwargs):
        
        if kwargs['process'] == 'fourpoint-algorithm':
            return cv2_fourpoint_algorithm(fpath, fpath_dst, **kwargs)
        else:
            return None

    # def draw_info2video(self, fpath: str, fpath_dst: str, **kwargs):
        
    #     if kwargs['process'] == 'conversion-video':
    #         return convert_video(fpath, fpath_dst, **kwargs)
    #     else:
    #         return None

    