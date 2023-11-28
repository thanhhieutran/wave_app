from h2o_wave import ui, data, Q
from .common import global_nav
from .synthetic_data import *
from .query_db import *
import time

async def show_dashboard_kiln(q: Q):
    q.page['meta'] = ui.meta_card(box='', layouts=[
        ui.layout(
            breakpoint='xs',
            width='1200px',
            zones=[
                ui.zone('header', size='76px'),
                ui.zone('title'),
                ui.zone('top', direction=ui.ZoneDirection.ROW, size='385px', zones=[
                    ui.zone('top_left'),
                    ui.zone('top_right', zones=[
                        ui.zone('top_right_top', direction=ui.ZoneDirection.ROW, size='1'),
                        ui.zone('top_right_bottom', size='1'),
                    ]),
                ]),
                ui.zone('middle', direction=ui.ZoneDirection.ROW, size='385px'),
                ui.zone('bottom', direction=ui.ZoneDirection.ROW, size='385px', zones=[
                    ui.zone('bottom_left'),
                    ui.zone('bottom_right', size='66%'),
                ]),
                ui.zone('footer', size='80px'),
            ]
        )
    ])

    q.page['header'] = ui.header_card(box='header', title='Thông tin lò nung', subtitle='Kiln Dashboard',
                                      image='https://wave.h2o.ai/img/h2o-logo.svg',
                                      items=[ui.tabs(name='Dashboards', value='#dashboards/kiln', 
                                                     items=global_nav),])
    q.page['title'] = ui.section_card(
        box='title',
        title=next(sample_title),
        subtitle=next(sample_caption),
        items=[
            ui.label(label='Start:'),
            ui.date_picker(name='target_date1', label='', value='2020-12-20'),
            ui.label(label='End:'),
            ui.date_picker(name='target_date2', label='', value='2020-12-25'),
        ],
    )

    value_new = get_kiln_data(tag='Pyrometer', limit=1)
    if value_new is not None:
        q.page['audience_metrics'] = ui.form_card(
            box='top_left',
            title='Test dữ liệu',
            items=[
                ui.text(f'{value_new}'),
            ],
        )



    q.page['footer'] = ui.footer_card(box='footer', caption='(c) 2021 H2O.ai. All rights reserved.')

    await q.page.save()
