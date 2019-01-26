# -*- coding:utf8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler

from apps.szgbidding.jobs.szzfcg import Szzfcg


def start_schedulers():
    sched = BlockingScheduler()
    # TODO : add your job here
    sched.add_job(Szzfcg.run, trigger='cron', second='*/10')

    sched.start()
