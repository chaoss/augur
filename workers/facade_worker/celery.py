from celery import celery

facadeApp = celery('Facade Worker',
                    broker='redis://localhost:6379/0'
                    include=['facade_worker.tasks'])


if __name__ == '__main__':
    facadeApp.start()