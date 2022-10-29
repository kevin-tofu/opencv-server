import os, sys
print(sys.path)
from fastapi import APIRouter, File, UploadFile, Header, Depends
from fastapi import BackgroundTasks
from typing import List, Optional

from routes.opencv_depends import params_fourpoint_algorithm
from controllers.opencv import opencv_controller
import config
opencv_ctr = opencv_controller(config)


router = APIRouter(prefix="")

@router.post('/4point-algorithm/')
# async def coco_image(file: UploadFile = File(...), \
def fourpoint_algorithm(file: UploadFile = File(...), \
                        bgtask: BackgroundTasks = BackgroundTasks(), \
                        params: dict = Depends(params_fourpoint_algorithm)):
    """
    Args:
        file (UploadFile): Image file to get coco format.\n
        params (dict):  th_conf -> threshold for confidence level to get bbox (0.5-0.99). The bboxes are detected if confidence level is above the value.\n
                        th_nms -> Non-Maximm-Suppression threshold to get bbox (0.5-0.99). The bboxes are detected if NMS-level is above the value.\n
                        resize -> Image will be resized when to detect bbox.\n


    Returns:
        JSONResponse: coco-information on the image. \n
    """

    params['process'] = 'fourpoint-algorithm'
    # return await topdown.draw_info2image(file, **params)
    return opencv_ctr.post_image_fg(file, bgtask, **params)



