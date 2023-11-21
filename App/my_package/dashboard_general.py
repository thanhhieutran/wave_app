from h2o_wave import ui, data, Q
from .common import global_nav
from .synthetic_data import *
from .config import *


async def show_general_dashboard(q: Q):
#----- Setup Layout
    q.page['meta'] = ui.meta_card(box='', layouts=[
        ui.layout(
            breakpoint='xs',
            min_width='800px',
            zones=[
                ui.zone('header', size='76px'),
                ui.zone('title'),
                ui.zone('body', size='1000px', zones=[
                    ui.zone('top', direction=ui.ZoneDirection.ROW, size='50%', zones=[
                        ui.zone('top_left', direction=ui.ZoneDirection.ROW, size='75%'),
                        ui.zone('top_right'),
                    ]),
                    ui.zone('bottom', direction=ui.ZoneDirection.ROW, size='50%'),
                ]),
                ui.zone('footer', size='300px'),
            ]
        )
    ])
#----- Header
    q.page['header'] = ui.header_card(box='header', title='ỨNG DỤNG SỐ HÓA NHÀ MÁY', subtitle='Tình hình hoạt động của nhà máy',
                                      image= bk_logo,
                                      items=[ui.tabs(name='Dashboards', value='#dashboards/general',  
                                                     items=global_nav),])

#----- Body

    q.page['layout1'] = ui.form_card(
        box='top_left',
        title='top_left',
        items=[
        ],
    )
    q.page['layout2'] = ui.form_card(
        box='middle',
        title='middle',
        items=[
        ],
    )
    q.page['layout3'] = ui.form_card(
        box='bottom',
        title='bottom',
        items=[
        ],
    )

 
#----- Footer
    q.page['footer'] = ui.footer_card(box='footer', caption='''
![estec-logo](https://www.biendongco.vn/resources/img/theme-setting/6-2018/2-logo.png)

Sản phẩm phục vụ Đồ Án Tốt Nghiệp được xây dựng bằng H2O Frame - https://wave.h2o.ai/ \n
Hướng dẫn bởi ESTEC   '''
)

    await q.page.save()
