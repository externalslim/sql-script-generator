import os
import pandas as pnd
import codecs
from operations.query_generator import QueryGenerator

query_generate = QueryGenerator

### delete file if exist
if os.path.exists('script.sql'):
    os.remove('script.sql')

### read excel ###
data_frame = pnd.read_excel('~/Desktop/data_gscript.xlsx')

### generate query ###
script_array = query_generate.script_generate(data_frame)

with open('script.sql', 'w') as f:
    f.write('\n------------------------------------------------------------------------\n'.join(script_array))