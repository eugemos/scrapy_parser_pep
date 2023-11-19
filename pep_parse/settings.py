from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR_NAME = 'results'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{OUTPUT_DIR_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

DATE_TIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
