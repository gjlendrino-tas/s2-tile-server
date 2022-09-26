uvicorn app:app --reload

docker run --name titiler \
    -p 8000:8000 \
    --env PORT=8000 \
    --env WORKERS_PER_CORE=1 \
    --rm -it ghcr.io/developmentseed/titiler:latest

sceneid[0] = S2A_30NWK_20220401_0_L2A
                 30
                   N
                    WK
                       2022
                            4
                             S2A_30NWK_20220401_0_L2A
aws s3 ls --no-sign-request s3://sentinel-cogs/sentinel-s2-l2a-cogs/30/N/WK/2022/4/S2A_30NWK_20220401_0_L2A/

sceneid[0] = S2A_31PCK_20220915_0_L2A
                 31
                   P
                    CK
                       2022
                            9
                             S2A_31PCK_20220915_0_L2A
aws s3 ls --no-sign-request s3://sentinel-cogs/sentinel-s2-l2a-cogs/31/P/CK/2022/9/S2A_31PCK_20220915_0_L2A/
S2A_31PCK_20220915_0_L2A'

http://oin-hotosm.s3.amazonaws.com/56f9b5a963ebf4bc00074e70/0/56f9c2d42b67227a79b4faec.tif
curl 'http://127.0.0.1:8000/cog/bounds?url=http%3A%2F%2Foin-hotosm.s3.amazonaws.com%2F56f9b5a963ebf4bc00074e70%2F0%2F56f9c2d42b67227a79b4faec.tif' | python3 -m json.tool
{
  "bounds": [
    168.45251984367613,
    -17.557596404471102,
    168.459511241736,
    -17.54927007461763
  ]
}
curl 'http://127.0.0.1:8000/cog/info?url=http%3A%2F%2Foin-hotosm.s3.amazonaws.com%2F56f9b5a963ebf4bc00074e70%2F0%2F56f9c2d42b67227a79b4faec.tif' | python3 -m json.tool
{
  "bounds": [
    168.45251984367613,
    -17.557596404471102,
    168.459511241736,
    -17.54927007461763
  ],
  "minzoom": 15,
  "maxzoom": 22,
  "band_metadata": [
    [
      "1",
      {}
    ],
    [
      "2",
      {}
    ],
    [
      "3",
      {}
    ]
  ],
  "band_descriptions": [
    [
      "1",
      ""
    ],
    [
      "2",
      ""
    ],
    [
      "3",
      ""
    ]
  ],
  "dtype": "uint8",
  "nodata_type": "None",
  "colorinterp": [
    "red",
    "green",
    "blue"
  ],
  "count": 3,
  "overviews": [
    2,
    4,
    8,
    16,
    32,
    64
  ],
  "width": 20179,
  "driver": "GTiff",
  "height": 25201
}

print(mercantile.tile((168.45251984367613 + 168.459511241736)/2.0, (-17.557596404471102 - 17.54927007461763)/2.0, 15))
Tile(x=31717, y=18007, z=15)

curl 'http://127.0.0.1:8000/cog/tiles/15/31717/18007?url=http%3A%2F%2Foin-hotosm.s3.amazonaws.com%2F56f9b5a963ebf4bc00074e70%2F0%2F56f9c2d42b67227a79b4faec.tif' -o i.png

curl 'https://tiles.rdnt.io/bounds?url=http%3A%2F%2Foin-hotosm.s3.amazonaws.com%2F56f9b5a963ebf4bc00074e70%2F0%2F56f9c2d42b67227a79b4faec.tif' \
  -H 'authority: tiles.rdnt.io' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'accept-language: es-419,es;q=0.9,en;q=0.8' \
  -H 'origin: https://www.cogeo.org' \
  -H 'referer: https://www.cogeo.org/' \
  -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  --compressed

curl 'https://tiles.rdnt.io/tiles/17/126871/72027?url=http%3A%2F%2Foin-hotosm.s3.amazonaws.com%2F56f9b5a963ebf4bc00074e70%2F0%2F56f9c2d42b67227a79b4faec.tif' \
  -H 'authority: tiles.rdnt.io' \
  -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
  -H 'accept-language: es-419,es;q=0.9,en;q=0.8' \
  -H 'referer: https://www.cogeo.org/' \
  -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: image' \
  -H 'sec-fetch-mode: no-cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  --compressed

curl 'https://tiles.rdnt.io/tiles/17/126866/72027?url=http%3A%2F%2Foin-hotosm.s3.amazonaws.com%2F56f9b5a963ebf4bc00074e70%2F0%2F56f9c2d42b67227a79b4faec.tif' \
  -H 'authority: tiles.rdnt.io' \
  -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
  -H 'accept-language: es-419,es;q=0.9,en;q=0.8' \
  -H 'referer: https://www.cogeo.org/' \
  -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: image' \
  -H 'sec-fetch-mode: no-cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  --compressed