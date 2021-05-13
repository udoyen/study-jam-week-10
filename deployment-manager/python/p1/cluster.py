def GenerateConfig(context):
  """Generate YAML resource configuration."""

  cluster_name = context.properties['cluster_name']
  cluster_zone = context.properties['cluster_zone']
  number_of_nodes = context.properties['number_of_nodes']

  resources = []
  outputs = []
  resources.append({
      'name': context.properties['cluster_name'],
      'type': 'container.v1.cluster',
      'properties': {
          'zone': context.properties['cluster_zone'],
          'cluster': {
              'name': context.properties['cluster_name'],
              'initialNodeCount': context.properties['number_of_nodes'],
              'nodeConfig': {
                  'oauthScopes': [
                      'https://www.googleapis.com/auth/' + scope
                      for scope in [
                          'compute',
                          'devstorage.read_only',
                          'logging.write',
                          'monitoring'
                        ]
                    ]
                }
            }
        }
    })
  outputs.append({
        'name': 'endpoint',
        'value': '$(ref.' + context.properties['cluster_name'] + '.endpoint)'
    })
  return {'resources': resources, 'outputs': outputs}