#!/usr/bin/env python3
"""
从论文JSON文件中提取标题并翻译为中文
"""
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

from src.utils import load_config, setup_logging
from src.summarizer.llm_factory import LLMClientFactory


def extract_titles(papers_file: str) -> List[str]:
    """从论文JSON文件中提取标题
    
    Args:
        papers_file: 论文JSON文件路径
        
    Returns:
        标题列表
    """
    with open(papers_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    
    titles = [paper['title'] for paper in papers]
    return titles


def translate_titles(titles: List[str], llm_client: Any) -> List[Dict[str, str]]:
    """将标题列表翻译为中文
    
    Args:
        titles: 英文标题列表
        llm_client: LLM客户端
        
    Returns:
        包含英文标题和中文翻译的字典列表
    """
    results = []
    
    # 翻译提示
    system_prompt = "你是一个专业的学术翻译助手，请将给定的英文论文标题翻译成准确、流畅的中文。保持学术术语的一致性和准确性。"
    user_prompt_template = "请将以下英文论文标题翻译成中文：\n\n{title}"
    
    for title in titles:
        try:
            user_prompt = user_prompt_template.format(title=title)
            translated = llm_client.generate(user_prompt, system_prompt, max_tokens=200)
            results.append({
                'english': title,
                'chinese': translated
            })
            print(f"✓ 翻译完成: {title[:50]}...")
        except Exception as e:
            logging.error(f"翻译失败: {title}: {str(e)}")
            results.append({
                'english': title,
                'chinese': f"翻译失败: {str(e)}"
            })
    
    return results


def main():
    """主函数"""
    # 配置和日志
    config = load_config()
    logger = setup_logging(config)
    
    # 论文文件路径
    papers_file = "data/papers/papers_2026-01-09.json"
    papers_path = Path(papers_file)
    
    if not papers_path.exists():
        logger.error(f"文件不存在: {papers_file}")
        return
    
    # 提取标题
    logger.info(f"从 {papers_file} 提取标题...")
    titles = extract_titles(papers_file)
    logger.info(f"共提取到 {len(titles)} 个标题")
    
    # 初始化LLM客户端
    logger.info("初始化翻译模型...")
    llm_client = LLMClientFactory.create_client(config)
    
    # 翻译标题
    logger.info("开始翻译标题...")
    translations = translate_titles(titles, llm_client)
    
    # 保存结果
    output_file = f"data/papers/translated_titles_{papers_path.stem}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    
    logger.info(f"翻译结果已保存到: {output_file}")
    
    # 打印部分结果
    print("\n翻译结果预览：")
    for i, trans in enumerate(translations[:5]):
        print(f"\n[{i+1}] 英文: {trans['english']}")
        print(f"    中文: {trans['chinese']}")


if __name__ == "__main__":
    main()