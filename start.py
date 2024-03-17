import os

# python 环境配置

# os.system('mkdir -p /home/xlab-app-center')  # 首先创建一个工作目录
os.system('apt-get install git-lfs')
os.chdir('/home/xlab-app-center')  # 这个目录应该是浦语官方的存放应用的目录，不需要你自己创建
os.system('mkdir -p download/xtuner019')
os.chdir('download/xtuner019')
os.system('git clone -b v0.1.9 https://gitee.com/Internlm/xtuner')
os.chdir('xtuner')
os.system("pip install -e '.[all]'")

# 加载微调后的模型
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel
# 创建model存放路径
os.chdir('/home/xlab-app-center')
os.system('mkdir a_simple_chat_model')
os.system('echo "--/home/xlab-app-center--"')
os.system('pwd')
os.system('ls')
os.system('echo "--/home/xlab-app-center--"')
# 开始加载模型
base_path = '/home/xlab-app-center/a_simple_chat_model'
os.system('apt install git')
os.system('apt install git-lfs')
os.system(f'git clone https://code.openxlab.org.cn/Xuanyuan/a_simple_chat_model.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
os.system('echo "--/home/xlab-app-center/a_simple_chat_model--"')
os.system('pwd')
os.system('ls')
os.system('echo "--/home/xlab-app-center/a_simple_chat_model--"')

tokenizer = AutoTokenizer.from_pretrained(base_path,trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_path,trust_remote_code=True, torch_dtype=torch.float16).cuda()
os.system('echo "----模型加载完成--"')
# # OpenXLab 环境配置
# # 导入基座模型
# from openxlab.model import download
# download(model_repo='OpenLMLab/InternLM-chat-7b', output='/home/xlab-app-center/model/InternLM-chat-7b')
# # 导入 Adapter
# download(model_repo='WanpengXu/Personal_Assistant_Adapter', output='/home/xlab-app-center/model/pa_hf_weights')
#
# os.system('echo "模型和Adapter融合开始"')
# # Merge
# os.system('''
# xtuner convert merge \
#     '/home/xlab-app-center/model/InternLM-chat-7b' \
#     '/home/xlab-app-center/model/pa_hf_weights' \
#     '/home/xlab-app-center/model/pa_merged' \
#     --max-shard-size 2GB
# ''')
#
# # run
# os.chdir('/home/xlab-app-center/model/')
# os.system('echo "----"')
# os.system('pwd')
# os.system('ls')
# os.system('echo "----"')
#
# os.chdir('/home/xlab-app-center/model/pa_merged')
# os.system('echo "----"')
# os.system('pwd')
# os.system('ls')
# os.system('echo "----"')
#
# # os.system('cd /home/xlab-app-center/code/InternLM_Lite')
# os.chdir('/home/xlab-app-center/code/InternLM_Lite')
# os.system('echo "----"')
# os.system('pwd')
# os.system('ls')
# os.system('echo "----"')
# 执行前端界面
os.chdir('/home/xlab-app-center') # 回到目界面
os.system('streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')
