#!/bin/bash

ncs=/oceano/gmeteo/WORK/ensembles/downscalingPortal/GCMData/ERA_INTERIM_DM/data

find ${ncs} -type f | python ../publisher/todf.py \
  -v time \
  --drs '.*/G_INTERIM_([^_]+)_([^_]+)_([^_]+)_?([^_]+)?\.nc' \
  --facets level,variable,start,end \
  interim20_daily.pickle
python df.py
python ../publisher/jdataset.py -t template.ncml.j2 -d interim20_daily.ncml interim20_daily.pickle
