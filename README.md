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
r.system_dir是系统生成的摘要的保存路径
r.model_dir是golden摘要路径
然后设置文件名称，可以使用正则表达式，例如：
some_name.(\d+).txt
```
summarization.1.txt
summarization.2.txt
summarization.3.txt
...
```
some_name.[A-Z].#ID#.txt
```
summarization.A.1.txt
summarization.A.2.txt
summarization.B.1.txt
...
```
evaluation_file_path是生成的评估结果文档路径。
全部设置好之后，最后调用r.convert_and_evaluate()即可。


#注意
pyrouge本质上是对ROUGE-1.5.5的使用进行封装，在得到cmd命令后，启动子程序时，如果出现 %1 不是win32程序 错误，需要修改pyrouge中调用子程序部分，添加参数shell=True，以shell形式运行。
