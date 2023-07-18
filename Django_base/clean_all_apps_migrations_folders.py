"""
使用os及shutil，快速將apps下的所有應用，如果有migrations/及其過往migrate紀錄
一鍵刪除
"""
import os
import shutil

for app in os.listdir('apps'):
    if os.path.exists(f'apps/{app}/migrations/'):
        shutil.rmtree(f'apps/{app}/migrations/')
        print(f'clean migrations: {app}')
