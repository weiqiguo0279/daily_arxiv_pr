"""
arXiv 论文爬取器

使用 arxiv API 获取指定领域的最新论文
"""
import arxiv
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any
from pathlib import Path

from src.utils import save_json, get_date_string, get_data_path


class ArxivFetcher:
    """arXiv 论文爬取器"""
    
    def __init__(self, config: Dict[str, Any]):
        """初始化
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.arxiv_config = config.get('arxiv', {})
        self.logger = logging.getLogger('daily_arxiv.fetcher')
        
        # 获取配置
        self.categories = self.arxiv_config.get('categories', ['cs.AI'])
        self.keywords = self.arxiv_config.get('keywords', [])
        self.max_results = self.arxiv_config.get('max_results', 20)
        self.sort_by = self.arxiv_config.get('sort_by', 'submittedDate')
        self.sort_order = self.arxiv_config.get('sort_order', 'descending')
        
    def build_query(self) -> str:
        """构建搜索查询
        
        Returns:
            查询字符串
        """
        # 构建类别查询
        if len(self.categories) == 1:
            category_query = f"cat:{self.categories[0]}"
        else:
            category_parts = [f"cat:{cat}" for cat in self.categories]
            category_query = "(" + " OR ".join(category_parts) + ")"
        
        # 如果有关键词，添加关键词过滤
        if self.keywords:
            # 构建关键词查询（在标题或摘要中搜索）
            keyword_parts = []
            for keyword in self.keywords:
                # 在标题和摘要中搜索关键词
                keyword_parts.append(f'(ti:"{keyword}" OR abs:"{keyword}")')
            keyword_query = "(" + " OR ".join(keyword_parts) + ")"
            
            # 组合类别和关键词
            query = f"{category_query} AND {keyword_query}"
        else:
            query = category_query
        
        self.logger.info(f"构建的查询: {query}")
        return query
    
    def fetch_papers(self, days_back: int = 1) -> List[Dict[str, Any]]:
        """获取论文
        
        Args:
            days_back: 获取过去几天的论文，默认1天
            
        Returns:
            论文列表
        """
        self.logger.info("=" * 60)
        self.logger.info("开始爬取 arXiv 论文")
        self.logger.info(f"类别: {', '.join(self.categories)}")
        if self.keywords:
            self.logger.info(f"关键词: {', '.join(self.keywords)}")
        self.logger.info(f"最大结果数: {self.max_results}")
        self.logger.info("=" * 60)
        
        # 构建查询
        query = self.build_query()
        
        # 设置排序方式
        sort_by_map = {
            'submittedDate': arxiv.SortCriterion.SubmittedDate,
            'relevance': arxiv.SortCriterion.Relevance,
            'lastUpdatedDate': arxiv.SortCriterion.LastUpdatedDate,
        }
        sort_criterion = sort_by_map.get(self.sort_by, arxiv.SortCriterion.SubmittedDate)
        
        sort_order_map = {
            'descending': arxiv.SortOrder.Descending,
            'ascending': arxiv.SortOrder.Ascending,
        }
        sort_order = sort_order_map.get(self.sort_order, arxiv.SortOrder.Descending)
        
        # 创建搜索对象
        search = arxiv.Search(
            query=query,
            max_results=self.max_results,
            sort_by=sort_criterion,
            sort_order=sort_order
        )
        
        # 获取论文
        papers = []
        cutoff_date = datetime.now() - timedelta(days=days_back)
        
        try:
            self.logger.info("正在获取论文...")
            for result in search.results():
                # 检查提交日期
                if result.published.replace(tzinfo=None) < cutoff_date:
                    self.logger.debug(f"论文 {result.title} 发布于 {result.published}，早于截止日期")
                    continue
                
                # 提取论文信息
                paper = self._extract_paper_info(result)
                papers.append(paper)
                
                self.logger.info(f"✓ [{len(papers)}] {paper['title'][:60]}...")
            
            self.logger.info("=" * 60)
            self.logger.info(f"✅ 成功获取 {len(papers)} 篇论文")
            self.logger.info("=" * 60)
            
            # 保存论文数据
            self._save_papers(papers)
            
            return papers
            
        except Exception as e:
            self.logger.error(f"❌ 获取论文失败: {str(e)}", exc_info=True)
            raise
    
    def _extract_paper_info(self, result: arxiv.Result) -> Dict[str, Any]:
        """提取论文信息
        
        Args:
            result: arxiv.Result 对象
            
        Returns:
            论文信息字典
        """
        return {
            'id': result.entry_id.split('/')[-1],  # arXiv ID
            'title': result.title,
            'authors': [author.name for author in result.authors],
            'abstract': result.summary.replace('\n', ' ').strip(),
            'categories': result.categories,
            'primary_category': result.primary_category,
            'published': result.published.isoformat(),
            'updated': result.updated.isoformat(),
            'pdf_url': result.pdf_url,
            'entry_url': result.entry_id,
            'comment': result.comment if hasattr(result, 'comment') else None,
            'journal_ref': result.journal_ref if hasattr(result, 'journal_ref') else None,
            'doi': result.doi if hasattr(result, 'doi') else None,
            'fetched_at': datetime.now().isoformat(),
        }
    
    def _save_papers(self, papers: List[Dict[str, Any]]):
        """保存论文数据
        
        Args:
            papers: 论文列表
        """
        if not papers:
            self.logger.warning("没有论文需要保存")
            return
        
        # 获取存储路径
        data_path = get_data_path(self.config, 'papers')
        Path(data_path).mkdir(parents=True, exist_ok=True)
        
        # 按日期保存
        date_str = get_date_string()
        filepath = f"{data_path}/papers_{date_str}.json"
        
        # 保存数据
        save_json(papers, filepath)
        self.logger.info(f"💾 论文数据已保存到: {filepath}")
        
        # 同时保存一份到 latest.json，方便 Web 服务读取
        latest_filepath = f"{data_path}/latest.json"
        save_json({
            'date': date_str,
            'count': len(papers),
            'papers': papers
        }, latest_filepath)
        self.logger.info(f"💾 最新数据已保存到: {latest_filepath}")
    
    def get_paper_stats(self, papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """获取论文统计信息
        
        Args:
            papers: 论文列表
            
        Returns:
            统计信息字典
        """
        if not papers:
            return {}
        
        # 统计类别分布
        category_counts = {}
        for paper in papers:
            for category in paper['categories']:
                category_counts[category] = category_counts.get(category, 0) + 1
        
        # 统计作者数量
        author_counts = {}
        for paper in papers:
            for author in paper['authors']:
                author_counts[author] = author_counts.get(author, 0) + 1
        
        # 找出高产作者（发表2篇以上）
        prolific_authors = {k: v for k, v in author_counts.items() if v >= 2}
        
        stats = {
            'total_papers': len(papers),
            'category_distribution': category_counts,
            'total_authors': len(author_counts),
            'prolific_authors': prolific_authors,
            'date': get_date_string(),
        }
        
        return stats
    
    def print_paper_summary(self, papers: List[Dict[str, Any]]):
        """打印论文摘要
        
        Args:
            papers: 论文列表
        """
        if not papers:
            self.logger.info("没有找到论文")
            return
        
        self.logger.info("\n" + "=" * 80)
        self.logger.info(f"📚 今日论文摘要 ({len(papers)} 篇)")
        self.logger.info("=" * 80)
        
        for i, paper in enumerate(papers, 1):
            self.logger.info(f"\n[{i}] {paper['title']}")
            self.logger.info(f"    作者: {', '.join(paper['authors'][:3])}" + 
                           (" et al." if len(paper['authors']) > 3 else ""))
            self.logger.info(f"    类别: {', '.join(paper['categories'][:3])}")
            self.logger.info(f"    链接: {paper['pdf_url']}")
            self.logger.info(f"    摘要: {paper['abstract'][:150]}...")
        
        # 显示统计信息
        stats = self.get_paper_stats(papers)
        self.logger.info("\n" + "=" * 80)
        self.logger.info("📊 统计信息")
        self.logger.info("=" * 80)
        self.logger.info(f"总论文数: {stats['total_papers']}")
        self.logger.info(f"总作者数: {stats['total_authors']}")
        
        if stats.get('prolific_authors'):
            self.logger.info("\n高产作者 (2篇以上):")
            for author, count in sorted(stats['prolific_authors'].items(), 
                                       key=lambda x: x[1], reverse=True)[:5]:
                self.logger.info(f"  - {author}: {count} 篇")
        
        self.logger.info("\n类别分布:")
        for category, count in sorted(stats['category_distribution'].items(), 
                                     key=lambda x: x[1], reverse=True):
            self.logger.info(f"  - {category}: {count} 篇")
        
        self.logger.info("=" * 80 + "\n")


def main():
    """测试函数"""
    from src.utils import load_config, load_env, setup_logging
    
    load_env()
    config = load_config()
    logger = setup_logging(config)
    
    fetcher = ArxivFetcher(config)
    papers = fetcher.fetch_papers(days_back=2)  # 获取过去2天的论文
    
    if papers:
        fetcher.print_paper_summary(papers)


if __name__ == "__main__":
    main()
