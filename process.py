
from win10toast import ToastNotifier
title = 'Message'
content = 'Hello world!'
toaster = ToastNotifier()
dut = 10
toaster.show_toast(f'{title}', f'{content}', duration=dut)