# -*- coding: utf-8 -*-

import os.path

from hdmf.spec import NamespaceBuilder, GroupSpec, AttributeSpec, \
    LinkSpec, DatasetSpec, DtypeSpec, RefSpec


def main():
    # these arguments were auto-generated from your cookie-cutter inputs
    ns_builder = NamespaceBuilder(
        doc="""Objects for rigorously defining spatial coordinates, object shapes, and transformations""",
        name="""ndx-spatial-coordinates""",
        version="""0.1.0""",
        author=list(map(str.strip, """Ben Dichter""".split(','))),
        contact=list(map(str.strip, """ben.dichter@catalystneuro.com""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types
    # as of HDMF 1.6.1, the full ancestry of the neurodata_types that are used by
    # the extension should be included, i.e., the neurodata_type and its parent
    # type and its parent type and so on. this will be addressed in a future
    # release of HDMF.
    ns_builder.include_type('Container', namespace='hdmf-common')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information

    Space = GroupSpec(
        data_type_def='Space',
        data_type_inc='Container',
        doc='space',
        attributes=[
            AttributeSpec(
                name='R',
                doc='dimensionality of space',
                dtype='int'
            )
        ]
    )

    Spaces = GroupSpec(
        data_type_def='Spaces',
        data_type_inc='Container',
        doc='contains spaces',
        groups=[
            GroupSpec(
                data_type_inc=Space,
                quantity='*',
                doc='spaces are stored here'
            )
        ]
    )

    CoordinateSystem = GroupSpec(
        data_type_def='CoordinateSystem',
        data_type_inc='Container',
        doc='coordinate system',
    )

    CoordinateSystems = GroupSpec(
        data_type_def='CoordinateSystems',
        data_type_inc='Container',
        doc='coordinate systems',
        groups=[
            GroupSpec(
                data_type_inc=CoordinateSystem,
                quantity='*',
                doc='coordinate systems are stored here'
            )
        ],
        links=[
            LinkSpec(
                doc='link to space',
                target_type='Space',
                name='space'
            )
        ]
    )

    RegistrationProtocol = GroupSpec(
        data_type_def='RegistrationProtocol',
        data_type_inc='Container',
        doc='registration protocol'
    )

    RegistrationProtocols = GroupSpec(
        data_type_def='RegistrationProtocols',
        data_type_inc='Container',
        doc='registration protocols',
        groups=[
            GroupSpec(
                data_type_inc=RegistrationProtocol,
                quantity='*',
                doc='registration protocols are stored here'
            )
        ],
    )

    CoordinateRegistrationProcess = GroupSpec(
        data_type_def='CoordinateRegistrationProcess',
        data_type_inc='Container',
        doc='coordinate registration process',
        links=[
            LinkSpec(
                doc='registration protocol',
                target_type='RegistrationProtocol',
                name='registration_protocol'
            )
        ]
    )

    CoordinateRegistrationProcesses = GroupSpec(
        data_type_def='CoordinateRegistrationProcesses',
        data_type_inc='Container',
        doc='registration process',
        groups=[
            GroupSpec(
                data_type_inc=CoordinateRegistrationProcess,
                quantity='*',
                doc='registration processes are stored here'
            )
        ],
    )

    Transform = GroupSpec(
        data_type_def='Transform',
        data_type_inc='Container',
        doc='transform',
        links=[
            LinkSpec(
                doc='domain coordinate system',
                target_type='CoordinateSystem',
                name='domain_coordinate_system'
            ),
            LinkSpec(
                doc='range coordinate system',
                target_type='CoordinateSystem',
                name='range_coordinate_system'
            )
        ],
    )

    AffineTransform = GroupSpec(
        data_type_def='AffineTransform',
        data_type_inc=Transform,
        doc='affine transform',
        datasets=[
            DatasetSpec(
                doc='affine transform matrix',
                dtype='float',
                name='M'
            )
        ]
    )

    DeformableTransform = GroupSpec(
        data_type_def='DeformableTransform',
        data_type_inc=Transform,
        doc='deformable transform',
        datasets=[
            DatasetSpec(
                doc='vector image',
                dtype='float',
                name='I'
            )
        ]
    )

    Transforms = GroupSpec(
        data_type_def='Transforms',
        data_type_inc='Container',
        doc='transforms',
        groups=[
            GroupSpec(
                data_type_inc=Transform,
                quantity='*',
                doc='transforms are stored here'
            )
        ],
    )

    PhysicalObjectType = GroupSpec(
        data_type_def='PhysicalObjectType',
        data_type_inc='Container',
        doc='physical object type',
        groups=[
            GroupSpec(
                name='geometry',
                doc='geometry',
                datasets=[
                    DatasetSpec(
                        name='nodes',
                        doc='nodes',
                        dtype='float',
                        shape=(None, 3)
                    ),
                    DatasetSpec(
                        name='edges',
                        doc='edges',
                        dtype='uint',
                        shape=(None, 3)
                    )
                ]
            )
        ],
        links=[
            LinkSpec(
                doc='coordinate system',
                target_type='CoordinateSystem'
            )
        ]
    )

    ElectrodeType = GroupSpec(
        data_type_def='ElectrodeType',
        data_type_inc=PhysicalObjectType,
        doc='electrode type',
        attributes=[
            AttributeSpec(
                name='electrode_type',
                doc='electrode type',
                dtype='text'
            )
        ]
    )

    ElectrodeTypes = GroupSpec(
        data_type_def='ElectrodeTypes',
        data_type_inc='Container',
        doc='electrode types',
        groups=[
            GroupSpec(
                data_type_inc=ElectrodeType,
                quantity='*',
                doc='electrode types are stored here'
            )
        ],
    ),

    PhysicalObjectWithSubObjectsType = GroupSpec(
        data_type_def='PhysicalObjectWithSubObjectsType',
        data_type_inc=PhysicalObjectType,
        doc='physical object with sub objects',
        groups=[
            GroupSpec(
                name='sites',
                doc='sites',
                datasets=[
                    DatasetSpec(
                        name='sites',
                        doc='sites',
                        dtype=[
                            DtypeSpec(
                                name='position',
                                doc='position',
                                dtype='float',
                                #shape=(3,)
                            ),
                            DtypeSpec(
                                name='normal',
                                doc='normal',
                                dtype='float',
                                #shape=(3,)
                            ),
                            DtypeSpec(
                                name='object_type',
                                doc='object type',
                                dtype=RefSpec(
                                    target_type='PhysicalObjectType',
                                    reftype='object'
                                )
                            ),
                        ]
                    )
                ]

            )
        ]

    )

    ProbeType = GroupSpec(
        data_type_def='ProbeType',
        data_type_inc=PhysicalObjectWithSubObjectsType,
        doc='probe type',
    )

    ProbeTypes = GroupSpec(
        data_type_def='ProbeTypes',
        data_type_inc='Container',
        doc='probe types',
        groups=[
            GroupSpec(
                data_type_inc=ProbeType,
                quantity='*',
                doc='probe types are stored here'
            )
        ],
    )

    SubjectBrain = GroupSpec(
        data_type_def='SubjectBrain',
        data_type_inc=PhysicalObjectWithSubObjectsType,
        doc='subject brain'
    )

    SpaceInfo = GroupSpec(
        data_type_def='SpaceInfo',
        data_type_inc='Container',
        doc='all space info goes in here',
        groups=[
            GroupSpec(
                data_type_inc=Spaces,
                doc='spaces'
            ),
            GroupSpec(
                data_type_inc=CoordinateSystems,
                doc='coordinate systems'
            ),
            GroupSpec(
                data_type_inc=RegistrationProtocols,
                doc='registration protocols'
            ),
            GroupSpec(
                data_type_inc=CoordinateRegistrationProcesses,
                doc='registration processes'
            ),
            GroupSpec(
                data_type_inc=Transforms,
                doc='transforms'
            ),
            GroupSpec(
                data_type_inc=ElectrodeTypes,
                doc='electrode types'
            ),
            GroupSpec(
                data_type_inc=ProbeTypes,
                doc='probe types'
            ),
            GroupSpec(
                data_type_inc=SubjectBrain,
                doc='subject brain'
            )
        ]
    )


    # TODO: add all of your new data types to this list
    new_data_types = [SpaceInfo, AffineTransform, DeformableTransform]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
