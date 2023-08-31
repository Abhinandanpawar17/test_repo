
event= {'key':'s3://distributor-app-dev-bucket/Silver/client=CULLEN/source=TA_Payment/filename=TA_avg_assets/'}
input_file_path = event['key'].split("/")[0] + "/" + event['key'].split("/")[1] + "/" + event['key'].split("/")[2] + "/" + event['key'].split("/")[3] + "/" + event['key'].split("/")[4] + "/" + event['key'].split("/")[5] + "/" + event['key'].split("/")[6] + "/"
sample_input_string=input_file_path

data_client = (sample_input_string.split("/")[4]).split("=")[1]
source = (sample_input_string.split("/")[5]).split("=")[1]
filename = (sample_input_string.split("/")[6]).split("=")[1]
folder_name = ((sample_input_string.split("/")[6])).replace("=", "_")
tbl_prefix = f'tbl_{data_client}_{source}_'
if '#' in tbl_prefix:
    tbl_prefix = 'tbl' + tbl_prefix.split('#')[1]
sample_tbl_name = (f'{tbl_prefix}{folder_name}').lower()
crawler_name = f'{data_client}_{source}_{filename}_Silver_Crawler'


print(crawler_name)
print(sample_tbl_name)

# tbl_prefix = f'tbl_{data_client}_{source}_'
# print(tbl_prefix)
# print(tbl_prefix.split('#'))
# print(tbl_prefix.split('#')[1])
# if '#' in tbl_prefix:
#     tbl_prefix = 'tbl' + tbl_prefix.split('#')[1]
# sample_tbl_name = (f'{tbl_prefix}{folder_name}').lower()
# print(sample_tbl_name)
