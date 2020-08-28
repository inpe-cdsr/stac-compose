#!/usr/bin/env python3


MAX_LIMIT = 3000


def rename_fields_from_feature_collection(feature_collection):
    """This function renames feature collection keys to leave it according to STAC 9.0 and it is returned"""

    if 'meta' in feature_collection:
        # rename 'meta' key to 'context'
        feature_collection['context'] = feature_collection.pop('meta')

    if 'found' in feature_collection['context']:
        # rename 'found' key to 'matched'
        feature_collection['context']['matched'] = feature_collection['context'].pop('found')

    return feature_collection


def destructuring_dict(d, *args):
    """
    Destructuring a dictionary (i.e. d) into variables

    d (dict): dictionary to destructure
    *args (list): list of arguments to remove from d
    """
    result = [d[arg] if arg in d else None for arg in args]
    if len(result) == 1:
        return result[0]
    else:
        return result


def get_limit_to_search(limit):
    # if 'limit' is less than the maximum I can search, then I can use 'limit' to search my features just one time
    if limit <= MAX_LIMIT:
        return limit
    # if 'limit' is greater than the maximum I can search, then I use the maximum number and I search by pages
    else:
        return MAX_LIMIT


def add_context_field_in_the_feature_collection_if_it_does_not_exist(feature_collection, page=1, limit=MAX_LIMIT):
    """add `context` field in the feature collection if it does not exist"""

    if 'context' not in feature_collection:
        # if there is not a `context` field in the feature collection, then I create a fake one
        context = {
            'matched': 0,
            'returned': 0,
            'page': page,
            'limit': limit
        }

        if 'features' in feature_collection:
            # create a fake `context` using the size of results returned as 'matched' and 'returned' fields
            returned = len(feature_collection['features'])
            context['matched'] = returned
            context['returned'] = returned

            feature_collection['context'] = context
        else:
            # create a fake `context` using the default one
            feature_collection['context'] = context

    return feature_collection


def create_new_feature_collection(limit=0, matched= 0, page=1, returned=0, features=[], error=None):
    feature_collection = {
        'context': {
            'limit': limit,
            'matched': matched,
            'page': page,
            'returned': returned
        },
        "type": "FeatureCollection",
        "features": features
    }

    # if error is not None, then I add the error to the context
    if error is not None:
        feature_collection['context']['meta'] = {
            'error': str(error)
        }

    return feature_collection
