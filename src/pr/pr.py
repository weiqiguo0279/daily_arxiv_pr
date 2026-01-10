import requests
import base64
from datetime import datetime
import os

def create_github_pr(config, gh_token, file_path, pr_body=""):
    """Create a PR to GitHub repository with the updated papers"""
    # Read the generated markdown
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # GitHub API endpoints
    repo = f"{config['github']['repo_owner']}/{config['github']['repo_name']}"
    
    # 1. Create a new branch
    branch_name = f"update-papers-{datetime.now().strftime('%Y%m%d-%H%M')}"
    
    # Get latest commit on main branch
    headers = {
        'Authorization': f'token {gh_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Get reference to main branch
    ref_url = f"https://api.github.com/repos/{repo}/git/refs/heads/main"
    response = requests.get(ref_url, headers=headers)
    if response.status_code != 200:
        print(f"Error getting main branch reference: {response.text}")
        return None
    main_sha = response.json()['object']['sha']
    
    # Create new branch
    branch_data = {
        'ref': f'refs/heads/{branch_name}',
        'sha': main_sha
    }
    branch_response = requests.post(f'https://api.github.com/repos/{repo}/git/refs', 
                headers=headers, json=branch_data)
    if branch_response.status_code != 201:
        print(f"Error creating branch: {branch_response.text}")
        return None
    
    # 2. Update file in new branch
    # 优先使用配置中指定的GitHub文件路径
    if config['github'].get('file_path'):
        repo_file_path = config['github']['file_path']
        # 如果配置的是目录，添加文件名
        if repo_file_path.endswith('/'):
            file_name = os.path.basename(file_path)
            repo_file_path = f"{repo_file_path}{file_name}"
    else:
        # 回退到原来的方法
        repo_file_path = file_path.replace(os.path.abspath(os.path.dirname(__file__)) + "\\", "")
    
    file_url = f"https://api.github.com/repos/{repo}/contents/{repo_file_path}"
    response = requests.get(file_url, headers=headers)
    
    file_data = {
        'message': f'Update papers: {datetime.now().strftime("%Y-%m-%d")}',
        'content': base64.b64encode(content.encode('utf-8')).decode('utf-8'),
        'branch': branch_name
    }
    
    if response.status_code == 200:
        file_data['sha'] = response.json()['sha']
    
    update_response = requests.put(file_url, headers=headers, json=file_data)
    if update_response.status_code != 200 and update_response.status_code != 201:
        print(f"Error updating file: {update_response.text}")
        return None
    
    # 3. Create Pull Request
    pr_title = f'Automatic Papers Update: {datetime.now().strftime("%Y-%m-%d")}'
    if not pr_body:
        pr_body = 'This PR contains the latest papers collected from arXiv.'
    
    pr_data = {
        'title': pr_title,
        'body': pr_body,
        'head': branch_name,
        'base': config['github']['branch']
    }
    
    pr_response = requests.post(
        f'https://api.github.com/repos/{repo}/pulls',
        headers=headers,
        json=pr_data
    )
    
    if pr_response.status_code == 201:
        pr_url = pr_response.json()['html_url']
        print(f"PR created successfully: {pr_url}")
        return pr_url
    else:
        print(f"Error creating PR: {pr_response.text}")
        return None