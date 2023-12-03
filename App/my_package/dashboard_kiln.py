from h2o_wave import ui, data, Q
from .common import global_nav
from .synthetic_data import *
from .config import *
from .query_db import *
import time
import base64
from PIL import Image

async def show_dashboard_kiln(q: Q):
#----- Setup Layout
    q.page['meta'] = ui.meta_card(box='', layouts=[
        ui.layout(
            breakpoint='xs',
            min_width='800px',
            zones=[
                ui.zone('header', size='76px'),
                ui.zone('title'),
                ui.zone('body', size='1000px', zones=[
                    ui.zone('top', direction=ui.ZoneDirection.ROW, zones=[
                        ui.zone('top_left', direction=ui.ZoneDirection.COLUMN, size='30%'),
                        ui.zone('top_mid', direction=ui.ZoneDirection.COLUMN, size='30%'),
                        ui.zone('top_right', direction=ui.ZoneDirection.COLUMN, size='40%'),
                    ]),
                    # ui.zone('bottom', direction=ui.ZoneDirection.ROW, size='40%', zones=[
                    #     ui.zone('bottom_left', direction=ui.ZoneDirection.COLUMN, size='30%'),
                    #     ui.zone('bottom_mid', direction=ui.ZoneDirection.COLUMN, size='35%'),
                    #     ui.zone('bottom_right', direction=ui.ZoneDirection.COLUMN, size='35%'),
                    # ]),
                ]),
                ui.zone('footer', size='300px'),
            ]
        )
    ])

    q.page['header'] = ui.header_card(box='header', title='Thông tin lò nung', subtitle='Thông tin hoạt động của phân xưởng lò nung clinker',
                                      image=bk_logo,
                                      items=[ui.tabs(name='Dashboards', value='#dashboards/kiln', 
                                                   items=global_nav),])


#----- Body
##---- Thông tin thiết bị
    kiln_devices_list =tag_name_kiln()
    num_devices = len(tag_list)
    q.page['info_device'] = ui.form_card(
        box='top_right',
        title='Theo dõi thiết bị',
        items=[
            ui.dropdown(name='dropdown', label='Dropdown', choices=[
                ui.choice(name=next(kiln_devices_list), label=next(kiln_devices_list)) for i in range(2)
            ]),
            ui.text(f'{kiln_devices_list} and {num_devices} and {tag_list}'),
            ui.text(f'{", ".join(str(next(kiln_devices_list)) for _ in range(2))}'),
        ],
    )
##---- Test display data
    # value_new = get_kiln_data(tag='Pyrometer', limit=1)
    # if value_new is not None:
    #     q.page['audience_metrics'] = ui.form_card(
    #         box='top_left',
    #         title='Test dữ liệu',
    #         items=[
    #             ui.text(f'{value_new}'),
    #         ],
    #     )



#----- Footer
    q.page['footer'] = ui.footer_card(box='footer', caption='''
![estec-logo](https://www.biendongco.vn/resources/img/theme-setting/6-2018/2-logo.png)

Sản phẩm phục vụ Đồ Án Tốt Nghiệp được xây dựng bằng H2O Frame - https://wave.h2o.ai/ \n
Hướng dẫn bởi ESTEC   '''
)

    await q.page.save()