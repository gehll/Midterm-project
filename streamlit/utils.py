

def doc_to_latlng(doc):
    """
    Convert a doc from mongodb that has a "Location" key to a lat long list 
    """
    return [doc['Location']['coordinates'][1], doc['Location']['coordinates'][0]]
