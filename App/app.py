from h2o_wave import main, app, Q

# from .dashboard_red import show_red_dashboard
# from .dashboard_blue import show_blue_dashboard
# from .dashboard_orange import show_orange_dashboard
# from .dashboard_cyan import show_cyan_dashboard
# from .dashboard_grey import show_grey_dashboard
# from .dashboard_mint import show_mint_dashboard
# from .dashboard_purple import show_purple_dashboard
from .dashboard_01 import show_red_dashboard

@app('/')
async def serve(q: Q):
    route = q.args['#']
    q.page.drop()
    if route == 'dashboards/01':
        await show_red_dashboard(q)