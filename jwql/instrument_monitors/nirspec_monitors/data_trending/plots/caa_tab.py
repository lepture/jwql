#! /usr/bin/env python
"""Prepares plots for CAA tab

    Module prepares plots for mnemonics below. Combines plots in a grid and
    returns tab object.

    Plot 1 - Lamp Voltages and Currents (Distincted)
    INRSH_LAMP_SEL
    INRSI_C_CAA_CURRENT
    INRSI_C_CAA_VOLTAGE

    Plot 2 - CAA (Voltages and Currents)
    INRSH_CAA_VREFOFF
    INRSH_CAA_VREF

Authors
-------
    - Daniel Kühbacher

Use
---
    The functions within this module are intended to be imported and
    used by ``nirspec_dashboard.py``, e.g.:

    ::
        from .plots.voltage_tab import voltage_plots
        tab = voltage_plots(conn, start, end)

Dependencies
------------
    User must provide database "nirpsec_database.db"

"""
import copy

from astropy.time import Time
from bokeh.layouts import Column
from bokeh.models.widgets import Panel
from bokeh.plotting import figure

import jwql.instrument_monitors.nirspec_monitors.data_trending.plots.plot_functions as pf
import jwql.instrument_monitors.nirspec_monitors.data_trending.plots.tab_object as tabObjects
import jwql.instrument_monitors.nirspec_monitors.data_trending.utils.utils_f as utils


def lamp_volt(conn, start, end):
    '''Create specific plot and return plot object
    Parameters
    ----------
    conn : DBobject
        Connection object that represents database
    start : time
        Startlimit for x-axis and query (typ. datetime.now()- 4Months)
    end : time
        Endlimit for x-axis and query (typ. datetime.now())
    Return
    ------
    p : Plot object
        Bokeh plot
    '''

    # create a new plot with a title and axis labels
    p = figure(tools="pan,wheel_zoom,box_zoom,reset,save",
               toolbar_location="above",
               plot_width=1120,
               plot_height=800,
               x_range=utils.time_delta(Time(end)),
               y_range=[1.2, 2.3],
               x_axis_type='datetime',
               output_backend="webgl",
               x_axis_label='Date', y_axis_label='Voltage (V)')

    p.xaxis.formatter = copy.copy(utils.plot_x_axis_format)

    p.grid.visible = True
    p.title.text = "CAA Lamp Voltages"
    pf.add_basic_layout(p)

    l = pf.add_to_plot(p, "FLAT1", "LAMP_FLAT1_VOLT", start, end, conn, color="red")
    m = pf.add_to_plot(p, "FLAT2", "LAMP_FLAT2_VOLT", start, end, conn, color="green")
    n = pf.add_to_plot(p, "FLAT3", "LAMP_FLAT3_VOLT", start, end, conn, color="blue")
    o = pf.add_to_plot(p, "FLAT4", "LAMP_FLAT4_VOLT", start, end, conn, color="brown")
    x = pf.add_to_plot(p, "FLAT5", "LAMP_FLAT5_VOLT", start, end, conn, color="orange")
    q = pf.add_to_plot(p, "LINE1", "LAMP_LINE1_VOLT", start, end, conn, color="cyan")
    r = pf.add_to_plot(p, "LINE2", "LAMP_LINE2_VOLT", start, end, conn, color="darkmagenta")
    s = pf.add_to_plot(p, "LINE3", "LAMP_LINE3_VOLT", start, end, conn, color="burlywood")
    t = pf.add_to_plot(p, "LINE4", "LAMP_LINE4_VOLT", start, end, conn, color="darkkhaki")
    u = pf.add_to_plot(p, "REF", "LAMP_REF_VOLT", start, end, conn, color="darkblue")
    v = pf.add_to_plot(p, "TEST", "LAMP_TEST_VOLT", start, end, conn, color="goldenrod")

    pf.add_hover_tool(p, [l, m, n, o, x, q, r, s, t, u, v])

    p.legend.location = "bottom_right"
    p.legend.click_policy = "hide"
    p.legend.orientation = "horizontal"

    return p


def lamp_current(conn, start, end):
    '''Create specific plot and return plot object
    Parameters
    ----------
    conn : DBobject
        Connection object that represents database
    start : time
        Startlimit for x-axis and query (typ. datetime.now()- 4Months)
    end : time
        Endlimit for x-axis and query (typ. datetime.now())
    Return
    ------
    p : Plot object
        Bokeh plot
    '''

    # create a new plot with a title and axis labels
    p = figure(tools="pan,wheel_zoom,box_zoom,reset,save",
               toolbar_location="above",
               plot_width=1120,
               plot_height=600,
               x_range=utils.time_delta(Time(end)),
               y_range=[10.5, 14.5],
               x_axis_type='datetime',
               output_backend="webgl",
               x_axis_label='Date', y_axis_label='Current (mA)')

    p.xaxis.formatter = copy.copy(utils.plot_x_axis_format)

    p.grid.visible = True
    p.title.text = "CAA Lamp currents"
    pf.add_basic_layout(p)

    a = pf.add_to_plot(p, "FLAT1", "LAMP_FLAT1_CURR", start, end, conn, color="red")
    b = pf.add_to_plot(p, "FLAT2", "LAMP_FLAT2_CURR", start, end, conn, color="green")
    c = pf.add_to_plot(p, "FLAT3", "LAMP_FLAT3_CURR", start, end, conn, color="blue")
    d = pf.add_to_plot(p, "FLAT4", "LAMP_FLAT4_CURR", start, end, conn, color="brown")
    e = pf.add_to_plot(p, "FLAT5", "LAMP_FLAT5_CURR", start, end, conn, color="orange")
    f = pf.add_to_plot(p, "LINE1", "LAMP_LINE1_CURR", start, end, conn, color="cyan")
    g = pf.add_to_plot(p, "LINE2", "LAMP_LINE2_CURR", start, end, conn, color="darkmagenta")
    h = pf.add_to_plot(p, "LINE3", "LAMP_LINE3_CURR", start, end, conn, color="burlywood")
    i = pf.add_to_plot(p, "LINE4", "LAMP_LINE4_CURR", start, end, conn, color="darkkhaki")
    j = pf.add_to_plot(p, "REF", "LAMP_REF_CURR", start, end, conn, color="darkblue")
    k = pf.add_to_plot(p, "TEST", "LAMP_TEST_CURR", start, end, conn, color="goldenrod")

    pf.add_hover_tool(p, [a, b, c, d, e, f, g, h, i, j, k])

    p.legend.location = "bottom_right"
    p.legend.click_policy = "hide"
    p.legend.orientation = "horizontal"

    return p


def caa_volt(conn, start, end):
    '''Create specific plot and return plot object
    Parameters
    ----------
    conn : DBobject
        Connection object that represents database
    start : time
        Startlimit for x-axis and query (typ. datetime.now()- 4Months)
    end : time
        Endlimit for x-axis and query (typ. datetime.now())
    Return
    ------
    p : Plot object
        Bokeh plot
    '''

    p = figure(tools="pan,wheel_zoom,box_zoom,reset,save",
               toolbar_location="above",
               plot_width=1120,
               plot_height=600,
               x_range=utils.time_delta(Time(end)),
               x_axis_type='datetime',
               output_backend="webgl",
               x_axis_label='Date', y_axis_label='Voltage (V)')

    p.xaxis.formatter = copy.copy(utils.plot_x_axis_format)

    a = pf.add_to_plot(p, "CAA_VREFOFF", "INRSH_CAA_VREFOFF", start, end, conn, color="red")
    b = pf.add_to_plot(p, "CAA_VREF", "INRSH_CAA_VREF", start, end, conn, color="green")

    # pf.add_hover_tool(p,[a,b])

    p.legend.location = "bottom_right"
    p.legend.click_policy = "hide"

    return p


def caa_plots(conn, start, end):
    '''Combines plots to a tab

    Parameters
    ----------
    conn : DBobject
        Connection object that represents database
    start : time
        Startlimit for x-axis and query (typ. datetime.now()- 4Months)
    end : time
        Endlimit for x-axis and query (typ. datetime.now())

    Return
    ------
    p : tab object
        used by dashboard.py to set up dashboard
    '''

    descr = tabObjects.generate_tab_description(utils.description_caa)

    plot1 = lamp_volt(conn, start, end)
    plot2 = lamp_current(conn, start, end)
    # plot3 = caa_plots(conn, start, end)
    data_table = tabObjects.anomaly_table(conn, utils.list_caa)

    layout = Column(descr, plot1, plot2, data_table)

    tab = Panel(child=layout, title="CAA/LAMPS")

    return tab
