
from fastapi.testclient import TestClient
import config

path_data = config.PATH_DATA
name_video = 'test_video.mp4'
name_image = 'test_image.jpg'
name_image_wrong = 'test_image.jp'


from main import app
testclient = TestClient(app)


def test_read_main():
    res = testclient.get('')
    assert res.status_code == 200
    assert type(res.json()) == dict



# def test_video():

#     with open(f"{path_data}{name_video}", "rb") as _file:
#         res = testclient.post("/coco-video/?test=1", files={"file": (f"_{name_video}", _file, "image/jpeg")})
#     assert res.status_code == 200
#     assert type(res.json()) == dict

#     with open(f"{path_data}{name_video}", "rb") as _file:
#         res = testclient.post("/coco-video/?test=1", files={"file": (name_image_wrong, _file, "image/jpeg")})
#     assert res.status_code == 400

#     with open(f"{path_data}{name_image}", "rb") as _file:
#         res = testclient.post("/detection-image/?test=1", \
#                               files={"file": (f"_{name_image}", _file, "video/mp4")})
#     assert res.status_code == 200
#     assert type(res.json()) == dict

#     data = res.json()
#     print('data : ', data)
#     header = {'idData': data['idData'], "accept": "application/json"}
#     res = testclient.get(f'/video/?test=1', headers=header)
#     assert res.status_code == 200

#     res = testclient.get(f"/video/?test=1")
#     assert res.status_code == 400


# def test_image():

#     with open(f"{path_data}{name_image}", "rb") as _file:
#         res = testclient.post("/coco-image/?test=1", files={"file": (f"_{name_image}", _file, "image/jpeg")})
#     assert res.status_code == 200
#     assert type(res.json()) == dict

#     with open(f"{path_data}{name_image}", "rb") as _file:
#         res = testclient.post("/coco-image/?test=1", files={"file": (name_image_wrong, _file, "image/jpeg")})
#     assert res.status_code == 400

#     with open(f"{path_data}{name_image}", "rb") as _file:
#         res = testclient.post("/detection-image/?test=1", \
#                               files={"file": (f"_{name_image}", _file, "video/mp4")})
#     assert res.status_code == 200
#     assert type(res.json()) == dict

#     print(f'/detection-image/?fname={name_image}?test=1')

#     data = res.json()
#     print('data : ', data)
#     header = {'idData': data['idData'], "accept": "application/json"}
#     res = testclient.get(f'/image/?test=1', headers=header)
#     assert res.status_code == 200

#     res = testclient.get(f"/image/?test=1")
#     assert res.status_code == 400


if __name__ == "__main__":

    test_read_main()

#     test_image()
    
#     test_video()
    