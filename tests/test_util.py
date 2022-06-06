import postgrid


def test_camel_to_snake():
    assert postgrid._camel_to_snake('frontHTML') == 'front_html'
    assert postgrid._camel_to_snake('backHTML') == 'back_html'
    assert postgrid._camel_to_snake('letterID') == 'letter_id'
    assert postgrid._camel_to_snake('thisIsACamelStr') == 'this_is_acamel_str'


def test_preserve_vars_pm_convert_json_value():
    letter = postgrid._pm_convert_json_value({
        'object': 'letter',
        'to': {
            'addressLine1': 'Test',
            'countryCode': 'Test'
        },
        'from': {
            'addressLine1': 'Test',
            'countryCode': 'Test'
        },
        'html': 'Test',
        'doubleSided': True,
        'mergeVariables': {
            'testCamel': 1,
        },
        'metadata': {
            'testCamel': 1
        }
    })

    assert letter.merge_variables['testCamel'] == 1
    assert letter.metadata['testCamel'] == 1
