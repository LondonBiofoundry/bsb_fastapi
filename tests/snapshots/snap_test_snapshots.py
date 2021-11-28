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

snapshots['test_singular_build_csvs_with_files 1'] = 200

snapshots['test_singular_build_echoinstructions 1'] = 200

snapshots['test_singular_build_echoinstructions_with_files 1'] = 200

snapshots['test_singular_build_json 1'] = 200

snapshots['test_singular_build_json_with_files 1'] = 200

snapshots['test_singular_build_pdf 1'] = 200

snapshots['test_singular_build_pdf_with_files 1'] = 200

snapshots['test_singular_build_uniqueassemblies 1'] = 200

snapshots['test_singular_build_uniqueassemblies_with_files 1'] = 200

snapshots['test_singular_build_uniqueparts 1'] = 200

snapshots['test_singular_build_uniqueparts_with_files 1'] = 200

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

snapshots['test_viewpartlabels_success_with_files 1'] = 200

snapshots['test_viewpartlabels_success_with_files 2'] = [
    'label',
    'Feature'
]

snapshots['test_viewpartlabels_success_without_files 1'] = 200

snapshots['test_viewpartlabels_success_without_files 2'] = [
    'label',
    'Feature'
]

snapshots['test_viewseqlabels_success_with_files 1'] = 200

snapshots['test_viewseqlabels_success_with_files 2'] = [
    'label',
    'Feature'
]

snapshots['test_viewseqlabels_success_without_files 1'] = 200

snapshots['test_viewseqlabels_success_without_files 2'] = [
    'label',
    'Feature'
]
