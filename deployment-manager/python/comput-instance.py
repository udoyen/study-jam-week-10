def GenerateConfig(context):
      """[summary]

      Args:
          context ([type]): [description]
      """      
      resources = []
      resources.append({
            'name': 'vm-template',
            'type': 'compute.v1.instance',
            'properties': {
                  'zone': 'europe-west2-b',
                  'machineType': 'zone/europe-west2-b/machineType/n1-standard-2',
                  'disks': [{
                        'deviceName': 'boot',
                        'type': 'PRESISTENT',
                        'boot': True,
                        'autoDelete': True,
                        'initializeParams': {
                              'sourceImage': 'projects/debian-cloud/global/images/family/debian-9'
                        }
                  }],
                  'networkInterfaces': [{
                        'network': 'global/networks/default'
                  }]
            }
      })

      # [END use_basic_template]
      # [START use_template_with_variables]
      resources.append({
            'name': 'vm-' + context.env['deployment'],
            'type': 'compute.v1.instance',
            'properties': {
            'zone': 'us-central1-a',
            'machineType': ''.join(['zones/', context.properties['zone'],
                                    '/machineTypes/n1-standard-2']),
            'disks': [{
                  'deviceName': 'boot',
                  'type': 'PERSISTENT',
                  'boot': True,
                  'autoDelete': True,
                  'initializeParams': {
                        'sourceImage':
                        'projects/debian-cloud/global/images/family/debian-9'
                  }
            }],
            'networkInterfaces': [{
                  'network': 'global/networks/default'
            }]
            }

      })
      # [END use_template_with_variables]
      return {'resources': resources}