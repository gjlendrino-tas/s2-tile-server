import pathlib
import httpx
from common import titiler_endpoint, mosaic_file

mosaic = str(pathlib.Path(mosaic_file).absolute())
data = httpx.get(f"{titiler_endpoint}/mosaic/tilejson.json?url=file:///{mosaic}&bands=B01&rescale=0,1000").json()
print(data)
