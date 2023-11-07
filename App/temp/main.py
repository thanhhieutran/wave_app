# Import thư viện
from h2o_wave import Q, main, app, ui, site
import sqlite3

# Thông báo trạng thái App
def on_startup():
    print('App started!')

def on_shutdown():
    print('App stopped!')


# Chương trình chính
@app('/home', on_startup=on_startup, on_shutdown=on_shutdown)
async def serve(q: Q):
    site = q.site


    await q.page.save()

