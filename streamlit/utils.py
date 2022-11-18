from folium import Marker, Icon
from transports import get_colorIcon, get_tooltip


def doc_to_latlng(doc):
    """
    Convert a doc from mongodb that has a "Location" key to a lat long list 
    """
    return [doc['Location']['coordinates'][1], doc['Location']['coordinates'][0]]


def create_marker(doc, t_type):
    colorIcon = get_colorIcon(t_type)
    marker = Marker(doc_to_latlng(doc),
                    popup=f"<i>{doc['Station']}</i>",
                    tooltip=get_tooltip(t_type),
                    icon=Icon(**colorIcon, prefix='fa'))

    return marker
