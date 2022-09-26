from cogeo_mosaic.backends import MosaicBackend
from typing import Dict, List, Sequence, Optional
from pygeos import polygons
import mercantile
from common import get_query, mosaic_file

query = get_query(2.120361328125,
                  8.254982704877875)
# Simple Mosaic
def custom_accessor(feature):
    """Return feature identifier."""
    return feature["id"]

with MosaicBackend(
    "stac+https://earth-search.aws.element84.com/v0/search",
    query,
    minzoom=8,
    maxzoom=15,
    mosaic_options={"accessor": custom_accessor},
) as mosaic:
    # print(mosaic.metadata)
    mosaic_doc = mosaic.mosaic_def.dict(exclude_none=True)

# Optimized Mosaic
def optimized_filter(
    tile: mercantile.Tile,  # noqa
    dataset: Sequence[Dict],
    geoms: Sequence[polygons],
    minimum_tile_cover=None,  # noqa
    tile_cover_sort=False,  # noqa
    maximum_items_per_tile: Optional[int] = None,
) -> List:
    """Optimized filter that keeps only one item per grid ID."""
    gridid: List[str] = []
    selected_dataset: List[Dict] = []

    for item in dataset:
        grid = item["id"].split("_")[1]
        if grid not in gridid:
            gridid.append(grid)
            selected_dataset.append(item)

    dataset = selected_dataset

    indices = list(range(len(dataset)))
    if maximum_items_per_tile:
        indices = indices[:maximum_items_per_tile]

    return [dataset[ind] for ind in indices]


with MosaicBackend(
    "stac+https://earth-search.aws.element84.com/v0/search",
    query,
    minzoom=8,
    maxzoom=14,
    mosaic_options={"accessor": custom_accessor, "asset_filter": optimized_filter},
) as mosaic:
    # print(mosaic.metadata)
    mosaic_doc = mosaic.mosaic_def

# Write the mosaic
with MosaicBackend(mosaic_file, mosaic_def=mosaic_doc) as mosaic:
    mosaic.write(overwrite=True)
