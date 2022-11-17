'''
This is a dictionary with the code of ech type of transport that we have
and several parameters that will be used for the markers in the map.
'''

transports = {'Bus': {'Code': ['K014', 'K015'], 'icon': 'bus', 'tooltip': 'Bus', 'color': 'beige'},
              'Bus_airport': {'Code': ['K016'], 'icon': 'bus', 'tooltip': 'Bus-airpot', 'color': 'orange'},
              'Bus_station': {'Code': ['K017'], 'icon': 'bus', 'tooltip': 'Bus-station', 'color': 'lightred'},
              'Metro': {'Code': ['K001'], 'icon': 'subway', 'tooltip': 'Subway', 'color': 'lightgreen'},
              'Railway': {'Code': ['K002'], 'icon': 'train', 'tooltip': 'Railway', 'color': 'gray'},
              'Renfe': {'Code': ['K003'], 'icon': 'train', 'tooltip': 'RENFE', 'color': 'lightgray'},
              'Airport_train': {'Code': ['K004'], 'icon': 'train', 'tooltip': 'Airport-train', 'color': 'darkpurple'},
              'Maritime_station': {'Code': ['K008'], 'icon': 'ship', 'tooltip': 'Maritime-station', 'color': 'lightblue'},
              'Funicular': {'Code': ['K009'], 'icon': 'arrow-up', 'tooltip': 'Funicular', 'color': 'cadetblue'},
              'Cableway': {'Code': ['K010'], 'icon': 'square-o', 'tooltip': 'Cableway', 'color': 'purple'},
              'Tramvia': {'Code': ['K011'], 'icon': 'minus', 'tooltip': 'Tramvia', 'color': 'green'}
              }


def get_colorIcon(t_type):
    """
    Get transport object without "Code" key
    """
    if not t_type in transports:
        raise ValueError("Invalid code")
    return {k: v for k, v in transports[t_type].items() if k not in ["Code", "tooltip"]}


def get_tooltip(t_type):
    """
    Get tooltip for document
    """
    if not t_type in transports:
        raise ValueError("Invalid code")
    return transports[t_type]['tooltip']
