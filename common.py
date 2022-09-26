import datetime
from rasterio.features import bounds as featureBounds

# Endpoint variables
titiler_endpoint = "http://127.0.0.1:8000"
stac_endpoint = "https://earth-search.aws.element84.com/v0/search"

#https://stac-utils.github.io/stac-server/#tocscatalogdefinition
def get_query(x, y):
    geojson_ori = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "properties": {},
          "geometry": {
            "type": "Polygon",
            "coordinates": [
              [
                [
                  -2.83447265625,
                  4.12728532324537
                ],
                [
                  2.120361328125,
                  4.12728532324537
                ],
                [
                  2.120361328125,
                  8.254982704877875
                ],
                [
                  -2.83447265625,
                  8.254982704877875
                ],
                [
                  -2.83447265625,
                  4.12728532324537
                ]
              ]
            ]
          }
        }
      ]
    }
    geojson = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "properties": {},
          "geometry": {
            "type": "Point",
            "coordinates": [
                x,
                y
            ]
          }
        }
      ]
    }

    bounds = featureBounds(geojson)

    start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d").strftime("%Y-%m-%dT00:00:00Z")
    end = datetime.datetime.strptime("2019-12-11", "%Y-%m-%d").strftime("%Y-%m-%dT23:59:59Z")

    # POST body
    query_ori = {
        "collections": ["sentinel-s2-l2a-cogs"],
        "datetime": f"{start}/{end}",
        "query": {
            "eo:cloud_cover": {
                "lt": 3
            },
            "sentinel:data_coverage": {
                "gt": 10
            }
        },
        "intersects": geojson["features"][0]["geometry"],
        "limit": 1000,
        "fields": {
          'include': ['id', 'properties.datetime', 'properties.eo:cloud_cover'],  # This will limit the size of returned body
          'exclude': ['assets', 'links']  # This will limit the size of returned body
        },
        "sortby": [
            {
                "field": "properties.eo:cloud_cover",
                "direction": "desc"
            },
        ]
    }
    query = {
        "collections": ["sentinel-s2-l2a-cogs"],
        "intersects": geojson["features"][0]["geometry"],
        "limit": 1000,
        "fields": {
          'include': ['id', 'properties.datetime'],  # This will limit the size of returned body
          'exclude': ['assets', 'links']  # This will limit the size of returned body
        },
        "sortby": [
            {
                "field": "properties.datetime",
                "direction": "desc"
            },
        ]
    }
    return query

mosaic_file = "mymosaic.json.gz"
