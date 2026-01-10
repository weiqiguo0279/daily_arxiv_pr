"""
GitHub 文件上传模块
用于将本地文件上传到 GitHub 仓库指定路径
"""
import requests
import base64
from datetime import datetime
import os

def upload_to_github(config, gh_token, file_path):
    """
    将本地文件上传到 GitHub 仓库指定路径
    
    Args:
        config: 配置字典，包含 GitHub 相关配置
        gh_token: GitHub 访问令牌
        file_path: 本地文件路径
        
    Returns:
        bool: 上传是否成功
    """
    # 读取本地文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # GitHub API 配置
    repo = f"{config['github']['repo_owner']}/{config['github']['repo_name']}"
    branch = config['github']['branch']
    
    # 构建 GitHub 上的文件路径
    if config['github'].get('file_path'):
        repo_file_path = config['github']['file_path']
        # 如果配置的是目录，添加文件名
        if repo_file_path.endswith('/'):
            file_name = os.path.basename(file_path)
            repo_file_path = f"{repo_file_path}{file_name}"
    else:
        # 回退到使用本地文件名
        repo_file_path = os.path.basename(file_path)
    
    # 设置请求头
    headers = {
        'Authorization': f'token {gh_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # 检查文件是否存在
    file_url = f"https://api.github.com/repos/{repo}/contents/{repo_file_path}"
    response = requests.get(file_url, headers=headers)
    
    # 准备文件数据
    file_data = {
        'message': f'Upload file: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        'content': base64.b64encode(content.encode('utf-8')).decode('utf-8'),
        'branch': branch
    }
    
    # 如果文件存在，需要提供 sha 值
    if response.status_code == 200:
        file_data['sha'] = response.json()['sha']
    
    # 上传文件
    update_response = requests.put(file_url, headers=headers, json=file_data)
    
    if update_response.status_code in (200, 201):
        print(f"文件上传成功: {repo_file_path}")
        return True
    else:
        print(f"文件上传失败: {update_response.text}")
        return False