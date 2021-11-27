# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_collection_names 1'] = 200

snapshots['test_collection_names 2'] = {
    'data': [
        'BASIC_BIOLEGIO_LINKERS',
        'BASIC_CDS_PARTS',
        'BASIC_PROMOTER_PARTS',
        'BASIC_SEVA_PARTS'
    ]
}

snapshots['test_root_hello_world 1'] = 200

snapshots['test_root_hello_world 2'] = {
    'message': 'Hello World'
}

snapshots['test_singular_build_csvs 1'] = 200

snapshots['test_singular_build_csvs 2'] = b'PK\x03\x04\x14\x00\x00\x00\x00\x00S\xb4{S\xfc\x9c^\xb3)\x00\x00\x00)\x00\x00\x00\x0e\x00\x00\x00assemblies.csvAssembly Index,Assembly ID,Clip indexes\r\nPK\x03\x04\x14\x00\x00\x00\x00\x00S\xb4{Sb\xdayM\xa1\x00\x00\x00\xa1\x00\x00\x00\t\x00\x00\x00clips.csvClip Index,Prefix ID,Part ID,Part Name,Part suggested stock concentration (ng/\xc2\xb5L),Part stock per 30 \xc2\xb5L clip (\xc2\xb5L),Suffix ID,Total assemblies,Assembly indexes\r\nPK\x01\x02\x14\x03\x14\x00\x00\x00\x00\x00S\xb4{S\xfc\x9c^\xb3)\x00\x00\x00)\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\x00\x00\x00\x00assemblies.csvPK\x01\x02\x14\x03\x14\x00\x00\x00\x00\x00S\xb4{Sb\xdayM\xa1\x00\x00\x00\xa1\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81U\x00\x00\x00clips.csvPK\x05\x06\x00\x00\x00\x00\x02\x00\x02\x00s\x00\x00\x00\x1d\x01\x00\x00\x00\x00'

snapshots['test_singular_build_csvs_with_files 1'] = 200

snapshots['test_singular_build_csvs_with_files 2'] = b'PK\x03\x04\x14\x00\x00\x00\x00\x00S\xb4{S\xfc\x9c^\xb3)\x00\x00\x00)\x00\x00\x00\x0e\x00\x00\x00assemblies.csvAssembly Index,Assembly ID,Clip indexes\r\nPK\x03\x04\x14\x00\x00\x00\x00\x00S\xb4{Sb\xdayM\xa1\x00\x00\x00\xa1\x00\x00\x00\t\x00\x00\x00clips.csvClip Index,Prefix ID,Part ID,Part Name,Part suggested stock concentration (ng/\xc2\xb5L),Part stock per 30 \xc2\xb5L clip (\xc2\xb5L),Suffix ID,Total assemblies,Assembly indexes\r\nPK\x01\x02\x14\x03\x14\x00\x00\x00\x00\x00S\xb4{S\xfc\x9c^\xb3)\x00\x00\x00)\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\x00\x00\x00\x00assemblies.csvPK\x01\x02\x14\x03\x14\x00\x00\x00\x00\x00S\xb4{Sb\xdayM\xa1\x00\x00\x00\xa1\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81U\x00\x00\x00clips.csvPK\x05\x06\x00\x00\x00\x00\x02\x00\x02\x00s\x00\x00\x00\x1d\x01\x00\x00\x00\x00'

snapshots['test_singular_build_echoinstructions 1'] = 200

snapshots['test_singular_build_echoinstructions 2'] = b'{"result":false,"message":"To many clips in the build to be handled by a single 384 \\n                source plate, considering you alternate_well setting."}'

snapshots['test_singular_build_echoinstructions_with_files 1'] = 200

snapshots['test_singular_build_echoinstructions_with_files 2'] = b'{"result":false,"message":"To many clips in the build to be handled by a single 384 \\n                source plate, considering you alternate_well setting."}'

snapshots['test_validate_fail_with_files 1'] = 200

snapshots['test_validate_fail_with_files 2'] = {
    'message': "Alternating BasicPart, BasicLinker instances required: SEVA_12 is preceeded by <class 'basicsynbio.main.BasicPart'> and is of type <class 'basicsynbio.main.BasicPart'>.",
    'result': False
}

snapshots['test_validate_fail_without_files 1'] = 200

snapshots['test_validate_fail_without_files 2'] = {
    'message': "Alternating BasicPart, BasicLinker instances required: b0cc681c00c117b6c86cdfbcb050b272 is preceeded by <class 'basicsynbio.main.BasicPart'> and is of type <class 'basicsynbio.main.BasicPart'>.",
    'result': False
}

snapshots['test_validate_success_with_files 1'] = 200

snapshots['test_validate_success_with_files 2'] = {
    'message': None,
    'result': True
}

snapshots['test_validate_success_without_files 1'] = 200

snapshots['test_validate_success_without_files 2'] = {
    'message': None,
    'result': True
}
