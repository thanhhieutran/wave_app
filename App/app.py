from h2o_wave import main, app, Q

from my_package.dashboard_kiln import show_dashboard_kiln
from my_package.dashboard_general import show_general_dashboard
#---------------------------------
from my_package.dashboard_red import show_red_dashboard
from my_package.dashboard_blue import show_blue_dashboard
from my_package.dashboard_orange import show_orange_dashboard
from my_package.dashboard_cyan import show_cyan_dashboard
from my_package.dashboard_grey import show_grey_dashboard
from my_package.dashboard_mint import show_mint_dashboard
from my_package.dashboard_purple import show_purple_dashboard


@app('/')
async def serve(q: Q):
    route = q.args['#'] # Trang mặc định: http://localhost:10101/#
    q.page.drop()
    if route == 'dashboards/kiln': # Trang : http://localhost:10101/#dashboards/kiln
        await show_dashboard_kiln(q)
    elif route == 'dashboards/general':
        await show_general_dashboard(q)
#-------------------------------------------------------
    elif route == 'dashboards/red':
        await show_red_dashboard(q)    
    elif route == 'dashboards/blue':
        await show_blue_dashboard(q)
    elif route == 'dashboards/orange':
        await show_orange_dashboard(q)
    elif route == 'dashboards/cyan':
        await show_cyan_dashboard(q)
    elif route == 'dashboards/grey':
        await show_grey_dashboard(q)
    elif route == 'dashboards/mint':
        await show_mint_dashboard(q)
    elif route == 'dashboards/purple':
        await show_purple_dashboard(q)
    else:
        await show_mint_dashboard(q)
