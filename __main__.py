from sys import exit
from argparse import ArgumentParser
from pyperclip import copy, paste
from split import split

argParser = ArgumentParser(
	description = 'Разделение больших файлов на сообщения для discord'
)
argParser.add_argument(
	'file',
	help = 'Входной файл. Если не указан, будет прочитан буфер обмена.',
	nargs = '?'
)
argParser.add_argument(
	'--nitro', '-n',
	help = 'Использовать ограничение, соответствующее наличию nitro',
	action = 'store_true'
)
args = argParser.parse_args()

data = open(args.file).read() if args.file else paste()
if (len(data) == 0):
	print('Ошибка! Отсутствуют вводные данные.')
	exit()

print(
	'Сейчас сообщения полетят в буфер обмена.'
	+ ' Чтобы скопировать очередное сообщение, нажмите enter.',
	end = ''
)

for chunk in split(data, 4000 if args.nitro else 2000):
	input()
	copy(chunk)
	print('Скопировано!', end = '')

print('\nКонец.')