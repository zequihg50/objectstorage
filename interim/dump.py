import os
import dask,xarray
import s3fs

url = 'http://data.meteo.unican.es/tds5/dodsC/interim/daily/interim20_daily.ncml'
ds = xarray.open_dataset(url, chunks='auto')

fs = s3fs.S3FileSystem(
  client_kwargs=dict(endpoint_url='https://cephrgw01.ifca.es:8080'),
  anon=False,
  key='9a1b9204bdc44acd9ca086b5026a5d18',
  secret='88167cd8f1034fecb2f37363f35fd505') 

store = s3fs.S3Map(root='santandermetgroup/interim20_daily', s3=fs, check=False)
ds.to_zarr(store)

ds.close()
