"""
论文总结器

使用 LLM 对 arXiv 论文进行智能总结
"""
import logging
import re
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path
from tqdm import tqdm

from src.utils import save_json, get_date_string, get_data_path
from .llm_factory import LLMClientFactory


class PaperSummarizer:
    """论文总结器"""
    
    # 系统提示词
    SYSTEM_PROMPT = """You are a precise formatting assistant that outputs EXACTLY the requested markdown format. No explanations, no additional text."""
    
    def __init__(self, config: Dict[str, Any]):
        """初始化
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.logger = logging.getLogger('daily_arxiv.summarizer')
        
        # 创建 LLM 客户端
        try:
            self.llm_client = LLMClientFactory.create_client(config)
            self.logger.info(f"使用 LLM: {self.llm_client.get_provider_name()}")
        except Exception as e:
            self.logger.error(f"初始化 LLM 客户端失败: {str(e)}")
            raise
    
    def extract_paper_info(self, paper: Dict[str, Any]) -> Dict[str, Any]:
        """Extract key information from arXiv paper"""
        # 从paper字典中提取arxiv_id
        arxiv_id = paper.get('id', '')
        if arxiv_id.startswith('arXiv:'):
            arxiv_id = arxiv_id[6:]
        
        return {
            'arxiv_id': arxiv_id,
            'title': paper.get('title', ''),
            'authors': paper.get('authors', []),
            'published': paper.get('published', ''),
            'updated': paper.get('updated', ''),
            'summary': paper.get('abstract', ''),
            'pdf_url': paper.get('pdf_url', ''),
            'primary_category': paper.get('primary_category', ''),
            'categories': paper.get('categories', []),
            'doi': paper.get('doi', None)
        }
    
    def format_with_llm(self, paper_info: Dict[str, Any]) -> str:
        """Use LLM API to format paper information into specific markdown format"""
        prompt = f"""Please format the following arXiv paper information in EXACTLY this markdown format:

    - [ReCogDrive: A Reinforced Cognitive Framework for End-to-End Autonomous Driving](https://arxiv.org/abs/2506.08052)
    - Yongkang Li, Kaixin Xiong, Xiangyu Guo, Fang Li, Sixu Yan, Gangwei Xu, Lijun Zhou, Long Chen, Haiyang Sun, Bing Wang, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang
    - Publisher: Huazhong University of Science and Technology, Xiaomi EV
    - Publish Date: 2025.06.09
    - Project Page: [ReCogDrive](https://xiaomi-research.github.io/recogdrive/)
    - Code: [ReCogDrive](https://xiaomi-research.github.io/recogdrive/)
    - Task: Planning
    - Datasets: [NAVSIM](https://github.com/autonomousvision/navsim)
    - Summary：
        - ReCogDrive, a novel reinforced cognitive framework for End-to-End Autonomous Driving, with a Vision-Language Model (VLM) and a Diffusion-based Planner enhanced by Reinforcement Learning.
        - ReCogDrive utilizes a three-stage training paradigm, starting with driving pre-training, followed by imitation learning and GRPO reinforcement learning to enhance the planning capabilities of the Vision-Language-Action (VLA) system.

    Paper Information:
    Title: {paper_info['title']}
    Authors: {', '.join(paper_info['authors'])}
    Abstract: {paper_info['summary']}
    Published Date: {paper_info['published']}
    PDF URL: {paper_info['pdf_url']}
    Categories: {', '.join(paper_info['categories'])}
    DOI: {paper_info.get('doi', 'N/A')}

    Generate a formatted entry in EXACTLY the same markdown format. Follow these rules:

    1. **Start with a dash and paper title as markdown link**:
    - `- [Paper Title](arxiv_url)`

    2. **Each field must be on a new line with 2-space indentation**:
    - `  - Author1, Author2, Author3`
    - `  - Publisher: Institution1, Institution2`
    - `  - Publish Date: YYYY.MM.DD`
    - `  - Project Page: [Link Text](url)` (if available)
    - `  - Code: [Link Text](url)` (if available)
    - `  - Task: Task Type`
    - `  - Datasets: [Dataset Name](url)` (if available)
    - `  - Summary：` (note the Chinese colon)
        - `    - First summary point.`
        - `    - Second summary point.`

    3. **URL rules**:
    - arXiv URL: `https://arxiv.org/abs/arxiv_id`
    - GitHub code: Extract from abstract or infer common patterns
    - Project page: Look for "project page" or "website" in abstract
    - Dataset links: Use standard dataset URLs when possible

    4. **Field extraction guidelines**:
    - **Publisher**: Extract from authors' affiliations mentioned in abstract or infer from title/categories
    - **Publish Date**: Format as YYYY.MM.DD
    - **Project Page**: Look for phrases like "project page", "website", "demo", "homepage"
    - **Code**: Look for "github.com", "code available", "we release code"
    - **Task**: One of: VQA, Planning, Prediction, Perception, Detection, Tracking, Reasoning, Navigation, Control, End-to-End
    - **Datasets**: Extract from mentions of Waymo, nuScenes, KITTI, Argoverse, BDD100K, CARLA, NAVSIM, etc.
    - **Summary**: Create 2-3 bullet points summarizing key contributions

    5. **Important**:
    - Output ONLY the formatted markdown entry
    - Use exactly the same indentation (2 spaces per level)
    - If a field is not mentioned, OMIT IT completely (don't include empty fields)
    - Maintain consistent formatting
    - Summary bullet points should start with `    - ` (4 spaces dash space)

    Return ONLY the formatted markdown entry with no additional text or explanations."""

        try:
            # 生成总结
            summary = self.llm_client.generate(
                prompt=prompt,
                system_prompt=self.SYSTEM_PROMPT
            )
            return summary
        except Exception as e:
            self.logger.error(f"LLM 格式化失败: {str(e)}")
            return self.format_manually(paper_info)

    def format_manually(self, paper_info: Dict[str, Any]) -> str:
        """Fallback manual formatting into markdown format"""
        # Format date
        pub_date = paper_info.get('published', '')
        date_str = "2024.01.01"  # Default date
        try:
            pub_date_dt = datetime.fromisoformat(pub_date)
            date_str = pub_date_dt.strftime("%Y.%m.%d")
        except:
            pass
        
        # ArXiv URL
        arxiv_url = f"https://arxiv.org/abs/{paper_info.get('arxiv_id', '')}"
        
        # Extract information
        summary = paper_info.get('summary', '')
        
        # Try to extract various info
        code_url = self.extract_code_mention(summary)
        dataset_info = self.extract_dataset_info(summary)
        task_type = self.infer_task_type(summary)
        publisher_info = self.extract_publisher_info(paper_info)
        project_page = self.extract_project_page(summary)
        
        # Build markdown
        formatted = f"- [{paper_info.get('title', '')}]({arxiv_url})\n"
        formatted += f"  - {', '.join(paper_info.get('authors', [])[:10])}{' et al.' if len(paper_info.get('authors', [])) > 10 else ''}\n"
        
        if publisher_info:
            formatted += f"  - Publisher: {publisher_info}\n"
        
        formatted += f"  - Publish Date: {date_str}\n"
        
        if project_page:
            formatted += f"  - Project Page: {project_page}\n"
        
        if code_url:
            # Clean up code URL
            if 'github.com' in code_url.lower():
                repo_name = code_url.split('/')[-1] if '/' in code_url else code_url
                formatted += f"  - Code: [{repo_name}]({code_url})\n"
            else:
                formatted += f"  - Code: {code_url}\n"
        
        if task_type:
            formatted += f"  - Task: {task_type}\n"
        
        if dataset_info:
            formatted += f"  - Datasets: {dataset_info}\n"
        
        # Create summary bullet points
        summary_points = self.create_summary_points(summary)
        if summary_points:
            formatted += f"  - Summary：\n"
            for point in summary_points:
                formatted += f"    - {point}\n"
        
        return formatted.rstrip()

    def extract_publisher_info(self, paper_info: Dict[str, Any]) -> str:
        """Extract publisher/institution information"""
        # Try to infer from categories
        category_venue = self.infer_venue(paper_info.get('categories', []))
        if category_venue:
            return category_venue
        
        # Look for common institution patterns in abstract
        abstract = paper_info.get('summary', '')
        institutions = []
        
        # Common institution patterns
        patterns = [
            r'(?:University|Institute|Lab|Center) of [A-Z][a-z]+',
            r'[A-Z][a-z]+ (?:University|Institute)',
            r'[A-Z]+ (?:Research|AI|Tech)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, abstract, re.IGNORECASE)
            institutions.extend(matches)
        
        if institutions:
            return ', '.join(list(dict.fromkeys(institutions))[:3])  # Remove duplicates, keep first 3
        
        return ""

    def extract_project_page(self, text: str) -> str:
        """Extract project page URL"""
        patterns = [
            r'project page\s*:\s*(https?://\S+)',
            r'website\s*:\s*(https?://\S+)',
            r'demo\s*:\s*(https?://\S+)',
            r'homepage\s*:\s*(https?://\S+)',
            r'\(https?://[^)]+\)[^)]*(?:project|demo|website)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                url = match.group(1).strip(')')
                # Get display name from URL
                if 'github.io' in url:
                    project_name = url.split('/')[-1] if url.split('/')[-1] else url.split('/')[-2]
                    return f"[{project_name}]({url})"
                else:
                    return url
        
        return ""

    def extract_dataset_info(self, text: str) -> str:
        """Extract dataset information with links"""
        # Map of common datasets to their URLs
        dataset_urls = {
            'waymo': 'https://waymo.com/open',
            'nuscenes': 'https://www.nuscenes.org',
            'kitti': 'http://www.cvlibs.net/datasets/kitti',
            'argoverse': 'https://www.argoverse.org',
            'bdd100k': 'https://bdd100k.com',
            'carla': 'https://carla.org',
            'navsim': 'https://github.com/autonomousvision/navsim',
            'womd': 'https://waymo.com/open/download'
        }
        
        text_lower = text.lower()
        found_datasets = []
        
        for dataset_name, dataset_url in dataset_urls.items():
            if dataset_name in text_lower:
                found_datasets.append(f"[{dataset_name.upper()}]({dataset_url})")
        
        return ', '.join(found_datasets)

    def create_summary_points(self, abstract: str) -> List[str]:
        """Create bullet points from abstract"""
        # Split into sentences
        sentences = re.split(r'[.!?]+', abstract)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        # Take first 2-3 meaningful sentences
        points = []
        for sentence in sentences[:3]:
            if len(sentence) > 30:  # Ensure meaningful length
                # Clean up the sentence
                sentence = re.sub(r'\s+', ' ', sentence)
                points.append(sentence)
        
        return points
    
    def extract_code_mention(self, text: str) -> str:
        """Extract code repository URL from text"""
        # Look for GitHub URLs
        patterns = [
            r'github\.com/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+',
            r'https?://github\.com/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+',
            r'code available at\s*(https?://\S+)',
            r'we release code at\s*(https?://\S+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                url = match.group(1) if match.groups() else match.group(0)
                if not url.startswith('http'):
                    url = f'https://{url}'
                return url
        
        return ""
    
    def infer_task_type(self, text: str) -> str:
        """Infer task type from abstract"""
        text_lower = text.lower()
        
        # Common task keywords mapping
        task_keywords = {
            'VQA': ['visual question answering', 'vqa'],
            'Planning': ['planning', 'trajectory planning'],
            'Prediction': ['prediction', 'forecasting'],
            'Perception': ['perception', 'visual perception'],
            'Detection': ['detection', 'object detection'],
            'Tracking': ['tracking', 'multi-object tracking'],
            'Reasoning': ['reasoning', 'visual reasoning'],
            'Navigation': ['navigation', 'autonomous navigation'],
            'Control': ['control', 'vehicle control'],
            'End-to-End': ['end-to-end', 'fully autonomous']
        }
        
        for task, keywords in task_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return task
        
        return ""
    
    def infer_venue(self, categories: List[str]) -> str:
        """Infer venue from arXiv categories"""
        # Map of categories to venues
        category_venues = {
            'cs.CV': 'Computer Vision',
            'cs.RO': 'Robotics',
            'cs.AI': 'Artificial Intelligence',
            'cs.LG': 'Machine Learning',
            'cs.NE': 'Neural Networks',
            'eess.SP': 'Signal Processing',
            'eess.IV': 'Image and Video Processing'
        }
        
        for category in categories:
            if category in category_venues:
                return category_venues[category]
        
        return ""

    def summarize_paper(self, paper: Dict[str, Any]) -> Dict[str, Any]:
        """总结单篇论文
        
        Args:
            paper: 论文信息字典
            
        Returns:
            包含总结的论文信息
        """
        try:
            # 提取论文信息
            paper_info = self.extract_paper_info(paper)
            
            # 使用LLM或手动格式化生成总结
            summary = self.format_with_llm(paper_info)
            
            # 添加总结到论文信息
            paper_with_summary = paper.copy()
            paper_with_summary['summary'] = summary
            paper_with_summary['summarized_at'] = datetime.now().isoformat()
            
            return paper_with_summary
            
        except Exception as e:
            self.logger.error(f"总结论文失败 [{paper.get('title', 'Unknown')}]: {str(e)}")
            paper_with_summary = paper.copy()
            paper_with_summary['summary'] = f"总结生成失败: {str(e)}"
            paper_with_summary['summary_error'] = True
            return paper_with_summary
    
    def summarize_papers(self, papers: List[Dict[str, Any]], 
                        show_progress: bool = True) -> List[Dict[str, Any]]:
        """批量总结论文
        
        Args:
            papers: 论文列表
            show_progress: 是否显示进度条
            
        Returns:
            包含总结的论文列表
        """
        if not papers:
            self.logger.warning("没有论文需要总结")
            return []
        
        self.logger.info("=" * 60)
        self.logger.info(f"开始总结 {len(papers)} 篇论文")
        self.logger.info(f"使用模型: {self.llm_client.model}")
        self.logger.info("=" * 60)
        
        summarized_papers = []
        
        # 使用进度条
        iterator = tqdm(papers, desc="总结论文") if show_progress else papers
        
        for i, paper in enumerate(iterator, 1):
            try:
                self.logger.info(f"\n[{i}/{len(papers)}] 正在总结: {paper['title'][:50]}...")
                
                summarized_paper = self.summarize_paper(paper)
                summarized_papers.append(summarized_paper)
                
                if not summarized_paper.get('summary_error'):
                    self.logger.info(f"✓ 总结完成")
                    if not show_progress:
                        # 如果没有进度条，显示总结预览
                        summary_preview = summarized_paper['summary'][:100]
                        self.logger.info(f"  总结预览: {summary_preview}...")
                else:
                    self.logger.warning(f"⚠ 总结失败")
                    
            except Exception as e:
                self.logger.error(f"处理论文时出错: {str(e)}")
                paper_with_error = paper.copy()
                paper_with_error['summary'] = f"处理失败: {str(e)}"
                paper_with_error['summary_error'] = True
                summarized_papers.append(paper_with_error)
        
        # 统计
        success_count = sum(1 for p in summarized_papers if not p.get('summary_error'))
        fail_count = len(summarized_papers) - success_count
        
        self.logger.info("\n" + "=" * 60)
        self.logger.info(f"✅ 总结完成: {success_count} 篇成功, {fail_count} 篇失败")
        self.logger.info("=" * 60)
        
        # 保存结果
        self._save_summaries(summarized_papers)
        
        return summarized_papers
    
    def _save_summaries(self, papers: List[Dict[str, Any]]):
        """保存总结结果
        
        Args:
            papers: 包含总结的论文列表
        """
        if not papers:
            return
        
        # 获取存储路径
        data_path = get_data_path(self.config, 'summaries')
        Path(data_path).mkdir(parents=True, exist_ok=True)
        
        # 按日期保存
        date_str = get_date_string()
        filepath = f"{data_path}/summaries_{date_str}.json"
        
        # 保存数据
        save_json(papers, filepath)
        self.logger.info(f"💾 总结数据已保存到: {filepath}")
        
        # 同时保存一份到 latest.json
        latest_filepath = f"{data_path}/latest.json"
        save_json({
            'date': date_str,
            'count': len(papers),
            'papers': papers,
            'llm_provider': self.llm_client.get_provider_name(),
            'llm_model': self.llm_client.model,
        }, latest_filepath)
        self.logger.info(f"💾 最新总结已保存到: {latest_filepath}")
    
    def generate_daily_report(self, papers: List[Dict[str, Any]]) -> str:
        """生成每日报告
        
        Args:
            papers: 包含总结的论文列表
            
        Returns:
            报告文本
        """
        if not papers:
            return "今日没有论文。"
        
        report_parts = []
        report_parts.append(f"# 📚 每日 arXiv 论文总结(LLM4AD/VLM4AD/VLA4AD)")
        report_parts.append(f"\n**日期**: {get_date_string()}")
        report_parts.append(f"**论文数量**: {len(papers)} 篇")
        report_parts.append(f"**LLM**: {self.llm_client.get_provider_name()} ({self.llm_client.model})")
        report_parts.append("\n---\n")
        
        for i, paper in enumerate(papers, 1):
            
            if 'summary' in paper and not paper.get('summary_error'):
                report_parts.append(f"\n{paper['summary']}")
            else:
                report_parts.append(f"\n**总结**: 暂无")
            
            report_parts.append("\n---\n")
        
        return "\n".join(report_parts)


def main():
    """测试函数"""
    from src.utils import load_config, load_env, setup_logging, load_json
    
    load_env()
    config = load_config()
    logger = setup_logging(config)
    
    # 加载已爬取的论文
    data_path = get_data_path(config, 'papers')
    latest_file = f"{data_path}/latest.json"
    data = load_json(latest_file)
    
    if not data or not data.get('papers'):
        logger.error("没有找到论文数据，请先运行论文爬取")
        return
    
    papers = data['papers'][:3]  # 只测试前3篇
    
    # 创建总结器
    summarizer = PaperSummarizer(config)
    
    # 总结论文
    summarized_papers = summarizer.summarize_papers(papers)
    
    # 生成报告
    report = summarizer.generate_daily_report(summarized_papers)
    print("\n" + report)


if __name__ == "__main__":
    main()