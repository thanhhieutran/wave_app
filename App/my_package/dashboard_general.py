from h2o_wave import ui, data, Q
from .common import global_nav
from .synthetic_data import *
from .config import *
from .query_db import * # import all function to querry db
#-----
import base64
from PIL import Image

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
##---- Prepare Data
    process_image = get_image_from_path('/home/hieutran/Documents/wave_app/App/media/cement_factory.jpg')
    process_image_base64 = process_image[2]

    
##---- Thông tin tổng quan nhà máy
    q.page['layout1'] = ui.form_card(
        box='top_left',
        title='',
        items=[
            ui.inline(direction='row',items=[
                ui.inline(direction='column', items=[
                    ui.text(content='Cối đập', size='xl'),
                    ui.text(content='Cối đập', size='xl'),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Nghiền bột sống', size='xl'),
                    ui.text(content='Nghiền bột sống', size='xl'),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Nghiền than', size='xl'),
                    ui.text(content='Nghiền than', size='xl'),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Lò nung', size='xl'),
                    ui.text(content='Lò nung', size='xl'),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Nghiền xi măng', size='xl'),
                    ui.text(content='Nghiền xi măng', size='xl'),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Đóng bao', size='xl'),
                    ui.text(content='Đóng bao', size='xl'),
                ]),
                
            ]),
            ui.image(title='Image title', path=f'data:image/jpg;base64,{process_image_base64}', width='100%'),
        ],
    )

    # q.page['layout3'] = ui.image_card(
    #     box='bottom',
    #     title='image',
    #     path='App/media/photo.jpg',
    # )

 
#----- Footer
    q.page['footer'] = ui.footer_card(box='footer', caption='''
![estec-logo](https://www.biendongco.vn/resources/img/theme-setting/6-2018/2-logo.png)

Sản phẩm phục vụ Đồ Án Tốt Nghiệp được xây dựng bằng H2O Frame - https://wave.h2o.ai/ \n
Hướng dẫn bởi ESTEC   '''
)

    await q.page.save()
