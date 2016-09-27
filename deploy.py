from bootstrapper import Deployment, Properties, UPSERT
import itertools
import os.path
import pprint

this_dir = os.path.dirname(os.path.abspath(__file__))
printer = pprint.PrettyPrinter()

deployments = []
def _add_deployments(environments, data_centers, applications, stripes, instances):
    for environment, data_center, application, stripe, instance in itertools.product(environments, data_centers, applications, stripes, instances):
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

_environments = ['dev']
_data_centers = ['AM3']
_applications = ['HTA3']
_add_deployments(_environments, _data_centers, _applications, ['sequencer', 'eventdrop', 'extradrop'], ['primary', 'backup'])
_add_deployments(_environments, _data_centers, _applications, ['commander'], ['singleton'])


# TODO Remove before tagging
for deployment in deployments:
    deployment.create()
