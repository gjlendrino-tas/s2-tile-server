from titiler.core.factory import MultiBandTilerFactory
from titiler.core.dependencies import BandsExprParams
from titiler.mosaic.factory import MosaicTilerFactory

from rio_tiler_pds.sentinel.aws import S2COGReader
from rio_tiler_pds.sentinel.utils import s2_sceneid_parser

from fastapi import FastAPI, Query


def CustomPathParams(
    sceneid: str = Query(..., description="Sentinel 2 Sceneid.")
):
    """Create dataset path from args"""
    assert s2_sceneid_parser(sceneid)  # Makes sure the sceneid is valid
    return sceneid


app = FastAPI()

scene_tiler = MultiBandTilerFactory(reader=S2COGReader, path_dependency=CustomPathParams, router_prefix="scenes")
app.include_router(scene_tiler.router, prefix="/scenes", tags=["scenes"])

mosaic_tiler = MosaicTilerFactory(
    router_prefix="mosaic",
    dataset_reader=S2COGReader,
    layer_dependency=BandsExprParams,
)
app.include_router(mosaic_tiler.router, prefix="/mosaic", tags=["mosaic"])