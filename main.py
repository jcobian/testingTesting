import os
import civis
from civis.base import Endpoint
Endpoint._base_url = 'https://api-staging.civisanalytics.com/'
from civis.io import file_to_civis
client = civis.APIClient()
file_name = "output file with awesome things in it"
file_id = file_to_civis("this file is so cool yay", file_name)
job_id = os.environ.get('CIVIS_JOB_ID')
run_id = os.environ.get('CIVIS_RUN_ID')
# create file output
client.scripts.post_python3_runs_outputs(job_id, run_id, 'File', file_id)
# create table output
table_id = 2127734
client.scripts.post_python3_runs_outputs(job_id, run_id, 'Table', table_id)
# create report output
report_id = 26876
client.scripts.post_python3_runs_outputs(job_id, run_id, 'Report', report_id)



