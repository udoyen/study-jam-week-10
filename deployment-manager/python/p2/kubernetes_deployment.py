def GenerateConfig(context):
    """Generate YAML resource configuration."""

    cluster_types_root = '{}/kubernetes'.format(context.env['project'])
    cluster_types = {
        'Service': '{}-v1:/api/v1/namespaces/{namespace}/services'.format(cluster_types_root),
        'Deployment': '{}-v1beta1-apps:/apis/apps/v1beta1/namespaces/{namespace}/deployments'.format(cluster_types_root),
        'Ingress': '{}-v1beta1-extensions:/apis/extensions/v1beta1/namespaces/{namespace}/ingresses'.format(cluster_types_root)

    }

    name = context.properties['NAME']
    image = context.properties['IMAGE_NAME']
    port = context.properties['PORT']

    resources = [
         {
            'name': name + '-deployment',
            'type': cluster_types['Deployment'],
            'properties': {
                'apiVersion': 'apps/v1beta1',
                'kind': 'Deployment',
                'namespace': 'default',
                'metadata': {
                    'name': name + '-deployment'
                },
                'spec': {
                    'replicas': 1,
                    'template': {
                        'metadata': {
                            'labels': {
                                'name': name + '-deployment',
                                'app': name
                            }
                        },
                        'spec': {
                            'containers': [{
                                'name': 'container',
                                'image': image,
                                'ports': [{
                                    'containerPort': 8080
                                }]
                            }]
                        }
                    }
                }
            }
        },
            {
            'name': name + '-service',
            'type': cluster_types['Service'],
            'properties': {
                'apiVersion': 'v1',
                'kind': 'Service',
                'namespace': 'default',
                'metadata': {
                    'name': name + '-service',
                    'labels': {
                        'id': 'deployment-manager'
                    }
                },
                'spec': {
                    'type': 'NodePort',
                    'ports': [{
                        'port': port,
                        'targetPort': 8080,
                        'protocol': 'TCP'
                    }],
                    'selector': {
                        'app': name
                    }
                }
            }
        }, {
            'name': name + '-ingress',
            'type': cluster_types['Ingress'],
            'properties': {
                'apiVersion': 'extensions/v1beta1',
                'kind': 'Ingress',
                'namespace': 'default',
                'metadata': {
                    'name': name + '-ingress',
                    'labels': {
                        'id': 'deployment-manager-ingress'
                    }
                },
                'spec': {
                    'rules': [{
                        'http': {
                            'paths': [{
                                'pathType': 'Prefix',
                                'path': '/*',
                                'backend': {
                                    'serviceName': name + '-service',
                                    'servicePort': port
                                            
                                    }
                                }]
                            }
                        }]
                    }
                }
            }

    ]

    return {'resources': resources}
