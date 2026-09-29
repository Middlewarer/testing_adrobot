import time
import requests


def check_speed(url):
    total_time = 0
    total_bytes = 0

    for i in range(10):
        start = time.time()

        response = requests.get(url)
        response.raise_for_status()

        request_time = time.time() - start
        size = len(response.content)

        total_time += request_time
        total_bytes += size

        print(f"Запрос {i + 1}: {request_time} сек")

    average_time = total_time / 10
    total_mb = total_bytes / 1024 / 1024
    speed = total_mb / total_time

    print()
    print(f"Среднее время запроса: {average_time} сек")
    print(f"Скачано: {total_mb:.2f} MB")
    print(f"Скорость: {speed:.2f} MB/s")


check_speed("https://yandex.ru/images/search?text=%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B5+%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5&img_url=https%3A%2F%2Fwallpaper.forfun.com%2Ffetch%2F2e%2F2e730eaa57a36a7ab529e3898f96d372.jpeg&pos=1&rpt=simage&stype=image&lr=7&parent-reqid=1790662997909330-15485742163132875859-balancer-l7leveler-kubr-yp-klg-8-BAL&source=serp")