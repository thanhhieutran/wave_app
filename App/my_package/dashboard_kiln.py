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
                ui.zone('body', size='1400px', zones=[
                    ui.zone('top', direction=ui.ZoneDirection.ROW, zones=[
                        ui.zone('top_left', direction=ui.ZoneDirection.COLUMN, size='20%'),
                        ui.zone('top_mid', direction=ui.ZoneDirection.COLUMN, size='40%'),
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
##----- Tiêu đề chung
    # q.page['title1'] = ui.form_card(box=ui.box('top_left', height='70px'), items=[ui.text_xl('Thông tin tổng hợp')])
    # q.page['title2'] = ui.form_card(box=ui.box('top_mid', height='70px'), items=[ui.text_xl('Danh sách tín hiệu')])
    # q.page['title3'] = ui.form_card(box=ui.box('top_right', height='70px'), items=[ui.text_xl('Các chỉ số quan trọng')])
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
##----- Thông tin hoạt động chung
    q.page['general_operation'] = ui.form_card(
        box=ui.box('top_left'),
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
                        ui.stat(label='Tốc độ lò', value='15',caption='RPM', icon_color='#000000'),
                            ]),
                    
                    ui.stats( inset=True, items=[
                        ui.stat(label='Dòng điện gầu tải 2', value='170.28',caption='A', icon_color='#000000'),
                            ]),
                    ui.stats( inset=True, items=[
                        ui.stat(label='Tổng lượng dầu sử dụng', value='2.3',caption='Lít / giờ', icon_color='#000000'),
                            ]),
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
    # Khai báo các giá trị sẽ hiển thị
    limit_data = 20

    ### Pyrometer
    pyrometer_data = get_kiln_data (tag="Pyrometer", limit=limit_data)  
    # pyrometer_time_data = [item[-1] for item in pyrometer_data]
    pyrometer_pv_data = [item[2] for item in pyrometer_data]
    pyrometer_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(), item[2]) for item in pyrometer_data]

    
    q.page['process_value_pyrometer'] = ui.plot_card(
        box='top_mid',
        title='Xu hướng nhiệt độ khu vực vùng đốt (Pyrometer)',
        data=data('TimeStamp Value', 20, rows=pyrometer_data_return),
        plot=ui.plot([ui.mark(
            type='line', 
            x_scale='time-category', 
            x='={{intl TimeStamp type="time" month="numeric" day="numeric" hour="numeric" minute="numeric" hourCycle="h24" }}',
            y='=Value', 
            y_min=min(pyrometer_pv_data)-10, 
            x_title='Time', 
            y_title='Process Value',
            color='=red',
                )
            ])
    )

    ### Oxy (Ga01, Ga02)
    Ga01_data = get_kiln_data (tag="Ga01", limit=limit_data)  
    Ga02_data = get_kiln_data (tag="Ga02", limit=limit_data)  
    # pyrometer_time_data = [item[-1] for item in pyrometer_data]
    Ga01_pv_data = [item[2] for item in Ga01_data]
    Ga01_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(),"Ga01", item[2]) for item in Ga01_data]
    Ga02_pv_data = [item[2] for item in Ga02_data]
    Ga02_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(),"Ga02", item[2]) for item in Ga02_data]
    Oxy_data = []
    for x in range(len(Ga01_data_return)):
        Oxy_data.append(Ga01_data_return[x])
        Oxy_data.append(Ga02_data_return[x])
    
    q.page['process_value_oxy'] = ui.plot_card(
        box='top_mid',
        title='Xu hướng chỉ số Oxi trong lò',
        data=data('TimeStamp Type Value', 40, rows=Oxy_data),
        plot=ui.plot([ui.mark(
            type='line', 
            x_scale='time-category', 
            x='={{intl TimeStamp type="time" month="numeric" day="numeric" hour="numeric" minute="numeric" hourCycle="h24" }}',
            y='=Value', 
            y_min=(min(Ga01_pv_data)+min(Ga02_pv_data))/2-10, 
            x_title='Time', 
            y_title='Process Value',
            color='=Type',
                )
            ])
    )

    ### BET - Nhiệt độ đầu lò
    BET_data = get_kiln_data (tag="BET", limit=limit_data)  
    # pyrometer_time_data = [item[-1] for item in pyrometer_data]
    BET_pv_data = [item[2] for item in BET_data]
    BET_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(), item[2]) for item in BET_data]

    
    q.page['process_value_BET'] = ui.plot_card(
        box='top_mid',
        title='Xu hướng nhiệt độ đầu lò (BET)',
        data=data('TimeStamp Value', 20, rows=BET_data_return),
        plot=ui.plot([ui.mark(
            type='line', 
            x_scale='time-category', 
            x='={{intl TimeStamp type="time" month="numeric" day="numeric" hour="numeric" minute="numeric" hourCycle="h24" }}',
            y='=Value', 
            y_min=min(BET_pv_data)-10, 
            x_title='Time', 
            y_title='Process Value',
            color='=green',
                )
            ])
    )

    ### NOx - Chỉ số Nitơ
    NOx_data = get_kiln_data (tag="NOx", limit=limit_data)  
    # pyrometer_time_data = [item[-1] for item in pyrometer_data]
    NOx_pv_data = [item[2] for item in NOx_data]
    NOx_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(), item[2]) for item in NOx_data]

    
    q.page['process_value_NOx'] = ui.plot_card(
        box='top_mid',
        title='Xu hướng nồng độ NOx ',
        data=data('TimeStamp Value', 20, rows=NOx_data_return),
        plot=ui.plot([ui.mark(
            type='line', 
            x_scale='time-category', 
            x='={{intl TimeStamp type="time" month="numeric" day="numeric" hour="numeric" minute="numeric" hourCycle="h24" }}',
            y='=Value', 
            y_min=min(NOx_pv_data)-10, 
            x_title='Time', 
            y_title='Process Value',
            color='#E36414',
                )
            ])
    )


    

##---- Tra cứu thông tin đối tượng
    list_tags = get_distinct_data(table="kiln", name_col="tag")
    # q.page['form'] = ui.form_card(box='top_right', items=[ui.text(f'{list_tags}')])
    tag_view = "Pyrometer"
    if q.args.show_inputs:
        if q.args.dropdown == None:
            tag_view = "Pyrometer"
        else:
            tag_view =q.args.dropdown
        # d = repair_info[tag_view]
        q.page['drop_down_page'] = ui.form_card(
        box=ui.box('top_right', height='100px'),
        title='Danh sách tín hiệu',
        items=[
            ui.inline(inset=True, items=[
                ui.dropdown(name='dropdown', value=q.args.dropdown, choices=[
                    ui.choice(name=f'{tag[0]}', label=tag[0]) for tag in list_tags
                        ]),
                ui.button(name='show_form', label='Xem', primary=True),
            ]),
        ])
        


        tag_view_data = get_kiln_data (tag=f"{tag_view}", limit=limit_data)
        tag_view_pv_data = [item[2] for item in tag_view_data]
        tag_view_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(), item[2]) for item in tag_view_data]
        q.page['display_chart'] = ui.plot_card(
            box='top_right',
            title=f'Xu hướng chỉ số {tag_view} ',
            data=data('TimeStamp Value', 20, rows=tag_view_data_return),
            animate=True,
            plot=ui.plot([ui.mark(
                type='line', 
                x_scale='time-category', 
                x='={{intl TimeStamp type="time" month="numeric" day="numeric" hour="numeric" minute="numeric" hourCycle="h24" }}',
                y='=Value', 
                y_min=min(tag_view_pv_data)-10, 
                x_title='Time', 
                y_title='Process Value',
                color='#557C55',
                
                    )
                ])
        )

        q.page['summary_data'] = ui.form_card(
        box=ui.box('top_right', height='100px'),
        title="",
        items=[
            ui.inline(direction='row',items=[
                ui.stats( inset=True, items=[
                        ui.stat(label='Giá trị tối đa', value=f"{max(tag_view_pv_data)}",caption='', icon_color='#000000'),
                            ]),
                ui.stats( inset=True, items=[
                        ui.stat(label='Giá trị trung bình', value=f"{sum(tag_view_pv_data) / len(tag_view_pv_data)}",caption='', icon_color='#000000'),
                            ]),
                ui.stats( inset=True, items=[
                        ui.stat(label='Giá trị tối thiểu', value=f"{min(tag_view_pv_data)}",caption='', icon_color='#000000'),
                            ]),
                
                
                ]),
            ],
        )

        
    else:
        if q.args.dropdown == None:
            tag_view = "Pyrometer"
        else:
            tag_view =q.args.dropdown
        # d = repair_info[tag_view]
        q.page['drop_down_page'] = ui.form_card(
        box=ui.box('top_right', height='100px'),
        title='Danh sách tín hiệu',
        items=[
            ui.inline(inset=True, align='center', items=[
                ui.dropdown(name='dropdown', value=q.args.dropdown, choices=[
                    ui.choice(name=f'{tag[0]}', label=tag[0]) for tag in list_tags
                        ]),
                ui.button(name='show_inputs', label='Xem', primary=True),
            ]),
        ])
        

        tag_view_data = get_kiln_data (tag=f"{tag_view}", limit=limit_data)
        tag_view_pv_data = [item[2] for item in tag_view_data]
        tag_view_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(), item[2]) for item in tag_view_data]
        q.page['display_chart'] = ui.plot_card(
            box='top_right',
            title=f'Xu hướng chỉ số {tag_view} ',
            animate=True,
            data=data('TimeStamp Value', 20, rows=tag_view_data_return),
            plot=ui.plot([ui.mark(
                type='line', 
                x_scale='time-category', 
                x='={{intl TimeStamp type="time" month="numeric" day="numeric" hour="numeric" minute="numeric" hourCycle="h24" }}',
                y='=Value', 
                y_min=min(tag_view_pv_data)-10, 
                # y_min=0, 
                x_title='Time', 
                y_title='Process Value',
                color='#FF6C22',
                    )
                ])
        )

        q.page['summary_data'] = ui.form_card(
        box=ui.box('top_right', height='100px'),
        title="",
        items=[
            ui.inline(direction='row',items=[
                ui.stats( inset=True, items=[
                        ui.stat(label='Giá trị tối đa', value=f"{max(tag_view_pv_data)}",caption='', icon_color='#000000'),
                            ]),
                ui.stats( inset=True, items=[
                        ui.stat(label='Giá trị trung bình', value=f"{sum(tag_view_pv_data) / len(tag_view_pv_data)}",caption='', icon_color='#000000'),
                            ]),
                ui.stats( inset=True, items=[
                        ui.stat(label='Giá trị tối thiểu', value=f"{min(tag_view_pv_data)}",caption='', icon_color='#000000'),
                            ]),
                
                
                ]),
            ],
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
        box=ui.box('top_right', height='500px'),
        title='Mức điện năng tiêu hao',
        items=[
            ui.text('Mức điện năng tiêu hao trung bình từng giờ'),
            ui.visualization(
                plot=ui.plot([
                    ui.mark(type='line',  x='=month', y='=value', color='=tag_view',
                            color_range='#1640D6'),
                ]),
                data=data(
                    fields=['tag_view', 'month', 'value'],
                    rows=[('Lò Nung', next(env_month2), next(env_lo_nung)) for i in range(9)],
                    pack=True
                ),
                height='300px',
            )
        ],
    )

    ### Kiln_Amp - Tải lò
    Kiln_Amp_data = get_kiln_data (tag="Kiln_Amp", limit=limit_data)
    Kiln_Amp_pv_data = [item[2] for item in Kiln_Amp_data]
    Kiln_Amp_data_return = [(datetime.datetime.strptime(item[-1], '%Y-%m-%d %H:%M:%S:%f').replace(microsecond=0).isoformat(), item[2]) for item in Kiln_Amp_data]

    
    q.page['process_value_Kiln_Amp'] = ui.plot_card(
        box='top_right',
        title='Xu hướng chỉ số tải lò ',
        data=data('TimeStamp Value', 20, rows=Kiln_Amp_data_return),
        plot=ui.plot([ui.mark(
            type='line', 
            x_scale='time-category', 
            x='={{intl TimeStamp type="time" month="numeric" day="numeric" hour="numeric" minute="numeric" hourCycle="h24" }}',
            y='=Value', 
            y_min=min(Kiln_Amp_pv_data)-10, 
            x_title='Time', 
            y_title='Process Value',
            color='#3081D0',
                )
            ])
    )

#----- Footer
    q.page['footer'] = ui.footer_card(box='footer', caption='''
![estec-logo](https://www.biendongco.vn/resources/img/theme-setting/6-2018/2-logo.png)

Sản phẩm phục vụ Đồ Án Tốt Nghiệp được xây dựng bằng H2O Frame - https://wave.h2o.ai/ \n
Hướng dẫn bởi ESTEC   '''
)

    await q.page.save()