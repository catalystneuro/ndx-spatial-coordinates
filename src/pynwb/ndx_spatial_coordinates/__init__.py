import os
from pynwb import load_namespaces, get_class

# Set path of the namespace.yaml file to the expected install location
ndx_spatial_coordinates_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-spatial-coordinates.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_spatial_coordinates_specpath):
    ndx_spatial_coordinates_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-spatial-coordinates.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_spatial_coordinates_specpath)

# TODO: import your classes here or define your class using get_class to make
# them accessible at the package level

Space = get_class('Space', 'ndx-spatial-coordinates')
Spaces = get_class('Spaces', 'ndx-spatial-coordinates')
CoordinateSystem = get_class('CoordinateSystem', 'ndx-spatial-coordinates')
CoordinateSystems = get_class('CoordinateSystems', 'ndx-spatial-coordinates')
RegistrationProtocol = get_class('RegistrationProtocol', 'ndx-spatial-coordinates')
RegistrationProtocols = get_class('RegistrationProtocols', 'ndx-spatial-coordinates')
CoordinateRegistrationProcess = get_class('CoordinateRegistrationProcess', 'ndx-spatial-coordinates')
CoordinateRegistrationProcesses = get_class('CoordinateRegistrationProcesses', 'ndx-spatial-coordinates')
Transform = get_class('Transform', 'ndx-spatial-coordinates')
AffineTransform = get_class('AffineTransform', 'ndx-spatial-coordinates')
DeformableTransform = get_class('DeformableTransform', 'ndx-spatial-coordinates')
Transforms = get_class('Transforms', 'ndx-spatial-coordinates')
PhysicalObjectType = get_class('PhysicalObjectType', 'ndx-spatial-coordinates')
ElectrodeType = get_class('ElectrodeType', 'ndx-spatial-coordinates')
ElectrodeTypes = get_class('ElectrodeTypes', 'ndx-spatial-coordinates')
PhysicalObjectWithSubObjectsType = get_class('PhysicalObjectWithSubObjectsType', 'ndx-spatial-coordinates')
ProbeType = get_class('ProbeType', 'ndx-spatial-coordinates')
ProbeTypes = get_class('ProbeTypes', 'ndx-spatial-coordinates')
SubjectBrain = get_class('SubjectBrain', 'ndx-spatial-coordinates')
SpaceInfo = get_class('SpaceInfo', 'ndx-spatial-coordinates')
