# -*- coding:utf8 -*-
from apscheduler.schedulers.background import BackgroundScheduler

from apps.szgbidding.jobs.szzfcg import Szzfcg


def start_schedulers():
    sched = BackgroundScheduler()
    # TODO : add your job here
    sched.add_job(Szzfcg.run, trigger='cron', second='*/10')

    sched.start()
