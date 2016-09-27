from bootstrapper import Deployment, Properties, UPSERT
import itertools
import os.path
import pprint

this_dir = os.path.dirname(os.path.abspath(__file__))
printer = pprint.PrettyPrinter()

deployments = []
for environment, data_center, application, stripe, instance in itertools.product(['dev'], ['AM3'], ['HTA3'], ['sequencer'], ['primary', 'backup']):
    deployment = Deployment(
        environment=environment,
        data_center=data_center,
        application=application,
        stripe=stripe,
        instance=instance,
        overrides_dir=os.path.join(this_dir, 'overrides', stripe))

    if instance == 'primary':
        deployment.properties.save('AS_PRIMARY', 'PRIMARY=true', UPSERT)
    else:
        deployment.properties.save('AS_PRIMARY', 'PRIMARY=false', UPSERT)

    deployments.append(deployment)


for deployment in deployments:
    deployment.create()
