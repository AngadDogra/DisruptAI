from django.shortcuts import render
import plotly.graph_objs as go
from plotly.offline import plot

# Create your views here.
def home(request):
    return render(request, 'mapview/home.html')

def dashboard(request):
    shipments = ['Truck 101', 'Truck 102', 'Truck 103', 'Truck 104']
    delays = [10, 20, 5, 15]

    # Bar chart
    bar_fig = go.Figure(
        data=[
            go.Bar(x=shipments, y=delays, marker_color='indianred')
        ],
        layout=go.Layout(
            title='Shipment Delays (in minutes)',
            xaxis=dict(title='Truck'),
            yaxis=dict(title='Delay (min)'),
            width=540,
            height=180,
            margin=dict(t=40, b=40, l=30, r=30)
        )
    )
    bar_plot_html = plot(bar_fig, output_type='div')

    # Pie chart
    pie_fig = go.Figure(
        data=[
            go.Pie(labels=['On-Time', 'Delayed'], values=[70, 30])
        ],
        layout=go.Layout(
            title='Shipment Status Overview',
            width=540,
            height=180,
            margin=dict(t=40, b=40, l=30, r=30)
        )
    )
    pie_plot_html = plot(pie_fig, output_type='div')

    return render(request, 'mapview/dashboard.html', {
        'bar_plot': bar_plot_html,
        'pie_plot': pie_plot_html
    })

def alerts(request):
    return render(request, 'mapview/alerts.html')

def map(request):
    return render(request, 'mapview/map.html')

def settings(request):
    return render(request, 'mapview/settings.html')
