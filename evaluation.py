from pyrouge import Rouge155

r = Rouge155()
# 系统生成的摘要路径
r.system_dir = r"D:\Python\AAAI2018\data\new_summary\SNSR\T1701\setting_2\lamada2=1\alpha=1.1"
# golden 摘要路径
r.model_dir = r"D:\Python\AAAI2018\data\expert_summary\T1701"
# 文件名称
r.system_filename_pattern = "T1701.(\d+).txt"                  # 'some_name.(\d+).txt'
r.model_filename_pattern = "T1701_#ID#.txt"                   # 'some_name.[A-Z].#ID#.txt'
# 评估文件路径
evaluation_file_path = r.system_dir + "\evaluation.txt"
output = r.convert_and_evaluate()
print(output)
with open(evaluation_file_path, 'w', encoding='utf-8') as f:
    f.write(output)
output_dict = r.output_to_dict(output)
print(output_dict)








# 子进程
# import subprocess
# cmd = r"D:\wendang\nlp\AAAI2018\实验代码\数据\评价方法\RELEASE-1.5.5\ROUGE-1.5.5.pl " \
#       r"-e D:\wendang\nlp\AAAI2018\实验代码\数据\评价方法\RELEASE-1.5.5\data " \
#       r"-c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -a " \
#       r"-m C:\Users\LIU951~1\AppData\Local\Temp\tmp9nnzhdju\rouge_conf.xml"
# # cmd = "ping www.baidu.com"
# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
# p.wait()
# result_lines = p.stdout.readlines()
#
# for line in result_lines:
#     print(line)