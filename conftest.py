import pytest


@pytest.fixture()
def make_stat(start_time):
    name = "stat.txt"
    with open(name, "a", encoding="utf-8") as f:

 f.write(''.join(get_out(f"echo 'время: {start_time}, количество файлов: {count}, размер файла: {size1}\n'; cat /proc/loadavg >> {name}")[0]))







