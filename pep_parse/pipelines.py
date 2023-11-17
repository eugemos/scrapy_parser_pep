from collections import defaultdict
import csv
from datetime import datetime

from .constants import BASE_DIR, OUTPUT_DIR_NAME


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_count_by_status = defaultdict(int)

    def process_item(self, item, spider):
        self.pep_count_by_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        time_str = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        filename = (
            BASE_DIR / OUTPUT_DIR_NAME / f'status_summary_{time_str}.csv'
        )
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(('Статус', 'Количество'))
            csv_writer.writerows(self.pep_count_by_status.items())
            csv_writer.writerow(
                ('Total', sum(self.pep_count_by_status.values()))
            )
