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

snapshots['test_viewseqann_success_with_files 1'] = 200

snapshots['test_viewseqann_success_with_files 2'] = {
    'annotations': [
        {
            'direction': 1,
            'end': 3639,
            'name': 'SEVA_T1',
            'start': 3534
        },
        {
            'direction': 1,
            'end': 51,
            'name': 'Prefix',
            'start': 33
        },
        {
            'direction': 1,
            'end': 1286,
            'name': 'Linker04',
            'start': 1241
        },
        {
            'direction': 1,
            'end': 3666,
            'name': 'Suffix',
            'start': 3648
        },
        {
            'direction': 1,
            'end': 4833,
            'name': 'terminator_B0015',
            'start': 4704
        },
        {
            'direction': 1,
            'end': 4668,
            'name': 'mscarlett',
            'start': 3963
        },
        {
            'direction': 1,
            'end': 160,
            'name': 'SEVA_T0',
            'start': 57
        },
        {
            'direction': 1,
            'end': 3520,
            'name': 'SEVA_RK2',
            'start': 1298
        },
        {
            'direction': 1,
            'end': 47,
            'name': 'LinkerA',
            'start': 0
        },
        {
            'direction': 1,
            'end': 3705,
            'name': 'LMS',
            'start': 3648
        },
        {
            'direction': 1,
            'end': 3701,
            'name': 'LinkerB',
            'start': 3654
        },
        {
            'direction': 1,
            'end': 4843,
            'name': 'LMP',
            'start': 4837
        },
        {
            'direction': 1,
            'end': 1225,
            'name': 'SEVA_Ap',
            'start': 186
        },
        {
            'direction': 1,
            'end': 4668,
            'name': 'mScarlett',
            'start': 3963
        },
        {
            'direction': 1,
            'end': 279,
            'name': 'Amp prom',
            'start': 250
        },
        {
            'direction': 1,
            'end': 3832,
            'name': 'PJ23119',
            'start': 3797
        }
    ]
}

snapshots['test_viewseqann_success_without_files 1'] = 200

snapshots['test_viewseqann_success_without_files 2'] = {
    'annotations': [
        {
            'direction': 1,
            'end': 160,
            'name': 'SEVA_T0',
            'start': 57
        },
        {
            'direction': 1,
            'end': 3832,
            'name': 'J23119',
            'start': 3797
        },
        {
            'direction': 1,
            'end': 4843,
            'name': 'LMP',
            'start': 4837
        },
        {
            'direction': 1,
            'end': 4833,
            'name': 'B0015',
            'start': 4704
        },
        {
            'direction': 1,
            'end': 3705,
            'name': 'LMS',
            'start': 3648
        },
        {
            'direction': 1,
            'end': 4668,
            'name': 'mScarlett',
            'start': 3963
        },
        {
            'direction': 1,
            'end': 3639,
            'name': 'SEVA_T1',
            'start': 3534
        },
        {
            'direction': 1,
            'end': 3520,
            'name': 'SEVA_RK2',
            'start': 1298
        },
        {
            'direction': 1,
            'end': 1225,
            'name': 'SEVA_Ap',
            'start': 186
        }
    ]
}

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
