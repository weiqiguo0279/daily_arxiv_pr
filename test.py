"""
Daily arXiv Agent - 主程序入口

每日追踪 arXiv 最新论文，使用 LLM 进行总结和分析
"""
import sys
import time
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.utils import load_config, load_env, setup_logging, get_date_string, get_github_token
from src.pr import create_github_pr, merge_github_pr
from src.upload import upload_to_github
from src.notifier.email_notifier import EmailNotifier


def main():
    """主函数"""
    # 记录任务开始时间
    start_time = time.time()
    
    # 加载配置
    load_env()
    config = load_config()
    gh_token = get_github_token()
    logger = setup_logging(config)
    
    # 初始化邮件通知器
    notifier = None
    if config.get('scheduler', {}).get('notification', {}).get('enabled', False):
        notifier = EmailNotifier(config['scheduler']['notification']['email'])
    
    logger.info("=" * 60)
    logger.info("Daily arXiv Agent 启动")
    logger.info(f"日期: {get_date_string()}")
    logger.info("=" * 60)
    
    # 任务状态和统计信息
    task_success = False
    stats = {}
    error_msg = None
    
    try:
        # 第一步 - 实现论文爬取 ✅
        logger.info("步骤 1: 爬取 arXiv 论文...")
        from src.crawler.arxiv_fetcher import ArxivFetcher
        fetcher = ArxivFetcher(config)
        
        # 尝试获取论文，如果没找到，逐步放宽条件
        # papers = fetcher.fetch_papers(days_back=210)
        papers = fetcher.fetch_papers(days_back=3)
        if not papers:
            logger.warning("⚠️  过去2天没有找到符合条件的论文...")
            # logger.warning("⚠️  过去2天没有找到符合条件的论文，尝试扩大到7天...")
            # papers = fetcher.fetch_papers(days_back=7)
        
        if papers:
            fetcher.print_paper_summary(papers)
            # 更新统计信息
            stats['papers_count'] = len(papers)
            stats['categories_count'] = len(config.get('arxiv', {}).get('categories', []))
            stats['keywords_count'] = len(config.get('arxiv', {}).get('keywords', []))
        else:
            logger.warning("⚠️  没有找到符合条件的论文")
            logger.info("💡 提示: 可以尝试以下方法：")
            logger.info("   1. 在 config.yaml 中增加 days_back 或 max_results")
            logger.info("   2. 减少或删除关键词过滤（设置 keywords: []）")
            logger.info("   3. 修改类别范围")
            return
        
        # 第二步 - 实现论文总结 ✅
        logger.info("\n步骤 2: 总结论文...")
        from src.summarizer.paper_summarizer import PaperSummarizer
        
        summarized_papers = None
        try:
            summarizer = PaperSummarizer(config)
            summarized_papers = summarizer.summarize_papers(papers)
            
            # 生成每日报告
            logger.info("\n生成每日报告...")
            report = summarizer.generate_daily_report(summarized_papers)
            
            # 保存报告
            report_path = f"data/summaries/report_{get_date_string()}.md"
            from pathlib import Path
            Path(report_path).parent.mkdir(parents=True, exist_ok=True)
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            logger.info(f"📄 每日报告已保存到: {report_path}")
            
            # 更新统计信息
            stats['summaries_count'] = len(summarized_papers)
            
        except Exception as e:
            logger.error(f"论文总结失败: {str(e)}")
            logger.info("继续执行后续步骤...")
            summarized_papers = papers


        # 第三步——创建 GitHub PR ✅
        logger.info("\n步骤 3: 创建 GitHub PR...")
        try:
            if gh_token and config.get('github'):
                logger.info("\n创建 GitHub PR...")
                report_path = f"data/summaries/report_{get_date_string()}.md"
                #create_github_pr(config, gh_token, report_path)
                #merge_github_pr(config, gh_token, report_path)
                upload_to_github(config, gh_token, report_path)
        except Exception as e:
            logger.error(f"创建 PR 失败: {str(e)}")
        
        # 任务执行成功
        task_success = True
        
    except Exception as e:
        logger.error(f"❌ 执行出错: {str(e)}", exc_info=True)
        error_msg = str(e)
        sys.exit(1)
    finally:
        # 计算任务执行时间
        duration = time.time() - start_time
        
        # 发送邮件通知
        if notifier:
            logger.info("\n步骤 4: 发送邮件通知...")
            try:
                notifier.send_notification(
                    success=task_success,
                    stats=stats,
                    error_msg=error_msg,
                    duration=duration
                )
            except Exception as e:
                logger.error(f"邮件通知发送失败: {str(e)}")
        
        # 记录任务完成信息
        if task_success:
            logger.info("=" * 60)
            logger.info("✅ Daily arXiv Agent 任务完成")
            logger.info(f"执行时间: {duration:.2f} 秒")
            logger.info("=" * 60)
        else:
            logger.info("=" * 60)
            logger.info("❌ Daily arXiv Agent 任务失败")
            logger.info(f"执行时间: {duration:.2f} 秒")
            logger.info("=" * 60)


# 在文件末尾添加
if __name__ == "__main__":
    main()