# ROUGE_evaluation
使用pyrouge进行ROUGE评估

使用pyrouge进行ROUGE评估，需要提前安装ROUGE。

# 使用方法
```python
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
```
