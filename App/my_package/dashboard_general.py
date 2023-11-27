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
                    ui.zone('top', direction=ui.ZoneDirection.ROW, size='60%', zones=[
                        ui.zone('top_left', direction=ui.ZoneDirection.COLUMN, size='70%'),
                        ui.zone('top_right'),
                    ]),
                    ui.zone('bottom', direction=ui.ZoneDirection.ROW, size='40%', zones=[
                        ui.zone('bottom_left', direction=ui.ZoneDirection.COLUMN, size='30%'),
                        ui.zone('bottom_mid', direction=ui.ZoneDirection.COLUMN, size='35%'),
                        ui.zone('bottom_right', direction=ui.ZoneDirection.COLUMN, size='35%'),
                    ]),
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
    process_image = get_image_from_path('cement_factory.jpg')
    process_image_base64 = process_image[2]


##---- Thông tin tổng quan nhà máy
    q.page['Thong_tin_chung'] = ui.form_card(
        box='top_left',
        title='',
        items=[
            ui.inline(direction='row',items=[
                ui.inline(direction='column', justify='center', items=[
                    ui.text(content='Khu Vực Cối đập', size='xl'),
                    ui.stats(inset=True, items=[
                        ui.stat(label='OEE', value='100%', icon='Bullseye', icon_color='$green'),
                            ]),
                    ui.stats(inset=True, items=[
                        ui.stat(label='Trạng thái', value='Chạy', icon='ProcessingRun', icon_color='$orange'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Sản lượng', value='2,110,270 Tấn', icon='ReportDocument', icon_color='$red'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Năng suất', value='927 T/h', icon='Diagnostic', icon_color='$brown'),
                            ]),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Nghiền bột sống', size='xl'),
                    ui.stats(inset=True, items=[
                        ui.stat(label='OEE', value='100%', icon='Bullseye', icon_color='$green'),
                            ]),
                    ui.stats(inset=True, items=[
                        ui.stat(label='Trạng thái', value='Chạy', icon='ProcessingRun', icon_color='$orange'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Sản lượng', value='2,110,270 Tấn', icon='ReportDocument', icon_color='$red'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Năng suất', value='927 T/h', icon='Diagnostic', icon_color='$brown'),
                            ]),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Nghiền than', size='xl'),
                    ui.stats(inset=True, items=[
                        ui.stat(label='OEE', value='100%', icon='Bullseye', icon_color='$green'),
                            ]),
                    ui.stats(inset=True, items=[
                        ui.stat(label='Trạng thái', value='Chạy', icon='ProcessingRun', icon_color='$orange'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Sản lượng', value='2,110,270 Tấn', icon='ReportDocument', icon_color='$red'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Năng suất', value='927 T/h', icon='Diagnostic', icon_color='$brown'),
                            ]),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Lò nung', size='xl'),
                    ui.stats(inset=True, items=[
                        ui.stat(label='OEE', value='100%', icon='Bullseye', icon_color='$green'),
                            ]),
                    ui.stats(inset=True, items=[
                        ui.stat(label='Trạng thái', value='Chạy', icon='ProcessingRun', icon_color='$orange'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Sản lượng', value='2,110,270 Tấn', icon='ReportDocument', icon_color='$red'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Năng suất', value='927 T/h', icon='Diagnostic', icon_color='$brown'),
                            ]),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Nghiền xi măng', size='xl'),
                    ui.stats(inset=True, items=[
                        ui.stat(label='OEE', value='100%', icon='Bullseye', icon_color='$green'),
                            ]),
                    ui.stats(inset=True, items=[
                        ui.stat(label='Trạng thái', value='Chạy', icon='ProcessingRun', icon_color='$orange'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Sản lượng', value='2,110,270 Tấn', icon='ReportDocument', icon_color='$red'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Năng suất', value='927 T/h', icon='Diagnostic', icon_color='$brown'),
                            ]),
                ]),
                ui.inline(direction='column', items=[
                    ui.text(content='Đóng bao', size='xl'),
                    ui.stats(inset=True, items=[
                        ui.stat(label='OEE', value='100%', icon='Bullseye', icon_color='$green'),
                            ]),
                    ui.stats(inset=True, items=[
                        ui.stat(label='Trạng thái', value='Chạy', icon='ProcessingRun', icon_color='$orange'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Sản lượng', value='2,110,270 Tấn', icon='ReportDocument', icon_color='$red'),
                            ]),
                    ui.stats(inset=True,items=[
                        ui.stat(label='Năng suất', value='927 T/h', icon='Diagnostic', icon_color='$brown'),
                            ]),
                ]),
                
            ]),
            ui.image(title='Image title', path=f'data:image/jpg;base64,{process_image_base64}', width='100%'),
        ],
    )
    
    san_luong_xm = generate_random_walk(1000, 8000)
    chung_loai_xm = generate_type_cement(type_cement)
    q.page['Thong_tin_san_pham'] = ui.plot_card(
        box='top_right',
        title='Sản lượng các chủng loại xi măng sản xuất',
        data=data(
            fields=['Chung_Loai', 'Khoi_Luong'],
            rows=[(next(chung_loai_xm), next(san_luong_xm)) for i in range(9)],
            pack=True,
        ),
        plot=ui.plot([
            ui.mark(type='interval', x='=Khoi_Luong', y='=Chung_Loai', y_min=0, color='$red')
        ])
    )
##---- Mục tiêu sản xuất
    q.page['transactions'] = ui.stat_table_card(
        box=ui.box('bottom_left', order=1, size=2),
        title='Mục tiêu sản xuất',
        subtitle=next(sample_caption),
        columns=[next(sample_term) for i in range(4)],
        items=[
            ui.stat_table_item(
                label=next(sample_title),
                caption=f'{random.randint(1, 5)} hours ago',
                values=[next(sample_percent), next(sample_amount), next(sample_dollars)],
                icon=next(sample_icon), icon_color='$mint') for i in range(6)
        ]
    )
##---- Thông tin sửa chữa
    if q.args.show_inputs:
        if q.args.dropdown == None:
            areas = 0
        else:
            areas =int(q.args.dropdown)-1
        d = repair_info[areas]
        q.page['drop_down_page'] = ui.form_card(
        box='bottom_mid',
        title='Khu vực sửa chữa',
        items=[
            ui.inline(inset=True, items=[
                ui.dropdown(name='dropdown', value='1', choices=[
                    ui.choice('1','Cối Đập'),
                    ui.choice('2','Nghiền Bột Sống'),
                    ui.choice('3','Lò Nung'),
                    ui.choice('4', 'Nghiền Xi Măng'),
                    ui.choice('5', 'Máy Đóng Bao'),
                    ui.choice('6', 'Xuất Xi Măng Rời'),
                        ]),
                ui.button(name='show_form', label='Xem', primary=True),
            ]),
        ])
        q.page['Pie_chart'] = ui.wide_pie_stat_card(
            box='bottom_mid',
            title=f'Tỷ lệ sửa chữa khu vực {d[0]}',
            pies=[
                ui.pie(label='Sửa chữa cơ', value=f'{d[3]}', fraction=d[5], color=f'{d[7]}', aux_value=f'{d[1]}'),
                ui.pie(label='Sửa chữa điện', value=f'{d[4]}', fraction=d[6], color=f'{d[8]}', aux_value=f'{d[2]}'),
            ]
        )
    else:
        if q.args.dropdown == None:
            areas = 0
        else:
            areas =int(q.args.dropdown)-1
        d = repair_info[areas]
        q.page['drop_down_page'] = ui.form_card(
        box='bottom_mid',
        title='Khu vực sửa chữa',
        items=[
            ui.inline(inset=True, align='center', items=[
                ui.dropdown(name='dropdown', value='1', choices=[
                    ui.choice('1','Cối Đập'),
                    ui.choice('2','Nghiền Bột Sống'),
                    ui.choice('3','Lò Nung'),
                    ui.choice('4', 'Nghiền Xi Măng'),
                    ui.choice('5', 'Máy Đóng Bao'),
                    ui.choice('6', 'Xuất Xi Măng Rời'),
                        ]),
                ui.button(name='show_inputs', label='Xem', primary=True),
            ]),
        ])
        q.page['Pie_chart'] = ui.wide_pie_stat_card(
            box='bottom_mid',
            title=f'Tỷ lệ sửa chữa khu vực {d[0]}',
            pies=[
                ui.pie(label='Sửa chữa cơ', value=f'{d[3]}', fraction=d[5], color=f'{d[7]}', aux_value=f'{d[1]}'),
                ui.pie(label='Sửa chữa điện', value=f'{d[4]}', fraction=d[6], color=f'{d[8]}', aux_value=f'{d[2]}'),
            ]
        )

##---- Thông tin môi trường
    env_nghien_than = env_value('nghien_than')
    env_lo_nung = env_value('lo_nung')
    env_lam_nguoi = env_value('lam_nguoi')
    env_xi_mang = env_value('xi_mang')
    env_month1 = env_value('month')
    env_month2 = env_value('month')
    env_month3 = env_value('month')
    env_month4 = env_value('month')
    q.page['moi_truong'] = ui.form_card(
        box='bottom_right',
        title='Thông tin môi trường',
        items=[
            ui.text('Nồng độ bụi tại các khu vực'),
            ui.visualization(
                plot=ui.plot([
                    ui.mark(type='line',  x='=month', y='=valuse', color='=areas',
                            color_range='#1640D6 #BE3144 #FF6C22 #557C55'),
                ]),
                data=data(
                    fields=['areas', 'month', 'valuse'],
                    rows=[('Nghiền Than', next(env_month1), next(env_nghien_than)) for i in range(9)] + 
                        [('Lò Nung', next(env_month2), next(env_lo_nung)) for i in range(9)] +
                        [('Làm Nguội', next(env_month3), next(env_lam_nguoi)) for i in range(9)] +
                        [('Xi Măng', next(env_month4), next(env_xi_mang)) for i in range(9)],
                    pack=True
                ),
                height='300px',
            )
        ],
    )
#----- Footer
    q.page['footer'] = ui.footer_card(box='footer', caption='''
![estec-logo](https://www.biendongco.vn/resources/img/theme-setting/6-2018/2-logo.png)

Sản phẩm phục vụ Đồ Án Tốt Nghiệp được xây dựng bằng H2O Frame - https://wave.h2o.ai/ \n
Hướng dẫn bởi ESTEC   '''
)

    await q.page.save()
