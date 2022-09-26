import httpx
from common import get_query, titiler_endpoint

# Endpoint variables
stac_endpoint = "https://earth-search.aws.element84.com/v0/search"

# Make sure both are up
assert httpx.get(f"{titiler_endpoint}/docs").status_code == 200
assert httpx.get(stac_endpoint).status_code == 200

query = get_query(2.120361328125,
                  8.254982704877875)

# POST Headers
headers = {
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip",
    "Accept": "application/geo+json",
}

data = httpx.post(stac_endpoint, headers=headers, json=query).json()
print("Results context:")
print(data["context"])

sceneid = [f["id"] for f in data["features"]]
print(sceneid[0])
# cloudcover = [f["properties"]["eo:cloud_cover"] for f in data["features"]]
# dates = [f["properties"]["datetime"][0:10] for f in data["features"]]

# Fetch TileJSON
# For this example we use the first `sceneid` returned from the STAC API
# and we sent the Bands to B04,B03,B02 which are red,green,blue
data = httpx.get(f"{titiler_endpoint}/scenes/tilejson.json?sceneid={sceneid[0]}&bands=B04&bands=B03&bands=B02&rescale=0,2000").json()
print(data)
