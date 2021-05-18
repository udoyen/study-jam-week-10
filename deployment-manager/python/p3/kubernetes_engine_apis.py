def GenerateConfig(context):
  """Generate YAML resource configuration."""

  endpoints = {
      '-v1': 'api/v1',
      '-v1beta1-apps': 'apis/apps/v1beta1',
      '-v1beta1-extensions': 'apis/extensions/v1beta1'
  }

  resources = []
  outputs = []

  for type_suffix, endpoint in endpoints.items():
    resources.append({
        'name': 'kubernetes' + type_suffix,
        'type': 'deploymentmanager.v2beta.typeProvider',
        'properties': {
            'options': {
                'validationOptions': {
                    'schemaValidation': 'IGNORE_WITH_WARNINGS'
                },
                'inputMappings': [
                    {
                        'fieldName': 'name',
                        'location': 'PATH',
                        'methodMatch': '^(GET|DELETE|PUT)$',
                        'value': '$.ifNull('
                                '$.resource.properties.metadata.name, '
                                '$.resource.name)'
                    }, {
                        'fieldName': 'metadata.name',
                        'location': 'BODY',
                        'methodMatch': '^(PUT|POST)$',
                        'value': '$.ifNull('
                                '$.resource.properties.metadata.name, '
                                '$.resource.name)'
                    }, {
                        'fieldName': 'namespace',
                        'location': 'PATH',
                        'methodMatch': '^(GET|DELETE|PUT|POST|PATCH)$',
                        'value': '$.ifNull('
                                '$.resource.properties.namespace,)'
                                '$.resource.namespace'
                    }, {
                        'fieldName': 'Authorization',
                        'location': 'HEADER',
                        'value': '$.concat("Bearer ",'
                                '$.googleOauth2AccessToken())'
                    }, {
                        'fieldName': 'metadata.resourceVersion',
                        'location': 'BODY',
                        'methodMatch': '^(PUT|PATCH)$',
                        'value': '$.resource.self.metadata.resourceVersion'
                        }, {
                        'fieldName': 'id',
                        'location': 'PATH',
                        'methodMatch': '^(GET|DELETE|PUT|POST|PATCH)$',
                        'value': '$.resource.properties.id'
                    }
                ]
            },
            'descriptorUrl':
                ''.join([
                    'https://' + context.properties["clustername"] + '.' + context.properties['endpoint'] + '/openapi/v2', 
                    endpoint
                ])
        }
    })
    outputs.append({
      'name': 'banger',
      'value': 'one'
    })

    return {'resources': resources, 'outputs': outputs}