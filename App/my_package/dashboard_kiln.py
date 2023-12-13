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
##----- Thông tin OEE
    q.page['OEE'] = ui.tall_gauge_stat_card(
    box=ui.box('top_left', height='160px'),
    title="Hiệu suất tổng thể thiết bị- OEE",
    value='={{intl oee_value style="percent" minimum_fraction_digits=2 maximum_fraction_digits=2}}',
    aux_value="",
    plot_color='$green',
    progress=0.56,
    data=dict(oee_value=0.56),
    )   
##----- Thông tin Thời gian chạy, lỗi
    q.page['running_time'] = ui.form_card(
        box=ui.box('top_left'),
        title="Tình hình chạy máy trong tháng",
        items=[
            ui.inline(direction='row',items=[
                ui.inline(direction='column', justify='center', items=[
                    ui.stats( items=[
                        ui.stat(label='Thời gian hoạt động', value='15 giờ', icon='Bullseye', icon_color='$green'),
                            ]),
                    ui.stats( items=[
                        ui.stat(label='Thời gian dừng lỗi', value='5 giờ', icon='AlarmClock', icon_color='$red'),
                            ]),
                ]),
                ui.inline(direction='column', justify='center', items=[
                    ui.stats( items=[
                        ui.stat(label='Số lần dừng lỗi', value='10 lần', icon='AlertSettings', icon_color='#FFFF00'),
                            ]),
                    ui.stats( items=[
                        ui.stat(label='MTBF', value='50 giờ', icon='CRMServices', icon_color='#FFA500'),
                            ]),
                ]),
            ]),
        ],
    )
##----- Thông tin sản lượng
    q.page['quantity'] = ui.large_stat_card(
        box='top_left',
        title="Sản lượng Clinker ",
        value='={{intl quantity minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        aux_value="Tấn",
        data=dict(quantity=3948),
        caption="Sản lượng Clinker sản xuất trong tháng",
    )
    q.page['productivity'] = ui.large_stat_card(
        box='top_left',
        title="Năng suất sx Clinker ",
        value='={{intl productivity minimum_fraction_digits=2 maximum_fraction_digits=2}}',
        aux_value="Tấn/ giờ",
        data=dict(productivity=251),
        caption="Số tấn clinker được sản xuất trong 1 giờ",
    )
##----- Mức điện năng tiêu hao
    env_nghien_than = env_value('nghien_than')
    env_lo_nung = env_value('lo_nung')
    env_lam_nguoi = env_value('lam_nguoi')
    env_xi_mang = env_value('xi_mang')
    env_month1 = env_value('month')
    env_month2 = env_value('month')
    env_month3 = env_value('month')
    env_month4 = env_value('month')
    q.page['electricity'] = ui.form_card(
        box='top_left',
        title='Mức điện năng tiêu hao',
        items=[
            ui.text('Mức điện năng tiêu hao trung bình từng giờ'),
            ui.visualization(
                plot=ui.plot([
                    ui.mark(type='line',  x='=month', y='=value', color='=areas',
                            color_range='#1640D6'),
                ]),
                data=data(
                    fields=['areas', 'month', 'value'],
                    rows=[('Lò Nung', next(env_month2), next(env_lo_nung)) for i in range(9)],
                    pack=True
                ),
                height='300px',
            )
        ],
    )
##----- Thông tin hoạt động chung
    q.page['general_operation'] = ui.form_card(
        box=ui.box('top_mid'),
        title="Thông tin hoạt động lò",
        items=[
            ui.inline(direction='row',items=[
                ui.inline(direction='column', justify='center', items=[
                    ui.stats( inset=True, items=[
                        ui.stat(label='Tốc độ cấp liệu', value='415.0',caption='Tấn/ giờ', icon_color='#000000'),
                            ]),
                    ui.stats( inset=True, items=[
                        ui.stat(label='Dòng điện gầu tải 1', value='179.55',caption='A', icon_color='#000000'),
                            ]),
                    ui.stats( inset=True, items=[
                        ui.stat(label='Tổng lượng than sử dụng', value='6.23',caption='Tấn/ giờ', icon_color='#000000'),
                            ]),
                    
                ]),
                ui.inline(direction='column', justify='center', items=[
                    ui.stats( inset=True, items=[
                        ui.stat(label='Tốc độ lò', value='15',caption='RPM', icon_color='#000000'),
                            ]),
                    
                    ui.stats( inset=True, items=[
                        ui.stat(label='Dòng điện tải 2', value='170.28',caption='A', icon_color='#000000'),
                            ]),
                    ui.stats( inset=True, items=[
                        ui.stat(label='Tổng lượng dầu sử dụng', value='2.3',caption='Lít / giờ', icon_color='#000000'),
                            ]),
                ]),
            ]),
        ],
    )
##----- Thông tin các thông số quan trọng
    q.page['parameter'] = ui.form_card(
        box=ui.box('top_mid'),
        title="Các thông số quan trọng",
        items=[
            ui.inline(direction='row',items=[
                ui.inline(direction='column', justify='center', items=[
                    ui.stats( inset=True, items=[
                        ui.stat(label='Pyrometer', value='415.0',caption='Tấn/ giờ', icon_color='#000000'),
                            ]),
                    ui.stats( inset=True, items=[
                        ui.stat(label='Oxy cuối lò', value='179.55',caption='A', icon_color='#000000'),
                            ]),
                    ui.stats( inset=True, items=[
                        ui.stat(label='Chỉ số NOx', value='6.23',caption='Tấn/ giờ', icon_color='#000000'),
                            ]),
                    
                ]),
                ui.inline(direction='column', justify='center', items=[
                    ui.stats( inset=True, items=[
                        ui.stat(label='Nhiệt độ đầu lò (BET)', value='15',caption='RPM', icon_color='#000000'),
                            ]),
                    
                    ui.stats( inset=True, items=[
                        ui.stat(label='Oxy đầu lò', value='170.28',caption='A', icon_color='#000000'),
                            ]),
                    ui.stats( inset=True, items=[
                        ui.stat(label='Nhiệt tháp liệu', value='2.3',caption='Lít / giờ', icon_color='#000000'),
                            ]),
                ]),
            ]),
        ],
    )

##----- Chart xu  hướng các chỉ số
    # timeframe_pyrometer = get_timeseries_data('time')
    # pv_pyrometer = get_timeseries_data('pv')
    # q.page['process_value_pyrometer'] = ui.form_card(
    #     box='top_right',
    #     title='Xu hướng chỉ số Pyrometer',
    #     items=[
    #         ui.text('Xu hướng chỉ số Pyromter'),
    #         ui.visualization(
    #             plot=ui.plot([
    #                 ui.mark(type='line',  x='=month', y='=value', color='=areas',
    #                         color_range='#1640D6'),
    #             ]),
    #             data=data(
    #                 fields=['areas', 'month', 'value'],
    #                 rows=[('Nghiền Than', next(timeframe_pyrometer), next(pv_pyrometer)) for i in range(9)], 
    #                 pack=True
    #             ),
    #             height='300px',
    #         )
    #     ],
    # )
    limit_data = 10
    pyrometer_data = get_kiln_data (tag="Pyrometer", limit=limit_data)  
    pyrometer_time_data = [item[-1] for item in pyrometer_data]
    pyrometer_pv_data = [item[2] for item in pyrometer_data]
    pyrometer_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').isoformat(),item[2]) for item in pyrometer_data]
    q.page['process_value_pyrometer'] = ui.plot_card(
    box='top_right',
    title='Line',
    data=data('year value', 20, rows=pyrometer_data_return),
    plot=ui.plot([ui.mark(type='line', x_scale='time', x='=year', y='=value', y_min=0)])
)
    q.page['form'] = ui.form_card(box='top_right', items=[ui.text(f'{pyrometer_data_return}')])





#----- Footer
    q.page['footer'] = ui.footer_card(box='footer', caption='''
![estec-logo](https://www.biendongco.vn/resources/img/theme-setting/6-2018/2-logo.png)

Sản phẩm phục vụ Đồ Án Tốt Nghiệp được xây dựng bằng H2O Frame - https://wave.h2o.ai/ \n
Hướng dẫn bởi ESTEC   '''
)

    await q.page.save()