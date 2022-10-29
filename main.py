
import os
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from routes import fourpoints
import config
from logconf import mylogger
logger = mylogger(__name__)

app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_credentials=False,
    allow_methods=["*"],
    # allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

serverinfo = {
    "version": config.VERSION,
    "author": config.AUTHOR
}

@app.get("/")
def root():
    return serverinfo

app.include_router(fourpoints.router)

if __name__ == "__main__":

    import uvicorn
    import argparse
    # from mediapipe_if import test_mediapipe
    
    # test_mediapipe.test()

    # myport = os.environ['APP_PORT']
    # os.getenv('NEW_KEY')
    myport = config.APP_PORT
    logger.info(f"myport: {myport}")
    logger.info(f"config.PATH_DATA : {config.PATH_DATA}")
    logger.info(f"config.SLEEP_SEC_REMOVE: {config.SLEEP_SEC_REMOVE}")
    logger.info(f"config.SLEEP_SEC_REMOVE_RESPONSE: {config.SLEEP_SEC_REMOVE_RESPONSE}")

    parser = argparse.ArgumentParser()
    # parser.add_argument('--gpu', '-G', type=int, default='-1', help='gpu number')
    parser.add_argument('--port', '-P', type=int, default=myport, help='port for http server')
    args = parser.parse_args()

    uvicorn.run('main:app', host="0.0.0.0", port=args.port)