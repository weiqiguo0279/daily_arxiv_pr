import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# 导入所需的模块和函数
from src.utils import load_config, load_env, get_github_token
from src.pr.pr import create_github_pr

def main():
    """
    使用现有的pr.py函数将指定的markdown文件上传到GitHub并创建PR
    """
    # 加载环境变量
    load_env()
    
    # 加载配置
    config = load_config()
    
    # 获取GitHub令牌
    gh_token = get_github_token()
    
    if not gh_token:
        print("ERROR: GitHub token not found in environment variables")
        return
    
    # 要上传的文件路径
    file_path = r"C:\Users\Administrator\Desktop\homework\daily-arxiv\data\summaries\report_2025-06-16-2026-01-09.md"
    
    # 调用现有的create_github_pr函数
    pr_url = create_github_pr(
        config=config,
        gh_token=gh_token,
        file_path=file_path,
        pr_body="This PR contains the latest report from arXiv summarizer."
    )
    
    if pr_url:
        print(f"PR created successfully: {pr_url}")
    else:
        print("Failed to create PR")

if __name__ == "__main__":
    main()