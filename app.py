from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.combining import OrTrigger 
from apscheduler.triggers.cron import CronTrigger
from utils import getMarketPrice, TICKERS

job_defaults = {
    'coalesce': True,
    'max_instances': 3
}
scheduler = BlockingScheduler(timezone='Asia/Singapore')

# GMT-5 > 09:30am - 4pm
# GMT+8 > 10:30pm - 5am
trigger = OrTrigger([
    CronTrigger(second='*/10', hour='0-4'),
    CronTrigger(second='*/10', minute='30-59', hour='22-23')
])

scheduler.add_job(getMarketPrice, trigger=trigger, args=[TICKERS], name='getMarketPrice')
scheduler.start()