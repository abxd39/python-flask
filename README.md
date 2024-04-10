##启动顺序和命令
进入到当前目录
第一步：激活虚拟环境
windows 
.venv\Scripts\activate
mac 
cd .venv/bin
source active
第二步：执行以下命令
pip3 install flask 
flask --app ./flash_cv_model.py run --host=0.0.0.0

#详情
https://dormousehole.readthedocs.io/en/latest/quickstart.html

windows环境下
创建一个虚拟环境
> mkdir myproject
> cd myproject
> py -3 -m venv .venv

激活虚拟环境
> .venv\Scripts\activate