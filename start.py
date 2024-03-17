import os

# python 环境配置
os.chdir('/home/xlab-app-center')  # 这个目录应该是浦语官方的存放应用的目录，不需要你自己创建
os.system('mkdir -p download/xtuner019')
os.chdir('download/xtuner019')
os.system('git clone -b v0.1.9 https://gitee.com/Internlm/xtuner')
os.chdir('xtuner')
os.system("pip install -e '.[all]'")
# 创建model存放路径
os.chdir('/home/xlab-app-center')
os.system('mkdir -p model/a_simple_chat_model')  
# 加载微调后的模型
from openxlab.model import download
download(model_repo='Xuanyuan/a_simple_chat_model', output='/home/xlab-app-center/model/a_simple_chat_model')
# 查看模型库目录
os.chdir('/home/xlab-app-center/model')
os.system('echo "--/home/xlab-app-center/model--"')
os.system('pwd')
os.system('ls')
os.system('echo "--/home/xlab-app-center/model--"')
# 查看a_simple_chat_model目录
os.chdir('/home/xlab-app-center/model/a_simple_chat_model')
os.system('echo "--/home/xlab-app-center/model/a_simple_chat_model--"')
os.system('pwd')
os.system('ls')
os.system('echo "--/home/xlab-app-center/model/a_simple_chat_model--"')
# 执行前端界面
os.chdir('/home/xlab-app-center') # 回到目界面
os.system('streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')
