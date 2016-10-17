from bootstrapper import RUN_DIRECTORY_KEY
from bootstrapper.deployment import Deployment
from bootstrapper.properties import Properties, UPSERT, INSERT
from bootstrapper.commands import PlatformCommandBuilder, StreamFileBuilder, SequencerCommandsFileBuilder, CommanderCommandsFileBuilder
import itertools
import os.path

__all__ = ['deployments']

this_dir = os.path.dirname(os.path.abspath(__file__))
run_directory_base = os.path.join(os.sep, 'home', 'foran', 'Documents', 'config-historic-stream', 'var', 'redi', 'runtime')

TEXT_ADMIN_PORTS = {
        'sequencer': 1500,
        'commander': 1501,
        'eventdrop': 1502,
        'extradrop': 1503
        }

deployments = []
def _add_deployments(environments, data_centers, applications, stripes, instances):
    stream_file_builder = StreamFileBuilder()
    for environment, data_center, application, stripe, instance in itertools.product(environments, data_centers, applications, stripes, instances):
        builders = [PlatformCommandBuilder(TEXT_ADMIN_PORTS[stripe])]
        if stripe == 'sequencer':
            builders.append(SequencerCommandsFileBuilder())
        else:
            builders.append(stream_file_builder)
            
        if stripe == 'commander':
            builders.append(CommanderCommandsFileBuilder())

        deployment = Deployment(
            environment=environment,
            data_center=data_center,
            application=application,
            stripe=stripe,
            instance=instance,
            overrides_dir=os.path.join(this_dir, 'overrides', stripe),
            common_dir=os.path.join(this_dir, 'common'),
            properties="%s.properties" % environment,
            builders=builders)

        if instance == 'primary':
            deployment.properties.save('AS_PRIMARY', 'PRIMARY=true', UPSERT)
        else:
            deployment.properties.save('AS_PRIMARY', 'PRIMARY=false', UPSERT)
        deployment.properties.save(RUN_DIRECTORY_KEY, run_directory_base, INSERT)

        deployments.append(deployment)


_environments = ['dev', 'qa', 'prod']
_data_centers = ['AW1']
_applications = ['HTA1']
_add_deployments(_environments, _data_centers, _applications, ['sequencer', 'eventdrop', 'extradrop'], ['primary', 'backup'])
_add_deployments(_environments, _data_centers, _applications, ['commander'], ['singleton'])
