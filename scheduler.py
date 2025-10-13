"""
定时调度器

使用 APScheduler 实现每日自动运行
"""
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import pytz
import traceback
import logging

from src.utils import load_config, load_env, setup_logging, load_json
from src.notifier import EmailNotifier
from main import main as run_daily_task


def scheduled_task(logger=None, notifier=None):
    """定时执行的任务"""
    start_time = datetime.now()
    
    print("\n" + "=" * 60)
    print(f"⏰ 定时任务触发 - {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")
    
    if logger:
        logger.info(f"定时任务开始执行 - {start_time}")
    
    try:
        # 执行主任务
        run_daily_task()
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print("\n" + "=" * 60)
        print(f"✅ 任务执行成功！")
        print(f"⏱️  耗时: {duration:.2f} 秒")
        print(f"🕐 完成时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60 + "\n")
        
        if logger:
            logger.info(f"定时任务执行成功，耗时 {duration:.2f} 秒")
        
        # 发送成功通知
        if notifier:
            try:
                # 读取统计信息
                stats = load_json(Path('data/papers/latest.json'))
                stats_info = {
                    'papers_count': len(stats) if stats else 0,
                    'summaries_count': len(load_json(Path('data/summaries/latest.json')) or {}),
                    'categories_count': len(set(p.get('primary_category', '') for p in stats)) if stats else 0,
                    'keywords_count': 50  # 从分析结果获取
                }
                notifier.send_notification(success=True, stats=stats_info, duration=duration)
            except Exception as e:
                logger.warning(f"发送邮件通知失败: {str(e)}")
        
        return True
        
    except Exception as e:
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print("\n" + "=" * 60)
        print(f"❌ 任务执行失败！")
        print(f"⏱️  耗时: {duration:.2f} 秒")
        print(f"🔴 错误: {str(e)}")
        print("=" * 60)
        print("\n详细错误信息:")
        traceback.print_exc()
        print()
        
        if logger:
            logger.error(f"定时任务执行失败: {str(e)}", exc_info=True)
        
        # 发送失败通知
        if notifier:
            try:
                notifier.send_notification(
                    success=False,
                    error_msg=f"{str(e)}\n\n{traceback.format_exc()}",
                    duration=duration
                )
            except Exception as email_error:
                logger.warning(f"发送邮件通知失败: {str(email_error)}")
        
        return False


def main():
    """主函数"""
    # 加载配置
    load_env()
    config = load_config()
    logger = setup_logging(config)
    
    scheduler_config = config.get('scheduler', {})
    
    if not scheduler_config.get('enabled', False):
        logger.warning("定时调度未启用，请在 config.yaml 中设置 scheduler.enabled = true")
        print("\n⚠️  定时调度未启用")
        print("请在 config/config.yaml 中设置:")
        print("  scheduler:")
        print("    enabled: true")
        return
    
    # 获取配置
    run_time = scheduler_config.get('run_time', '09:00')
    timezone = scheduler_config.get('timezone', 'Asia/Shanghai')
    run_on_start = scheduler_config.get('run_on_start', False)
    
    # 解析运行时间
    try:
        hour, minute = map(int, run_time.split(':'))
    except ValueError:
        logger.error(f"无效的运行时间格式: {run_time}，应为 HH:MM 格式")
        print(f"❌ 无效的运行时间格式: {run_time}")
        print("请使用 HH:MM 格式，例如: 09:00")
        return
    
    tz = pytz.timezone(timezone)
    
    # 创建调度器
    scheduler = BlockingScheduler(timezone=tz)
    
    # 添加定时任务
    trigger = CronTrigger(
        hour=hour,
        minute=minute,
        timezone=tz
    )
    
    # 初始化邮件通知器
    notifier = None
    notification_config = scheduler_config.get('notification', {})
    if notification_config.get('enabled', False):
        email_config = notification_config.get('email', {})
        notifier = EmailNotifier(email_config)
        logger.info("邮件通知已启用")
    
    scheduler.add_job(
        scheduled_task,
        trigger=trigger,
        args=[logger, notifier],
        id='daily_arxiv_task',
        name='Daily arXiv Paper Fetching',
        max_instances=1,
        coalesce=True
    )
    
    # 计算下次运行时间
    next_run = datetime.now(tz).replace(hour=hour, minute=minute, second=0, microsecond=0)
    if next_run <= datetime.now(tz):
        from datetime import timedelta
        next_run += timedelta(days=1)
    
    logger.info(f"定时调度器已启动，将在每天 {run_time} ({timezone}) 执行任务")
    print("\n" + "=" * 60)
    print("⏰ Daily arXiv 定时调度器")
    print("=" * 60)
    print(f"📅 执行时间: 每天 {run_time}")
    print(f"🌍 时区: {timezone}")
    print(f"⏭️  下次运行: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔄 启动时立即运行: {'是' if run_on_start else '否'}")
    print("=" * 60)
    print("\n按 Ctrl+C 停止调度器\n")
    
    # 启动时立即运行一次
    if run_on_start:
        logger.info("启动时立即执行任务...")
        print("🚀 启动时立即执行任务...\n")
        scheduled_task(logger, notifier)
    
    try:
        # 启动调度器
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("定时调度器已停止")
        print("\n" + "=" * 60)
        print("👋 定时调度器已停止")
        print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
