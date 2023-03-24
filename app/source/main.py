from logs import Logs

# [TAG] Text here..
print(Logs.success_log(tag='SUCCESS', text='This is a log!'))
print(Logs.warning_log(tag='WARNING', text='This is a log!'))
print(Logs.error_log(tag='ERROR', text='This is a log!'))
print(Logs.info_log(tag='INFO', text='This is a log!'))

# Text here..
print(Logs.success_log(text='This is a log!'))
print(Logs.warning_log(text='This is a log!'))
print(Logs.error_log(text='This is a log!'))
print(Logs.info_log(text='This is a log!'))
