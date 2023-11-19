from collections import defaultdict
import csv
from datetime import datetime
from itertools import islice

from .settings import BASE_DIR, OUTPUT_DIR_NAME, DATE_TIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_count_by_status = defaultdict(int, {'Статус': 'Количество'})

    def process_item(self, item, spider):
        self.pep_count_by_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.pep_count_by_status['Total'] = sum(
            islice(self.pep_count_by_status.values(), 1, None)
        )
        time_str = datetime.now().strftime(DATE_TIME_FORMAT)
        filename = (
            BASE_DIR / OUTPUT_DIR_NAME / f'status_summary_{time_str}.csv'
        )
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(self.pep_count_by_status.items())
