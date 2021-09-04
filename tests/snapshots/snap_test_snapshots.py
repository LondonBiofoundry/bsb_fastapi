# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_collection_data 1"] = 200

snapshots["test_collection_data 2"] = {
    "data": [
        {
            "name": "BASIC_BIOLEGIO_LINKERS",
            "v0.1": [
                {
                    "accessor": "L1",
                    "binaryString": """LOCUS       L1                        55 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   0893fc2b9795b280f4c43ee3267489aa
VERSION     0893fc2b9795b280f4c43ee3267489aa
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..55
                     /label="L1"
ORIGIN
        1 ggctcgttac ttacgacact ccgagacagt cagagggtat ttattgaact agtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "L1",
                },
                {
                    "accessor": "L2",
                    "binaryString": """LOCUS       L2                        55 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   edd651940d345a5447cf8d52a7e55bb8
VERSION     edd651940d345a5447cf8d52a7e55bb8
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..55
                     /label="L2"
ORIGIN
        1 ggctcgatcg gtgtgaaaag tcagtatcca gtcgtgtagt tcttattacc tgtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "L2",
                },
                {
                    "accessor": "L3",
                    "binaryString": """LOCUS       L3                        55 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   97c74b65b44da2f7067b124118549149
VERSION     97c74b65b44da2f7067b124118549149
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..55
                     /label="L3"
ORIGIN
        1 ggctcgatca cggcactaca ctcgttgctt tatcggtatt gttattacag agtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "L3",
                },
                {
                    "accessor": "L4",
                    "binaryString": """LOCUS       L4                        55 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   7a22202a9f583aa0162a950092b42214
VERSION     7a22202a9f583aa0162a950092b42214
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..55
                     /label="L4"
ORIGIN
        1 ggctcgagaa gtagtgccac agacagtatt gcttacgagt tgatttatcc tgtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "L4",
                },
                {
                    "accessor": "L5",
                    "binaryString": """LOCUS       L5                        55 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   cc431c8b2d3171f61db4e06226457930
VERSION     cc431c8b2d3171f61db4e06226457930
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..55
                     /label="L5"
ORIGIN
        1 ggctcggtat tgtaaagcac gaaacctacg ataagagtgt cagttctcct tgtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "L5",
                },
                {
                    "accessor": "L6",
                    "binaryString": """LOCUS       L6                        55 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   0ce3392fcc9379be69a6827f905e0060
VERSION     0ce3392fcc9379be69a6827f905e0060
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..55
                     /label="L6"
ORIGIN
        1 ggctcgaact tttacgggtg ccgactcact attacagact tactacaatc tgtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "L6",
                },
                {
                    "accessor": "LMP",
                    "binaryString": """LOCUS       LMP                       57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   00d898637a50a35f638cd3c4bc3ef744
VERSION     00d898637a50a35f638cd3c4bc3ef744
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LMP",
                },
                {
                    "accessor": "LMS",
                    "binaryString": """LOCUS       LMS                       57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   1b62864ef7e8ad38d30e92a2dbc17670
VERSION     1b62864ef7e8ad38d30e92a2dbc17670
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMS"
ORIGIN
        1 ggctcgggag acctatcggt aataacagtc caatctggtg taacttcgga atcgtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LMS",
                },
                {
                    "accessor": "LF1",
                    "binaryString": """LOCUS       LF1                       54 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   3dba4a2ad654e64e225a6f2f8bb7af56
VERSION     3dba4a2ad654e64e225a6f2f8bb7af56
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..54
                     /label="LF1"
ORIGIN
        1 ggctcgggct cgggctccga aaacttgtac ttccagggat cgggctccgg gtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LF1",
                },
                {
                    "accessor": "LF2",
                    "binaryString": """LOCUS       LF2                       57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   9363b002ab3c87830711d0b41e4b64bf
VERSION     9363b002ab3c87830711d0b41e4b64bf
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LF2"
ORIGIN
        1 ggctcgggct cgggctccct ggaagttctg tttcaaggtc catcgggctc cgggtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LF2",
                },
                {
                    "accessor": "LF3",
                    "binaryString": """LOCUS       LF3                       54 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   e153fef2c069e165c5ec2dba6a1404da
VERSION     e153fef2c069e165c5ec2dba6a1404da
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..54
                     /label="LF3"
ORIGIN
        1 ggctcgggct cgggctccgg atctggttca ggttcaggat cgggctccgg gtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LF3",
                },
                {
                    "accessor": "LF4",
                    "binaryString": """LOCUS       LF4                       60 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   d5b4666ba1dd2443a66c39ab86faa6c9
VERSION     d5b4666ba1dd2443a66c39ab86faa6c9
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..60
                     /label="LF4"
ORIGIN
        1 ggctcgggct cgggctccgg atcaggatct ggttcaggtt caggatcggg ctccgggtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LF4",
                },
                {
                    "accessor": "LF5",
                    "binaryString": """LOCUS       LF5                       66 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   15593e99c7f9ee8ff0ad0a99fe8836c8
VERSION     15593e99c7f9ee8ff0ad0a99fe8836c8
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..66
                     /label="LF5"
ORIGIN
        1 ggctcgggct cgggctccgg atcaggatct ggttcaggtt caggatcagg atcgggctcc
       61 gggtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LF5",
                },
                {
                    "accessor": "LF6",
                    "binaryString": """LOCUS       LF6                       63 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   c13be98895e10de91aef13c0730dc91c
VERSION     c13be98895e10de91aef13c0730dc91c
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..63
                     /label="LF6"
ORIGIN
        1 ggctcggccg aagcggctgc taaagaagca gctgctaaag aggcggccgc caaggcaggg
       61 tcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "LF6",
                },
                {
                    "accessor": "UTR1-RBS1",
                    "binaryString": """LOCUS       UTR1-RBS1                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   64ae9c70fd948887b240d8ad3c6a5a76
VERSION     64ae9c70fd948887b240d8ad3c6a5a76
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR1-RBS1"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tcacacagga ctagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS1",
                },
                {
                    "accessor": "UTR1-RBS2",
                    "binaryString": """LOCUS       UTR1-RBS2                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   6bbd830ee167938f0dae3f872bc965b1
VERSION     6bbd830ee167938f0dae3f872bc965b1
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR1-RBS2"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa aagaggggaa atagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS2",
                },
                {
                    "accessor": "UTR1-RBS3",
                    "binaryString": """LOCUS       UTR1-RBS3                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   8cb7b58a64af42b6a789aff6c1964d71
VERSION     8cb7b58a64af42b6a789aff6c1964d71
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR1-RBS3"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa aagaggagaa atagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS3",
                },
                {
                    "accessor": "UTR1-RBS-A01",
                    "binaryString": """LOCUS       UTR1-RBS-A01              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   0907969930e261cda278aa298685f146
VERSION     0907969930e261cda278aa298685f146
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A01"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tctggggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A01",
                },
                {
                    "accessor": "UTR1-RBS-A02",
                    "binaryString": """LOCUS       UTR1-RBS-A02              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   baeee0c134f95d27d490ba64e60f5e21
VERSION     baeee0c134f95d27d490ba64e60f5e21
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A02"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tccggggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A02",
                },
                {
                    "accessor": "UTR1-RBS-A03",
                    "binaryString": """LOCUS       UTR1-RBS-A03              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   5cdc9bf0184268b9545803457105ee1c
VERSION     5cdc9bf0184268b9545803457105ee1c
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A03"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tctgaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A03",
                },
                {
                    "accessor": "UTR1-RBS-A04",
                    "binaryString": """LOCUS       UTR1-RBS-A04              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   391980d42f427c819286cbf9ad29d2a9
VERSION     391980d42f427c819286cbf9ad29d2a9
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A04"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tccagggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A04",
                },
                {
                    "accessor": "UTR1-RBS-A05",
                    "binaryString": """LOCUS       UTR1-RBS-A05              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   37e342ed4eb7552ec1d49e7f13510ba7
VERSION     37e342ed4eb7552ec1d49e7f13510ba7
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A05"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tcccgggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A05",
                },
                {
                    "accessor": "UTR1-RBS-A06",
                    "binaryString": """LOCUS       UTR1-RBS-A06              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   fa6d79f20fe200ab7372923981e65be7
VERSION     fa6d79f20fe200ab7372923981e65be7
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A06"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tccgaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A06",
                },
                {
                    "accessor": "UTR1-RBS-A07",
                    "binaryString": """LOCUS       UTR1-RBS-A07              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   5f7a05b009c57070b62ba9ccf0ed30a1
VERSION     5f7a05b009c57070b62ba9ccf0ed30a1
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A07"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tctcaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A07",
                },
                {
                    "accessor": "UTR1-RBS-A08",
                    "binaryString": """LOCUS       UTR1-RBS-A08              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   12b6f530b162ee31c3a6a51585c2b18c
VERSION     12b6f530b162ee31c3a6a51585c2b18c
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A08"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tccaaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A08",
                },
                {
                    "accessor": "UTR1-RBS-A09",
                    "binaryString": """LOCUS       UTR1-RBS-A09              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   752c823d5da16e77328abf1534185857
VERSION     752c823d5da16e77328abf1534185857
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A09"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tctagggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A09",
                },
                {
                    "accessor": "UTR1-RBS-A10",
                    "binaryString": """LOCUS       UTR1-RBS-A10              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   3279858541bb7efc8cbf57e7d2e47d2a
VERSION     3279858541bb7efc8cbf57e7d2e47d2a
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A10"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tcccaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A10",
                },
                {
                    "accessor": "UTR1-RBS-A11",
                    "binaryString": """LOCUS       UTR1-RBS-A11              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   2ac35f789459fe582bbf4fc4cd809ec0
VERSION     2ac35f789459fe582bbf4fc4cd809ec0
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A11"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tctcgggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A11",
                },
                {
                    "accessor": "UTR1-RBS-A12",
                    "binaryString": """LOCUS       UTR1-RBS-A12              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   7306fd414dbf389a2760afff5bf6a395
VERSION     7306fd414dbf389a2760afff5bf6a395
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-A12"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tctaaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-A12",
                },
                {
                    "accessor": "UTR2-RBS1",
                    "binaryString": """LOCUS       UTR2-RBS1                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   f0f4d42a987078be33f5b3a9c1dbc3cb
VERSION     f0f4d42a987078be33f5b3a9c1dbc3cb
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR2-RBS1"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tcacacagga ctagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS1",
                },
                {
                    "accessor": "UTR2-RBS2",
                    "binaryString": """LOCUS       UTR2-RBS2                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   ab672049c8b56106d458b65235492868
VERSION     ab672049c8b56106d458b65235492868
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR2-RBS2"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa aagaggggaa atagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS2",
                },
                {
                    "accessor": "UTR2-RBS3",
                    "binaryString": """LOCUS       UTR2-RBS3                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   d1b71c47c0be2efa1abad479c1ec5413
VERSION     d1b71c47c0be2efa1abad479c1ec5413
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR2-RBS3"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa aagaggagaa atagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS3",
                },
                {
                    "accessor": "UTR2-RBS-A01",
                    "binaryString": """LOCUS       UTR2-RBS-A01              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   718e056a59d5903802c37d9d6b3e5f90
VERSION     718e056a59d5903802c37d9d6b3e5f90
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A01"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tctggggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A01",
                },
                {
                    "accessor": "UTR2-RBS-A02",
                    "binaryString": """LOCUS       UTR2-RBS-A02              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   a6171892e133a3d2bcd6ababba241fe8
VERSION     a6171892e133a3d2bcd6ababba241fe8
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A02"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tccggggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A02",
                },
                {
                    "accessor": "UTR2-RBS-A03",
                    "binaryString": """LOCUS       UTR2-RBS-A03              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   685a5074af227291b1a223793eb50c5c
VERSION     685a5074af227291b1a223793eb50c5c
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A03"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tctgaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A03",
                },
                {
                    "accessor": "UTR2-RBS-A04",
                    "binaryString": """LOCUS       UTR2-RBS-A04              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   e7d767bd7fbe1e3212eb1d10bca1fd65
VERSION     e7d767bd7fbe1e3212eb1d10bca1fd65
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A04"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tccagggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A04",
                },
                {
                    "accessor": "UTR2-RBS-A05",
                    "binaryString": """LOCUS       UTR2-RBS-A05              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   d706b105571c3a4bafa1d04f3007b84b
VERSION     d706b105571c3a4bafa1d04f3007b84b
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A05"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tcccgggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A05",
                },
                {
                    "accessor": "UTR2-RBS-A06",
                    "binaryString": """LOCUS       UTR2-RBS-A06              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   f9374efcdb0a0e11bbe677f03d63d805
VERSION     f9374efcdb0a0e11bbe677f03d63d805
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A06"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tccgaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A06",
                },
                {
                    "accessor": "UTR2-RBS-A07",
                    "binaryString": """LOCUS       UTR2-RBS-A07              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   3a853eed70dd58e5d1c4788c31db5f87
VERSION     3a853eed70dd58e5d1c4788c31db5f87
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A07"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tctcaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A07",
                },
                {
                    "accessor": "UTR2-RBS-A08",
                    "binaryString": """LOCUS       UTR2-RBS-A08              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   7bdd5ddcf9c9164ed17af84788b5e4ee
VERSION     7bdd5ddcf9c9164ed17af84788b5e4ee
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A08"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tccaaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A08",
                },
                {
                    "accessor": "UTR2-RBS-A09",
                    "binaryString": """LOCUS       UTR2-RBS-A09              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   22661c99debdb0045cc853ebc5dc8168
VERSION     22661c99debdb0045cc853ebc5dc8168
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A09"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tctagggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A09",
                },
                {
                    "accessor": "UTR2-RBS-A10",
                    "binaryString": """LOCUS       UTR2-RBS-A10              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   1471223a787dc58a6499f26bba1178ce
VERSION     1471223a787dc58a6499f26bba1178ce
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A10"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tcccaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A10",
                },
                {
                    "accessor": "UTR2-RBS-A11",
                    "binaryString": """LOCUS       UTR2-RBS-A11              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   078fcc54c3bc19d2d40af6a50d5da5dd
VERSION     078fcc54c3bc19d2d40af6a50d5da5dd
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A11"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tctcgggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A11",
                },
                {
                    "accessor": "UTR2-RBS-A12",
                    "binaryString": """LOCUS       UTR2-RBS-A12              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   58b633636914793217f8b87cf9667e74
VERSION     58b633636914793217f8b87cf9667e74
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-A12"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tctaaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-A12",
                },
                {
                    "accessor": "UTR3-RBS1",
                    "binaryString": """LOCUS       UTR3-RBS1                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   bca77c7687ab87e13e28f91b224e774b
VERSION     bca77c7687ab87e13e28f91b224e774b
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR3-RBS1"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tcacacagga ctagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS1",
                },
                {
                    "accessor": "UTR3-RBS2",
                    "binaryString": """LOCUS       UTR3-RBS2                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   f012ae13cc4ea6fd256b9352284fb4e0
VERSION     f012ae13cc4ea6fd256b9352284fb4e0
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR3-RBS2"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa aagaggggaa atagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS2",
                },
                {
                    "accessor": "UTR3-RBS3",
                    "binaryString": """LOCUS       UTR3-RBS3                 57 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   2d97cb65f8cdc1ad30e1aeeaf2bee326
VERSION     2d97cb65f8cdc1ad30e1aeeaf2bee326
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="UTR3-RBS3"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa aagaggagaa atagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS3",
                },
                {
                    "accessor": "UTR3-RBS-A01",
                    "binaryString": """LOCUS       UTR3-RBS-A01              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   a56d39731ca82b3cb7546e8fc4a00d48
VERSION     a56d39731ca82b3cb7546e8fc4a00d48
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A01"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tctggggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A01",
                },
                {
                    "accessor": "UTR3-RBS-A02",
                    "binaryString": """LOCUS       UTR3-RBS-A02              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   668593d5460b6d84ebc0046dd0d33ef3
VERSION     668593d5460b6d84ebc0046dd0d33ef3
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A02"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tccggggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A02",
                },
                {
                    "accessor": "UTR3-RBS-A03",
                    "binaryString": """LOCUS       UTR3-RBS-A03              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   f3976d8ef3d08745c33eaf4de32909e3
VERSION     f3976d8ef3d08745c33eaf4de32909e3
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A03"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tctgaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A03",
                },
                {
                    "accessor": "UTR3-RBS-A04",
                    "binaryString": """LOCUS       UTR3-RBS-A04              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   2fdacd0087234f3ccfb2dc2923334178
VERSION     2fdacd0087234f3ccfb2dc2923334178
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A04"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tccagggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A04",
                },
                {
                    "accessor": "UTR3-RBS-A05",
                    "binaryString": """LOCUS       UTR3-RBS-A05              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   2ce398b62951e59ff1f79fc129d6597c
VERSION     2ce398b62951e59ff1f79fc129d6597c
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A05"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tcccgggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A05",
                },
                {
                    "accessor": "UTR3-RBS-A06",
                    "binaryString": """LOCUS       UTR3-RBS-A06              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   1b5be340f5cc1f618932601e4a63a755
VERSION     1b5be340f5cc1f618932601e4a63a755
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A06"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tccgaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A06",
                },
                {
                    "accessor": "UTR3-RBS-A07",
                    "binaryString": """LOCUS       UTR3-RBS-A07              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   73a8ff224fe7eaf60725634baa0247a7
VERSION     73a8ff224fe7eaf60725634baa0247a7
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A07"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tctcaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A07",
                },
                {
                    "accessor": "UTR3-RBS-A08",
                    "binaryString": """LOCUS       UTR3-RBS-A08              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   67cdcf1bc190bd99968c37f344530e6c
VERSION     67cdcf1bc190bd99968c37f344530e6c
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A08"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tccaaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A08",
                },
                {
                    "accessor": "UTR3-RBS-A09",
                    "binaryString": """LOCUS       UTR3-RBS-A09              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   98d31e83ff42da8a5fbc5ad79e794148
VERSION     98d31e83ff42da8a5fbc5ad79e794148
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A09"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tctagggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A09",
                },
                {
                    "accessor": "UTR3-RBS-A10",
                    "binaryString": """LOCUS       UTR3-RBS-A10              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   8b36ca67ee9eadf1f392e9aee3829773
VERSION     8b36ca67ee9eadf1f392e9aee3829773
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A10"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tcccaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A10",
                },
                {
                    "accessor": "UTR3-RBS-A11",
                    "binaryString": """LOCUS       UTR3-RBS-A11              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   8d48211a02d2270fbdfa8d80008893a1
VERSION     8d48211a02d2270fbdfa8d80008893a1
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A11"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tctcgggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A11",
                },
                {
                    "accessor": "UTR3-RBS-A12",
                    "binaryString": """LOCUS       UTR3-RBS-A12              56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   7ca01cfe4061cf2ceb4999cd99a026d8
VERSION     7ca01cfe4061cf2ceb4999cd99a026d8
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-A12"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tctaaggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-A12",
                },
                {
                    "accessor": "UTR1-RBS-AM12",
                    "binaryString": """LOCUS       UTR1-RBS-AM12             56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   874f2eec71f58b5ea689948f074d2d5a
VERSION     874f2eec71f58b5ea689948f074d2d5a
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-AM12"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tcyvrggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-AM12",
                },
                {
                    "accessor": "UTR1-RBS-AM24",
                    "binaryString": """LOCUS       UTR1-RBS-AM24             56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   4ec1b460101a3af758c528b91f3992bb
VERSION     4ec1b460101a3af758c528b91f3992bb
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR1-RBS-AM24"
ORIGIN
        1 ggctcgttga acaccgtctc aggtaagtat cagttgtaaa tcyvrggrgg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR1-RBS-AM24",
                },
                {
                    "accessor": "UTR2-RBS-AM12",
                    "binaryString": """LOCUS       UTR2-RBS-AM12             56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   08bd28b5b76160cd713a99bf67343daa
VERSION     08bd28b5b76160cd713a99bf67343daa
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-AM12"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tcyvrggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-AM12",
                },
                {
                    "accessor": "UTR2-RBS-AM24",
                    "binaryString": """LOCUS       UTR2-RBS-AM24             56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   e8066eb21f1d4809c78abd8925dd900e
VERSION     e8066eb21f1d4809c78abd8925dd900e
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR2-RBS-AM24"
ORIGIN
        1 ggctcgtgtt actattggct gagataaggg tagcagaaaa tcyvrggrgg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR2-RBS-AM24",
                },
                {
                    "accessor": "UTR3-RBS-AM12",
                    "binaryString": """LOCUS       UTR3-RBS-AM12             56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   f56ae28c523fde9db2521cc1adb8a5fa
VERSION     f56ae28c523fde9db2521cc1adb8a5fa
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-AM12"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tcyvrggagg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-AM12",
                },
                {
                    "accessor": "UTR3-RBS-AM24",
                    "binaryString": """LOCUS       UTR3-RBS-AM24             56 bp    DNA              UNK 01-JAN-1980
DEFINITION  visit https://www.biolegio.com/products-services/basic/ for further
            information..
ACCESSION   c1e2a75d330308ac4419cc0bd09b80c3
VERSION     c1e2a75d330308ac4419cc0bd09b80c3
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     misc_feature    3..56
                     /label="UTR3-RBS-AM24"
ORIGIN
        1 ggctcggtat ctcgtggtct gacggtaaaa tctattgtaa tcyvrggrgg tagtcc
//
""",
                    "collection": "BASIC_BIOLEGIO_LINKERS",
                    "description": "visit https://www.biolegio.com/products-services/basic/ for further information.",
                    "label": "UTR3-RBS-AM24",
                },
            ],
        },
        {
            "name": "BASIC_CDS_PARTS",
            "v0.1": [
                {
                    "accessor": "sfGFP",
                    "binaryString": """LOCUS       BASIC_sfGFP_CDS         3141 bp    DNA     circular UNK 23-JUL-2020
DEFINITION  sfGFP stored in BASIC_SEVA_18.
ACCESSION   f3eb90a77c18c828cc1c0e2ce99d9f83
VERSION     f3eb90a77c18c828cc1c0e2ce99d9f83
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    136..1174
                     /label="SEVA_Ap"
     regulatory      2191..2295
                     /label="SEVA_T1"
     misc_feature    1248..2176
                     /label="SEVA_pUC"
     regulatory      7..109
                     /label="SEVA_T0"
     misc_feature    2307..2361
                     /label="LMP"
     CDS             2362..3084
                     /label="sfGFP"
     misc_feature    3087..3141
                     /label="LMS"
ORIGIN
        1 actagtcttg gactcctgtt gatagatcca gtaatgacct cagaactcca tctggatttg
       61 ttcagaacgc tcggttgccg ccgggcgttt tttattggtg agaatccagg ggtccccaat
      121 aattacgatt taaattagta gcccgcctaa tgagcgggct tttttttaat tcccctattt
      181 gtttattttt ctaaatacat tcaaatatgt atccgctcat gagacaataa ccctgataaa
      241 tgcttcaata atattgaaaa aggaagagta tgagcattca gcattttcgt gtggcgctga
      301 ttccgttttt tgcggcgttt tgcctgccgg tgtttgcgca tccggaaacc ctggtgaaag
      361 tgaaagatgc ggaagatcaa ctgggtgcgc gcgtgggcta tattgaactg gatctgaaca
      421 gcggcaaaat tctggaatct tttcgtccgg aagaacgttt tccgatgatg agcaccttta
      481 aagtgctgct gtgcggtgcg gttctgagcc gtgtggatgc gggccaggaa caactgggcc
      541 gtcgtattca ttatagccag aacgatctgg tggaatatag cccggtgacc gaaaaacatc
      601 tgaccgatgg catgaccgtg cgtgaactgt gcagcgcggc gattaccatg agcgataaca
      661 ccgcggcgaa cctgctgctg acgaccattg gcggtccgaa agaactgacc gcgtttctgc
      721 ataacatggg cgatcatgtg acccgtctgg atcgttggga accggaactg aacgaagcga
      781 ttccgaacga tgaacgtgat accaccatgc cggcagcaat ggcgaccacc ctgcgtaaac
      841 tgctgacggg tgagctgctg accctggcaa gccgccagca actgattgat tggatggaag
      901 cggataaagt ggcgggtccg ctgctgcgta gcgcgctgcc ggctggctgg tttattgcgg
      961 ataaaagcgg tgcgggcgaa cgtggcagcc gtggcattat tgcggcgctg ggcccggatg
     1021 gtaaaccgag ccgtattgtg gtgatttata ccaccggcag ccaggcgacg atggatgaac
     1081 gtaaccgtca gattgcggaa attggcgcga gcctgattaa acattggtaa accgatacaa
     1141 ttaaaggctc cttttggagc cttttttttt ggacgaccct tgtcggctcg acccacgact
     1201 attgactgct ctgagaaagt tgattgttac gattagtccg gccggccccg tagaaaagat
     1261 caaaggatct tcttgagatc ctttttttct gcgcgtaatc tgctgcttgc aaacaaaaaa
     1321 accaccgcta ccagcggtgg tttgtttgcc ggatcaagag ctaccaactc tttttccgaa
     1381 ggtaactggc ttcagcagag cgcagatacc aaatactgtt cttctagtgt agccgtagtt
     1441 aggccaccac ttcaagaact ctgtagcacc gcctacatac ctcgctctgc taatcctgtt
     1501 accagtggct gctgccagtg gcgataagtc gtgtcttacc gggttggact caagacgata
     1561 gttaccggat aaggcgcagc ggtcgggctg aacggggggt tcgtgcacac agcccagctt
     1621 ggagcgaacg acctacaccg aactgagata cctacagcgt gagctttgag aaagcgccac
     1681 gcttcccgaa gggagaaagg cggacaggta tccggtaagc ggcagggtcg gaacaggaga
     1741 gcgcacgagg gagcttccag ggggaaacgc ctggtatctt tatagtcctg tcgggtttcg
     1801 ccacctctga cttgagcgtc gatttttgtg atgctcgtca ggggggcgga gcctatggaa
     1861 aaacgccagc aacgcggcct ttttacggtt cctggccttt tgctggcctt ttgctcacat
     1921 gttctttcct gcgttatccc ctgattctgt ggataaccgt attaccgcct ttgagtgagc
     1981 tgataccgct cgccgcagcc gaacgaccga gcgcagcgag tcagtgagcg aggaagcgga
     2041 agagcgccca atacgcaaac cgcctctccc cgcgcgttgg ccgattcatt aatgcagctg
     2101 gcacgacagg tttcccgact ggaaagcggg cagtgagcgc aacgcaatta atgtgagtta
     2161 gctcactcat taggcaggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga
     2221 gagcgttcac cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc
     2281 gttttatttg atgcctttaa ttaaggctcg ggtaagaact cgcacttcgt ggaaacacta
     2341 ttatctggtg ggtctctgtc catgcgtaaa ggcgaagaac tgttcacggg cgtagttccg
     2401 attctggtcg agctggacgg cgatgtgaac ggtcataagt ttagcgttcg cggtgaaggt
     2461 gagggcgacg cgaccaacgg caaactgacc ctgaagttca tctgcaccac cggtaaactg
     2521 ccggtgcctt ggccgacctt ggtgacgacg ttgacgtatg gcgtgcagtg ttttgcgcgt
     2581 tatccggacc acatgaaaca acacgatttc ttcaaatctg cgatgccgga gggttacgtc
     2641 caggagcgta ccatttcctt caaggatgat ggcacttaca aaactcgcgc agaggttaag
     2701 tttgaaggtg acacgctggt caatcgtatc gaattgaagg gtatcgactt taaagaggat
     2761 ggtaacattc tgggccataa actggagtat aacttcaaca gccataatgt ttacattacg
     2821 gcagacaagc aaaagaacgg catcaaggcc aatttcaaga ttcgccacaa tgttgaggac
     2881 ggtagcgtcc aactggccga ccattaccag cagaacaccc caattggtga cggtccggtt
     2941 ttgctgccgg ataatcacta tctgagcacc caaagcgtgc tgagcaaaga tccgaacgaa
     3001 aaacgtgatc acatggtcct gctggaattt gtgaccgctg cgggcatcac ccacggtatg
     3061 gacgagctgt ataagcgtcc gtaaggctcg ggagacctat cggtaataac agtccaatct
     3121 ggtgtaactt cggaatcgtc c
//
""",
                    "collection": "BASIC_CDS_PARTS",
                    "description": "sfGFP stored in BASIC_SEVA_18",
                    "label": "BASIC_sfGFP_CDS",
                },
                {
                    "accessor": "mCherry",
                    "binaryString": """LOCUS       BASIC_mCherry_CDS       3129 bp    DNA     circular UNK 23-JUL-2020
DEFINITION  mCherry stored in BASIC_SEVA_18.
ACCESSION   62771c44c2711126d5250509d5b64554
VERSION     62771c44c2711126d5250509d5b64554
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    136..1174
                     /label="SEVA_Ap"
     regulatory      2191..2295
                     /label="SEVA_T1"
     misc_feature    1248..2176
                     /label="SEVA_pUC"
     regulatory      7..109
                     /label="SEVA_T0"
     misc_feature    2307..2361
                     /label="LMP"
     CDS             2362..3072
                     /label="mCherry"
     misc_feature    3075..3129
                     /label="LMS"
ORIGIN
        1 actagtcttg gactcctgtt gatagatcca gtaatgacct cagaactcca tctggatttg
       61 ttcagaacgc tcggttgccg ccgggcgttt tttattggtg agaatccagg ggtccccaat
      121 aattacgatt taaattagta gcccgcctaa tgagcgggct tttttttaat tcccctattt
      181 gtttattttt ctaaatacat tcaaatatgt atccgctcat gagacaataa ccctgataaa
      241 tgcttcaata atattgaaaa aggaagagta tgagcattca gcattttcgt gtggcgctga
      301 ttccgttttt tgcggcgttt tgcctgccgg tgtttgcgca tccggaaacc ctggtgaaag
      361 tgaaagatgc ggaagatcaa ctgggtgcgc gcgtgggcta tattgaactg gatctgaaca
      421 gcggcaaaat tctggaatct tttcgtccgg aagaacgttt tccgatgatg agcaccttta
      481 aagtgctgct gtgcggtgcg gttctgagcc gtgtggatgc gggccaggaa caactgggcc
      541 gtcgtattca ttatagccag aacgatctgg tggaatatag cccggtgacc gaaaaacatc
      601 tgaccgatgg catgaccgtg cgtgaactgt gcagcgcggc gattaccatg agcgataaca
      661 ccgcggcgaa cctgctgctg acgaccattg gcggtccgaa agaactgacc gcgtttctgc
      721 ataacatggg cgatcatgtg acccgtctgg atcgttggga accggaactg aacgaagcga
      781 ttccgaacga tgaacgtgat accaccatgc cggcagcaat ggcgaccacc ctgcgtaaac
      841 tgctgacggg tgagctgctg accctggcaa gccgccagca actgattgat tggatggaag
      901 cggataaagt ggcgggtccg ctgctgcgta gcgcgctgcc ggctggctgg tttattgcgg
      961 ataaaagcgg tgcgggcgaa cgtggcagcc gtggcattat tgcggcgctg ggcccggatg
     1021 gtaaaccgag ccgtattgtg gtgatttata ccaccggcag ccaggcgacg atggatgaac
     1081 gtaaccgtca gattgcggaa attggcgcga gcctgattaa acattggtaa accgatacaa
     1141 ttaaaggctc cttttggagc cttttttttt ggacgaccct tgtcggctcg acccacgact
     1201 attgactgct ctgagaaagt tgattgttac gattagtccg gccggccccg tagaaaagat
     1261 caaaggatct tcttgagatc ctttttttct gcgcgtaatc tgctgcttgc aaacaaaaaa
     1321 accaccgcta ccagcggtgg tttgtttgcc ggatcaagag ctaccaactc tttttccgaa
     1381 ggtaactggc ttcagcagag cgcagatacc aaatactgtt cttctagtgt agccgtagtt
     1441 aggccaccac ttcaagaact ctgtagcacc gcctacatac ctcgctctgc taatcctgtt
     1501 accagtggct gctgccagtg gcgataagtc gtgtcttacc gggttggact caagacgata
     1561 gttaccggat aaggcgcagc ggtcgggctg aacggggggt tcgtgcacac agcccagctt
     1621 ggagcgaacg acctacaccg aactgagata cctacagcgt gagctttgag aaagcgccac
     1681 gcttcccgaa gggagaaagg cggacaggta tccggtaagc ggcagggtcg gaacaggaga
     1741 gcgcacgagg gagcttccag ggggaaacgc ctggtatctt tatagtcctg tcgggtttcg
     1801 ccacctctga cttgagcgtc gatttttgtg atgctcgtca ggggggcgga gcctatggaa
     1861 aaacgccagc aacgcggcct ttttacggtt cctggccttt tgctggcctt ttgctcacat
     1921 gttctttcct gcgttatccc ctgattctgt ggataaccgt attaccgcct ttgagtgagc
     1981 tgataccgct cgccgcagcc gaacgaccga gcgcagcgag tcagtgagcg aggaagcgga
     2041 agagcgccca atacgcaaac cgcctctccc cgcgcgttgg ccgattcatt aatgcagctg
     2101 gcacgacagg tttcccgact ggaaagcggg cagtgagcgc aacgcaatta atgtgagtta
     2161 gctcactcat taggcaggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga
     2221 gagcgttcac cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc
     2281 gttttatttg atgcctttaa ttaaggctcg ggtaagaact cgcacttcgt ggaaacacta
     2341 ttatctggtg ggtctctgtc catggtgagc aagggcgagg aggataacat ggccatcatc
     2401 aaggagttca tgcgcttcaa ggtgcacatg gagggctccg tgaacggcca cgagttcgag
     2461 atcgagggcg agggcgaggg ccgcccctac gagggcaccc agaccgccaa gctgaaggtg
     2521 accaagggtg gccccctgcc cttcgcctgg gacatcctgt cccctcagtt catgtacggc
     2581 tccaaggcct acgtgaagca ccccgccgac atccccgact acttgaagct gtccttcccc
     2641 gagggcttca agtgggagcg cgtgatgaac ttcgaggacg gcggcgtggt gaccgtgacc
     2701 caggactcct ccttgcagga cggcgagttc atctacaagg tgaagctgcg cggcaccaac
     2761 ttcccctccg acggccccgt aatgcagaag aagaccatgg gctgggaggc ctcctccgag
     2821 cggatgtacc ccgaggacgg cgccctgaag ggcgagatca agcagaggct gaagctgaag
     2881 gacggcggcc actacgacgc tgaggtcaag accacctaca aggccaagaa gcccgtgcag
     2941 ctgcccggcg cctacaacgt caacatcaag ttggacatca cctcccacaa cgaggactac
     3001 accatcgtgg aacagtacga acgcgccgag ggccgccact ccaccggcgg catggacgag
     3061 ctgtacaagt aaggctcggg agacctatcg gtaataacag tccaatctgg tgtaacttcg
     3121 gaatcgtcc
//
""",
                    "collection": "BASIC_CDS_PARTS",
                    "description": "mCherry stored in BASIC_SEVA_18",
                    "label": "BASIC_mCherry_CDS",
                },
                {
                    "accessor": "mTagBFP2",
                    "binaryString": """LOCUS       BASIC_mTagBFP2_CDS      3126 bp    DNA     circular UNK 23-JUL-2020
DEFINITION  mTagBFP2 stored in BASIC_SEVA_18.
ACCESSION   adb85d1208ec49e5cf26279bbf0391c0
VERSION     adb85d1208ec49e5cf26279bbf0391c0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    136..1174
                     /label="SEVA_Ap"
     regulatory      2191..2295
                     /label="SEVA_T1"
     misc_feature    1248..2176
                     /label="SEVA_pUC"
     regulatory      7..109
                     /label="SEVA_T0"
     misc_feature    2307..2361
                     /label="LMP"
     CDS             2362..3069
                     /label="mTagBFP2"
     misc_feature    3072..3126
                     /label="LMS"
ORIGIN
        1 actagtcttg gactcctgtt gatagatcca gtaatgacct cagaactcca tctggatttg
       61 ttcagaacgc tcggttgccg ccgggcgttt tttattggtg agaatccagg ggtccccaat
      121 aattacgatt taaattagta gcccgcctaa tgagcgggct tttttttaat tcccctattt
      181 gtttattttt ctaaatacat tcaaatatgt atccgctcat gagacaataa ccctgataaa
      241 tgcttcaata atattgaaaa aggaagagta tgagcattca gcattttcgt gtggcgctga
      301 ttccgttttt tgcggcgttt tgcctgccgg tgtttgcgca tccggaaacc ctggtgaaag
      361 tgaaagatgc ggaagatcaa ctgggtgcgc gcgtgggcta tattgaactg gatctgaaca
      421 gcggcaaaat tctggaatct tttcgtccgg aagaacgttt tccgatgatg agcaccttta
      481 aagtgctgct gtgcggtgcg gttctgagcc gtgtggatgc gggccaggaa caactgggcc
      541 gtcgtattca ttatagccag aacgatctgg tggaatatag cccggtgacc gaaaaacatc
      601 tgaccgatgg catgaccgtg cgtgaactgt gcagcgcggc gattaccatg agcgataaca
      661 ccgcggcgaa cctgctgctg acgaccattg gcggtccgaa agaactgacc gcgtttctgc
      721 ataacatggg cgatcatgtg acccgtctgg atcgttggga accggaactg aacgaagcga
      781 ttccgaacga tgaacgtgat accaccatgc cggcagcaat ggcgaccacc ctgcgtaaac
      841 tgctgacggg tgagctgctg accctggcaa gccgccagca actgattgat tggatggaag
      901 cggataaagt ggcgggtccg ctgctgcgta gcgcgctgcc ggctggctgg tttattgcgg
      961 ataaaagcgg tgcgggcgaa cgtggcagcc gtggcattat tgcggcgctg ggcccggatg
     1021 gtaaaccgag ccgtattgtg gtgatttata ccaccggcag ccaggcgacg atggatgaac
     1081 gtaaccgtca gattgcggaa attggcgcga gcctgattaa acattggtaa accgatacaa
     1141 ttaaaggctc cttttggagc cttttttttt ggacgaccct tgtcggctcg acccacgact
     1201 attgactgct ctgagaaagt tgattgttac gattagtccg gccggccccg tagaaaagat
     1261 caaaggatct tcttgagatc ctttttttct gcgcgtaatc tgctgcttgc aaacaaaaaa
     1321 accaccgcta ccagcggtgg tttgtttgcc ggatcaagag ctaccaactc tttttccgaa
     1381 ggtaactggc ttcagcagag cgcagatacc aaatactgtt cttctagtgt agccgtagtt
     1441 aggccaccac ttcaagaact ctgtagcacc gcctacatac ctcgctctgc taatcctgtt
     1501 accagtggct gctgccagtg gcgataagtc gtgtcttacc gggttggact caagacgata
     1561 gttaccggat aaggcgcagc ggtcgggctg aacggggggt tcgtgcacac agcccagctt
     1621 ggagcgaacg acctacaccg aactgagata cctacagcgt gagctttgag aaagcgccac
     1681 gcttcccgaa gggagaaagg cggacaggta tccggtaagc ggcagggtcg gaacaggaga
     1741 gcgcacgagg gagcttccag ggggaaacgc ctggtatctt tatagtcctg tcgggtttcg
     1801 ccacctctga cttgagcgtc gatttttgtg atgctcgtca ggggggcgga gcctatggaa
     1861 aaacgccagc aacgcggcct ttttacggtt cctggccttt tgctggcctt ttgctcacat
     1921 gttctttcct gcgttatccc ctgattctgt ggataaccgt attaccgcct ttgagtgagc
     1981 tgataccgct cgccgcagcc gaacgaccga gcgcagcgag tcagtgagcg aggaagcgga
     2041 agagcgccca atacgcaaac cgcctctccc cgcgcgttgg ccgattcatt aatgcagctg
     2101 gcacgacagg tttcccgact ggaaagcggg cagtgagcgc aacgcaatta atgtgagtta
     2161 gctcactcat taggcaggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga
     2221 gagcgttcac cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc
     2281 gttttatttg atgcctttaa ttaaggctcg ggtaagaact cgcacttcgt ggaaacacta
     2341 ttatctggtg ggtctctgtc catgtccgag ttgatcaaag agaacatgca tatgaaatta
     2401 tatatggaag gcactgtaga taatcatcat tttaaatgta cgtcggaagg cgaaggtaaa
     2461 ccatatgaag gtacgcagac gatgcgcatc aaggtggtgg agggcggtcc gctgccattc
     2521 gctttcgata ttttagccac gagcttcctc tacggttcta aaactttcat caatcacacg
     2581 cagggtattc cggacttctt taaacagtcg ttcccggagg gtttcacctg ggaacgcgtt
     2641 accacgtatg aagatggtgg tgtgcttacg gcaacgcagg acacgagcct tcaggatggg
     2701 tgtttgattt acaacgtgaa aattcgtggt gtgaacttca cgtctaacgg cccggtgatg
     2761 cagaaaaaaa cactgggttg ggaagccttt accgaaaccc tgtatccggc ggacggtggc
     2821 ctggaaggcc gtaatgatat ggccttgaaa ttagtcggcg gttcacacct gatcgcgaac
     2881 gcgaaaacaa cctatcgtag taaaaaacca gccaaaaacc tgaaaatgcc gggcgtctac
     2941 tacgtagact accgtctgga gcgcattaaa gaggcgaata atgaaaccta tgtcgagcag
     3001 cacgaagttg cggttgcacg ctattgcgat ctgcccagca aactgggcca caagcttaat
     3061 ggtagctaag gctcgggaga cctatcggta ataacagtcc aatctggtgt aacttcggaa
     3121 tcgtcc
//
""",
                    "collection": "BASIC_CDS_PARTS",
                    "description": "mTagBFP2 stored in BASIC_SEVA_18",
                    "label": "BASIC_mTagBFP2_CDS",
                },
            ],
        },
        {
            "name": "BASIC_PROMOTER_PARTS",
            "v0.1": [
                {
                    "accessor": "B-P1",
                    "binaryString": """LOCUS       B-P1_Terminator1_J23119_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P1 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P1,
            contains a J23119 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   140aff43fdac9c3adddb754116e1630b
VERSION     140aff43fdac9c3adddb754116e1630b
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      139..173
                     /label="J23119"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt gacagctagc tcagtcctag gtataatgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P1 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P1, contains a J23119 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P1_Terminator1_J23119_RiboA",
                },
                {
                    "accessor": "B-P2",
                    "binaryString": """LOCUS       B-P2_Terminator1_J23111_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P2 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P2,
            contains a J23111 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   373e6bfcc3cfd521c725e6667029aa9f
VERSION     373e6bfcc3cfd521c725e6667029aa9f
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      139..173
                     /label="J23111"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt gacggctagc tcagtcctag gtatagtgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P2 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P2, contains a J23111 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P2_Terminator1_J23111_RiboA",
                },
                {
                    "accessor": "B-P3",
                    "binaryString": """LOCUS       B-P3_Terminator1_J23104_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P3 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P3,
            contains a J23104 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   04dd87f307037cb34338c8d46fdec78a
VERSION     04dd87f307037cb34338c8d46fdec78a
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      139..173
                     /label="J23104"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt gacagctagc tcagtcctag gtattgtgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P3 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P3, contains a J23104 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P3_Terminator1_J23104_RiboA",
                },
                {
                    "accessor": "B-P4",
                    "binaryString": """LOCUS       B-P4_Terminator1_J23101_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P4 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P4,
            contains a J23101 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   93fdffea8985598476d07a621ab13441
VERSION     93fdffea8985598476d07a621ab13441
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      139..173
                     /label="J23101"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt tacagctagc tcagtcctag gtattatgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P4 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P4, contains a J23101 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P4_Terminator1_J23101_RiboA",
                },
                {
                    "accessor": "B-P5",
                    "binaryString": """LOCUS       B-P5_Terminator1_J23108_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P5 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P5,
            contains a J23108 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   741f2bdde85d6df3b029ceddf0560ba1
VERSION     741f2bdde85d6df3b029ceddf0560ba1
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      139..173
                     /label="J23108"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctct gacagctagc tcagtcctag gtataatgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P5 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P5, contains a J23108 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P5_Terminator1_J23108_RiboA",
                },
                {
                    "accessor": "B-P6",
                    "binaryString": """LOCUS       B-P6_Terminator1_J23106_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P6 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P6,
            contains a J23106 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   fd822f2a69a7d1fba7843f933c1d7a30
VERSION     fd822f2a69a7d1fba7843f933c1d7a30
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      139..173
                     /label="J23106"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt tacggctagc tcagtcctag gtatagtgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P6 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P6, contains a J23106 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P6_Terminator1_J23106_RiboA",
                },
                {
                    "accessor": "B-P7",
                    "binaryString": """LOCUS       B-P7_Terminator1_J23105_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P7 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P7,
            contains a J23105 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   63f7d6ad25024b0a6501661f11b70416
VERSION     63f7d6ad25024b0a6501661f11b70416
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      139..173
                     /label="J23105"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt tacggctagc tcagtcctag gtactatgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P7 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P7, contains a J23105 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P7_Terminator1_J23105_RiboA",
                },
                {
                    "accessor": "B-P8",
                    "binaryString": """LOCUS       B-P8_Terminator1_J23116_RiboA 2609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P8 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P8,
            contains a J23116 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   b376f975081d9e9d603a43174ff51509
VERSION     b376f975081d9e9d603a43174ff51509
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     regulatory      139..173
                     /label="J23116"
     misc_feature    174..248
                     /label="RiboA"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    251..305
                     /label="LMS"
     misc_feature    441..1479
                     /label="SEVA_Ap"
     misc_feature    1553..2481
                     /label="SEVA_pUC"
     misc_feature    312..414
                     /label="SEVA_T0"
     misc_feature    2496..2600
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt gacagctagc tcagtcctag ggactatgct agcagctgtc
      181 accggatgtg ctttccggtc tgatgagtcc gtgaggacga aacagcctct acaaataatt
      241 ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
      301 cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg
      361 atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc
      421 ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc
      481 tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg
      541 ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc
      601 gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt
      661 gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct
      721 gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac
      781 ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact
      841 gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa
      901 acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga
      961 taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt
     1021 tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga
     1081 agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg
     1141 taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat
     1201 ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat
     1261 tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc
     1321 ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga
     1381 tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga
     1441 tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca
     1501 cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa
     1561 aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca
     1621 aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt
     1681 ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg
     1741 tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc
     1801 ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga
     1861 cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc
     1921 agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc
     1981 gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca
     2041 ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg
     2101 tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta
     2161 tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct
     2221 cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag
     2281 tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa
     2341 gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc
     2401 agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg
     2461 agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact
     2521 caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc
     2581 ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P8 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P8, contains a J23116 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P8_Terminator1_J23116_RiboA",
                },
                {
                    "accessor": "B-P9",
                    "binaryString": """LOCUS       B-P9_Terminator2_J23119_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P9 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P9,
            contains a J23119 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   e0be959d24f89e3a21244d76abfca953
VERSION     e0be959d24f89e3a21244d76abfca953
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    170..244
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     regulatory      135..169
                     /label="J23119"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctttgaca gctagctcag tcctaggtat aatgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P9 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P9, contains a J23119 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P9_Terminator2_J23119_RiboB",
                },
                {
                    "accessor": "B-P10",
                    "binaryString": """LOCUS       B-P10_Terminator2_J23111_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P10 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P10,
            contains a J23111 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   ee7183692c893fa4a0e463be64c0067b
VERSION     ee7183692c893fa4a0e463be64c0067b
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      135..169
                     /label="J23111"
     misc_feature    170..244
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctttgacg gctagctcag tcctaggtat agtgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P10 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P10, contains a J23111 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P10_Terminator2_J23111_RiboB",
                },
                {
                    "accessor": "B-P11",
                    "binaryString": """LOCUS       B-P11_Terminator2_J23104_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P11 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P11,
            contains a J23104 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   baee1c5c40e63e2c9846dec120fe97f4
VERSION     baee1c5c40e63e2c9846dec120fe97f4
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    170..244
                     /label="RiboB"
     regulatory      135..169
                     /label="J23104"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctttgaca gctagctcag tcctaggtat tgtgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P11 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P11, contains a J23104 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P11_Terminator2_J23104_RiboB",
                },
                {
                    "accessor": "B-P12",
                    "binaryString": """LOCUS       B-P12_Terminator2_J23101_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P12 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P12,
            contains a J23101 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   6fb15e609c9e58b6249ab21587510d0e
VERSION     6fb15e609c9e58b6249ab21587510d0e
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      135..169
                     /label="J23101"
     misc_feature    170..244
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttttaca gctagctcag tcctaggtat tatgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P12 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P12, contains a J23101 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P12_Terminator2_J23101_RiboB",
                },
                {
                    "accessor": "B-P13",
                    "binaryString": """LOCUS       B-P13_Terminator2_J23108_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P13 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P13,
            contains a J23108 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   c3c77ad0c5b3ae043d031657f7b21c62
VERSION     c3c77ad0c5b3ae043d031657f7b21c62
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..114
                     /label="Terminator2"
     regulatory      135..169
                     /label="J23108"
     misc_feature    170..244
                     /label="RiboB"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctctgaca gctagctcag tcctaggtat aatgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P13 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P13, contains a J23108 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P13_Terminator2_J23108_RiboB",
                },
                {
                    "accessor": "B-P14",
                    "binaryString": """LOCUS       B-P14_Terminator2_J23106_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P14 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P14,
            contains a J23106 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   d9ef427406d95e12935e346c0aca1ff0
VERSION     d9ef427406d95e12935e346c0aca1ff0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    170..244
                     /label="RiboB"
     regulatory      135..169
                     /label="J23106"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttttacg gctagctcag tcctaggtat agtgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P14 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P14, contains a J23106 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P14_Terminator2_J23106_RiboB",
                },
                {
                    "accessor": "B-P15",
                    "binaryString": """LOCUS       B-P15_Terminator2_J23105_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P15 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P15,
            contains a J23105 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   0c1318ac5dd7dc9f013463d281b442f6
VERSION     0c1318ac5dd7dc9f013463d281b442f6
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    170..244
                     /label="RiboB"
     regulatory      135..169
                     /label="J23105"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttttacg gctagctcag tcctaggtac tatgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P15 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P15, contains a J23105 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P15_Terminator2_J23105_RiboB",
                },
                {
                    "accessor": "B-P16",
                    "binaryString": """LOCUS       B-P16_Terminator2_J23116_RiboB 2605 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P16 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P16,
            contains a J23116 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   c88d787d494b6416793f6171b143710d
VERSION     c88d787d494b6416793f6171b143710d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    170..244
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     regulatory      135..169
                     /label="J23116"
     misc_feature    247..301
                     /label="LMS"
     misc_feature    437..1475
                     /label="SEVA_Ap"
     misc_feature    1549..2477
                     /label="SEVA_pUC"
     misc_feature    308..410
                     /label="SEVA_T0"
     misc_feature    2492..2596
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctttgaca gctagctcag tcctagggac tatgctagca gcgctcaacg
      181 ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc gcctctacaa ataattttgt
      241 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
      301 cactagtctt ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt
      361 gttcagaacg ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa
      421 taattacgat ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt
      481 tgtttatttt tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa
      541 atgcttcaat aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg
      601 attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa
      661 gtgaaagatg cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac
      721 agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt
      781 aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc
      841 cgtcgtattc attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat
      901 ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac
      961 accgcggcga acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg
     1021 cataacatgg gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg
     1081 attccgaacg atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa
     1141 ctgctgacgg gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa
     1201 gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg
     1261 gataaaagcg gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat
     1321 ggtaaaccga gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa
     1381 cgtaaccgtc agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca
     1441 attaaaggct ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac
     1501 tattgactgc tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga
     1561 tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa
     1621 aaccaccgct accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga
     1681 aggtaactgg cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt
     1741 taggccacca cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt
     1801 taccagtggc tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat
     1861 agttaccgga taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct
     1921 tggagcgaac gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca
     1981 cgcttcccga agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag
     2041 agcgcacgag ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc
     2101 gccacctctg acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga
     2161 aaaacgccag caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca
     2221 tgttctttcc tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag
     2281 ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg
     2341 aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct
     2401 ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt
     2461 agctcactca ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg
     2521 agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt
     2581 cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P16 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P16, contains a J23116 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P16_Terminator2_J23116_RiboB",
                },
                {
                    "accessor": "B-P17",
                    "binaryString": """LOCUS       B-P17_Terminator3_J23119_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P17 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P17,
            contains a J23119 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   95e12f081eb6c938b7b5761f722fc567
VERSION     95e12f081eb6c938b7b5761f722fc567
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      129..163
                     /label="J23119"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    164..238
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt gacagctagc tcagtcctag gtataatgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P17 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P17, contains a J23119 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P17_Terminator3_J23119_RiboC",
                },
                {
                    "accessor": "B-P18",
                    "binaryString": """LOCUS       B-P18_Terminator3_J23111_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P18 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P18,
            contains a J23111 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   3be3cf2b12c9b3c5c25488190a874b86
VERSION     3be3cf2b12c9b3c5c25488190a874b86
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    164..238
                     /label="RiboC"
     regulatory      129..163
                     /label="J23111"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt gacggctagc tcagtcctag gtatagtgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P18 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P18, contains a J23111 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P18_Terminator3_J23111_RiboC",
                },
                {
                    "accessor": "B-P19",
                    "binaryString": """LOCUS       B-P19_Terminator3_J23104_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P19 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P19,
            contains a J23104 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   da194de45dd62324fb2035cb22679a2e
VERSION     da194de45dd62324fb2035cb22679a2e
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..108
                     /label="Terminator3"
     regulatory      129..163
                     /label="J23104"
     misc_feature    164..238
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt gacagctagc tcagtcctag gtattgtgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P19 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P19, contains a J23104 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P19_Terminator3_J23104_RiboC",
                },
                {
                    "accessor": "B-P20",
                    "binaryString": """LOCUS       B-P20_Terminator3_J23101_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P20 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P20,
            contains a J23101 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   029367dd9ae1ce3bca4c3df38ebdacbe
VERSION     029367dd9ae1ce3bca4c3df38ebdacbe
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    164..238
                     /label="RiboC"
     regulatory      58..108
                     /label="Terminator3"
     regulatory      129..163
                     /label="J23101"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt tacagctagc tcagtcctag gtattatgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P20 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P20, contains a J23101 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P20_Terminator3_J23101_RiboC",
                },
                {
                    "accessor": "B-P21",
                    "binaryString": """LOCUS       B-P21_Terminator3_J23108_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P21 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P21,
            contains a J23108 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   c1414fc1f7dc4ae25dcdf61e0e04473a
VERSION     c1414fc1f7dc4ae25dcdf61e0e04473a
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      129..163
                     /label="J23108"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    164..238
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctct gacagctagc tcagtcctag gtataatgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P21 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P21, contains a J23108 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P21_Terminator3_J23108_RiboC",
                },
                {
                    "accessor": "B-P22",
                    "binaryString": """LOCUS       B-P22_Terminator3_J23106_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P22 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P22,
            contains a J23106 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   57c8fdd1cbcfa1b30a14ee5c2207f399
VERSION     57c8fdd1cbcfa1b30a14ee5c2207f399
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      129..163
                     /label="J23106"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    164..238
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt tacggctagc tcagtcctag gtatagtgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P22 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P22, contains a J23106 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P22_Terminator3_J23106_RiboC",
                },
                {
                    "accessor": "B-P23",
                    "binaryString": """LOCUS       B-P23_Terminator3_J23105_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P23 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P23,
            contains a J23105 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   59081ef7095a024cd8526c81cf96b257
VERSION     59081ef7095a024cd8526c81cf96b257
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    164..238
                     /label="RiboC"
     regulatory      58..108
                     /label="Terminator3"
     regulatory      129..163
                     /label="J23105"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt tacggctagc tcagtcctag gtactatgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P23 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P23, contains a J23105 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P23_Terminator3_J23105_RiboC",
                },
                {
                    "accessor": "B-P24",
                    "binaryString": """LOCUS       B-P24_Terminator3_J23116_RiboC 2599 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P24 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P24,
            contains a J23116 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   70ac2741b20f24c0500471a4063566e3
VERSION     70ac2741b20f24c0500471a4063566e3
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    164..238
                     /label="RiboC"
     regulatory      129..163
                     /label="J23116"
     misc_feature    241..295
                     /label="LMS"
     misc_feature    431..1469
                     /label="SEVA_Ap"
     misc_feature    1543..2471
                     /label="SEVA_pUC"
     misc_feature    302..404
                     /label="SEVA_T0"
     misc_feature    2486..2590
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt gacagctagc tcagtcctag ggactatgct agcagtagtc accggctgtg
      181 cttgccggtc tgatgagcct gtgaaggcga aactacctct acaaataatt ttgtttaagg
      241 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccactag
      301 tcttggactc ctgttgatag atccagtaat gacctcagaa ctccatctgg atttgttcag
      361 aacgctcggt tgccgccggg cgttttttat tggtgagaat ccaggggtcc ccaataatta
      421 cgatttaaat tagtagcccg cctaatgagc gggctttttt ttaattcccc tatttgttta
      481 tttttctaaa tacattcaaa tatgtatccg ctcatgagac aataaccctg ataaatgctt
      541 caataatatt gaaaaaggaa gagtatgagc attcagcatt ttcgtgtggc gctgattccg
      601 ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg aaaccctggt gaaagtgaaa
      661 gatgcggaag atcaactggg tgcgcgcgtg ggctatattg aactggatct gaacagcggc
      721 aaaattctgg aatcttttcg tccggaagaa cgttttccga tgatgagcac ctttaaagtg
      781 ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc aggaacaact gggccgtcgt
      841 attcattata gccagaacga tctggtggaa tatagcccgg tgaccgaaaa acatctgacc
      901 gatggcatga ccgtgcgtga actgtgcagc gcggcgatta ccatgagcga taacaccgcg
      961 gcgaacctgc tgctgacgac cattggcggt ccgaaagaac tgaccgcgtt tctgcataac
     1021 atgggcgatc atgtgacccg tctggatcgt tgggaaccgg aactgaacga agcgattccg
     1081 aacgatgaac gtgataccac catgccggca gcaatggcga ccaccctgcg taaactgctg
     1141 acgggtgagc tgctgaccct ggcaagccgc cagcaactga ttgattggat ggaagcggat
     1201 aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg gctggtttat tgcggataaa
     1261 agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg cgctgggccc ggatggtaaa
     1321 ccgagccgta ttgtggtgat ttataccacc ggcagccagg cgacgatgga tgaacgtaac
     1381 cgtcagattg cggaaattgg cgcgagcctg attaaacatt ggtaaaccga tacaattaaa
     1441 ggctcctttt ggagcctttt tttttggacg acccttgtcg gctcgaccca cgactattga
     1501 ctgctctgag aaagttgatt gttacgatta gtccggccgg ccccgtagaa aagatcaaag
     1561 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1621 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1681 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1741 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1801 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1861 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1921 gaacgaccta caccgaactg agatacctac agcgtgagct ttgagaaagc gccacgcttc
     1981 ccgaagggag aaaggcggac aggtatccgg taagcggcag ggtcggaaca ggagagcgca
     2041 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     2101 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     2161 ccagcaacgc ggccttttta cggttcctgg ccttttgctg gccttttgct cacatgttct
     2221 ttcctgcgtt atcccctgat tctgtggata accgtattac cgcctttgag tgagctgata
     2281 ccgctcgccg cagccgaacg accgagcgca gcgagtcagt gagcgaggaa gcggaagagc
     2341 gcccaatacg caaaccgcct ctccccgcgc gttggccgat tcattaatgc agctggcacg
     2401 acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc aattaatgtg agttagctca
     2461 ctcattaggc aggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     2521 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     2581 atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P24 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P24, contains a J23116 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P24_Terminator3_J23116_RiboC",
                },
                {
                    "accessor": "B-P25",
                    "binaryString": """LOCUS       B-P25_Terminator1_Phlf_RiboA 2640 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P25 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P25,
            contains a Phlf promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   c5c99d6f9edc250cc2036824925fef12
VERSION     c5c99d6f9edc250cc2036824925fef12
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     regulatory      139..204
                     /label="Phlf"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    205..279
                     /label="RiboA"
     misc_feature    282..336
                     /label="LMS"
     misc_feature    472..1510
                     /label="SEVA_Ap"
     misc_feature    1584..2512
                     /label="SEVA_pUC"
     misc_feature    343..445
                     /label="SEVA_T0"
     misc_feature    2527..2631
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctcg acgtacggtg gaatctgatt cgttaccaat tgacatgata
      181 cgaaacgtac cgtatcgtta aggtagctgt caccggatgt gctttccggt ctgatgagtc
      241 cgtgaggacg aaacagcctc tacaaataat tttgtttaag gctcgggaga cctatcggta
      301 ataacagtcc aatctggtgt aacttcggaa tcgtccacta gtcttggact cctgttgata
      361 gatccagtaa tgacctcaga actccatctg gatttgttca gaacgctcgg ttgccgccgg
      421 gcgtttttta ttggtgagaa tccaggggtc cccaataatt acgatttaaa ttagtagccc
      481 gcctaatgag cgggcttttt tttaattccc ctatttgttt atttttctaa atacattcaa
      541 atatgtatcc gctcatgaga caataaccct gataaatgct tcaataatat tgaaaaagga
      601 agagtatgag cattcagcat tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc
      661 tgccggtgtt tgcgcatccg gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg
      721 gtgcgcgcgt gggctatatt gaactggatc tgaacagcgg caaaattctg gaatcttttc
      781 gtccggaaga acgttttccg atgatgagca cctttaaagt gctgctgtgc ggtgcggttc
      841 tgagccgtgt ggatgcgggc caggaacaac tgggccgtcg tattcattat agccagaacg
      901 atctggtgga atatagcccg gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg
      961 aactgtgcag cgcggcgatt accatgagcg ataacaccgc ggcgaacctg ctgctgacga
     1021 ccattggcgg tccgaaagaa ctgaccgcgt ttctgcataa catgggcgat catgtgaccc
     1081 gtctggatcg ttgggaaccg gaactgaacg aagcgattcc gaacgatgaa cgtgatacca
     1141 ccatgccggc agcaatggcg accaccctgc gtaaactgct gacgggtgag ctgctgaccc
     1201 tggcaagccg ccagcaactg attgattgga tggaagcgga taaagtggcg ggtccgctgc
     1261 tgcgtagcgc gctgccggct ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg
     1321 gcagccgtgg cattattgcg gcgctgggcc cggatggtaa accgagccgt attgtggtga
     1381 tttataccac cggcagccag gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg
     1441 gcgcgagcct gattaaacat tggtaaaccg atacaattaa aggctccttt tggagccttt
     1501 ttttttggac gacccttgtc ggctcgaccc acgactattg actgctctga gaaagttgat
     1561 tgttacgatt agtccggccg gccccgtaga aaagatcaaa ggatcttctt gagatccttt
     1621 ttttctgcgc gtaatctgct gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg
     1681 tttgccggat caagagctac caactctttt tccgaaggta actggcttca gcagagcgca
     1741 gataccaaat actgttcttc tagtgtagcc gtagttaggc caccacttca agaactctgt
     1801 agcaccgcct acatacctcg ctctgctaat cctgttacca gtggctgctg ccagtggcga
     1861 taagtcgtgt cttaccgggt tggactcaag acgatagtta ccggataagg cgcagcggtc
     1921 gggctgaacg gggggttcgt gcacacagcc cagcttggag cgaacgacct acaccgaact
     1981 gagataccta cagcgtgagc tttgagaaag cgccacgctt cccgaaggga gaaaggcgga
     2041 caggtatccg gtaagcggca gggtcggaac aggagagcgc acgagggagc ttccaggggg
     2101 aaacgcctgg tatctttata gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt
     2161 tttgtgatgc tcgtcagggg ggcggagcct atggaaaaac gccagcaacg cggccttttt
     2221 acggttcctg gccttttgct ggccttttgc tcacatgttc tttcctgcgt tatcccctga
     2281 ttctgtggat aaccgtatta ccgcctttga gtgagctgat accgctcgcc gcagccgaac
     2341 gaccgagcgc agcgagtcag tgagcgagga agcggaagag cgcccaatac gcaaaccgcc
     2401 tctccccgcg cgttggccga ttcattaatg cagctggcac gacaggtttc ccgactggaa
     2461 agcgggcagt gagcgcaacg caattaatgt gagttagctc actcattagg caggcgcgcc
     2521 cagctgtcta gggcggcgga tttgtcctac tcaggagagc gttcaccgac aaacaacaga
     2581 taaaacgaaa ggcccagtct ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P25 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P25, contains a Phlf promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P25_Terminator1_Phlf_RiboA",
                },
                {
                    "accessor": "B-P26",
                    "binaryString": """LOCUS       B-P26_Terminator1_CymR_RiboA 2664 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P26 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P26,
            contains a CymR promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   fc616faf5b211f7257d4ff95be8331ab
VERSION     fc616faf5b211f7257d4ff95be8331ab
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..118
                     /label="Terminator1"
     regulatory      139..228
                     /label="CymR"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    229..303
                     /label="RiboA"
     misc_feature    306..360
                     /label="LMS"
     misc_feature    496..1534
                     /label="SEVA_Ap"
     misc_feature    1608..2536
                     /label="SEVA_pUC"
     misc_feature    367..469
                     /label="SEVA_T0"
     misc_feature    2551..2655
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctaa caaacagaca atctggtctg tttgtattat ggaaaatttt
      181 tctgtataat agattcaaca aacagacaat ctggtctgtt tgtattatag ctgtcaccgg
      241 atgtgctttc cggtctgatg agtccgtgag gacgaaacag cctctacaaa taattttgtt
      301 taaggctcgg gagacctatc ggtaataaca gtccaatctg gtgtaacttc ggaatcgtcc
      361 actagtcttg gactcctgtt gatagatcca gtaatgacct cagaactcca tctggatttg
      421 ttcagaacgc tcggttgccg ccgggcgttt tttattggtg agaatccagg ggtccccaat
      481 aattacgatt taaattagta gcccgcctaa tgagcgggct tttttttaat tcccctattt
      541 gtttattttt ctaaatacat tcaaatatgt atccgctcat gagacaataa ccctgataaa
      601 tgcttcaata atattgaaaa aggaagagta tgagcattca gcattttcgt gtggcgctga
      661 ttccgttttt tgcggcgttt tgcctgccgg tgtttgcgca tccggaaacc ctggtgaaag
      721 tgaaagatgc ggaagatcaa ctgggtgcgc gcgtgggcta tattgaactg gatctgaaca
      781 gcggcaaaat tctggaatct tttcgtccgg aagaacgttt tccgatgatg agcaccttta
      841 aagtgctgct gtgcggtgcg gttctgagcc gtgtggatgc gggccaggaa caactgggcc
      901 gtcgtattca ttatagccag aacgatctgg tggaatatag cccggtgacc gaaaaacatc
      961 tgaccgatgg catgaccgtg cgtgaactgt gcagcgcggc gattaccatg agcgataaca
     1021 ccgcggcgaa cctgctgctg acgaccattg gcggtccgaa agaactgacc gcgtttctgc
     1081 ataacatggg cgatcatgtg acccgtctgg atcgttggga accggaactg aacgaagcga
     1141 ttccgaacga tgaacgtgat accaccatgc cggcagcaat ggcgaccacc ctgcgtaaac
     1201 tgctgacggg tgagctgctg accctggcaa gccgccagca actgattgat tggatggaag
     1261 cggataaagt ggcgggtccg ctgctgcgta gcgcgctgcc ggctggctgg tttattgcgg
     1321 ataaaagcgg tgcgggcgaa cgtggcagcc gtggcattat tgcggcgctg ggcccggatg
     1381 gtaaaccgag ccgtattgtg gtgatttata ccaccggcag ccaggcgacg atggatgaac
     1441 gtaaccgtca gattgcggaa attggcgcga gcctgattaa acattggtaa accgatacaa
     1501 ttaaaggctc cttttggagc cttttttttt ggacgaccct tgtcggctcg acccacgact
     1561 attgactgct ctgagaaagt tgattgttac gattagtccg gccggccccg tagaaaagat
     1621 caaaggatct tcttgagatc ctttttttct gcgcgtaatc tgctgcttgc aaacaaaaaa
     1681 accaccgcta ccagcggtgg tttgtttgcc ggatcaagag ctaccaactc tttttccgaa
     1741 ggtaactggc ttcagcagag cgcagatacc aaatactgtt cttctagtgt agccgtagtt
     1801 aggccaccac ttcaagaact ctgtagcacc gcctacatac ctcgctctgc taatcctgtt
     1861 accagtggct gctgccagtg gcgataagtc gtgtcttacc gggttggact caagacgata
     1921 gttaccggat aaggcgcagc ggtcgggctg aacggggggt tcgtgcacac agcccagctt
     1981 ggagcgaacg acctacaccg aactgagata cctacagcgt gagctttgag aaagcgccac
     2041 gcttcccgaa gggagaaagg cggacaggta tccggtaagc ggcagggtcg gaacaggaga
     2101 gcgcacgagg gagcttccag ggggaaacgc ctggtatctt tatagtcctg tcgggtttcg
     2161 ccacctctga cttgagcgtc gatttttgtg atgctcgtca ggggggcgga gcctatggaa
     2221 aaacgccagc aacgcggcct ttttacggtt cctggccttt tgctggcctt ttgctcacat
     2281 gttctttcct gcgttatccc ctgattctgt ggataaccgt attaccgcct ttgagtgagc
     2341 tgataccgct cgccgcagcc gaacgaccga gcgcagcgag tcagtgagcg aggaagcgga
     2401 agagcgccca atacgcaaac cgcctctccc cgcgcgttgg ccgattcatt aatgcagctg
     2461 gcacgacagg tttcccgact ggaaagcggg cagtgagcgc aacgcaatta atgtgagtta
     2521 gctcactcat taggcaggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga
     2581 gagcgttcac cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc
     2641 gttttatttg atgcctttaa ttaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P26 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P26, contains a CymR promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P26_Terminator1_CymR_RiboA",
                },
                {
                    "accessor": "B-P27",
                    "binaryString": """LOCUS       B-P27_Terminator1_TetR_RiboA 2650 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P27 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P27,
            contains a TetR promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   43e265b986607ce818f4106171afb6da
VERSION     43e265b986607ce818f4106171afb6da
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    215..289
                     /label="RiboA"
     regulatory      139..214
                     /label="TetR"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    292..346
                     /label="LMS"
     misc_feature    482..1520
                     /label="SEVA_Ap"
     misc_feature    1594..2522
                     /label="SEVA_pUC"
     misc_feature    353..455
                     /label="SEVA_T0"
     misc_feature    2537..2641
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttt ttcagcagga cgcactgacc tccctatcag tgatagagat
      181 tgacatccct atcagtgata gagatactga gcacagctgt caccggatgt gctttccggt
      241 ctgatgagtc cgtgaggacg aaacagcctc tacaaataat tttgtttaag gctcgggaga
      301 cctatcggta ataacagtcc aatctggtgt aacttcggaa tcgtccacta gtcttggact
      361 cctgttgata gatccagtaa tgacctcaga actccatctg gatttgttca gaacgctcgg
      421 ttgccgccgg gcgtttttta ttggtgagaa tccaggggtc cccaataatt acgatttaaa
      481 ttagtagccc gcctaatgag cgggcttttt tttaattccc ctatttgttt atttttctaa
      541 atacattcaa atatgtatcc gctcatgaga caataaccct gataaatgct tcaataatat
      601 tgaaaaagga agagtatgag cattcagcat tttcgtgtgg cgctgattcc gttttttgcg
      661 gcgttttgcc tgccggtgtt tgcgcatccg gaaaccctgg tgaaagtgaa agatgcggaa
      721 gatcaactgg gtgcgcgcgt gggctatatt gaactggatc tgaacagcgg caaaattctg
      781 gaatcttttc gtccggaaga acgttttccg atgatgagca cctttaaagt gctgctgtgc
      841 ggtgcggttc tgagccgtgt ggatgcgggc caggaacaac tgggccgtcg tattcattat
      901 agccagaacg atctggtgga atatagcccg gtgaccgaaa aacatctgac cgatggcatg
      961 accgtgcgtg aactgtgcag cgcggcgatt accatgagcg ataacaccgc ggcgaacctg
     1021 ctgctgacga ccattggcgg tccgaaagaa ctgaccgcgt ttctgcataa catgggcgat
     1081 catgtgaccc gtctggatcg ttgggaaccg gaactgaacg aagcgattcc gaacgatgaa
     1141 cgtgatacca ccatgccggc agcaatggcg accaccctgc gtaaactgct gacgggtgag
     1201 ctgctgaccc tggcaagccg ccagcaactg attgattgga tggaagcgga taaagtggcg
     1261 ggtccgctgc tgcgtagcgc gctgccggct ggctggttta ttgcggataa aagcggtgcg
     1321 ggcgaacgtg gcagccgtgg cattattgcg gcgctgggcc cggatggtaa accgagccgt
     1381 attgtggtga tttataccac cggcagccag gcgacgatgg atgaacgtaa ccgtcagatt
     1441 gcggaaattg gcgcgagcct gattaaacat tggtaaaccg atacaattaa aggctccttt
     1501 tggagccttt ttttttggac gacccttgtc ggctcgaccc acgactattg actgctctga
     1561 gaaagttgat tgttacgatt agtccggccg gccccgtaga aaagatcaaa ggatcttctt
     1621 gagatccttt ttttctgcgc gtaatctgct gcttgcaaac aaaaaaacca ccgctaccag
     1681 cggtggtttg tttgccggat caagagctac caactctttt tccgaaggta actggcttca
     1741 gcagagcgca gataccaaat actgttcttc tagtgtagcc gtagttaggc caccacttca
     1801 agaactctgt agcaccgcct acatacctcg ctctgctaat cctgttacca gtggctgctg
     1861 ccagtggcga taagtcgtgt cttaccgggt tggactcaag acgatagtta ccggataagg
     1921 cgcagcggtc gggctgaacg gggggttcgt gcacacagcc cagcttggag cgaacgacct
     1981 acaccgaact gagataccta cagcgtgagc tttgagaaag cgccacgctt cccgaaggga
     2041 gaaaggcgga caggtatccg gtaagcggca gggtcggaac aggagagcgc acgagggagc
     2101 ttccaggggg aaacgcctgg tatctttata gtcctgtcgg gtttcgccac ctctgacttg
     2161 agcgtcgatt tttgtgatgc tcgtcagggg ggcggagcct atggaaaaac gccagcaacg
     2221 cggccttttt acggttcctg gccttttgct ggccttttgc tcacatgttc tttcctgcgt
     2281 tatcccctga ttctgtggat aaccgtatta ccgcctttga gtgagctgat accgctcgcc
     2341 gcagccgaac gaccgagcgc agcgagtcag tgagcgagga agcggaagag cgcccaatac
     2401 gcaaaccgcc tctccccgcg cgttggccga ttcattaatg cagctggcac gacaggtttc
     2461 ccgactggaa agcgggcagt gagcgcaacg caattaatgt gagttagctc actcattagg
     2521 caggcgcgcc cagctgtcta gggcggcgga tttgtcctac tcaggagagc gttcaccgac
     2581 aaacaacaga taaaacgaaa ggcccagtct ttcgactgag cctttcgttt tatttgatgc
     2641 ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P27 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P27, contains a TetR promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P27_Terminator1_TetR_RiboA",
                },
                {
                    "accessor": "B-P28",
                    "binaryString": """LOCUS       B-P28_Terminator1_VanR_RiboA 2624 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P28 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P28,
            contains a VanR promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   498d8f796750f5ab0cb36d73b1e471d6
VERSION     498d8f796750f5ab0cb36d73b1e471d6
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      139..188
                     /label="VanR"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    189..263
                     /label="RiboA"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    266..320
                     /label="LMS"
     misc_feature    456..1494
                     /label="SEVA_Ap"
     misc_feature    1568..2496
                     /label="SEVA_pUC"
     misc_feature    327..429
                     /label="SEVA_T0"
     misc_feature    2511..2615
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctat tggatccaat tgacagctag ctcagtccta ggtaccattg
      181 gatccaatag ctgtcaccgg atgtgctttc cggtctgatg agtccgtgag gacgaaacag
      241 cctctacaaa taattttgtt taaggctcgg gagacctatc ggtaataaca gtccaatctg
      301 gtgtaacttc ggaatcgtcc actagtcttg gactcctgtt gatagatcca gtaatgacct
      361 cagaactcca tctggatttg ttcagaacgc tcggttgccg ccgggcgttt tttattggtg
      421 agaatccagg ggtccccaat aattacgatt taaattagta gcccgcctaa tgagcgggct
      481 tttttttaat tcccctattt gtttattttt ctaaatacat tcaaatatgt atccgctcat
      541 gagacaataa ccctgataaa tgcttcaata atattgaaaa aggaagagta tgagcattca
      601 gcattttcgt gtggcgctga ttccgttttt tgcggcgttt tgcctgccgg tgtttgcgca
      661 tccggaaacc ctggtgaaag tgaaagatgc ggaagatcaa ctgggtgcgc gcgtgggcta
      721 tattgaactg gatctgaaca gcggcaaaat tctggaatct tttcgtccgg aagaacgttt
      781 tccgatgatg agcaccttta aagtgctgct gtgcggtgcg gttctgagcc gtgtggatgc
      841 gggccaggaa caactgggcc gtcgtattca ttatagccag aacgatctgg tggaatatag
      901 cccggtgacc gaaaaacatc tgaccgatgg catgaccgtg cgtgaactgt gcagcgcggc
      961 gattaccatg agcgataaca ccgcggcgaa cctgctgctg acgaccattg gcggtccgaa
     1021 agaactgacc gcgtttctgc ataacatggg cgatcatgtg acccgtctgg atcgttggga
     1081 accggaactg aacgaagcga ttccgaacga tgaacgtgat accaccatgc cggcagcaat
     1141 ggcgaccacc ctgcgtaaac tgctgacggg tgagctgctg accctggcaa gccgccagca
     1201 actgattgat tggatggaag cggataaagt ggcgggtccg ctgctgcgta gcgcgctgcc
     1261 ggctggctgg tttattgcgg ataaaagcgg tgcgggcgaa cgtggcagcc gtggcattat
     1321 tgcggcgctg ggcccggatg gtaaaccgag ccgtattgtg gtgatttata ccaccggcag
     1381 ccaggcgacg atggatgaac gtaaccgtca gattgcggaa attggcgcga gcctgattaa
     1441 acattggtaa accgatacaa ttaaaggctc cttttggagc cttttttttt ggacgaccct
     1501 tgtcggctcg acccacgact attgactgct ctgagaaagt tgattgttac gattagtccg
     1561 gccggccccg tagaaaagat caaaggatct tcttgagatc ctttttttct gcgcgtaatc
     1621 tgctgcttgc aaacaaaaaa accaccgcta ccagcggtgg tttgtttgcc ggatcaagag
     1681 ctaccaactc tttttccgaa ggtaactggc ttcagcagag cgcagatacc aaatactgtt
     1741 cttctagtgt agccgtagtt aggccaccac ttcaagaact ctgtagcacc gcctacatac
     1801 ctcgctctgc taatcctgtt accagtggct gctgccagtg gcgataagtc gtgtcttacc
     1861 gggttggact caagacgata gttaccggat aaggcgcagc ggtcgggctg aacggggggt
     1921 tcgtgcacac agcccagctt ggagcgaacg acctacaccg aactgagata cctacagcgt
     1981 gagctttgag aaagcgccac gcttcccgaa gggagaaagg cggacaggta tccggtaagc
     2041 ggcagggtcg gaacaggaga gcgcacgagg gagcttccag ggggaaacgc ctggtatctt
     2101 tatagtcctg tcgggtttcg ccacctctga cttgagcgtc gatttttgtg atgctcgtca
     2161 ggggggcgga gcctatggaa aaacgccagc aacgcggcct ttttacggtt cctggccttt
     2221 tgctggcctt ttgctcacat gttctttcct gcgttatccc ctgattctgt ggataaccgt
     2281 attaccgcct ttgagtgagc tgataccgct cgccgcagcc gaacgaccga gcgcagcgag
     2341 tcagtgagcg aggaagcgga agagcgccca atacgcaaac cgcctctccc cgcgcgttgg
     2401 ccgattcatt aatgcagctg gcacgacagg tttcccgact ggaaagcggg cagtgagcgc
     2461 aacgcaatta atgtgagtta gctcactcat taggcaggcg cgcccagctg tctagggcgg
     2521 cggatttgtc ctactcagga gagcgttcac cgacaaacaa cagataaaac gaaaggccca
     2581 gtctttcgac tgagcctttc gttttatttg atgcctttaa ttaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P28 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P28, contains a VanR promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P28_Terminator1_VanR_RiboA",
                },
                {
                    "accessor": "B-P29",
                    "binaryString": """LOCUS       B-P29_Terminator1_LuxR_RiboA 2629 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P29 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P29,
            contains a LuxR promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   85bcb7964cf965dab7c268797d4b14b6
VERSION     85bcb7964cf965dab7c268797d4b14b6
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    194..268
                     /label="RiboA"
     misc_feature    119..138
                     /label="SpacerA"
     regulatory      139..193
                     /label="LuxR"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    271..325
                     /label="LMS"
     misc_feature    461..1499
                     /label="SEVA_Ap"
     misc_feature    1573..2501
                     /label="SEVA_pUC"
     misc_feature    332..434
                     /label="SEVA_T0"
     misc_feature    2516..2620
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctac ctgtaggatc gtacaggttt acgcaagaaa atggtttgtt
      181 acagtcgaat aaaagctgtc accggatgtg ctttccggtc tgatgagtcc gtgaggacga
      241 aacagcctct acaaataatt ttgtttaagg ctcgggagac ctatcggtaa taacagtcca
      301 atctggtgta acttcggaat cgtccactag tcttggactc ctgttgatag atccagtaat
      361 gacctcagaa ctccatctgg atttgttcag aacgctcggt tgccgccggg cgttttttat
      421 tggtgagaat ccaggggtcc ccaataatta cgatttaaat tagtagcccg cctaatgagc
      481 gggctttttt ttaattcccc tatttgttta tttttctaaa tacattcaaa tatgtatccg
      541 ctcatgagac aataaccctg ataaatgctt caataatatt gaaaaaggaa gagtatgagc
      601 attcagcatt ttcgtgtggc gctgattccg ttttttgcgg cgttttgcct gccggtgttt
      661 gcgcatccgg aaaccctggt gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg
      721 ggctatattg aactggatct gaacagcggc aaaattctgg aatcttttcg tccggaagaa
      781 cgttttccga tgatgagcac ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg
      841 gatgcgggcc aggaacaact gggccgtcgt attcattata gccagaacga tctggtggaa
      901 tatagcccgg tgaccgaaaa acatctgacc gatggcatga ccgtgcgtga actgtgcagc
      961 gcggcgatta ccatgagcga taacaccgcg gcgaacctgc tgctgacgac cattggcggt
     1021 ccgaaagaac tgaccgcgtt tctgcataac atgggcgatc atgtgacccg tctggatcgt
     1081 tgggaaccgg aactgaacga agcgattccg aacgatgaac gtgataccac catgccggca
     1141 gcaatggcga ccaccctgcg taaactgctg acgggtgagc tgctgaccct ggcaagccgc
     1201 cagcaactga ttgattggat ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg
     1261 ctgccggctg gctggtttat tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc
     1321 attattgcgg cgctgggccc ggatggtaaa ccgagccgta ttgtggtgat ttataccacc
     1381 ggcagccagg cgacgatgga tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg
     1441 attaaacatt ggtaaaccga tacaattaaa ggctcctttt ggagcctttt tttttggacg
     1501 acccttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt gttacgatta
     1561 gtccggccgg ccccgtagaa aagatcaaag gatcttcttg agatcctttt tttctgcgcg
     1621 taatctgctg cttgcaaaca aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc
     1681 aagagctacc aactcttttt ccgaaggtaa ctggcttcag cagagcgcag ataccaaata
     1741 ctgttcttct agtgtagccg tagttaggcc accacttcaa gaactctgta gcaccgccta
     1801 catacctcgc tctgctaatc ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc
     1861 ttaccgggtt ggactcaaga cgatagttac cggataaggc gcagcggtcg ggctgaacgg
     1921 ggggttcgtg cacacagccc agcttggagc gaacgaccta caccgaactg agatacctac
     1981 agcgtgagct ttgagaaagc gccacgcttc ccgaagggag aaaggcggac aggtatccgg
     2041 taagcggcag ggtcggaaca ggagagcgca cgagggagct tccaggggga aacgcctggt
     2101 atctttatag tcctgtcggg tttcgccacc tctgacttga gcgtcgattt ttgtgatgct
     2161 cgtcaggggg gcggagccta tggaaaaacg ccagcaacgc ggccttttta cggttcctgg
     2221 ccttttgctg gccttttgct cacatgttct ttcctgcgtt atcccctgat tctgtggata
     2281 accgtattac cgcctttgag tgagctgata ccgctcgccg cagccgaacg accgagcgca
     2341 gcgagtcagt gagcgaggaa gcggaagagc gcccaatacg caaaccgcct ctccccgcgc
     2401 gttggccgat tcattaatgc agctggcacg acaggtttcc cgactggaaa gcgggcagtg
     2461 agcgcaacgc aattaatgtg agttagctca ctcattaggc aggcgcgccc agctgtctag
     2521 ggcggcggat ttgtcctact caggagagcg ttcaccgaca aacaacagat aaaacgaaag
     2581 gcccagtctt tcgactgagc ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P29 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P29, contains a LuxR promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P29_Terminator1_LuxR_RiboA",
                },
                {
                    "accessor": "B-P30",
                    "binaryString": """LOCUS       B-P30_Terminator1_CinR_RiboA 2800 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P30 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P30,
            contains a CinR promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   850bbaead5b517b1ce7474177d789a12
VERSION     850bbaead5b517b1ce7474177d789a12
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      139..364
                     /label="CinR"
     misc_feature    365..439
                     /label="RiboA"
     misc_feature    119..138
                     /label="SpacerA"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    442..496
                     /label="LMS"
     misc_feature    632..1670
                     /label="SEVA_Ap"
     misc_feature    1744..2672
                     /label="SEVA_pUC"
     misc_feature    503..605
                     /label="SEVA_T0"
     misc_feature    2687..2791
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctcc ctttgtgcgt ccaaacggac gcacggcgct ctaaagcggg
      181 tcgcgatctt tcagattcgc tcctcgcgct ttcagtcttt gttttggcgc atgtcgttat
      241 cgcaaaaccg ctgcacactt ttgcgcgaca tgctctgatc cccctcatct gggggggcct
      301 atctgaggga atttccgatc cggctcgcct gaaccattct gctttccacg aacttgaaaa
      361 cgctagctgt caccggatgt gctttccggt ctgatgagtc cgtgaggacg aaacagcctc
      421 tacaaataat tttgtttaag gctcgggaga cctatcggta ataacagtcc aatctggtgt
      481 aacttcggaa tcgtccacta gtcttggact cctgttgata gatccagtaa tgacctcaga
      541 actccatctg gatttgttca gaacgctcgg ttgccgccgg gcgtttttta ttggtgagaa
      601 tccaggggtc cccaataatt acgatttaaa ttagtagccc gcctaatgag cgggcttttt
      661 tttaattccc ctatttgttt atttttctaa atacattcaa atatgtatcc gctcatgaga
      721 caataaccct gataaatgct tcaataatat tgaaaaagga agagtatgag cattcagcat
      781 tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc tgccggtgtt tgcgcatccg
      841 gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg gtgcgcgcgt gggctatatt
      901 gaactggatc tgaacagcgg caaaattctg gaatcttttc gtccggaaga acgttttccg
      961 atgatgagca cctttaaagt gctgctgtgc ggtgcggttc tgagccgtgt ggatgcgggc
     1021 caggaacaac tgggccgtcg tattcattat agccagaacg atctggtgga atatagcccg
     1081 gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg aactgtgcag cgcggcgatt
     1141 accatgagcg ataacaccgc ggcgaacctg ctgctgacga ccattggcgg tccgaaagaa
     1201 ctgaccgcgt ttctgcataa catgggcgat catgtgaccc gtctggatcg ttgggaaccg
     1261 gaactgaacg aagcgattcc gaacgatgaa cgtgatacca ccatgccggc agcaatggcg
     1321 accaccctgc gtaaactgct gacgggtgag ctgctgaccc tggcaagccg ccagcaactg
     1381 attgattgga tggaagcgga taaagtggcg ggtccgctgc tgcgtagcgc gctgccggct
     1441 ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg gcagccgtgg cattattgcg
     1501 gcgctgggcc cggatggtaa accgagccgt attgtggtga tttataccac cggcagccag
     1561 gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg gcgcgagcct gattaaacat
     1621 tggtaaaccg atacaattaa aggctccttt tggagccttt ttttttggac gacccttgtc
     1681 ggctcgaccc acgactattg actgctctga gaaagttgat tgttacgatt agtccggccg
     1741 gccccgtaga aaagatcaaa ggatcttctt gagatccttt ttttctgcgc gtaatctgct
     1801 gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg tttgccggat caagagctac
     1861 caactctttt tccgaaggta actggcttca gcagagcgca gataccaaat actgttcttc
     1921 tagtgtagcc gtagttaggc caccacttca agaactctgt agcaccgcct acatacctcg
     1981 ctctgctaat cctgttacca gtggctgctg ccagtggcga taagtcgtgt cttaccgggt
     2041 tggactcaag acgatagtta ccggataagg cgcagcggtc gggctgaacg gggggttcgt
     2101 gcacacagcc cagcttggag cgaacgacct acaccgaact gagataccta cagcgtgagc
     2161 tttgagaaag cgccacgctt cccgaaggga gaaaggcgga caggtatccg gtaagcggca
     2221 gggtcggaac aggagagcgc acgagggagc ttccaggggg aaacgcctgg tatctttata
     2281 gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt tttgtgatgc tcgtcagggg
     2341 ggcggagcct atggaaaaac gccagcaacg cggccttttt acggttcctg gccttttgct
     2401 ggccttttgc tcacatgttc tttcctgcgt tatcccctga ttctgtggat aaccgtatta
     2461 ccgcctttga gtgagctgat accgctcgcc gcagccgaac gaccgagcgc agcgagtcag
     2521 tgagcgagga agcggaagag cgcccaatac gcaaaccgcc tctccccgcg cgttggccga
     2581 ttcattaatg cagctggcac gacaggtttc ccgactggaa agcgggcagt gagcgcaacg
     2641 caattaatgt gagttagctc actcattagg caggcgcgcc cagctgtcta gggcggcgga
     2701 tttgtcctac tcaggagagc gttcaccgac aaacaacaga taaaacgaaa ggcccagtct
     2761 ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P30 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P30, contains a CinR promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P30_Terminator1_CinR_RiboA",
                },
                {
                    "accessor": "B-P31",
                    "binaryString": """LOCUS       B-P31_Terminator1_LacI_RiboA 2630 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P31 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P31,
            contains a LacI promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   799e7bc2877a34a4e77979a5a5dd7e32
VERSION     799e7bc2877a34a4e77979a5a5dd7e32
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    195..269
                     /label="RiboA"
     regulatory      139..194
                     /label="LacI"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    272..326
                     /label="LMS"
     misc_feature    462..1500
                     /label="SEVA_Ap"
     misc_feature    1574..2502
                     /label="SEVA_pUC"
     misc_feature    333..435
                     /label="SEVA_T0"
     misc_feature    2517..2621
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatcttg ttgacaatta atcatcggct cgtataatgt gtggaattgt
      181 gagcgctcac aattagctgt caccggatgt gctttccggt ctgatgagtc cgtgaggacg
      241 aaacagcctc tacaaataat tttgtttaag gctcgggaga cctatcggta ataacagtcc
      301 aatctggtgt aacttcggaa tcgtccacta gtcttggact cctgttgata gatccagtaa
      361 tgacctcaga actccatctg gatttgttca gaacgctcgg ttgccgccgg gcgtttttta
      421 ttggtgagaa tccaggggtc cccaataatt acgatttaaa ttagtagccc gcctaatgag
      481 cgggcttttt tttaattccc ctatttgttt atttttctaa atacattcaa atatgtatcc
      541 gctcatgaga caataaccct gataaatgct tcaataatat tgaaaaagga agagtatgag
      601 cattcagcat tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc tgccggtgtt
      661 tgcgcatccg gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg gtgcgcgcgt
      721 gggctatatt gaactggatc tgaacagcgg caaaattctg gaatcttttc gtccggaaga
      781 acgttttccg atgatgagca cctttaaagt gctgctgtgc ggtgcggttc tgagccgtgt
      841 ggatgcgggc caggaacaac tgggccgtcg tattcattat agccagaacg atctggtgga
      901 atatagcccg gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg aactgtgcag
      961 cgcggcgatt accatgagcg ataacaccgc ggcgaacctg ctgctgacga ccattggcgg
     1021 tccgaaagaa ctgaccgcgt ttctgcataa catgggcgat catgtgaccc gtctggatcg
     1081 ttgggaaccg gaactgaacg aagcgattcc gaacgatgaa cgtgatacca ccatgccggc
     1141 agcaatggcg accaccctgc gtaaactgct gacgggtgag ctgctgaccc tggcaagccg
     1201 ccagcaactg attgattgga tggaagcgga taaagtggcg ggtccgctgc tgcgtagcgc
     1261 gctgccggct ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg gcagccgtgg
     1321 cattattgcg gcgctgggcc cggatggtaa accgagccgt attgtggtga tttataccac
     1381 cggcagccag gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg gcgcgagcct
     1441 gattaaacat tggtaaaccg atacaattaa aggctccttt tggagccttt ttttttggac
     1501 gacccttgtc ggctcgaccc acgactattg actgctctga gaaagttgat tgttacgatt
     1561 agtccggccg gccccgtaga aaagatcaaa ggatcttctt gagatccttt ttttctgcgc
     1621 gtaatctgct gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg tttgccggat
     1681 caagagctac caactctttt tccgaaggta actggcttca gcagagcgca gataccaaat
     1741 actgttcttc tagtgtagcc gtagttaggc caccacttca agaactctgt agcaccgcct
     1801 acatacctcg ctctgctaat cctgttacca gtggctgctg ccagtggcga taagtcgtgt
     1861 cttaccgggt tggactcaag acgatagtta ccggataagg cgcagcggtc gggctgaacg
     1921 gggggttcgt gcacacagcc cagcttggag cgaacgacct acaccgaact gagataccta
     1981 cagcgtgagc tttgagaaag cgccacgctt cccgaaggga gaaaggcgga caggtatccg
     2041 gtaagcggca gggtcggaac aggagagcgc acgagggagc ttccaggggg aaacgcctgg
     2101 tatctttata gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt tttgtgatgc
     2161 tcgtcagggg ggcggagcct atggaaaaac gccagcaacg cggccttttt acggttcctg
     2221 gccttttgct ggccttttgc tcacatgttc tttcctgcgt tatcccctga ttctgtggat
     2281 aaccgtatta ccgcctttga gtgagctgat accgctcgcc gcagccgaac gaccgagcgc
     2341 agcgagtcag tgagcgagga agcggaagag cgcccaatac gcaaaccgcc tctccccgcg
     2401 cgttggccga ttcattaatg cagctggcac gacaggtttc ccgactggaa agcgggcagt
     2461 gagcgcaacg caattaatgt gagttagctc actcattagg caggcgcgcc cagctgtcta
     2521 gggcggcgga tttgtcctac tcaggagagc gttcaccgac aaacaacaga taaaacgaaa
     2581 ggcccagtct ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P31 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P31, contains a LacI promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P31_Terminator1_LacI_RiboA",
                },
                {
                    "accessor": "B-P32",
                    "binaryString": """LOCUS       B-P32_Terminator1_AraC_RiboA 2863 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P32 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P32,
            contains a AraC promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   65323e3f101fdfa95119f88b5a422479
VERSION     65323e3f101fdfa95119f88b5a422479
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     regulatory      139..427
                     /label="AraC"
     misc_feature    428..502
                     /label="RiboA"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    505..559
                     /label="LMS"
     misc_feature    695..1733
                     /label="SEVA_Ap"
     misc_feature    1807..2735
                     /label="SEVA_pUC"
     misc_feature    566..668
                     /label="SEVA_T0"
     misc_feature    2750..2854
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctag aaaccaattg tccatattgc atcagacatt gccgtcactg
      181 cgtcttttac tggctcttct cgctaaccaa accggtaacc ccgcttatta aaagcattct
      241 gtaacaaagc gggaccaaag ccatgacaaa aacgcgtaac aaaagtgtct ataatcacgg
      301 cagaaaagtc cacattgatt atttgcacgg cgtcacactt tgctatgcca tagcattttt
      361 atccataaga ttagcggatc ctacctgacg ctttttatcg caactctcta ctgtttctcc
      421 atacccgagc tgtcaccgga tgtgctttcc ggtctgatga gtccgtgagg acgaaacagc
      481 ctctacaaat aattttgttt aaggctcggg agacctatcg gtaataacag tccaatctgg
      541 tgtaacttcg gaatcgtcca ctagtcttgg actcctgttg atagatccag taatgacctc
      601 agaactccat ctggatttgt tcagaacgct cggttgccgc cgggcgtttt ttattggtga
      661 gaatccaggg gtccccaata attacgattt aaattagtag cccgcctaat gagcgggctt
      721 ttttttaatt cccctatttg tttatttttc taaatacatt caaatatgta tccgctcatg
      781 agacaataac cctgataaat gcttcaataa tattgaaaaa ggaagagtat gagcattcag
      841 cattttcgtg tggcgctgat tccgtttttt gcggcgtttt gcctgccggt gtttgcgcat
      901 ccggaaaccc tggtgaaagt gaaagatgcg gaagatcaac tgggtgcgcg cgtgggctat
      961 attgaactgg atctgaacag cggcaaaatt ctggaatctt ttcgtccgga agaacgtttt
     1021 ccgatgatga gcacctttaa agtgctgctg tgcggtgcgg ttctgagccg tgtggatgcg
     1081 ggccaggaac aactgggccg tcgtattcat tatagccaga acgatctggt ggaatatagc
     1141 ccggtgaccg aaaaacatct gaccgatggc atgaccgtgc gtgaactgtg cagcgcggcg
     1201 attaccatga gcgataacac cgcggcgaac ctgctgctga cgaccattgg cggtccgaaa
     1261 gaactgaccg cgtttctgca taacatgggc gatcatgtga cccgtctgga tcgttgggaa
     1321 ccggaactga acgaagcgat tccgaacgat gaacgtgata ccaccatgcc ggcagcaatg
     1381 gcgaccaccc tgcgtaaact gctgacgggt gagctgctga ccctggcaag ccgccagcaa
     1441 ctgattgatt ggatggaagc ggataaagtg gcgggtccgc tgctgcgtag cgcgctgccg
     1501 gctggctggt ttattgcgga taaaagcggt gcgggcgaac gtggcagccg tggcattatt
     1561 gcggcgctgg gcccggatgg taaaccgagc cgtattgtgg tgatttatac caccggcagc
     1621 caggcgacga tggatgaacg taaccgtcag attgcggaaa ttggcgcgag cctgattaaa
     1681 cattggtaaa ccgatacaat taaaggctcc ttttggagcc tttttttttg gacgaccctt
     1741 gtcggctcga cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg
     1801 ccggccccgt agaaaagatc aaaggatctt cttgagatcc tttttttctg cgcgtaatct
     1861 gctgcttgca aacaaaaaaa ccaccgctac cagcggtggt ttgtttgccg gatcaagagc
     1921 taccaactct ttttccgaag gtaactggct tcagcagagc gcagatacca aatactgttc
     1981 ttctagtgta gccgtagtta ggccaccact tcaagaactc tgtagcaccg cctacatacc
     2041 tcgctctgct aatcctgtta ccagtggctg ctgccagtgg cgataagtcg tgtcttaccg
     2101 ggttggactc aagacgatag ttaccggata aggcgcagcg gtcgggctga acggggggtt
     2161 cgtgcacaca gcccagcttg gagcgaacga cctacaccga actgagatac ctacagcgtg
     2221 agctttgaga aagcgccacg cttcccgaag ggagaaaggc ggacaggtat ccggtaagcg
     2281 gcagggtcgg aacaggagag cgcacgaggg agcttccagg gggaaacgcc tggtatcttt
     2341 atagtcctgt cgggtttcgc cacctctgac ttgagcgtcg atttttgtga tgctcgtcag
     2401 gggggcggag cctatggaaa aacgccagca acgcggcctt tttacggttc ctggcctttt
     2461 gctggccttt tgctcacatg ttctttcctg cgttatcccc tgattctgtg gataaccgta
     2521 ttaccgcctt tgagtgagct gataccgctc gccgcagccg aacgaccgag cgcagcgagt
     2581 cagtgagcga ggaagcggaa gagcgcccaa tacgcaaacc gcctctcccc gcgcgttggc
     2641 cgattcatta atgcagctgg cacgacaggt ttcccgactg gaaagcgggc agtgagcgca
     2701 acgcaattaa tgtgagttag ctcactcatt aggcaggcgc gcccagctgt ctagggcggc
     2761 ggatttgtcc tactcaggag agcgttcacc gacaaacaac agataaaacg aaaggcccag
     2821 tctttcgact gagcctttcg ttttatttga tgcctttaat taa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P32 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P32, contains a AraC promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P32_Terminator1_AraC_RiboA",
                },
                {
                    "accessor": "B-P33",
                    "binaryString": """LOCUS       B-P33_Terminator2_Phlf_RiboB 2636 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P33 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P33,
            contains a Phlf promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   507ac3bfc97bb142a411df94df08c21d
VERSION     507ac3bfc97bb142a411df94df08c21d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    201..275
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     regulatory      135..200
                     /label="Phlf"
     misc_feature    278..332
                     /label="LMS"
     misc_feature    468..1506
                     /label="SEVA_Ap"
     misc_feature    1580..2508
                     /label="SEVA_pUC"
     misc_feature    339..441
                     /label="SEVA_T0"
     misc_feature    2523..2627
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctcgacgt acggtggaat ctgattcgtt accaattgac atgatacgaa
      181 acgtaccgta tcgttaaggt agcgctcaac gggtgtgctt cccgttctga tgagtccgtg
      241 aggacgaaag cgcctctaca aataattttg tttaaggctc gggagaccta tcggtaataa
      301 cagtccaatc tggtgtaact tcggaatcgt ccactagtct tggactcctg ttgatagatc
      361 cagtaatgac ctcagaactc catctggatt tgttcagaac gctcggttgc cgccgggcgt
      421 tttttattgg tgagaatcca ggggtcccca ataattacga tttaaattag tagcccgcct
      481 aatgagcggg ctttttttta attcccctat ttgtttattt ttctaaatac attcaaatat
      541 gtatccgctc atgagacaat aaccctgata aatgcttcaa taatattgaa aaaggaagag
      601 tatgagcatt cagcattttc gtgtggcgct gattccgttt tttgcggcgt tttgcctgcc
      661 ggtgtttgcg catccggaaa ccctggtgaa agtgaaagat gcggaagatc aactgggtgc
      721 gcgcgtgggc tatattgaac tggatctgaa cagcggcaaa attctggaat cttttcgtcc
      781 ggaagaacgt tttccgatga tgagcacctt taaagtgctg ctgtgcggtg cggttctgag
      841 ccgtgtggat gcgggccagg aacaactggg ccgtcgtatt cattatagcc agaacgatct
      901 ggtggaatat agcccggtga ccgaaaaaca tctgaccgat ggcatgaccg tgcgtgaact
      961 gtgcagcgcg gcgattacca tgagcgataa caccgcggcg aacctgctgc tgacgaccat
     1021 tggcggtccg aaagaactga ccgcgtttct gcataacatg ggcgatcatg tgacccgtct
     1081 ggatcgttgg gaaccggaac tgaacgaagc gattccgaac gatgaacgtg ataccaccat
     1141 gccggcagca atggcgacca ccctgcgtaa actgctgacg ggtgagctgc tgaccctggc
     1201 aagccgccag caactgattg attggatgga agcggataaa gtggcgggtc cgctgctgcg
     1261 tagcgcgctg ccggctggct ggtttattgc ggataaaagc ggtgcgggcg aacgtggcag
     1321 ccgtggcatt attgcggcgc tgggcccgga tggtaaaccg agccgtattg tggtgattta
     1381 taccaccggc agccaggcga cgatggatga acgtaaccgt cagattgcgg aaattggcgc
     1441 gagcctgatt aaacattggt aaaccgatac aattaaaggc tccttttgga gccttttttt
     1501 ttggacgacc cttgtcggct cgacccacga ctattgactg ctctgagaaa gttgattgtt
     1561 acgattagtc cggccggccc cgtagaaaag atcaaaggat cttcttgaga tccttttttt
     1621 ctgcgcgtaa tctgctgctt gcaaacaaaa aaaccaccgc taccagcggt ggtttgtttg
     1681 ccggatcaag agctaccaac tctttttccg aaggtaactg gcttcagcag agcgcagata
     1741 ccaaatactg ttcttctagt gtagccgtag ttaggccacc acttcaagaa ctctgtagca
     1801 ccgcctacat acctcgctct gctaatcctg ttaccagtgg ctgctgccag tggcgataag
     1861 tcgtgtctta ccgggttgga ctcaagacga tagttaccgg ataaggcgca gcggtcgggc
     1921 tgaacggggg gttcgtgcac acagcccagc ttggagcgaa cgacctacac cgaactgaga
     1981 tacctacagc gtgagctttg agaaagcgcc acgcttcccg aagggagaaa ggcggacagg
     2041 tatccggtaa gcggcagggt cggaacagga gagcgcacga gggagcttcc agggggaaac
     2101 gcctggtatc tttatagtcc tgtcgggttt cgccacctct gacttgagcg tcgatttttg
     2161 tgatgctcgt caggggggcg gagcctatgg aaaaacgcca gcaacgcggc ctttttacgg
     2221 ttcctggcct tttgctggcc ttttgctcac atgttctttc ctgcgttatc ccctgattct
     2281 gtggataacc gtattaccgc ctttgagtga gctgataccg ctcgccgcag ccgaacgacc
     2341 gagcgcagcg agtcagtgag cgaggaagcg gaagagcgcc caatacgcaa accgcctctc
     2401 cccgcgcgtt ggccgattca ttaatgcagc tggcacgaca ggtttcccga ctggaaagcg
     2461 ggcagtgagc gcaacgcaat taatgtgagt tagctcactc attaggcagg cgcgcccagc
     2521 tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac aacagataaa
     2581 acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt aattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P33 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P33, contains a Phlf promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P33_Terminator2_Phlf_RiboB",
                },
                {
                    "accessor": "B-P34",
                    "binaryString": """LOCUS       B-P34_Terminator2_CymR_RiboB 2660 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P34 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P34,
            contains a CymR promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   9a90bfcef91d335edffe8a971329a723
VERSION     9a90bfcef91d335edffe8a971329a723
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    115..134
                     /label="SpacerA"
     regulatory      135..224
                     /label="CymR"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    225..299
                     /label="RiboB"
     misc_feature    302..356
                     /label="LMS"
     misc_feature    492..1530
                     /label="SEVA_Ap"
     misc_feature    1604..2532
                     /label="SEVA_pUC"
     misc_feature    363..465
                     /label="SEVA_T0"
     misc_feature    2547..2651
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctaacaaa cagacaatct ggtctgtttg tattatggaa aatttttctg
      181 tataatagat tcaacaaaca gacaatctgg tctgtttgta ttatagcgct caacgggtgt
      241 gcttcccgtt ctgatgagtc cgtgaggacg aaagcgcctc tacaaataat tttgtttaag
      301 gctcgggaga cctatcggta ataacagtcc aatctggtgt aacttcggaa tcgtccacta
      361 gtcttggact cctgttgata gatccagtaa tgacctcaga actccatctg gatttgttca
      421 gaacgctcgg ttgccgccgg gcgtttttta ttggtgagaa tccaggggtc cccaataatt
      481 acgatttaaa ttagtagccc gcctaatgag cgggcttttt tttaattccc ctatttgttt
      541 atttttctaa atacattcaa atatgtatcc gctcatgaga caataaccct gataaatgct
      601 tcaataatat tgaaaaagga agagtatgag cattcagcat tttcgtgtgg cgctgattcc
      661 gttttttgcg gcgttttgcc tgccggtgtt tgcgcatccg gaaaccctgg tgaaagtgaa
      721 agatgcggaa gatcaactgg gtgcgcgcgt gggctatatt gaactggatc tgaacagcgg
      781 caaaattctg gaatcttttc gtccggaaga acgttttccg atgatgagca cctttaaagt
      841 gctgctgtgc ggtgcggttc tgagccgtgt ggatgcgggc caggaacaac tgggccgtcg
      901 tattcattat agccagaacg atctggtgga atatagcccg gtgaccgaaa aacatctgac
      961 cgatggcatg accgtgcgtg aactgtgcag cgcggcgatt accatgagcg ataacaccgc
     1021 ggcgaacctg ctgctgacga ccattggcgg tccgaaagaa ctgaccgcgt ttctgcataa
     1081 catgggcgat catgtgaccc gtctggatcg ttgggaaccg gaactgaacg aagcgattcc
     1141 gaacgatgaa cgtgatacca ccatgccggc agcaatggcg accaccctgc gtaaactgct
     1201 gacgggtgag ctgctgaccc tggcaagccg ccagcaactg attgattgga tggaagcgga
     1261 taaagtggcg ggtccgctgc tgcgtagcgc gctgccggct ggctggttta ttgcggataa
     1321 aagcggtgcg ggcgaacgtg gcagccgtgg cattattgcg gcgctgggcc cggatggtaa
     1381 accgagccgt attgtggtga tttataccac cggcagccag gcgacgatgg atgaacgtaa
     1441 ccgtcagatt gcggaaattg gcgcgagcct gattaaacat tggtaaaccg atacaattaa
     1501 aggctccttt tggagccttt ttttttggac gacccttgtc ggctcgaccc acgactattg
     1561 actgctctga gaaagttgat tgttacgatt agtccggccg gccccgtaga aaagatcaaa
     1621 ggatcttctt gagatccttt ttttctgcgc gtaatctgct gcttgcaaac aaaaaaacca
     1681 ccgctaccag cggtggtttg tttgccggat caagagctac caactctttt tccgaaggta
     1741 actggcttca gcagagcgca gataccaaat actgttcttc tagtgtagcc gtagttaggc
     1801 caccacttca agaactctgt agcaccgcct acatacctcg ctctgctaat cctgttacca
     1861 gtggctgctg ccagtggcga taagtcgtgt cttaccgggt tggactcaag acgatagtta
     1921 ccggataagg cgcagcggtc gggctgaacg gggggttcgt gcacacagcc cagcttggag
     1981 cgaacgacct acaccgaact gagataccta cagcgtgagc tttgagaaag cgccacgctt
     2041 cccgaaggga gaaaggcgga caggtatccg gtaagcggca gggtcggaac aggagagcgc
     2101 acgagggagc ttccaggggg aaacgcctgg tatctttata gtcctgtcgg gtttcgccac
     2161 ctctgacttg agcgtcgatt tttgtgatgc tcgtcagggg ggcggagcct atggaaaaac
     2221 gccagcaacg cggccttttt acggttcctg gccttttgct ggccttttgc tcacatgttc
     2281 tttcctgcgt tatcccctga ttctgtggat aaccgtatta ccgcctttga gtgagctgat
     2341 accgctcgcc gcagccgaac gaccgagcgc agcgagtcag tgagcgagga agcggaagag
     2401 cgcccaatac gcaaaccgcc tctccccgcg cgttggccga ttcattaatg cagctggcac
     2461 gacaggtttc ccgactggaa agcgggcagt gagcgcaacg caattaatgt gagttagctc
     2521 actcattagg caggcgcgcc cagctgtcta gggcggcgga tttgtcctac tcaggagagc
     2581 gttcaccgac aaacaacaga taaaacgaaa ggcccagtct ttcgactgag cctttcgttt
     2641 tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P34 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P34, contains a CymR promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P34_Terminator2_CymR_RiboB",
                },
                {
                    "accessor": "B-P35",
                    "binaryString": """LOCUS       B-P35_Terminator2_TetR_RiboB 2646 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P35 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P35,
            contains a TetR promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   1f9db58ce8a2f58de8a3dde19aeebe76
VERSION     1f9db58ce8a2f58de8a3dde19aeebe76
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      135..210
                     /label="TetR"
     misc_feature    211..285
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    288..342
                     /label="LMS"
     misc_feature    478..1516
                     /label="SEVA_Ap"
     misc_feature    1590..2518
                     /label="SEVA_pUC"
     misc_feature    349..451
                     /label="SEVA_T0"
     misc_feature    2533..2637
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctttttca gcaggacgca ctgacctccc tatcagtgat agagattgac
      181 atccctatca gtgatagaga tactgagcac agcgctcaac gggtgtgctt cccgttctga
      241 tgagtccgtg aggacgaaag cgcctctaca aataattttg tttaaggctc gggagaccta
      301 tcggtaataa cagtccaatc tggtgtaact tcggaatcgt ccactagtct tggactcctg
      361 ttgatagatc cagtaatgac ctcagaactc catctggatt tgttcagaac gctcggttgc
      421 cgccgggcgt tttttattgg tgagaatcca ggggtcccca ataattacga tttaaattag
      481 tagcccgcct aatgagcggg ctttttttta attcccctat ttgtttattt ttctaaatac
      541 attcaaatat gtatccgctc atgagacaat aaccctgata aatgcttcaa taatattgaa
      601 aaaggaagag tatgagcatt cagcattttc gtgtggcgct gattccgttt tttgcggcgt
      661 tttgcctgcc ggtgtttgcg catccggaaa ccctggtgaa agtgaaagat gcggaagatc
      721 aactgggtgc gcgcgtgggc tatattgaac tggatctgaa cagcggcaaa attctggaat
      781 cttttcgtcc ggaagaacgt tttccgatga tgagcacctt taaagtgctg ctgtgcggtg
      841 cggttctgag ccgtgtggat gcgggccagg aacaactggg ccgtcgtatt cattatagcc
      901 agaacgatct ggtggaatat agcccggtga ccgaaaaaca tctgaccgat ggcatgaccg
      961 tgcgtgaact gtgcagcgcg gcgattacca tgagcgataa caccgcggcg aacctgctgc
     1021 tgacgaccat tggcggtccg aaagaactga ccgcgtttct gcataacatg ggcgatcatg
     1081 tgacccgtct ggatcgttgg gaaccggaac tgaacgaagc gattccgaac gatgaacgtg
     1141 ataccaccat gccggcagca atggcgacca ccctgcgtaa actgctgacg ggtgagctgc
     1201 tgaccctggc aagccgccag caactgattg attggatgga agcggataaa gtggcgggtc
     1261 cgctgctgcg tagcgcgctg ccggctggct ggtttattgc ggataaaagc ggtgcgggcg
     1321 aacgtggcag ccgtggcatt attgcggcgc tgggcccgga tggtaaaccg agccgtattg
     1381 tggtgattta taccaccggc agccaggcga cgatggatga acgtaaccgt cagattgcgg
     1441 aaattggcgc gagcctgatt aaacattggt aaaccgatac aattaaaggc tccttttgga
     1501 gccttttttt ttggacgacc cttgtcggct cgacccacga ctattgactg ctctgagaaa
     1561 gttgattgtt acgattagtc cggccggccc cgtagaaaag atcaaaggat cttcttgaga
     1621 tccttttttt ctgcgcgtaa tctgctgctt gcaaacaaaa aaaccaccgc taccagcggt
     1681 ggtttgtttg ccggatcaag agctaccaac tctttttccg aaggtaactg gcttcagcag
     1741 agcgcagata ccaaatactg ttcttctagt gtagccgtag ttaggccacc acttcaagaa
     1801 ctctgtagca ccgcctacat acctcgctct gctaatcctg ttaccagtgg ctgctgccag
     1861 tggcgataag tcgtgtctta ccgggttgga ctcaagacga tagttaccgg ataaggcgca
     1921 gcggtcgggc tgaacggggg gttcgtgcac acagcccagc ttggagcgaa cgacctacac
     1981 cgaactgaga tacctacagc gtgagctttg agaaagcgcc acgcttcccg aagggagaaa
     2041 ggcggacagg tatccggtaa gcggcagggt cggaacagga gagcgcacga gggagcttcc
     2101 agggggaaac gcctggtatc tttatagtcc tgtcgggttt cgccacctct gacttgagcg
     2161 tcgatttttg tgatgctcgt caggggggcg gagcctatgg aaaaacgcca gcaacgcggc
     2221 ctttttacgg ttcctggcct tttgctggcc ttttgctcac atgttctttc ctgcgttatc
     2281 ccctgattct gtggataacc gtattaccgc ctttgagtga gctgataccg ctcgccgcag
     2341 ccgaacgacc gagcgcagcg agtcagtgag cgaggaagcg gaagagcgcc caatacgcaa
     2401 accgcctctc cccgcgcgtt ggccgattca ttaatgcagc tggcacgaca ggtttcccga
     2461 ctggaaagcg ggcagtgagc gcaacgcaat taatgtgagt tagctcactc attaggcagg
     2521 cgcgcccagc tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac
     2581 aacagataaa acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt
     2641 aattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P35 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P35, contains a TetR promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P35_Terminator2_TetR_RiboB",
                },
                {
                    "accessor": "B-P36",
                    "binaryString": """LOCUS       B-P36_Terminator2_VanR_RiboB 2620 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P36 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P36,
            contains a VanR promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   7e1c61ba98d06b168606a185623bff8e
VERSION     7e1c61ba98d06b168606a185623bff8e
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    185..259
                     /label="RiboB"
     regulatory      135..184
                     /label="VanR"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    262..316
                     /label="LMS"
     misc_feature    452..1490
                     /label="SEVA_Ap"
     misc_feature    1564..2492
                     /label="SEVA_pUC"
     misc_feature    323..425
                     /label="SEVA_T0"
     misc_feature    2507..2611
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctattgga tccaattgac agctagctca gtcctaggta ccattggatc
      181 caatagcgct caacgggtgt gcttcccgtt ctgatgagtc cgtgaggacg aaagcgcctc
      241 tacaaataat tttgtttaag gctcgggaga cctatcggta ataacagtcc aatctggtgt
      301 aacttcggaa tcgtccacta gtcttggact cctgttgata gatccagtaa tgacctcaga
      361 actccatctg gatttgttca gaacgctcgg ttgccgccgg gcgtttttta ttggtgagaa
      421 tccaggggtc cccaataatt acgatttaaa ttagtagccc gcctaatgag cgggcttttt
      481 tttaattccc ctatttgttt atttttctaa atacattcaa atatgtatcc gctcatgaga
      541 caataaccct gataaatgct tcaataatat tgaaaaagga agagtatgag cattcagcat
      601 tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc tgccggtgtt tgcgcatccg
      661 gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg gtgcgcgcgt gggctatatt
      721 gaactggatc tgaacagcgg caaaattctg gaatcttttc gtccggaaga acgttttccg
      781 atgatgagca cctttaaagt gctgctgtgc ggtgcggttc tgagccgtgt ggatgcgggc
      841 caggaacaac tgggccgtcg tattcattat agccagaacg atctggtgga atatagcccg
      901 gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg aactgtgcag cgcggcgatt
      961 accatgagcg ataacaccgc ggcgaacctg ctgctgacga ccattggcgg tccgaaagaa
     1021 ctgaccgcgt ttctgcataa catgggcgat catgtgaccc gtctggatcg ttgggaaccg
     1081 gaactgaacg aagcgattcc gaacgatgaa cgtgatacca ccatgccggc agcaatggcg
     1141 accaccctgc gtaaactgct gacgggtgag ctgctgaccc tggcaagccg ccagcaactg
     1201 attgattgga tggaagcgga taaagtggcg ggtccgctgc tgcgtagcgc gctgccggct
     1261 ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg gcagccgtgg cattattgcg
     1321 gcgctgggcc cggatggtaa accgagccgt attgtggtga tttataccac cggcagccag
     1381 gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg gcgcgagcct gattaaacat
     1441 tggtaaaccg atacaattaa aggctccttt tggagccttt ttttttggac gacccttgtc
     1501 ggctcgaccc acgactattg actgctctga gaaagttgat tgttacgatt agtccggccg
     1561 gccccgtaga aaagatcaaa ggatcttctt gagatccttt ttttctgcgc gtaatctgct
     1621 gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg tttgccggat caagagctac
     1681 caactctttt tccgaaggta actggcttca gcagagcgca gataccaaat actgttcttc
     1741 tagtgtagcc gtagttaggc caccacttca agaactctgt agcaccgcct acatacctcg
     1801 ctctgctaat cctgttacca gtggctgctg ccagtggcga taagtcgtgt cttaccgggt
     1861 tggactcaag acgatagtta ccggataagg cgcagcggtc gggctgaacg gggggttcgt
     1921 gcacacagcc cagcttggag cgaacgacct acaccgaact gagataccta cagcgtgagc
     1981 tttgagaaag cgccacgctt cccgaaggga gaaaggcgga caggtatccg gtaagcggca
     2041 gggtcggaac aggagagcgc acgagggagc ttccaggggg aaacgcctgg tatctttata
     2101 gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt tttgtgatgc tcgtcagggg
     2161 ggcggagcct atggaaaaac gccagcaacg cggccttttt acggttcctg gccttttgct
     2221 ggccttttgc tcacatgttc tttcctgcgt tatcccctga ttctgtggat aaccgtatta
     2281 ccgcctttga gtgagctgat accgctcgcc gcagccgaac gaccgagcgc agcgagtcag
     2341 tgagcgagga agcggaagag cgcccaatac gcaaaccgcc tctccccgcg cgttggccga
     2401 ttcattaatg cagctggcac gacaggtttc ccgactggaa agcgggcagt gagcgcaacg
     2461 caattaatgt gagttagctc actcattagg caggcgcgcc cagctgtcta gggcggcgga
     2521 tttgtcctac tcaggagagc gttcaccgac aaacaacaga taaaacgaaa ggcccagtct
     2581 ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P36 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P36, contains a VanR promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P36_Terminator2_VanR_RiboB",
                },
                {
                    "accessor": "B-P37",
                    "binaryString": """LOCUS       B-P37_Terminator2_LuxR_RiboB 2625 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P37 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P37,
            contains a LuxR promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   35394c3b5568eb599f5939d20759d28d
VERSION     35394c3b5568eb599f5939d20759d28d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..114
                     /label="Terminator2"
     regulatory      135..189
                     /label="LuxR"
     misc_feature    190..264
                     /label="RiboB"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    267..321
                     /label="LMS"
     misc_feature    457..1495
                     /label="SEVA_Ap"
     misc_feature    1569..2497
                     /label="SEVA_pUC"
     misc_feature    328..430
                     /label="SEVA_T0"
     misc_feature    2512..2616
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctacctgt aggatcgtac aggtttacgc aagaaaatgg tttgttacag
      181 tcgaataaaa gcgctcaacg ggtgtgcttc ccgttctgat gagtccgtga ggacgaaagc
      241 gcctctacaa ataattttgt ttaaggctcg ggagacctat cggtaataac agtccaatct
      301 ggtgtaactt cggaatcgtc cactagtctt ggactcctgt tgatagatcc agtaatgacc
      361 tcagaactcc atctggattt gttcagaacg ctcggttgcc gccgggcgtt ttttattggt
      421 gagaatccag gggtccccaa taattacgat ttaaattagt agcccgccta atgagcgggc
      481 ttttttttaa ttcccctatt tgtttatttt tctaaataca ttcaaatatg tatccgctca
      541 tgagacaata accctgataa atgcttcaat aatattgaaa aaggaagagt atgagcattc
      601 agcattttcg tgtggcgctg attccgtttt ttgcggcgtt ttgcctgccg gtgtttgcgc
      661 atccggaaac cctggtgaaa gtgaaagatg cggaagatca actgggtgcg cgcgtgggct
      721 atattgaact ggatctgaac agcggcaaaa ttctggaatc ttttcgtccg gaagaacgtt
      781 ttccgatgat gagcaccttt aaagtgctgc tgtgcggtgc ggttctgagc cgtgtggatg
      841 cgggccagga acaactgggc cgtcgtattc attatagcca gaacgatctg gtggaatata
      901 gcccggtgac cgaaaaacat ctgaccgatg gcatgaccgt gcgtgaactg tgcagcgcgg
      961 cgattaccat gagcgataac accgcggcga acctgctgct gacgaccatt ggcggtccga
     1021 aagaactgac cgcgtttctg cataacatgg gcgatcatgt gacccgtctg gatcgttggg
     1081 aaccggaact gaacgaagcg attccgaacg atgaacgtga taccaccatg ccggcagcaa
     1141 tggcgaccac cctgcgtaaa ctgctgacgg gtgagctgct gaccctggca agccgccagc
     1201 aactgattga ttggatggaa gcggataaag tggcgggtcc gctgctgcgt agcgcgctgc
     1261 cggctggctg gtttattgcg gataaaagcg gtgcgggcga acgtggcagc cgtggcatta
     1321 ttgcggcgct gggcccggat ggtaaaccga gccgtattgt ggtgatttat accaccggca
     1381 gccaggcgac gatggatgaa cgtaaccgtc agattgcgga aattggcgcg agcctgatta
     1441 aacattggta aaccgataca attaaaggct ccttttggag cctttttttt tggacgaccc
     1501 ttgtcggctc gacccacgac tattgactgc tctgagaaag ttgattgtta cgattagtcc
     1561 ggccggcccc gtagaaaaga tcaaaggatc ttcttgagat cctttttttc tgcgcgtaat
     1621 ctgctgcttg caaacaaaaa aaccaccgct accagcggtg gtttgtttgc cggatcaaga
     1681 gctaccaact ctttttccga aggtaactgg cttcagcaga gcgcagatac caaatactgt
     1741 tcttctagtg tagccgtagt taggccacca cttcaagaac tctgtagcac cgcctacata
     1801 cctcgctctg ctaatcctgt taccagtggc tgctgccagt ggcgataagt cgtgtcttac
     1861 cgggttggac tcaagacgat agttaccgga taaggcgcag cggtcgggct gaacgggggg
     1921 ttcgtgcaca cagcccagct tggagcgaac gacctacacc gaactgagat acctacagcg
     1981 tgagctttga gaaagcgcca cgcttcccga agggagaaag gcggacaggt atccggtaag
     2041 cggcagggtc ggaacaggag agcgcacgag ggagcttcca gggggaaacg cctggtatct
     2101 ttatagtcct gtcgggtttc gccacctctg acttgagcgt cgatttttgt gatgctcgtc
     2161 aggggggcgg agcctatgga aaaacgccag caacgcggcc tttttacggt tcctggcctt
     2221 ttgctggcct tttgctcaca tgttctttcc tgcgttatcc cctgattctg tggataaccg
     2281 tattaccgcc tttgagtgag ctgataccgc tcgccgcagc cgaacgaccg agcgcagcga
     2341 gtcagtgagc gaggaagcgg aagagcgccc aatacgcaaa ccgcctctcc ccgcgcgttg
     2401 gccgattcat taatgcagct ggcacgacag gtttcccgac tggaaagcgg gcagtgagcg
     2461 caacgcaatt aatgtgagtt agctcactca ttaggcaggc gcgcccagct gtctagggcg
     2521 gcggatttgt cctactcagg agagcgttca ccgacaaaca acagataaaa cgaaaggccc
     2581 agtctttcga ctgagccttt cgttttattt gatgccttta attaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P37 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P37, contains a LuxR promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P37_Terminator2_LuxR_RiboB",
                },
                {
                    "accessor": "B-P38",
                    "binaryString": """LOCUS       B-P38_Terminator2_CinR_RiboB 2796 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P38 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P38,
            contains a CinR promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   b4fac0a12e6b7829eb863441fd53892c
VERSION     b4fac0a12e6b7829eb863441fd53892c
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    361..435
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     regulatory      135..360
                     /label="CinR"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    438..492
                     /label="LMS"
     misc_feature    628..1666
                     /label="SEVA_Ap"
     misc_feature    1740..2668
                     /label="SEVA_pUC"
     misc_feature    499..601
                     /label="SEVA_T0"
     misc_feature    2683..2787
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctcccttt gtgcgtccaa acggacgcac ggcgctctaa agcgggtcgc
      181 gatctttcag attcgctcct cgcgctttca gtctttgttt tggcgcatgt cgttatcgca
      241 aaaccgctgc acacttttgc gcgacatgct ctgatccccc tcatctgggg gggcctatct
      301 gagggaattt ccgatccggc tcgcctgaac cattctgctt tccacgaact tgaaaacgct
      361 agcgctcaac gggtgtgctt cccgttctga tgagtccgtg aggacgaaag cgcctctaca
      421 aataattttg tttaaggctc gggagaccta tcggtaataa cagtccaatc tggtgtaact
      481 tcggaatcgt ccactagtct tggactcctg ttgatagatc cagtaatgac ctcagaactc
      541 catctggatt tgttcagaac gctcggttgc cgccgggcgt tttttattgg tgagaatcca
      601 ggggtcccca ataattacga tttaaattag tagcccgcct aatgagcggg ctttttttta
      661 attcccctat ttgtttattt ttctaaatac attcaaatat gtatccgctc atgagacaat
      721 aaccctgata aatgcttcaa taatattgaa aaaggaagag tatgagcatt cagcattttc
      781 gtgtggcgct gattccgttt tttgcggcgt tttgcctgcc ggtgtttgcg catccggaaa
      841 ccctggtgaa agtgaaagat gcggaagatc aactgggtgc gcgcgtgggc tatattgaac
      901 tggatctgaa cagcggcaaa attctggaat cttttcgtcc ggaagaacgt tttccgatga
      961 tgagcacctt taaagtgctg ctgtgcggtg cggttctgag ccgtgtggat gcgggccagg
     1021 aacaactggg ccgtcgtatt cattatagcc agaacgatct ggtggaatat agcccggtga
     1081 ccgaaaaaca tctgaccgat ggcatgaccg tgcgtgaact gtgcagcgcg gcgattacca
     1141 tgagcgataa caccgcggcg aacctgctgc tgacgaccat tggcggtccg aaagaactga
     1201 ccgcgtttct gcataacatg ggcgatcatg tgacccgtct ggatcgttgg gaaccggaac
     1261 tgaacgaagc gattccgaac gatgaacgtg ataccaccat gccggcagca atggcgacca
     1321 ccctgcgtaa actgctgacg ggtgagctgc tgaccctggc aagccgccag caactgattg
     1381 attggatgga agcggataaa gtggcgggtc cgctgctgcg tagcgcgctg ccggctggct
     1441 ggtttattgc ggataaaagc ggtgcgggcg aacgtggcag ccgtggcatt attgcggcgc
     1501 tgggcccgga tggtaaaccg agccgtattg tggtgattta taccaccggc agccaggcga
     1561 cgatggatga acgtaaccgt cagattgcgg aaattggcgc gagcctgatt aaacattggt
     1621 aaaccgatac aattaaaggc tccttttgga gccttttttt ttggacgacc cttgtcggct
     1681 cgacccacga ctattgactg ctctgagaaa gttgattgtt acgattagtc cggccggccc
     1741 cgtagaaaag atcaaaggat cttcttgaga tccttttttt ctgcgcgtaa tctgctgctt
     1801 gcaaacaaaa aaaccaccgc taccagcggt ggtttgtttg ccggatcaag agctaccaac
     1861 tctttttccg aaggtaactg gcttcagcag agcgcagata ccaaatactg ttcttctagt
     1921 gtagccgtag ttaggccacc acttcaagaa ctctgtagca ccgcctacat acctcgctct
     1981 gctaatcctg ttaccagtgg ctgctgccag tggcgataag tcgtgtctta ccgggttgga
     2041 ctcaagacga tagttaccgg ataaggcgca gcggtcgggc tgaacggggg gttcgtgcac
     2101 acagcccagc ttggagcgaa cgacctacac cgaactgaga tacctacagc gtgagctttg
     2161 agaaagcgcc acgcttcccg aagggagaaa ggcggacagg tatccggtaa gcggcagggt
     2221 cggaacagga gagcgcacga gggagcttcc agggggaaac gcctggtatc tttatagtcc
     2281 tgtcgggttt cgccacctct gacttgagcg tcgatttttg tgatgctcgt caggggggcg
     2341 gagcctatgg aaaaacgcca gcaacgcggc ctttttacgg ttcctggcct tttgctggcc
     2401 ttttgctcac atgttctttc ctgcgttatc ccctgattct gtggataacc gtattaccgc
     2461 ctttgagtga gctgataccg ctcgccgcag ccgaacgacc gagcgcagcg agtcagtgag
     2521 cgaggaagcg gaagagcgcc caatacgcaa accgcctctc cccgcgcgtt ggccgattca
     2581 ttaatgcagc tggcacgaca ggtttcccga ctggaaagcg ggcagtgagc gcaacgcaat
     2641 taatgtgagt tagctcactc attaggcagg cgcgcccagc tgtctagggc ggcggatttg
     2701 tcctactcag gagagcgttc accgacaaac aacagataaa acgaaaggcc cagtctttcg
     2761 actgagcctt tcgttttatt tgatgccttt aattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P38 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P38, contains a CinR promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P38_Terminator2_CinR_RiboB",
                },
                {
                    "accessor": "B-P39",
                    "binaryString": """LOCUS       B-P39_Terminator2_LacI_RiboB 2626 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P39 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P39,
            contains a LacI promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   cf6dd91a62bdf7f6f7bfe823ffa07fec
VERSION     cf6dd91a62bdf7f6f7bfe823ffa07fec
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      135..190
                     /label="LacI"
     misc_feature    191..265
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    268..322
                     /label="LMS"
     misc_feature    458..1496
                     /label="SEVA_Ap"
     misc_feature    1570..2498
                     /label="SEVA_pUC"
     misc_feature    329..431
                     /label="SEVA_T0"
     misc_feature    2513..2617
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttgttga caattaatca tcggctcgta taatgtgtgg aattgtgagc
      181 gctcacaatt agcgctcaac gggtgtgctt cccgttctga tgagtccgtg aggacgaaag
      241 cgcctctaca aataattttg tttaaggctc gggagaccta tcggtaataa cagtccaatc
      301 tggtgtaact tcggaatcgt ccactagtct tggactcctg ttgatagatc cagtaatgac
      361 ctcagaactc catctggatt tgttcagaac gctcggttgc cgccgggcgt tttttattgg
      421 tgagaatcca ggggtcccca ataattacga tttaaattag tagcccgcct aatgagcggg
      481 ctttttttta attcccctat ttgtttattt ttctaaatac attcaaatat gtatccgctc
      541 atgagacaat aaccctgata aatgcttcaa taatattgaa aaaggaagag tatgagcatt
      601 cagcattttc gtgtggcgct gattccgttt tttgcggcgt tttgcctgcc ggtgtttgcg
      661 catccggaaa ccctggtgaa agtgaaagat gcggaagatc aactgggtgc gcgcgtgggc
      721 tatattgaac tggatctgaa cagcggcaaa attctggaat cttttcgtcc ggaagaacgt
      781 tttccgatga tgagcacctt taaagtgctg ctgtgcggtg cggttctgag ccgtgtggat
      841 gcgggccagg aacaactggg ccgtcgtatt cattatagcc agaacgatct ggtggaatat
      901 agcccggtga ccgaaaaaca tctgaccgat ggcatgaccg tgcgtgaact gtgcagcgcg
      961 gcgattacca tgagcgataa caccgcggcg aacctgctgc tgacgaccat tggcggtccg
     1021 aaagaactga ccgcgtttct gcataacatg ggcgatcatg tgacccgtct ggatcgttgg
     1081 gaaccggaac tgaacgaagc gattccgaac gatgaacgtg ataccaccat gccggcagca
     1141 atggcgacca ccctgcgtaa actgctgacg ggtgagctgc tgaccctggc aagccgccag
     1201 caactgattg attggatgga agcggataaa gtggcgggtc cgctgctgcg tagcgcgctg
     1261 ccggctggct ggtttattgc ggataaaagc ggtgcgggcg aacgtggcag ccgtggcatt
     1321 attgcggcgc tgggcccgga tggtaaaccg agccgtattg tggtgattta taccaccggc
     1381 agccaggcga cgatggatga acgtaaccgt cagattgcgg aaattggcgc gagcctgatt
     1441 aaacattggt aaaccgatac aattaaaggc tccttttgga gccttttttt ttggacgacc
     1501 cttgtcggct cgacccacga ctattgactg ctctgagaaa gttgattgtt acgattagtc
     1561 cggccggccc cgtagaaaag atcaaaggat cttcttgaga tccttttttt ctgcgcgtaa
     1621 tctgctgctt gcaaacaaaa aaaccaccgc taccagcggt ggtttgtttg ccggatcaag
     1681 agctaccaac tctttttccg aaggtaactg gcttcagcag agcgcagata ccaaatactg
     1741 ttcttctagt gtagccgtag ttaggccacc acttcaagaa ctctgtagca ccgcctacat
     1801 acctcgctct gctaatcctg ttaccagtgg ctgctgccag tggcgataag tcgtgtctta
     1861 ccgggttgga ctcaagacga tagttaccgg ataaggcgca gcggtcgggc tgaacggggg
     1921 gttcgtgcac acagcccagc ttggagcgaa cgacctacac cgaactgaga tacctacagc
     1981 gtgagctttg agaaagcgcc acgcttcccg aagggagaaa ggcggacagg tatccggtaa
     2041 gcggcagggt cggaacagga gagcgcacga gggagcttcc agggggaaac gcctggtatc
     2101 tttatagtcc tgtcgggttt cgccacctct gacttgagcg tcgatttttg tgatgctcgt
     2161 caggggggcg gagcctatgg aaaaacgcca gcaacgcggc ctttttacgg ttcctggcct
     2221 tttgctggcc ttttgctcac atgttctttc ctgcgttatc ccctgattct gtggataacc
     2281 gtattaccgc ctttgagtga gctgataccg ctcgccgcag ccgaacgacc gagcgcagcg
     2341 agtcagtgag cgaggaagcg gaagagcgcc caatacgcaa accgcctctc cccgcgcgtt
     2401 ggccgattca ttaatgcagc tggcacgaca ggtttcccga ctggaaagcg ggcagtgagc
     2461 gcaacgcaat taatgtgagt tagctcactc attaggcagg cgcgcccagc tgtctagggc
     2521 ggcggatttg tcctactcag gagagcgttc accgacaaac aacagataaa acgaaaggcc
     2581 cagtctttcg actgagcctt tcgttttatt tgatgccttt aattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P39 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P39, contains a LacI promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P39_Terminator2_LacI_RiboB",
                },
                {
                    "accessor": "B-P40",
                    "binaryString": """LOCUS       B-P40_Terminator2_AraC_RiboB 2859 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P40 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P40,
            contains a AraC promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   4d3a1c37cb834f70e8b8196d27a410aa
VERSION     4d3a1c37cb834f70e8b8196d27a410aa
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    424..498
                     /label="RiboB"
     regulatory      135..423
                     /label="AraC"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    501..555
                     /label="LMS"
     misc_feature    691..1729
                     /label="SEVA_Ap"
     misc_feature    1803..2731
                     /label="SEVA_pUC"
     misc_feature    562..664
                     /label="SEVA_T0"
     misc_feature    2746..2850
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctagaaac caattgtcca tattgcatca gacattgccg tcactgcgtc
      181 ttttactggc tcttctcgct aaccaaaccg gtaaccccgc ttattaaaag cattctgtaa
      241 caaagcggga ccaaagccat gacaaaaacg cgtaacaaaa gtgtctataa tcacggcaga
      301 aaagtccaca ttgattattt gcacggcgtc acactttgct atgccatagc atttttatcc
      361 ataagattag cggatcctac ctgacgcttt ttatcgcaac tctctactgt ttctccatac
      421 ccgagcgctc aacgggtgtg cttcccgttc tgatgagtcc gtgaggacga aagcgcctct
      481 acaaataatt ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta
      541 acttcggaat cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa
      601 ctccatctgg atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat
      661 ccaggggtcc ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt
      721 ttaattcccc tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac
      781 aataaccctg ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt
      841 ttcgtgtggc gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg
      901 aaaccctggt gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg
      961 aactggatct gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga
     1021 tgatgagcac ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc
     1081 aggaacaact gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg
     1141 tgaccgaaaa acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta
     1201 ccatgagcga taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac
     1261 tgaccgcgtt tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg
     1321 aactgaacga agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga
     1381 ccaccctgcg taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga
     1441 ttgattggat ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg
     1501 gctggtttat tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg
     1561 cgctgggccc ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg
     1621 cgacgatgga tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt
     1681 ggtaaaccga tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg
     1741 gctcgaccca cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg
     1801 ccccgtagaa aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg
     1861 cttgcaaaca aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc
     1921 aactcttttt ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct
     1981 agtgtagccg tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc
     2041 tctgctaatc ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt
     2101 ggactcaaga cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg
     2161 cacacagccc agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct
     2221 ttgagaaagc gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag
     2281 ggtcggaaca ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag
     2341 tcctgtcggg tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg
     2401 gcggagccta tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg
     2461 gccttttgct cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac
     2521 cgcctttgag tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt
     2581 gagcgaggaa gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat
     2641 tcattaatgc agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc
     2701 aattaatgtg agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat
     2761 ttgtcctact caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt
     2821 tcgactgagc ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P40 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P40, contains a AraC promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P40_Terminator2_AraC_RiboB",
                },
                {
                    "accessor": "B-P41",
                    "binaryString": """LOCUS       B-P41_Terminator3_Phlf_RiboC 2630 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P41 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P41,
            contains a Phlf promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   dfe7d22dffcaa5dd14967c913e81bdba
VERSION     dfe7d22dffcaa5dd14967c913e81bdba
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    195..269
                     /label="RiboC"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    109..128
                     /label="SpacerA"
     regulatory      129..194
                     /label="Phlf"
     misc_feature    272..326
                     /label="LMS"
     misc_feature    462..1500
                     /label="SEVA_Ap"
     misc_feature    1574..2502
                     /label="SEVA_pUC"
     misc_feature    333..435
                     /label="SEVA_T0"
     misc_feature    2517..2621
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctcg acgtacggtg gaatctgatt cgttaccaat tgacatgata cgaaacgtac
      181 cgtatcgtta aggtagtagt caccggctgt gcttgccggt ctgatgagcc tgtgaaggcg
      241 aaactacctc tacaaataat tttgtttaag gctcgggaga cctatcggta ataacagtcc
      301 aatctggtgt aacttcggaa tcgtccacta gtcttggact cctgttgata gatccagtaa
      361 tgacctcaga actccatctg gatttgttca gaacgctcgg ttgccgccgg gcgtttttta
      421 ttggtgagaa tccaggggtc cccaataatt acgatttaaa ttagtagccc gcctaatgag
      481 cgggcttttt tttaattccc ctatttgttt atttttctaa atacattcaa atatgtatcc
      541 gctcatgaga caataaccct gataaatgct tcaataatat tgaaaaagga agagtatgag
      601 cattcagcat tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc tgccggtgtt
      661 tgcgcatccg gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg gtgcgcgcgt
      721 gggctatatt gaactggatc tgaacagcgg caaaattctg gaatcttttc gtccggaaga
      781 acgttttccg atgatgagca cctttaaagt gctgctgtgc ggtgcggttc tgagccgtgt
      841 ggatgcgggc caggaacaac tgggccgtcg tattcattat agccagaacg atctggtgga
      901 atatagcccg gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg aactgtgcag
      961 cgcggcgatt accatgagcg ataacaccgc ggcgaacctg ctgctgacga ccattggcgg
     1021 tccgaaagaa ctgaccgcgt ttctgcataa catgggcgat catgtgaccc gtctggatcg
     1081 ttgggaaccg gaactgaacg aagcgattcc gaacgatgaa cgtgatacca ccatgccggc
     1141 agcaatggcg accaccctgc gtaaactgct gacgggtgag ctgctgaccc tggcaagccg
     1201 ccagcaactg attgattgga tggaagcgga taaagtggcg ggtccgctgc tgcgtagcgc
     1261 gctgccggct ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg gcagccgtgg
     1321 cattattgcg gcgctgggcc cggatggtaa accgagccgt attgtggtga tttataccac
     1381 cggcagccag gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg gcgcgagcct
     1441 gattaaacat tggtaaaccg atacaattaa aggctccttt tggagccttt ttttttggac
     1501 gacccttgtc ggctcgaccc acgactattg actgctctga gaaagttgat tgttacgatt
     1561 agtccggccg gccccgtaga aaagatcaaa ggatcttctt gagatccttt ttttctgcgc
     1621 gtaatctgct gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg tttgccggat
     1681 caagagctac caactctttt tccgaaggta actggcttca gcagagcgca gataccaaat
     1741 actgttcttc tagtgtagcc gtagttaggc caccacttca agaactctgt agcaccgcct
     1801 acatacctcg ctctgctaat cctgttacca gtggctgctg ccagtggcga taagtcgtgt
     1861 cttaccgggt tggactcaag acgatagtta ccggataagg cgcagcggtc gggctgaacg
     1921 gggggttcgt gcacacagcc cagcttggag cgaacgacct acaccgaact gagataccta
     1981 cagcgtgagc tttgagaaag cgccacgctt cccgaaggga gaaaggcgga caggtatccg
     2041 gtaagcggca gggtcggaac aggagagcgc acgagggagc ttccaggggg aaacgcctgg
     2101 tatctttata gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt tttgtgatgc
     2161 tcgtcagggg ggcggagcct atggaaaaac gccagcaacg cggccttttt acggttcctg
     2221 gccttttgct ggccttttgc tcacatgttc tttcctgcgt tatcccctga ttctgtggat
     2281 aaccgtatta ccgcctttga gtgagctgat accgctcgcc gcagccgaac gaccgagcgc
     2341 agcgagtcag tgagcgagga agcggaagag cgcccaatac gcaaaccgcc tctccccgcg
     2401 cgttggccga ttcattaatg cagctggcac gacaggtttc ccgactggaa agcgggcagt
     2461 gagcgcaacg caattaatgt gagttagctc actcattagg caggcgcgcc cagctgtcta
     2521 gggcggcgga tttgtcctac tcaggagagc gttcaccgac aaacaacaga taaaacgaaa
     2581 ggcccagtct ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P41 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P41, contains a Phlf promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P41_Terminator3_Phlf_RiboC",
                },
                {
                    "accessor": "B-P42",
                    "binaryString": """LOCUS       B-P42_Terminator3_CymR_RiboC 2654 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P42 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P42,
            contains a CymR promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   63ab766b44eab288aea425ef34671dc7
VERSION     63ab766b44eab288aea425ef34671dc7
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    219..293
                     /label="RiboC"
     regulatory      129..218
                     /label="CymR"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    296..350
                     /label="LMS"
     misc_feature    486..1524
                     /label="SEVA_Ap"
     misc_feature    1598..2526
                     /label="SEVA_pUC"
     misc_feature    357..459
                     /label="SEVA_T0"
     misc_feature    2541..2645
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctaa caaacagaca atctggtctg tttgtattat ggaaaatttt tctgtataat
      181 agattcaaca aacagacaat ctggtctgtt tgtattatag tagtcaccgg ctgtgcttgc
      241 cggtctgatg agcctgtgaa ggcgaaacta cctctacaaa taattttgtt taaggctcgg
      301 gagacctatc ggtaataaca gtccaatctg gtgtaacttc ggaatcgtcc actagtcttg
      361 gactcctgtt gatagatcca gtaatgacct cagaactcca tctggatttg ttcagaacgc
      421 tcggttgccg ccgggcgttt tttattggtg agaatccagg ggtccccaat aattacgatt
      481 taaattagta gcccgcctaa tgagcgggct tttttttaat tcccctattt gtttattttt
      541 ctaaatacat tcaaatatgt atccgctcat gagacaataa ccctgataaa tgcttcaata
      601 atattgaaaa aggaagagta tgagcattca gcattttcgt gtggcgctga ttccgttttt
      661 tgcggcgttt tgcctgccgg tgtttgcgca tccggaaacc ctggtgaaag tgaaagatgc
      721 ggaagatcaa ctgggtgcgc gcgtgggcta tattgaactg gatctgaaca gcggcaaaat
      781 tctggaatct tttcgtccgg aagaacgttt tccgatgatg agcaccttta aagtgctgct
      841 gtgcggtgcg gttctgagcc gtgtggatgc gggccaggaa caactgggcc gtcgtattca
      901 ttatagccag aacgatctgg tggaatatag cccggtgacc gaaaaacatc tgaccgatgg
      961 catgaccgtg cgtgaactgt gcagcgcggc gattaccatg agcgataaca ccgcggcgaa
     1021 cctgctgctg acgaccattg gcggtccgaa agaactgacc gcgtttctgc ataacatggg
     1081 cgatcatgtg acccgtctgg atcgttggga accggaactg aacgaagcga ttccgaacga
     1141 tgaacgtgat accaccatgc cggcagcaat ggcgaccacc ctgcgtaaac tgctgacggg
     1201 tgagctgctg accctggcaa gccgccagca actgattgat tggatggaag cggataaagt
     1261 ggcgggtccg ctgctgcgta gcgcgctgcc ggctggctgg tttattgcgg ataaaagcgg
     1321 tgcgggcgaa cgtggcagcc gtggcattat tgcggcgctg ggcccggatg gtaaaccgag
     1381 ccgtattgtg gtgatttata ccaccggcag ccaggcgacg atggatgaac gtaaccgtca
     1441 gattgcggaa attggcgcga gcctgattaa acattggtaa accgatacaa ttaaaggctc
     1501 cttttggagc cttttttttt ggacgaccct tgtcggctcg acccacgact attgactgct
     1561 ctgagaaagt tgattgttac gattagtccg gccggccccg tagaaaagat caaaggatct
     1621 tcttgagatc ctttttttct gcgcgtaatc tgctgcttgc aaacaaaaaa accaccgcta
     1681 ccagcggtgg tttgtttgcc ggatcaagag ctaccaactc tttttccgaa ggtaactggc
     1741 ttcagcagag cgcagatacc aaatactgtt cttctagtgt agccgtagtt aggccaccac
     1801 ttcaagaact ctgtagcacc gcctacatac ctcgctctgc taatcctgtt accagtggct
     1861 gctgccagtg gcgataagtc gtgtcttacc gggttggact caagacgata gttaccggat
     1921 aaggcgcagc ggtcgggctg aacggggggt tcgtgcacac agcccagctt ggagcgaacg
     1981 acctacaccg aactgagata cctacagcgt gagctttgag aaagcgccac gcttcccgaa
     2041 gggagaaagg cggacaggta tccggtaagc ggcagggtcg gaacaggaga gcgcacgagg
     2101 gagcttccag ggggaaacgc ctggtatctt tatagtcctg tcgggtttcg ccacctctga
     2161 cttgagcgtc gatttttgtg atgctcgtca ggggggcgga gcctatggaa aaacgccagc
     2221 aacgcggcct ttttacggtt cctggccttt tgctggcctt ttgctcacat gttctttcct
     2281 gcgttatccc ctgattctgt ggataaccgt attaccgcct ttgagtgagc tgataccgct
     2341 cgccgcagcc gaacgaccga gcgcagcgag tcagtgagcg aggaagcgga agagcgccca
     2401 atacgcaaac cgcctctccc cgcgcgttgg ccgattcatt aatgcagctg gcacgacagg
     2461 tttcccgact ggaaagcggg cagtgagcgc aacgcaatta atgtgagtta gctcactcat
     2521 taggcaggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga gagcgttcac
     2581 cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc gttttatttg
     2641 atgcctttaa ttaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P42 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P42, contains a CymR promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P42_Terminator3_CymR_RiboC",
                },
                {
                    "accessor": "B-P43",
                    "binaryString": """LOCUS       B-P43_Terminator3_TetR_RiboC 2640 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P43 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P43,
            contains a TetR promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   19cc3a468322f28f945688208c29a88d
VERSION     19cc3a468322f28f945688208c29a88d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    205..279
                     /label="RiboC"
     regulatory      129..204
                     /label="TetR"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    282..336
                     /label="LMS"
     misc_feature    472..1510
                     /label="SEVA_Ap"
     misc_feature    1584..2512
                     /label="SEVA_pUC"
     misc_feature    343..445
                     /label="SEVA_T0"
     misc_feature    2527..2631
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttt ttcagcagga cgcactgacc tccctatcag tgatagagat tgacatccct
      181 atcagtgata gagatactga gcacagtagt caccggctgt gcttgccggt ctgatgagcc
      241 tgtgaaggcg aaactacctc tacaaataat tttgtttaag gctcgggaga cctatcggta
      301 ataacagtcc aatctggtgt aacttcggaa tcgtccacta gtcttggact cctgttgata
      361 gatccagtaa tgacctcaga actccatctg gatttgttca gaacgctcgg ttgccgccgg
      421 gcgtttttta ttggtgagaa tccaggggtc cccaataatt acgatttaaa ttagtagccc
      481 gcctaatgag cgggcttttt tttaattccc ctatttgttt atttttctaa atacattcaa
      541 atatgtatcc gctcatgaga caataaccct gataaatgct tcaataatat tgaaaaagga
      601 agagtatgag cattcagcat tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc
      661 tgccggtgtt tgcgcatccg gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg
      721 gtgcgcgcgt gggctatatt gaactggatc tgaacagcgg caaaattctg gaatcttttc
      781 gtccggaaga acgttttccg atgatgagca cctttaaagt gctgctgtgc ggtgcggttc
      841 tgagccgtgt ggatgcgggc caggaacaac tgggccgtcg tattcattat agccagaacg
      901 atctggtgga atatagcccg gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg
      961 aactgtgcag cgcggcgatt accatgagcg ataacaccgc ggcgaacctg ctgctgacga
     1021 ccattggcgg tccgaaagaa ctgaccgcgt ttctgcataa catgggcgat catgtgaccc
     1081 gtctggatcg ttgggaaccg gaactgaacg aagcgattcc gaacgatgaa cgtgatacca
     1141 ccatgccggc agcaatggcg accaccctgc gtaaactgct gacgggtgag ctgctgaccc
     1201 tggcaagccg ccagcaactg attgattgga tggaagcgga taaagtggcg ggtccgctgc
     1261 tgcgtagcgc gctgccggct ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg
     1321 gcagccgtgg cattattgcg gcgctgggcc cggatggtaa accgagccgt attgtggtga
     1381 tttataccac cggcagccag gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg
     1441 gcgcgagcct gattaaacat tggtaaaccg atacaattaa aggctccttt tggagccttt
     1501 ttttttggac gacccttgtc ggctcgaccc acgactattg actgctctga gaaagttgat
     1561 tgttacgatt agtccggccg gccccgtaga aaagatcaaa ggatcttctt gagatccttt
     1621 ttttctgcgc gtaatctgct gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg
     1681 tttgccggat caagagctac caactctttt tccgaaggta actggcttca gcagagcgca
     1741 gataccaaat actgttcttc tagtgtagcc gtagttaggc caccacttca agaactctgt
     1801 agcaccgcct acatacctcg ctctgctaat cctgttacca gtggctgctg ccagtggcga
     1861 taagtcgtgt cttaccgggt tggactcaag acgatagtta ccggataagg cgcagcggtc
     1921 gggctgaacg gggggttcgt gcacacagcc cagcttggag cgaacgacct acaccgaact
     1981 gagataccta cagcgtgagc tttgagaaag cgccacgctt cccgaaggga gaaaggcgga
     2041 caggtatccg gtaagcggca gggtcggaac aggagagcgc acgagggagc ttccaggggg
     2101 aaacgcctgg tatctttata gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt
     2161 tttgtgatgc tcgtcagggg ggcggagcct atggaaaaac gccagcaacg cggccttttt
     2221 acggttcctg gccttttgct ggccttttgc tcacatgttc tttcctgcgt tatcccctga
     2281 ttctgtggat aaccgtatta ccgcctttga gtgagctgat accgctcgcc gcagccgaac
     2341 gaccgagcgc agcgagtcag tgagcgagga agcggaagag cgcccaatac gcaaaccgcc
     2401 tctccccgcg cgttggccga ttcattaatg cagctggcac gacaggtttc ccgactggaa
     2461 agcgggcagt gagcgcaacg caattaatgt gagttagctc actcattagg caggcgcgcc
     2521 cagctgtcta gggcggcgga tttgtcctac tcaggagagc gttcaccgac aaacaacaga
     2581 taaaacgaaa ggcccagtct ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P43 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P43, contains a TetR promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P43_Terminator3_TetR_RiboC",
                },
                {
                    "accessor": "B-P44",
                    "binaryString": """LOCUS       B-P44_Terminator3_VanR_RiboC 2614 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P44 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P44,
            contains a VanR promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   fd90ec63fd091f9ad3024e4dfd59945a
VERSION     fd90ec63fd091f9ad3024e4dfd59945a
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      129..178
                     /label="VanR"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    179..253
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    256..310
                     /label="LMS"
     misc_feature    446..1484
                     /label="SEVA_Ap"
     misc_feature    1558..2486
                     /label="SEVA_pUC"
     misc_feature    317..419
                     /label="SEVA_T0"
     misc_feature    2501..2605
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctat tggatccaat tgacagctag ctcagtccta ggtaccattg gatccaatag
      181 tagtcaccgg ctgtgcttgc cggtctgatg agcctgtgaa ggcgaaacta cctctacaaa
      241 taattttgtt taaggctcgg gagacctatc ggtaataaca gtccaatctg gtgtaacttc
      301 ggaatcgtcc actagtcttg gactcctgtt gatagatcca gtaatgacct cagaactcca
      361 tctggatttg ttcagaacgc tcggttgccg ccgggcgttt tttattggtg agaatccagg
      421 ggtccccaat aattacgatt taaattagta gcccgcctaa tgagcgggct tttttttaat
      481 tcccctattt gtttattttt ctaaatacat tcaaatatgt atccgctcat gagacaataa
      541 ccctgataaa tgcttcaata atattgaaaa aggaagagta tgagcattca gcattttcgt
      601 gtggcgctga ttccgttttt tgcggcgttt tgcctgccgg tgtttgcgca tccggaaacc
      661 ctggtgaaag tgaaagatgc ggaagatcaa ctgggtgcgc gcgtgggcta tattgaactg
      721 gatctgaaca gcggcaaaat tctggaatct tttcgtccgg aagaacgttt tccgatgatg
      781 agcaccttta aagtgctgct gtgcggtgcg gttctgagcc gtgtggatgc gggccaggaa
      841 caactgggcc gtcgtattca ttatagccag aacgatctgg tggaatatag cccggtgacc
      901 gaaaaacatc tgaccgatgg catgaccgtg cgtgaactgt gcagcgcggc gattaccatg
      961 agcgataaca ccgcggcgaa cctgctgctg acgaccattg gcggtccgaa agaactgacc
     1021 gcgtttctgc ataacatggg cgatcatgtg acccgtctgg atcgttggga accggaactg
     1081 aacgaagcga ttccgaacga tgaacgtgat accaccatgc cggcagcaat ggcgaccacc
     1141 ctgcgtaaac tgctgacggg tgagctgctg accctggcaa gccgccagca actgattgat
     1201 tggatggaag cggataaagt ggcgggtccg ctgctgcgta gcgcgctgcc ggctggctgg
     1261 tttattgcgg ataaaagcgg tgcgggcgaa cgtggcagcc gtggcattat tgcggcgctg
     1321 ggcccggatg gtaaaccgag ccgtattgtg gtgatttata ccaccggcag ccaggcgacg
     1381 atggatgaac gtaaccgtca gattgcggaa attggcgcga gcctgattaa acattggtaa
     1441 accgatacaa ttaaaggctc cttttggagc cttttttttt ggacgaccct tgtcggctcg
     1501 acccacgact attgactgct ctgagaaagt tgattgttac gattagtccg gccggccccg
     1561 tagaaaagat caaaggatct tcttgagatc ctttttttct gcgcgtaatc tgctgcttgc
     1621 aaacaaaaaa accaccgcta ccagcggtgg tttgtttgcc ggatcaagag ctaccaactc
     1681 tttttccgaa ggtaactggc ttcagcagag cgcagatacc aaatactgtt cttctagtgt
     1741 agccgtagtt aggccaccac ttcaagaact ctgtagcacc gcctacatac ctcgctctgc
     1801 taatcctgtt accagtggct gctgccagtg gcgataagtc gtgtcttacc gggttggact
     1861 caagacgata gttaccggat aaggcgcagc ggtcgggctg aacggggggt tcgtgcacac
     1921 agcccagctt ggagcgaacg acctacaccg aactgagata cctacagcgt gagctttgag
     1981 aaagcgccac gcttcccgaa gggagaaagg cggacaggta tccggtaagc ggcagggtcg
     2041 gaacaggaga gcgcacgagg gagcttccag ggggaaacgc ctggtatctt tatagtcctg
     2101 tcgggtttcg ccacctctga cttgagcgtc gatttttgtg atgctcgtca ggggggcgga
     2161 gcctatggaa aaacgccagc aacgcggcct ttttacggtt cctggccttt tgctggcctt
     2221 ttgctcacat gttctttcct gcgttatccc ctgattctgt ggataaccgt attaccgcct
     2281 ttgagtgagc tgataccgct cgccgcagcc gaacgaccga gcgcagcgag tcagtgagcg
     2341 aggaagcgga agagcgccca atacgcaaac cgcctctccc cgcgcgttgg ccgattcatt
     2401 aatgcagctg gcacgacagg tttcccgact ggaaagcggg cagtgagcgc aacgcaatta
     2461 atgtgagtta gctcactcat taggcaggcg cgcccagctg tctagggcgg cggatttgtc
     2521 ctactcagga gagcgttcac cgacaaacaa cagataaaac gaaaggccca gtctttcgac
     2581 tgagcctttc gttttatttg atgcctttaa ttaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P44 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P44, contains a VanR promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P44_Terminator3_VanR_RiboC",
                },
                {
                    "accessor": "B-P45",
                    "binaryString": """LOCUS       B-P45_Terminator3_LuxR_RiboC 2619 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P45 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P45,
            contains a LuxR promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   0e6680c658b4b48f94acb8d75ca20548
VERSION     0e6680c658b4b48f94acb8d75ca20548
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    184..258
                     /label="RiboC"
     regulatory      58..108
                     /label="Terminator3"
     regulatory      129..183
                     /label="LuxR"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    261..315
                     /label="LMS"
     misc_feature    451..1489
                     /label="SEVA_Ap"
     misc_feature    1563..2491
                     /label="SEVA_pUC"
     misc_feature    322..424
                     /label="SEVA_T0"
     misc_feature    2506..2610
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctac ctgtaggatc gtacaggttt acgcaagaaa atggtttgtt acagtcgaat
      181 aaaagtagtc accggctgtg cttgccggtc tgatgagcct gtgaaggcga aactacctct
      241 acaaataatt ttgtttaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta
      301 acttcggaat cgtccactag tcttggactc ctgttgatag atccagtaat gacctcagaa
      361 ctccatctgg atttgttcag aacgctcggt tgccgccggg cgttttttat tggtgagaat
      421 ccaggggtcc ccaataatta cgatttaaat tagtagcccg cctaatgagc gggctttttt
      481 ttaattcccc tatttgttta tttttctaaa tacattcaaa tatgtatccg ctcatgagac
      541 aataaccctg ataaatgctt caataatatt gaaaaaggaa gagtatgagc attcagcatt
      601 ttcgtgtggc gctgattccg ttttttgcgg cgttttgcct gccggtgttt gcgcatccgg
      661 aaaccctggt gaaagtgaaa gatgcggaag atcaactggg tgcgcgcgtg ggctatattg
      721 aactggatct gaacagcggc aaaattctgg aatcttttcg tccggaagaa cgttttccga
      781 tgatgagcac ctttaaagtg ctgctgtgcg gtgcggttct gagccgtgtg gatgcgggcc
      841 aggaacaact gggccgtcgt attcattata gccagaacga tctggtggaa tatagcccgg
      901 tgaccgaaaa acatctgacc gatggcatga ccgtgcgtga actgtgcagc gcggcgatta
      961 ccatgagcga taacaccgcg gcgaacctgc tgctgacgac cattggcggt ccgaaagaac
     1021 tgaccgcgtt tctgcataac atgggcgatc atgtgacccg tctggatcgt tgggaaccgg
     1081 aactgaacga agcgattccg aacgatgaac gtgataccac catgccggca gcaatggcga
     1141 ccaccctgcg taaactgctg acgggtgagc tgctgaccct ggcaagccgc cagcaactga
     1201 ttgattggat ggaagcggat aaagtggcgg gtccgctgct gcgtagcgcg ctgccggctg
     1261 gctggtttat tgcggataaa agcggtgcgg gcgaacgtgg cagccgtggc attattgcgg
     1321 cgctgggccc ggatggtaaa ccgagccgta ttgtggtgat ttataccacc ggcagccagg
     1381 cgacgatgga tgaacgtaac cgtcagattg cggaaattgg cgcgagcctg attaaacatt
     1441 ggtaaaccga tacaattaaa ggctcctttt ggagcctttt tttttggacg acccttgtcg
     1501 gctcgaccca cgactattga ctgctctgag aaagttgatt gttacgatta gtccggccgg
     1561 ccccgtagaa aagatcaaag gatcttcttg agatcctttt tttctgcgcg taatctgctg
     1621 cttgcaaaca aaaaaaccac cgctaccagc ggtggtttgt ttgccggatc aagagctacc
     1681 aactcttttt ccgaaggtaa ctggcttcag cagagcgcag ataccaaata ctgttcttct
     1741 agtgtagccg tagttaggcc accacttcaa gaactctgta gcaccgccta catacctcgc
     1801 tctgctaatc ctgttaccag tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt
     1861 ggactcaaga cgatagttac cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg
     1921 cacacagccc agcttggagc gaacgaccta caccgaactg agatacctac agcgtgagct
     1981 ttgagaaagc gccacgcttc ccgaagggag aaaggcggac aggtatccgg taagcggcag
     2041 ggtcggaaca ggagagcgca cgagggagct tccaggggga aacgcctggt atctttatag
     2101 tcctgtcggg tttcgccacc tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg
     2161 gcggagccta tggaaaaacg ccagcaacgc ggccttttta cggttcctgg ccttttgctg
     2221 gccttttgct cacatgttct ttcctgcgtt atcccctgat tctgtggata accgtattac
     2281 cgcctttgag tgagctgata ccgctcgccg cagccgaacg accgagcgca gcgagtcagt
     2341 gagcgaggaa gcggaagagc gcccaatacg caaaccgcct ctccccgcgc gttggccgat
     2401 tcattaatgc agctggcacg acaggtttcc cgactggaaa gcgggcagtg agcgcaacgc
     2461 aattaatgtg agttagctca ctcattaggc aggcgcgccc agctgtctag ggcggcggat
     2521 ttgtcctact caggagagcg ttcaccgaca aacaacagat aaaacgaaag gcccagtctt
     2581 tcgactgagc ctttcgtttt atttgatgcc tttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P45 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P45, contains a LuxR promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P45_Terminator3_LuxR_RiboC",
                },
                {
                    "accessor": "B-P46",
                    "binaryString": """LOCUS       B-P46_Terminator3_CinR_RiboC 2790 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P46 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P46,
            contains a CinR promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   9d6ba241db99f774ae41453942acfd98
VERSION     9d6ba241db99f774ae41453942acfd98
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    355..429
                     /label="RiboC"
     regulatory      129..354
                     /label="CinR"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    432..486
                     /label="LMS"
     misc_feature    622..1660
                     /label="SEVA_Ap"
     misc_feature    1734..2662
                     /label="SEVA_pUC"
     misc_feature    493..595
                     /label="SEVA_T0"
     misc_feature    2677..2781
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctcc ctttgtgcgt ccaaacggac gcacggcgct ctaaagcggg tcgcgatctt
      181 tcagattcgc tcctcgcgct ttcagtcttt gttttggcgc atgtcgttat cgcaaaaccg
      241 ctgcacactt ttgcgcgaca tgctctgatc cccctcatct gggggggcct atctgaggga
      301 atttccgatc cggctcgcct gaaccattct gctttccacg aacttgaaaa cgctagtagt
      361 caccggctgt gcttgccggt ctgatgagcc tgtgaaggcg aaactacctc tacaaataat
      421 tttgtttaag gctcgggaga cctatcggta ataacagtcc aatctggtgt aacttcggaa
      481 tcgtccacta gtcttggact cctgttgata gatccagtaa tgacctcaga actccatctg
      541 gatttgttca gaacgctcgg ttgccgccgg gcgtttttta ttggtgagaa tccaggggtc
      601 cccaataatt acgatttaaa ttagtagccc gcctaatgag cgggcttttt tttaattccc
      661 ctatttgttt atttttctaa atacattcaa atatgtatcc gctcatgaga caataaccct
      721 gataaatgct tcaataatat tgaaaaagga agagtatgag cattcagcat tttcgtgtgg
      781 cgctgattcc gttttttgcg gcgttttgcc tgccggtgtt tgcgcatccg gaaaccctgg
      841 tgaaagtgaa agatgcggaa gatcaactgg gtgcgcgcgt gggctatatt gaactggatc
      901 tgaacagcgg caaaattctg gaatcttttc gtccggaaga acgttttccg atgatgagca
      961 cctttaaagt gctgctgtgc ggtgcggttc tgagccgtgt ggatgcgggc caggaacaac
     1021 tgggccgtcg tattcattat agccagaacg atctggtgga atatagcccg gtgaccgaaa
     1081 aacatctgac cgatggcatg accgtgcgtg aactgtgcag cgcggcgatt accatgagcg
     1141 ataacaccgc ggcgaacctg ctgctgacga ccattggcgg tccgaaagaa ctgaccgcgt
     1201 ttctgcataa catgggcgat catgtgaccc gtctggatcg ttgggaaccg gaactgaacg
     1261 aagcgattcc gaacgatgaa cgtgatacca ccatgccggc agcaatggcg accaccctgc
     1321 gtaaactgct gacgggtgag ctgctgaccc tggcaagccg ccagcaactg attgattgga
     1381 tggaagcgga taaagtggcg ggtccgctgc tgcgtagcgc gctgccggct ggctggttta
     1441 ttgcggataa aagcggtgcg ggcgaacgtg gcagccgtgg cattattgcg gcgctgggcc
     1501 cggatggtaa accgagccgt attgtggtga tttataccac cggcagccag gcgacgatgg
     1561 atgaacgtaa ccgtcagatt gcggaaattg gcgcgagcct gattaaacat tggtaaaccg
     1621 atacaattaa aggctccttt tggagccttt ttttttggac gacccttgtc ggctcgaccc
     1681 acgactattg actgctctga gaaagttgat tgttacgatt agtccggccg gccccgtaga
     1741 aaagatcaaa ggatcttctt gagatccttt ttttctgcgc gtaatctgct gcttgcaaac
     1801 aaaaaaacca ccgctaccag cggtggtttg tttgccggat caagagctac caactctttt
     1861 tccgaaggta actggcttca gcagagcgca gataccaaat actgttcttc tagtgtagcc
     1921 gtagttaggc caccacttca agaactctgt agcaccgcct acatacctcg ctctgctaat
     1981 cctgttacca gtggctgctg ccagtggcga taagtcgtgt cttaccgggt tggactcaag
     2041 acgatagtta ccggataagg cgcagcggtc gggctgaacg gggggttcgt gcacacagcc
     2101 cagcttggag cgaacgacct acaccgaact gagataccta cagcgtgagc tttgagaaag
     2161 cgccacgctt cccgaaggga gaaaggcgga caggtatccg gtaagcggca gggtcggaac
     2221 aggagagcgc acgagggagc ttccaggggg aaacgcctgg tatctttata gtcctgtcgg
     2281 gtttcgccac ctctgacttg agcgtcgatt tttgtgatgc tcgtcagggg ggcggagcct
     2341 atggaaaaac gccagcaacg cggccttttt acggttcctg gccttttgct ggccttttgc
     2401 tcacatgttc tttcctgcgt tatcccctga ttctgtggat aaccgtatta ccgcctttga
     2461 gtgagctgat accgctcgcc gcagccgaac gaccgagcgc agcgagtcag tgagcgagga
     2521 agcggaagag cgcccaatac gcaaaccgcc tctccccgcg cgttggccga ttcattaatg
     2581 cagctggcac gacaggtttc ccgactggaa agcgggcagt gagcgcaacg caattaatgt
     2641 gagttagctc actcattagg caggcgcgcc cagctgtcta gggcggcgga tttgtcctac
     2701 tcaggagagc gttcaccgac aaacaacaga taaaacgaaa ggcccagtct ttcgactgag
     2761 cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P46 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P46, contains a CinR promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P46_Terminator3_CinR_RiboC",
                },
                {
                    "accessor": "B-P47",
                    "binaryString": """LOCUS       B-P47_Terminator3_LacI_RiboC 2620 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P47 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P47,
            contains a LacI promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   3bcbe58d4d3bb671aa0ae4e22c9e0046
VERSION     3bcbe58d4d3bb671aa0ae4e22c9e0046
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      129..184
                     /label="LacI"
     misc_feature    185..259
                     /label="RiboC"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    262..316
                     /label="LMS"
     misc_feature    452..1490
                     /label="SEVA_Ap"
     misc_feature    1564..2492
                     /label="SEVA_pUC"
     misc_feature    323..425
                     /label="SEVA_T0"
     misc_feature    2507..2611
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatcttg ttgacaatta atcatcggct cgtataatgt gtggaattgt gagcgctcac
      181 aattagtagt caccggctgt gcttgccggt ctgatgagcc tgtgaaggcg aaactacctc
      241 tacaaataat tttgtttaag gctcgggaga cctatcggta ataacagtcc aatctggtgt
      301 aacttcggaa tcgtccacta gtcttggact cctgttgata gatccagtaa tgacctcaga
      361 actccatctg gatttgttca gaacgctcgg ttgccgccgg gcgtttttta ttggtgagaa
      421 tccaggggtc cccaataatt acgatttaaa ttagtagccc gcctaatgag cgggcttttt
      481 tttaattccc ctatttgttt atttttctaa atacattcaa atatgtatcc gctcatgaga
      541 caataaccct gataaatgct tcaataatat tgaaaaagga agagtatgag cattcagcat
      601 tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc tgccggtgtt tgcgcatccg
      661 gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg gtgcgcgcgt gggctatatt
      721 gaactggatc tgaacagcgg caaaattctg gaatcttttc gtccggaaga acgttttccg
      781 atgatgagca cctttaaagt gctgctgtgc ggtgcggttc tgagccgtgt ggatgcgggc
      841 caggaacaac tgggccgtcg tattcattat agccagaacg atctggtgga atatagcccg
      901 gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg aactgtgcag cgcggcgatt
      961 accatgagcg ataacaccgc ggcgaacctg ctgctgacga ccattggcgg tccgaaagaa
     1021 ctgaccgcgt ttctgcataa catgggcgat catgtgaccc gtctggatcg ttgggaaccg
     1081 gaactgaacg aagcgattcc gaacgatgaa cgtgatacca ccatgccggc agcaatggcg
     1141 accaccctgc gtaaactgct gacgggtgag ctgctgaccc tggcaagccg ccagcaactg
     1201 attgattgga tggaagcgga taaagtggcg ggtccgctgc tgcgtagcgc gctgccggct
     1261 ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg gcagccgtgg cattattgcg
     1321 gcgctgggcc cggatggtaa accgagccgt attgtggtga tttataccac cggcagccag
     1381 gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg gcgcgagcct gattaaacat
     1441 tggtaaaccg atacaattaa aggctccttt tggagccttt ttttttggac gacccttgtc
     1501 ggctcgaccc acgactattg actgctctga gaaagttgat tgttacgatt agtccggccg
     1561 gccccgtaga aaagatcaaa ggatcttctt gagatccttt ttttctgcgc gtaatctgct
     1621 gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg tttgccggat caagagctac
     1681 caactctttt tccgaaggta actggcttca gcagagcgca gataccaaat actgttcttc
     1741 tagtgtagcc gtagttaggc caccacttca agaactctgt agcaccgcct acatacctcg
     1801 ctctgctaat cctgttacca gtggctgctg ccagtggcga taagtcgtgt cttaccgggt
     1861 tggactcaag acgatagtta ccggataagg cgcagcggtc gggctgaacg gggggttcgt
     1921 gcacacagcc cagcttggag cgaacgacct acaccgaact gagataccta cagcgtgagc
     1981 tttgagaaag cgccacgctt cccgaaggga gaaaggcgga caggtatccg gtaagcggca
     2041 gggtcggaac aggagagcgc acgagggagc ttccaggggg aaacgcctgg tatctttata
     2101 gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt tttgtgatgc tcgtcagggg
     2161 ggcggagcct atggaaaaac gccagcaacg cggccttttt acggttcctg gccttttgct
     2221 ggccttttgc tcacatgttc tttcctgcgt tatcccctga ttctgtggat aaccgtatta
     2281 ccgcctttga gtgagctgat accgctcgcc gcagccgaac gaccgagcgc agcgagtcag
     2341 tgagcgagga agcggaagag cgcccaatac gcaaaccgcc tctccccgcg cgttggccga
     2401 ttcattaatg cagctggcac gacaggtttc ccgactggaa agcgggcagt gagcgcaacg
     2461 caattaatgt gagttagctc actcattagg caggcgcgcc cagctgtcta gggcggcgga
     2521 tttgtcctac tcaggagagc gttcaccgac aaacaacaga taaaacgaaa ggcccagtct
     2581 ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P47 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P47, contains a LacI promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P47_Terminator3_LacI_RiboC",
                },
                {
                    "accessor": "B-P48",
                    "binaryString": """LOCUS       B-P48_Terminator3_AraC_RiboC 2853 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P48 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P48,
            contains a AraC promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   c218f26fe11fb70b1b8f30029cfe46b0
VERSION     c218f26fe11fb70b1b8f30029cfe46b0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    418..492
                     /label="RiboC"
     regulatory      129..417
                     /label="AraC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    495..549
                     /label="LMS"
     misc_feature    685..1723
                     /label="SEVA_Ap"
     misc_feature    1797..2725
                     /label="SEVA_pUC"
     misc_feature    556..658
                     /label="SEVA_T0"
     misc_feature    2740..2844
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctag aaaccaattg tccatattgc atcagacatt gccgtcactg cgtcttttac
      181 tggctcttct cgctaaccaa accggtaacc ccgcttatta aaagcattct gtaacaaagc
      241 gggaccaaag ccatgacaaa aacgcgtaac aaaagtgtct ataatcacgg cagaaaagtc
      301 cacattgatt atttgcacgg cgtcacactt tgctatgcca tagcattttt atccataaga
      361 ttagcggatc ctacctgacg ctttttatcg caactctcta ctgtttctcc atacccgagt
      421 agtcaccggc tgtgcttgcc ggtctgatga gcctgtgaag gcgaaactac ctctacaaat
      481 aattttgttt aaggctcggg agacctatcg gtaataacag tccaatctgg tgtaacttcg
      541 gaatcgtcca ctagtcttgg actcctgttg atagatccag taatgacctc agaactccat
      601 ctggatttgt tcagaacgct cggttgccgc cgggcgtttt ttattggtga gaatccaggg
      661 gtccccaata attacgattt aaattagtag cccgcctaat gagcgggctt ttttttaatt
      721 cccctatttg tttatttttc taaatacatt caaatatgta tccgctcatg agacaataac
      781 cctgataaat gcttcaataa tattgaaaaa ggaagagtat gagcattcag cattttcgtg
      841 tggcgctgat tccgtttttt gcggcgtttt gcctgccggt gtttgcgcat ccggaaaccc
      901 tggtgaaagt gaaagatgcg gaagatcaac tgggtgcgcg cgtgggctat attgaactgg
      961 atctgaacag cggcaaaatt ctggaatctt ttcgtccgga agaacgtttt ccgatgatga
     1021 gcacctttaa agtgctgctg tgcggtgcgg ttctgagccg tgtggatgcg ggccaggaac
     1081 aactgggccg tcgtattcat tatagccaga acgatctggt ggaatatagc ccggtgaccg
     1141 aaaaacatct gaccgatggc atgaccgtgc gtgaactgtg cagcgcggcg attaccatga
     1201 gcgataacac cgcggcgaac ctgctgctga cgaccattgg cggtccgaaa gaactgaccg
     1261 cgtttctgca taacatgggc gatcatgtga cccgtctgga tcgttgggaa ccggaactga
     1321 acgaagcgat tccgaacgat gaacgtgata ccaccatgcc ggcagcaatg gcgaccaccc
     1381 tgcgtaaact gctgacgggt gagctgctga ccctggcaag ccgccagcaa ctgattgatt
     1441 ggatggaagc ggataaagtg gcgggtccgc tgctgcgtag cgcgctgccg gctggctggt
     1501 ttattgcgga taaaagcggt gcgggcgaac gtggcagccg tggcattatt gcggcgctgg
     1561 gcccggatgg taaaccgagc cgtattgtgg tgatttatac caccggcagc caggcgacga
     1621 tggatgaacg taaccgtcag attgcggaaa ttggcgcgag cctgattaaa cattggtaaa
     1681 ccgatacaat taaaggctcc ttttggagcc tttttttttg gacgaccctt gtcggctcga
     1741 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccccgt
     1801 agaaaagatc aaaggatctt cttgagatcc tttttttctg cgcgtaatct gctgcttgca
     1861 aacaaaaaaa ccaccgctac cagcggtggt ttgtttgccg gatcaagagc taccaactct
     1921 ttttccgaag gtaactggct tcagcagagc gcagatacca aatactgttc ttctagtgta
     1981 gccgtagtta ggccaccact tcaagaactc tgtagcaccg cctacatacc tcgctctgct
     2041 aatcctgtta ccagtggctg ctgccagtgg cgataagtcg tgtcttaccg ggttggactc
     2101 aagacgatag ttaccggata aggcgcagcg gtcgggctga acggggggtt cgtgcacaca
     2161 gcccagcttg gagcgaacga cctacaccga actgagatac ctacagcgtg agctttgaga
     2221 aagcgccacg cttcccgaag ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg
     2281 aacaggagag cgcacgaggg agcttccagg gggaaacgcc tggtatcttt atagtcctgt
     2341 cgggtttcgc cacctctgac ttgagcgtcg atttttgtga tgctcgtcag gggggcggag
     2401 cctatggaaa aacgccagca acgcggcctt tttacggttc ctggcctttt gctggccttt
     2461 tgctcacatg ttctttcctg cgttatcccc tgattctgtg gataaccgta ttaccgcctt
     2521 tgagtgagct gataccgctc gccgcagccg aacgaccgag cgcagcgagt cagtgagcga
     2581 ggaagcggaa gagcgcccaa tacgcaaacc gcctctcccc gcgcgttggc cgattcatta
     2641 atgcagctgg cacgacaggt ttcccgactg gaaagcgggc agtgagcgca acgcaattaa
     2701 tgtgagttag ctcactcatt aggcaggcgc gcccagctgt ctagggcggc ggatttgtcc
     2761 tactcaggag agcgttcacc gacaaacaac agataaaacg aaaggcccag tctttcgact
     2821 gagcctttcg ttttatttga tgcctttaat taa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P48 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P48, contains a AraC promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P48_Terminator3_AraC_RiboC",
                },
                {
                    "accessor": "B-P49",
                    "binaryString": """LOCUS       B-P49_Terminator1_T7_100_RiboA 2597 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P49 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P49,
            contains a T7_100 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   f7a49ade8938b0d405c2e93b26bdda7c
VERSION     f7a49ade8938b0d405c2e93b26bdda7c
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    162..236
                     /label="RiboA"
     regulatory      139..161
                     /label="T7_100"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    239..293
                     /label="LMS"
     misc_feature    429..1467
                     /label="SEVA_Ap"
     misc_feature    1541..2469
                     /label="SEVA_pUC"
     misc_feature    300..402
                     /label="SEVA_T0"
     misc_feature    2484..2588
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctta atacgactca ctatagggga cagctgtcac cggatgtgct
      181 ttccggtctg atgagtccgt gaggacgaaa cagcctctac aaataatttt gtttaaggct
      241 cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc
      301 ttggactcct gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa
      361 cgctcggttg ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg
      421 atttaaatta gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt
      481 tttctaaata cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca
      541 ataatattga aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt
      601 ttttgcggcg ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga
      661 tgcggaagat caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa
      721 aattctggaa tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct
      781 gctgtgcggt gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat
      841 tcattatagc cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga
      901 tggcatgacc gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc
      961 gaacctgctg ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat
     1021 gggcgatcat gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa
     1081 cgatgaacgt gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac
     1141 gggtgagctg ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa
     1201 agtggcgggt ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag
     1261 cggtgcgggc gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc
     1321 gagccgtatt gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg
     1381 tcagattgcg gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg
     1441 ctccttttgg agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact
     1501 gctctgagaa agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga
     1561 tcttcttgag atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg
     1621 ctaccagcgg tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact
     1681 ggcttcagca gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac
     1741 cacttcaaga actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg
     1801 gctgctgcca gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg
     1861 gataaggcgc agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga
     1921 acgacctaca ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc
     1981 gaagggagaa aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg
     2041 agggagcttc cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc
     2101 tgacttgagc gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc
     2161 agcaacgcgg cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt
     2221 cctgcgttat cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc
     2281 gctcgccgca gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc
     2341 ccaatacgca aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac
     2401 aggtttcccg actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact
     2461 cattaggcag gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt
     2521 caccgacaaa caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat
     2581 ttgatgcctt taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P49 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P49, contains a T7_100 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P49_Terminator1_T7_100_RiboA",
                },
                {
                    "accessor": "B-P50",
                    "binaryString": """LOCUS       B-P50_Terminator1_T7_52_RiboA 2597 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P50 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P50,
            contains a T7_52 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   9ec62f9104ad96390a89c4667d495a7a
VERSION     9ec62f9104ad96390a89c4667d495a7a
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      139..161
                     /label="T7_52"
     misc_feature    162..236
                     /label="RiboA"
     misc_feature    119..138
                     /label="SpacerA"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    239..293
                     /label="LMS"
     misc_feature    429..1467
                     /label="SEVA_Ap"
     misc_feature    1541..2469
                     /label="SEVA_pUC"
     misc_feature    300..402
                     /label="SEVA_T0"
     misc_feature    2484..2588
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctta atacgactca ctgccgggag aagctgtcac cggatgtgct
      181 ttccggtctg atgagtccgt gaggacgaaa cagcctctac aaataatttt gtttaaggct
      241 cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc
      301 ttggactcct gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa
      361 cgctcggttg ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg
      421 atttaaatta gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt
      481 tttctaaata cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca
      541 ataatattga aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt
      601 ttttgcggcg ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga
      661 tgcggaagat caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa
      721 aattctggaa tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct
      781 gctgtgcggt gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat
      841 tcattatagc cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga
      901 tggcatgacc gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc
      961 gaacctgctg ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat
     1021 gggcgatcat gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa
     1081 cgatgaacgt gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac
     1141 gggtgagctg ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa
     1201 agtggcgggt ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag
     1261 cggtgcgggc gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc
     1321 gagccgtatt gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg
     1381 tcagattgcg gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg
     1441 ctccttttgg agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact
     1501 gctctgagaa agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga
     1561 tcttcttgag atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg
     1621 ctaccagcgg tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact
     1681 ggcttcagca gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac
     1741 cacttcaaga actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg
     1801 gctgctgcca gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg
     1861 gataaggcgc agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga
     1921 acgacctaca ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc
     1981 gaagggagaa aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg
     2041 agggagcttc cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc
     2101 tgacttgagc gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc
     2161 agcaacgcgg cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt
     2221 cctgcgttat cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc
     2281 gctcgccgca gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc
     2341 ccaatacgca aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac
     2401 aggtttcccg actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact
     2461 cattaggcag gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt
     2521 caccgacaaa caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat
     2581 ttgatgcctt taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P50 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P50, contains a T7_52 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P50_Terminator1_T7_52_RiboA",
                },
                {
                    "accessor": "B-P51",
                    "binaryString": """LOCUS       B-P51_Terminator1_T7_50_RiboA 2597 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P51 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P51,
            contains a T7_50 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   e8e7d4adac5c136a5e15fc2806c6df24
VERSION     e8e7d4adac5c136a5e15fc2806c6df24
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    162..236
                     /label="RiboA"
     regulatory      139..161
                     /label="T7_50"
     misc_feature    119..138
                     /label="SpacerA"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    239..293
                     /label="LMS"
     misc_feature    429..1467
                     /label="SEVA_Ap"
     misc_feature    1541..2469
                     /label="SEVA_pUC"
     misc_feature    300..402
                     /label="SEVA_T0"
     misc_feature    2484..2588
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctta atacgactca ctatggggag aagctgtcac cggatgtgct
      181 ttccggtctg atgagtccgt gaggacgaaa cagcctctac aaataatttt gtttaaggct
      241 cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc
      301 ttggactcct gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa
      361 cgctcggttg ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg
      421 atttaaatta gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt
      481 tttctaaata cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca
      541 ataatattga aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt
      601 ttttgcggcg ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga
      661 tgcggaagat caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa
      721 aattctggaa tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct
      781 gctgtgcggt gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat
      841 tcattatagc cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga
      901 tggcatgacc gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc
      961 gaacctgctg ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat
     1021 gggcgatcat gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa
     1081 cgatgaacgt gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac
     1141 gggtgagctg ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa
     1201 agtggcgggt ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag
     1261 cggtgcgggc gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc
     1321 gagccgtatt gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg
     1381 tcagattgcg gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg
     1441 ctccttttgg agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact
     1501 gctctgagaa agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga
     1561 tcttcttgag atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg
     1621 ctaccagcgg tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact
     1681 ggcttcagca gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac
     1741 cacttcaaga actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg
     1801 gctgctgcca gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg
     1861 gataaggcgc agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga
     1921 acgacctaca ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc
     1981 gaagggagaa aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg
     2041 agggagcttc cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc
     2101 tgacttgagc gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc
     2161 agcaacgcgg cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt
     2221 cctgcgttat cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc
     2281 gctcgccgca gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc
     2341 ccaatacgca aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac
     2401 aggtttcccg actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact
     2461 cattaggcag gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt
     2521 caccgacaaa caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat
     2581 ttgatgcctt taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P51 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P51, contains a T7_50 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P51_Terminator1_T7_50_RiboA",
                },
                {
                    "accessor": "B-P52",
                    "binaryString": """LOCUS       B-P52_Terminator1_T7_25_RiboA 2597 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P52 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P52,
            contains a T7_25 promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   4362d6614da2053a11f81e72686b09d3
VERSION     4362d6614da2053a11f81e72686b09d3
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    162..236
                     /label="RiboA"
     regulatory      139..161
                     /label="T7_25"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    239..293
                     /label="LMS"
     misc_feature    429..1467
                     /label="SEVA_Ap"
     misc_feature    1541..2469
                     /label="SEVA_pUC"
     misc_feature    300..402
                     /label="SEVA_T0"
     misc_feature    2484..2588
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctta atacgactca ctgtcggggg aagctgtcac cggatgtgct
      181 ttccggtctg atgagtccgt gaggacgaaa cagcctctac aaataatttt gtttaaggct
      241 cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc
      301 ttggactcct gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa
      361 cgctcggttg ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg
      421 atttaaatta gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt
      481 tttctaaata cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca
      541 ataatattga aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt
      601 ttttgcggcg ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga
      661 tgcggaagat caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa
      721 aattctggaa tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct
      781 gctgtgcggt gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat
      841 tcattatagc cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga
      901 tggcatgacc gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc
      961 gaacctgctg ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat
     1021 gggcgatcat gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa
     1081 cgatgaacgt gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac
     1141 gggtgagctg ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa
     1201 agtggcgggt ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag
     1261 cggtgcgggc gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc
     1321 gagccgtatt gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg
     1381 tcagattgcg gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg
     1441 ctccttttgg agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact
     1501 gctctgagaa agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga
     1561 tcttcttgag atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg
     1621 ctaccagcgg tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact
     1681 ggcttcagca gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac
     1741 cacttcaaga actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg
     1801 gctgctgcca gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg
     1861 gataaggcgc agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga
     1921 acgacctaca ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc
     1981 gaagggagaa aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg
     2041 agggagcttc cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc
     2101 tgacttgagc gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc
     2161 agcaacgcgg cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt
     2221 cctgcgttat cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc
     2281 gctcgccgca gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc
     2341 ccaatacgca aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac
     2401 aggtttcccg actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact
     2461 cattaggcag gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt
     2521 caccgacaaa caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat
     2581 ttgatgcctt taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P52 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P52, contains a T7_25 promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P52_Terminator1_T7_25_RiboA",
                },
                {
                    "accessor": "B-P53",
                    "binaryString": """LOCUS       B-P53_Terminator2_T7_100_RiboB 2593 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P53 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P53,
            contains a T7_100 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   39f179ccb35b6cf05448ba186f7a97ec
VERSION     39f179ccb35b6cf05448ba186f7a97ec
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    158..232
                     /label="RiboB"
     regulatory      135..157
                     /label="T7_100"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    235..289
                     /label="LMS"
     misc_feature    425..1463
                     /label="SEVA_Ap"
     misc_feature    1537..2465
                     /label="SEVA_pUC"
     misc_feature    296..398
                     /label="SEVA_T0"
     misc_feature    2480..2584
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttaatac gactcactat aggggacagc gctcaacggg tgtgcttccc
      181 gttctgatga gtccgtgagg acgaaagcgc ctctacaaat aattttgttt aaggctcggg
      241 agacctatcg gtaataacag tccaatctgg tgtaacttcg gaatcgtcca ctagtcttgg
      301 actcctgttg atagatccag taatgacctc agaactccat ctggatttgt tcagaacgct
      361 cggttgccgc cgggcgtttt ttattggtga gaatccaggg gtccccaata attacgattt
      421 aaattagtag cccgcctaat gagcgggctt ttttttaatt cccctatttg tttatttttc
      481 taaatacatt caaatatgta tccgctcatg agacaataac cctgataaat gcttcaataa
      541 tattgaaaaa ggaagagtat gagcattcag cattttcgtg tggcgctgat tccgtttttt
      601 gcggcgtttt gcctgccggt gtttgcgcat ccggaaaccc tggtgaaagt gaaagatgcg
      661 gaagatcaac tgggtgcgcg cgtgggctat attgaactgg atctgaacag cggcaaaatt
      721 ctggaatctt ttcgtccgga agaacgtttt ccgatgatga gcacctttaa agtgctgctg
      781 tgcggtgcgg ttctgagccg tgtggatgcg ggccaggaac aactgggccg tcgtattcat
      841 tatagccaga acgatctggt ggaatatagc ccggtgaccg aaaaacatct gaccgatggc
      901 atgaccgtgc gtgaactgtg cagcgcggcg attaccatga gcgataacac cgcggcgaac
      961 ctgctgctga cgaccattgg cggtccgaaa gaactgaccg cgtttctgca taacatgggc
     1021 gatcatgtga cccgtctgga tcgttgggaa ccggaactga acgaagcgat tccgaacgat
     1081 gaacgtgata ccaccatgcc ggcagcaatg gcgaccaccc tgcgtaaact gctgacgggt
     1141 gagctgctga ccctggcaag ccgccagcaa ctgattgatt ggatggaagc ggataaagtg
     1201 gcgggtccgc tgctgcgtag cgcgctgccg gctggctggt ttattgcgga taaaagcggt
     1261 gcgggcgaac gtggcagccg tggcattatt gcggcgctgg gcccggatgg taaaccgagc
     1321 cgtattgtgg tgatttatac caccggcagc caggcgacga tggatgaacg taaccgtcag
     1381 attgcggaaa ttggcgcgag cctgattaaa cattggtaaa ccgatacaat taaaggctcc
     1441 ttttggagcc tttttttttg gacgaccctt gtcggctcga cccacgacta ttgactgctc
     1501 tgagaaagtt gattgttacg attagtccgg ccggccccgt agaaaagatc aaaggatctt
     1561 cttgagatcc tttttttctg cgcgtaatct gctgcttgca aacaaaaaaa ccaccgctac
     1621 cagcggtggt ttgtttgccg gatcaagagc taccaactct ttttccgaag gtaactggct
     1681 tcagcagagc gcagatacca aatactgttc ttctagtgta gccgtagtta ggccaccact
     1741 tcaagaactc tgtagcaccg cctacatacc tcgctctgct aatcctgtta ccagtggctg
     1801 ctgccagtgg cgataagtcg tgtcttaccg ggttggactc aagacgatag ttaccggata
     1861 aggcgcagcg gtcgggctga acggggggtt cgtgcacaca gcccagcttg gagcgaacga
     1921 cctacaccga actgagatac ctacagcgtg agctttgaga aagcgccacg cttcccgaag
     1981 ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg aacaggagag cgcacgaggg
     2041 agcttccagg gggaaacgcc tggtatcttt atagtcctgt cgggtttcgc cacctctgac
     2101 ttgagcgtcg atttttgtga tgctcgtcag gggggcggag cctatggaaa aacgccagca
     2161 acgcggcctt tttacggttc ctggcctttt gctggccttt tgctcacatg ttctttcctg
     2221 cgttatcccc tgattctgtg gataaccgta ttaccgcctt tgagtgagct gataccgctc
     2281 gccgcagccg aacgaccgag cgcagcgagt cagtgagcga ggaagcggaa gagcgcccaa
     2341 tacgcaaacc gcctctcccc gcgcgttggc cgattcatta atgcagctgg cacgacaggt
     2401 ttcccgactg gaaagcgggc agtgagcgca acgcaattaa tgtgagttag ctcactcatt
     2461 aggcaggcgc gcccagctgt ctagggcggc ggatttgtcc tactcaggag agcgttcacc
     2521 gacaaacaac agataaaacg aaaggcccag tctttcgact gagcctttcg ttttatttga
     2581 tgcctttaat taa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P53 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P53, contains a T7_100 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P53_Terminator2_T7_100_RiboB",
                },
                {
                    "accessor": "B-P54",
                    "binaryString": """LOCUS       B-P54_Terminator2_T7_52_RiboB 2593 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P54 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P54,
            contains a T7_52 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   527594e1b54b342d84d66f8410b0a65d
VERSION     527594e1b54b342d84d66f8410b0a65d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    158..232
                     /label="RiboB"
     regulatory      135..157
                     /label="T7_52"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    235..289
                     /label="LMS"
     misc_feature    425..1463
                     /label="SEVA_Ap"
     misc_feature    1537..2465
                     /label="SEVA_pUC"
     misc_feature    296..398
                     /label="SEVA_T0"
     misc_feature    2480..2584
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttaatac gactcactgc cgggagaagc gctcaacggg tgtgcttccc
      181 gttctgatga gtccgtgagg acgaaagcgc ctctacaaat aattttgttt aaggctcggg
      241 agacctatcg gtaataacag tccaatctgg tgtaacttcg gaatcgtcca ctagtcttgg
      301 actcctgttg atagatccag taatgacctc agaactccat ctggatttgt tcagaacgct
      361 cggttgccgc cgggcgtttt ttattggtga gaatccaggg gtccccaata attacgattt
      421 aaattagtag cccgcctaat gagcgggctt ttttttaatt cccctatttg tttatttttc
      481 taaatacatt caaatatgta tccgctcatg agacaataac cctgataaat gcttcaataa
      541 tattgaaaaa ggaagagtat gagcattcag cattttcgtg tggcgctgat tccgtttttt
      601 gcggcgtttt gcctgccggt gtttgcgcat ccggaaaccc tggtgaaagt gaaagatgcg
      661 gaagatcaac tgggtgcgcg cgtgggctat attgaactgg atctgaacag cggcaaaatt
      721 ctggaatctt ttcgtccgga agaacgtttt ccgatgatga gcacctttaa agtgctgctg
      781 tgcggtgcgg ttctgagccg tgtggatgcg ggccaggaac aactgggccg tcgtattcat
      841 tatagccaga acgatctggt ggaatatagc ccggtgaccg aaaaacatct gaccgatggc
      901 atgaccgtgc gtgaactgtg cagcgcggcg attaccatga gcgataacac cgcggcgaac
      961 ctgctgctga cgaccattgg cggtccgaaa gaactgaccg cgtttctgca taacatgggc
     1021 gatcatgtga cccgtctgga tcgttgggaa ccggaactga acgaagcgat tccgaacgat
     1081 gaacgtgata ccaccatgcc ggcagcaatg gcgaccaccc tgcgtaaact gctgacgggt
     1141 gagctgctga ccctggcaag ccgccagcaa ctgattgatt ggatggaagc ggataaagtg
     1201 gcgggtccgc tgctgcgtag cgcgctgccg gctggctggt ttattgcgga taaaagcggt
     1261 gcgggcgaac gtggcagccg tggcattatt gcggcgctgg gcccggatgg taaaccgagc
     1321 cgtattgtgg tgatttatac caccggcagc caggcgacga tggatgaacg taaccgtcag
     1381 attgcggaaa ttggcgcgag cctgattaaa cattggtaaa ccgatacaat taaaggctcc
     1441 ttttggagcc tttttttttg gacgaccctt gtcggctcga cccacgacta ttgactgctc
     1501 tgagaaagtt gattgttacg attagtccgg ccggccccgt agaaaagatc aaaggatctt
     1561 cttgagatcc tttttttctg cgcgtaatct gctgcttgca aacaaaaaaa ccaccgctac
     1621 cagcggtggt ttgtttgccg gatcaagagc taccaactct ttttccgaag gtaactggct
     1681 tcagcagagc gcagatacca aatactgttc ttctagtgta gccgtagtta ggccaccact
     1741 tcaagaactc tgtagcaccg cctacatacc tcgctctgct aatcctgtta ccagtggctg
     1801 ctgccagtgg cgataagtcg tgtcttaccg ggttggactc aagacgatag ttaccggata
     1861 aggcgcagcg gtcgggctga acggggggtt cgtgcacaca gcccagcttg gagcgaacga
     1921 cctacaccga actgagatac ctacagcgtg agctttgaga aagcgccacg cttcccgaag
     1981 ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg aacaggagag cgcacgaggg
     2041 agcttccagg gggaaacgcc tggtatcttt atagtcctgt cgggtttcgc cacctctgac
     2101 ttgagcgtcg atttttgtga tgctcgtcag gggggcggag cctatggaaa aacgccagca
     2161 acgcggcctt tttacggttc ctggcctttt gctggccttt tgctcacatg ttctttcctg
     2221 cgttatcccc tgattctgtg gataaccgta ttaccgcctt tgagtgagct gataccgctc
     2281 gccgcagccg aacgaccgag cgcagcgagt cagtgagcga ggaagcggaa gagcgcccaa
     2341 tacgcaaacc gcctctcccc gcgcgttggc cgattcatta atgcagctgg cacgacaggt
     2401 ttcccgactg gaaagcgggc agtgagcgca acgcaattaa tgtgagttag ctcactcatt
     2461 aggcaggcgc gcccagctgt ctagggcggc ggatttgtcc tactcaggag agcgttcacc
     2521 gacaaacaac agataaaacg aaaggcccag tctttcgact gagcctttcg ttttatttga
     2581 tgcctttaat taa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P54 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P54, contains a T7_52 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P54_Terminator2_T7_52_RiboB",
                },
                {
                    "accessor": "B-P55",
                    "binaryString": """LOCUS       B-P55_Terminator2_T7_50_RiboB 2593 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P55 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P55,
            contains a T7_50 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   5ea799cf09f81ca093f6f4da74552e19
VERSION     5ea799cf09f81ca093f6f4da74552e19
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      135..157
                     /label="T7_50"
     misc_feature    158..232
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    235..289
                     /label="LMS"
     misc_feature    425..1463
                     /label="SEVA_Ap"
     misc_feature    1537..2465
                     /label="SEVA_pUC"
     misc_feature    296..398
                     /label="SEVA_T0"
     misc_feature    2480..2584
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttaatac gactcactat ggggagaagc gctcaacggg tgtgcttccc
      181 gttctgatga gtccgtgagg acgaaagcgc ctctacaaat aattttgttt aaggctcggg
      241 agacctatcg gtaataacag tccaatctgg tgtaacttcg gaatcgtcca ctagtcttgg
      301 actcctgttg atagatccag taatgacctc agaactccat ctggatttgt tcagaacgct
      361 cggttgccgc cgggcgtttt ttattggtga gaatccaggg gtccccaata attacgattt
      421 aaattagtag cccgcctaat gagcgggctt ttttttaatt cccctatttg tttatttttc
      481 taaatacatt caaatatgta tccgctcatg agacaataac cctgataaat gcttcaataa
      541 tattgaaaaa ggaagagtat gagcattcag cattttcgtg tggcgctgat tccgtttttt
      601 gcggcgtttt gcctgccggt gtttgcgcat ccggaaaccc tggtgaaagt gaaagatgcg
      661 gaagatcaac tgggtgcgcg cgtgggctat attgaactgg atctgaacag cggcaaaatt
      721 ctggaatctt ttcgtccgga agaacgtttt ccgatgatga gcacctttaa agtgctgctg
      781 tgcggtgcgg ttctgagccg tgtggatgcg ggccaggaac aactgggccg tcgtattcat
      841 tatagccaga acgatctggt ggaatatagc ccggtgaccg aaaaacatct gaccgatggc
      901 atgaccgtgc gtgaactgtg cagcgcggcg attaccatga gcgataacac cgcggcgaac
      961 ctgctgctga cgaccattgg cggtccgaaa gaactgaccg cgtttctgca taacatgggc
     1021 gatcatgtga cccgtctgga tcgttgggaa ccggaactga acgaagcgat tccgaacgat
     1081 gaacgtgata ccaccatgcc ggcagcaatg gcgaccaccc tgcgtaaact gctgacgggt
     1141 gagctgctga ccctggcaag ccgccagcaa ctgattgatt ggatggaagc ggataaagtg
     1201 gcgggtccgc tgctgcgtag cgcgctgccg gctggctggt ttattgcgga taaaagcggt
     1261 gcgggcgaac gtggcagccg tggcattatt gcggcgctgg gcccggatgg taaaccgagc
     1321 cgtattgtgg tgatttatac caccggcagc caggcgacga tggatgaacg taaccgtcag
     1381 attgcggaaa ttggcgcgag cctgattaaa cattggtaaa ccgatacaat taaaggctcc
     1441 ttttggagcc tttttttttg gacgaccctt gtcggctcga cccacgacta ttgactgctc
     1501 tgagaaagtt gattgttacg attagtccgg ccggccccgt agaaaagatc aaaggatctt
     1561 cttgagatcc tttttttctg cgcgtaatct gctgcttgca aacaaaaaaa ccaccgctac
     1621 cagcggtggt ttgtttgccg gatcaagagc taccaactct ttttccgaag gtaactggct
     1681 tcagcagagc gcagatacca aatactgttc ttctagtgta gccgtagtta ggccaccact
     1741 tcaagaactc tgtagcaccg cctacatacc tcgctctgct aatcctgtta ccagtggctg
     1801 ctgccagtgg cgataagtcg tgtcttaccg ggttggactc aagacgatag ttaccggata
     1861 aggcgcagcg gtcgggctga acggggggtt cgtgcacaca gcccagcttg gagcgaacga
     1921 cctacaccga actgagatac ctacagcgtg agctttgaga aagcgccacg cttcccgaag
     1981 ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg aacaggagag cgcacgaggg
     2041 agcttccagg gggaaacgcc tggtatcttt atagtcctgt cgggtttcgc cacctctgac
     2101 ttgagcgtcg atttttgtga tgctcgtcag gggggcggag cctatggaaa aacgccagca
     2161 acgcggcctt tttacggttc ctggcctttt gctggccttt tgctcacatg ttctttcctg
     2221 cgttatcccc tgattctgtg gataaccgta ttaccgcctt tgagtgagct gataccgctc
     2281 gccgcagccg aacgaccgag cgcagcgagt cagtgagcga ggaagcggaa gagcgcccaa
     2341 tacgcaaacc gcctctcccc gcgcgttggc cgattcatta atgcagctgg cacgacaggt
     2401 ttcccgactg gaaagcgggc agtgagcgca acgcaattaa tgtgagttag ctcactcatt
     2461 aggcaggcgc gcccagctgt ctagggcggc ggatttgtcc tactcaggag agcgttcacc
     2521 gacaaacaac agataaaacg aaaggcccag tctttcgact gagcctttcg ttttatttga
     2581 tgcctttaat taa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P55 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P55, contains a T7_50 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P55_Terminator2_T7_50_RiboB",
                },
                {
                    "accessor": "B-P56",
                    "binaryString": """LOCUS       B-P56_Terminator2_T7_25_RiboB 2593 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P56 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P56,
            contains a T7_25 promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   12ed8a1648477c13f738878266007b01
VERSION     12ed8a1648477c13f738878266007b01
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      135..157
                     /label="T7_25"
     misc_feature    158..232
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    235..289
                     /label="LMS"
     misc_feature    425..1463
                     /label="SEVA_Ap"
     misc_feature    1537..2465
                     /label="SEVA_pUC"
     misc_feature    296..398
                     /label="SEVA_T0"
     misc_feature    2480..2584
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atcttaatac gactcactgt cgggggaagc gctcaacggg tgtgcttccc
      181 gttctgatga gtccgtgagg acgaaagcgc ctctacaaat aattttgttt aaggctcggg
      241 agacctatcg gtaataacag tccaatctgg tgtaacttcg gaatcgtcca ctagtcttgg
      301 actcctgttg atagatccag taatgacctc agaactccat ctggatttgt tcagaacgct
      361 cggttgccgc cgggcgtttt ttattggtga gaatccaggg gtccccaata attacgattt
      421 aaattagtag cccgcctaat gagcgggctt ttttttaatt cccctatttg tttatttttc
      481 taaatacatt caaatatgta tccgctcatg agacaataac cctgataaat gcttcaataa
      541 tattgaaaaa ggaagagtat gagcattcag cattttcgtg tggcgctgat tccgtttttt
      601 gcggcgtttt gcctgccggt gtttgcgcat ccggaaaccc tggtgaaagt gaaagatgcg
      661 gaagatcaac tgggtgcgcg cgtgggctat attgaactgg atctgaacag cggcaaaatt
      721 ctggaatctt ttcgtccgga agaacgtttt ccgatgatga gcacctttaa agtgctgctg
      781 tgcggtgcgg ttctgagccg tgtggatgcg ggccaggaac aactgggccg tcgtattcat
      841 tatagccaga acgatctggt ggaatatagc ccggtgaccg aaaaacatct gaccgatggc
      901 atgaccgtgc gtgaactgtg cagcgcggcg attaccatga gcgataacac cgcggcgaac
      961 ctgctgctga cgaccattgg cggtccgaaa gaactgaccg cgtttctgca taacatgggc
     1021 gatcatgtga cccgtctgga tcgttgggaa ccggaactga acgaagcgat tccgaacgat
     1081 gaacgtgata ccaccatgcc ggcagcaatg gcgaccaccc tgcgtaaact gctgacgggt
     1141 gagctgctga ccctggcaag ccgccagcaa ctgattgatt ggatggaagc ggataaagtg
     1201 gcgggtccgc tgctgcgtag cgcgctgccg gctggctggt ttattgcgga taaaagcggt
     1261 gcgggcgaac gtggcagccg tggcattatt gcggcgctgg gcccggatgg taaaccgagc
     1321 cgtattgtgg tgatttatac caccggcagc caggcgacga tggatgaacg taaccgtcag
     1381 attgcggaaa ttggcgcgag cctgattaaa cattggtaaa ccgatacaat taaaggctcc
     1441 ttttggagcc tttttttttg gacgaccctt gtcggctcga cccacgacta ttgactgctc
     1501 tgagaaagtt gattgttacg attagtccgg ccggccccgt agaaaagatc aaaggatctt
     1561 cttgagatcc tttttttctg cgcgtaatct gctgcttgca aacaaaaaaa ccaccgctac
     1621 cagcggtggt ttgtttgccg gatcaagagc taccaactct ttttccgaag gtaactggct
     1681 tcagcagagc gcagatacca aatactgttc ttctagtgta gccgtagtta ggccaccact
     1741 tcaagaactc tgtagcaccg cctacatacc tcgctctgct aatcctgtta ccagtggctg
     1801 ctgccagtgg cgataagtcg tgtcttaccg ggttggactc aagacgatag ttaccggata
     1861 aggcgcagcg gtcgggctga acggggggtt cgtgcacaca gcccagcttg gagcgaacga
     1921 cctacaccga actgagatac ctacagcgtg agctttgaga aagcgccacg cttcccgaag
     1981 ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg aacaggagag cgcacgaggg
     2041 agcttccagg gggaaacgcc tggtatcttt atagtcctgt cgggtttcgc cacctctgac
     2101 ttgagcgtcg atttttgtga tgctcgtcag gggggcggag cctatggaaa aacgccagca
     2161 acgcggcctt tttacggttc ctggcctttt gctggccttt tgctcacatg ttctttcctg
     2221 cgttatcccc tgattctgtg gataaccgta ttaccgcctt tgagtgagct gataccgctc
     2281 gccgcagccg aacgaccgag cgcagcgagt cagtgagcga ggaagcggaa gagcgcccaa
     2341 tacgcaaacc gcctctcccc gcgcgttggc cgattcatta atgcagctgg cacgacaggt
     2401 ttcccgactg gaaagcgggc agtgagcgca acgcaattaa tgtgagttag ctcactcatt
     2461 aggcaggcgc gcccagctgt ctagggcggc ggatttgtcc tactcaggag agcgttcacc
     2521 gacaaacaac agataaaacg aaaggcccag tctttcgact gagcctttcg ttttatttga
     2581 tgcctttaat taa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P56 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P56, contains a T7_25 promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P56_Terminator2_T7_25_RiboB",
                },
                {
                    "accessor": "B-P57",
                    "binaryString": """LOCUS       B-P57_Terminator3_T7_100_RiboC 2587 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P57 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P57,
            contains a T7_100 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   3b4a88794480e918265b485a386e7165
VERSION     3b4a88794480e918265b485a386e7165
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    152..226
                     /label="RiboC"
     regulatory      58..108
                     /label="Terminator3"
     regulatory      129..151
                     /label="T7_100"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    229..283
                     /label="LMS"
     misc_feature    419..1457
                     /label="SEVA_Ap"
     misc_feature    1531..2459
                     /label="SEVA_pUC"
     misc_feature    290..392
                     /label="SEVA_T0"
     misc_feature    2474..2578
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctta atacgactca ctatagggga cagtagtcac cggctgtgct tgccggtctg
      181 atgagcctgt gaaggcgaaa ctacctctac aaataatttt gtttaaggct cgggagacct
      241 atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc ttggactcct
      301 gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa cgctcggttg
      361 ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg atttaaatta
      421 gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt tttctaaata
      481 cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca ataatattga
      541 aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt ttttgcggcg
      601 ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga tgcggaagat
      661 caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa aattctggaa
      721 tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct gctgtgcggt
      781 gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat tcattatagc
      841 cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga tggcatgacc
      901 gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc gaacctgctg
      961 ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat gggcgatcat
     1021 gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa cgatgaacgt
     1081 gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac gggtgagctg
     1141 ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa agtggcgggt
     1201 ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag cggtgcgggc
     1261 gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc gagccgtatt
     1321 gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg tcagattgcg
     1381 gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg ctccttttgg
     1441 agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact gctctgagaa
     1501 agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga tcttcttgag
     1561 atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg ctaccagcgg
     1621 tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact ggcttcagca
     1681 gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac cacttcaaga
     1741 actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg gctgctgcca
     1801 gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg gataaggcgc
     1861 agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga acgacctaca
     1921 ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc gaagggagaa
     1981 aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg agggagcttc
     2041 cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc tgacttgagc
     2101 gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc agcaacgcgg
     2161 cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt cctgcgttat
     2221 cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc gctcgccgca
     2281 gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc ccaatacgca
     2341 aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac aggtttcccg
     2401 actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact cattaggcag
     2461 gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt caccgacaaa
     2521 caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat ttgatgcctt
     2581 taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P57 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P57, contains a T7_100 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P57_Terminator3_T7_100_RiboC",
                },
                {
                    "accessor": "B-P58",
                    "binaryString": """LOCUS       B-P58_Terminator3_T7_52_RiboC 2587 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P58 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P58,
            contains a T7_52 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   0716f7ec6f8963162f7a1f1ba43ec3cd
VERSION     0716f7ec6f8963162f7a1f1ba43ec3cd
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      129..151
                     /label="T7_52"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    152..226
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    229..283
                     /label="LMS"
     misc_feature    419..1457
                     /label="SEVA_Ap"
     misc_feature    1531..2459
                     /label="SEVA_pUC"
     misc_feature    290..392
                     /label="SEVA_T0"
     misc_feature    2474..2578
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctta atacgactca ctgccgggag aagtagtcac cggctgtgct tgccggtctg
      181 atgagcctgt gaaggcgaaa ctacctctac aaataatttt gtttaaggct cgggagacct
      241 atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc ttggactcct
      301 gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa cgctcggttg
      361 ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg atttaaatta
      421 gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt tttctaaata
      481 cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca ataatattga
      541 aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt ttttgcggcg
      601 ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga tgcggaagat
      661 caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa aattctggaa
      721 tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct gctgtgcggt
      781 gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat tcattatagc
      841 cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga tggcatgacc
      901 gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc gaacctgctg
      961 ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat gggcgatcat
     1021 gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa cgatgaacgt
     1081 gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac gggtgagctg
     1141 ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa agtggcgggt
     1201 ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag cggtgcgggc
     1261 gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc gagccgtatt
     1321 gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg tcagattgcg
     1381 gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg ctccttttgg
     1441 agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact gctctgagaa
     1501 agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga tcttcttgag
     1561 atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg ctaccagcgg
     1621 tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact ggcttcagca
     1681 gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac cacttcaaga
     1741 actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg gctgctgcca
     1801 gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg gataaggcgc
     1861 agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga acgacctaca
     1921 ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc gaagggagaa
     1981 aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg agggagcttc
     2041 cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc tgacttgagc
     2101 gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc agcaacgcgg
     2161 cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt cctgcgttat
     2221 cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc gctcgccgca
     2281 gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc ccaatacgca
     2341 aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac aggtttcccg
     2401 actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact cattaggcag
     2461 gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt caccgacaaa
     2521 caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat ttgatgcctt
     2581 taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P58 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P58, contains a T7_52 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P58_Terminator3_T7_52_RiboC",
                },
                {
                    "accessor": "B-P59",
                    "binaryString": """LOCUS       B-P59_Terminator3_T7_50_RiboC 2587 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P59 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P59,
            contains a T7_50 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   f5c5d3a7e16aef9a821b12cb66cf3338
VERSION     f5c5d3a7e16aef9a821b12cb66cf3338
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     misc_feature    152..226
                     /label="RiboC"
     regulatory      58..108
                     /label="Terminator3"
     regulatory      129..151
                     /label="T7_50"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    229..283
                     /label="LMS"
     misc_feature    419..1457
                     /label="SEVA_Ap"
     misc_feature    1531..2459
                     /label="SEVA_pUC"
     misc_feature    290..392
                     /label="SEVA_T0"
     misc_feature    2474..2578
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctta atacgactca ctatggggag aagtagtcac cggctgtgct tgccggtctg
      181 atgagcctgt gaaggcgaaa ctacctctac aaataatttt gtttaaggct cgggagacct
      241 atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc ttggactcct
      301 gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa cgctcggttg
      361 ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg atttaaatta
      421 gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt tttctaaata
      481 cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca ataatattga
      541 aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt ttttgcggcg
      601 ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga tgcggaagat
      661 caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa aattctggaa
      721 tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct gctgtgcggt
      781 gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat tcattatagc
      841 cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga tggcatgacc
      901 gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc gaacctgctg
      961 ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat gggcgatcat
     1021 gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa cgatgaacgt
     1081 gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac gggtgagctg
     1141 ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa agtggcgggt
     1201 ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag cggtgcgggc
     1261 gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc gagccgtatt
     1321 gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg tcagattgcg
     1381 gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg ctccttttgg
     1441 agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact gctctgagaa
     1501 agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga tcttcttgag
     1561 atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg ctaccagcgg
     1621 tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact ggcttcagca
     1681 gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac cacttcaaga
     1741 actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg gctgctgcca
     1801 gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg gataaggcgc
     1861 agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga acgacctaca
     1921 ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc gaagggagaa
     1981 aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg agggagcttc
     2041 cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc tgacttgagc
     2101 gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc agcaacgcgg
     2161 cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt cctgcgttat
     2221 cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc gctcgccgca
     2281 gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc ccaatacgca
     2341 aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac aggtttcccg
     2401 actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact cattaggcag
     2461 gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt caccgacaaa
     2521 caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat ttgatgcctt
     2581 taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P59 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P59, contains a T7_50 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P59_Terminator3_T7_50_RiboC",
                },
                {
                    "accessor": "B-P60",
                    "binaryString": """LOCUS       B-P60_Terminator3_T7_25_RiboC 2587 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P60 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P60,
            contains a T7_25 promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   7d164fce32bd2614755922c67cc39edd
VERSION     7d164fce32bd2614755922c67cc39edd
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      129..151
                     /label="T7_25"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    152..226
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     misc_feature    229..283
                     /label="LMS"
     misc_feature    419..1457
                     /label="SEVA_Ap"
     misc_feature    1531..2459
                     /label="SEVA_pUC"
     misc_feature    290..392
                     /label="SEVA_T0"
     misc_feature    2474..2578
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctta atacgactca ctgtcggggg aagtagtcac cggctgtgct tgccggtctg
      181 atgagcctgt gaaggcgaaa ctacctctac aaataatttt gtttaaggct cgggagacct
      241 atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccactagtc ttggactcct
      301 gttgatagat ccagtaatga cctcagaact ccatctggat ttgttcagaa cgctcggttg
      361 ccgccgggcg ttttttattg gtgagaatcc aggggtcccc aataattacg atttaaatta
      421 gtagcccgcc taatgagcgg gctttttttt aattccccta tttgtttatt tttctaaata
      481 cattcaaata tgtatccgct catgagacaa taaccctgat aaatgcttca ataatattga
      541 aaaaggaaga gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt ttttgcggcg
      601 ttttgcctgc cggtgtttgc gcatccggaa accctggtga aagtgaaaga tgcggaagat
      661 caactgggtg cgcgcgtggg ctatattgaa ctggatctga acagcggcaa aattctggaa
      721 tcttttcgtc cggaagaacg ttttccgatg atgagcacct ttaaagtgct gctgtgcggt
      781 gcggttctga gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat tcattatagc
      841 cagaacgatc tggtggaata tagcccggtg accgaaaaac atctgaccga tggcatgacc
      901 gtgcgtgaac tgtgcagcgc ggcgattacc atgagcgata acaccgcggc gaacctgctg
      961 ctgacgacca ttggcggtcc gaaagaactg accgcgtttc tgcataacat gggcgatcat
     1021 gtgacccgtc tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa cgatgaacgt
     1081 gataccacca tgccggcagc aatggcgacc accctgcgta aactgctgac gggtgagctg
     1141 ctgaccctgg caagccgcca gcaactgatt gattggatgg aagcggataa agtggcgggt
     1201 ccgctgctgc gtagcgcgct gccggctggc tggtttattg cggataaaag cggtgcgggc
     1261 gaacgtggca gccgtggcat tattgcggcg ctgggcccgg atggtaaacc gagccgtatt
     1321 gtggtgattt ataccaccgg cagccaggcg acgatggatg aacgtaaccg tcagattgcg
     1381 gaaattggcg cgagcctgat taaacattgg taaaccgata caattaaagg ctccttttgg
     1441 agcctttttt tttggacgac ccttgtcggc tcgacccacg actattgact gctctgagaa
     1501 agttgattgt tacgattagt ccggccggcc ccgtagaaaa gatcaaagga tcttcttgag
     1561 atcctttttt tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg ctaccagcgg
     1621 tggtttgttt gccggatcaa gagctaccaa ctctttttcc gaaggtaact ggcttcagca
     1681 gagcgcagat accaaatact gttcttctag tgtagccgta gttaggccac cacttcaaga
     1741 actctgtagc accgcctaca tacctcgctc tgctaatcct gttaccagtg gctgctgcca
     1801 gtggcgataa gtcgtgtctt accgggttgg actcaagacg atagttaccg gataaggcgc
     1861 agcggtcggg ctgaacgggg ggttcgtgca cacagcccag cttggagcga acgacctaca
     1921 ccgaactgag atacctacag cgtgagcttt gagaaagcgc cacgcttccc gaagggagaa
     1981 aggcggacag gtatccggta agcggcaggg tcggaacagg agagcgcacg agggagcttc
     2041 cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc tgacttgagc
     2101 gtcgattttt gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc agcaacgcgg
     2161 cctttttacg gttcctggcc ttttgctggc cttttgctca catgttcttt cctgcgttat
     2221 cccctgattc tgtggataac cgtattaccg cctttgagtg agctgatacc gctcgccgca
     2281 gccgaacgac cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc ccaatacgca
     2341 aaccgcctct ccccgcgcgt tggccgattc attaatgcag ctggcacgac aggtttcccg
     2401 actggaaagc gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact cattaggcag
     2461 gcgcgcccag ctgtctaggg cggcggattt gtcctactca ggagagcgtt caccgacaaa
     2521 caacagataa aacgaaaggc ccagtctttc gactgagcct ttcgttttat ttgatgcctt
     2581 taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P60 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P60, contains a T7_25 promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P60_Terminator3_T7_25_RiboC",
                },
                {
                    "accessor": "B-P61",
                    "binaryString": """LOCUS       B-P61_Terminator1_BetI_RiboA 2637 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P61 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P61,
            contains a BetI promoter with an upstream Terminator1 and a
            downstream RiboA.
ACCESSION   d7862cd6c317036242f4ee7e54226f9b
VERSION     d7862cd6c317036242f4ee7e54226f9b
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      139..201
                     /label="BetI"
     misc_feature    119..138
                     /label="SpacerA"
     misc_feature    202..276
                     /label="RiboA"
     regulatory      58..118
                     /label="Terminator1"
     misc_feature    279..333
                     /label="LMS"
     misc_feature    469..1507
                     /label="SEVA_Ap"
     misc_feature    1581..2509
                     /label="SEVA_pUC"
     misc_feature    340..442
                     /label="SEVA_T0"
     misc_feature    2524..2628
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag aggcctcccg aaaggggggc cttttttcgt tttggtccgt
      121 gcctactctg gaaaatctag cgcgggtgag agggattcgt taccaataga caattgattg
      181 gacgttcaat ataatgctag cagctgtcac cggatgtgct ttccggtctg atgagtccgt
      241 gaggacgaaa cagcctctac aaataatttt gtttaaggct cgggagacct atcggtaata
      301 acagtccaat ctggtgtaac ttcggaatcg tccactagtc ttggactcct gttgatagat
      361 ccagtaatga cctcagaact ccatctggat ttgttcagaa cgctcggttg ccgccgggcg
      421 ttttttattg gtgagaatcc aggggtcccc aataattacg atttaaatta gtagcccgcc
      481 taatgagcgg gctttttttt aattccccta tttgtttatt tttctaaata cattcaaata
      541 tgtatccgct catgagacaa taaccctgat aaatgcttca ataatattga aaaaggaaga
      601 gtatgagcat tcagcatttt cgtgtggcgc tgattccgtt ttttgcggcg ttttgcctgc
      661 cggtgtttgc gcatccggaa accctggtga aagtgaaaga tgcggaagat caactgggtg
      721 cgcgcgtggg ctatattgaa ctggatctga acagcggcaa aattctggaa tcttttcgtc
      781 cggaagaacg ttttccgatg atgagcacct ttaaagtgct gctgtgcggt gcggttctga
      841 gccgtgtgga tgcgggccag gaacaactgg gccgtcgtat tcattatagc cagaacgatc
      901 tggtggaata tagcccggtg accgaaaaac atctgaccga tggcatgacc gtgcgtgaac
      961 tgtgcagcgc ggcgattacc atgagcgata acaccgcggc gaacctgctg ctgacgacca
     1021 ttggcggtcc gaaagaactg accgcgtttc tgcataacat gggcgatcat gtgacccgtc
     1081 tggatcgttg ggaaccggaa ctgaacgaag cgattccgaa cgatgaacgt gataccacca
     1141 tgccggcagc aatggcgacc accctgcgta aactgctgac gggtgagctg ctgaccctgg
     1201 caagccgcca gcaactgatt gattggatgg aagcggataa agtggcgggt ccgctgctgc
     1261 gtagcgcgct gccggctggc tggtttattg cggataaaag cggtgcgggc gaacgtggca
     1321 gccgtggcat tattgcggcg ctgggcccgg atggtaaacc gagccgtatt gtggtgattt
     1381 ataccaccgg cagccaggcg acgatggatg aacgtaaccg tcagattgcg gaaattggcg
     1441 cgagcctgat taaacattgg taaaccgata caattaaagg ctccttttgg agcctttttt
     1501 tttggacgac ccttgtcggc tcgacccacg actattgact gctctgagaa agttgattgt
     1561 tacgattagt ccggccggcc ccgtagaaaa gatcaaagga tcttcttgag atcctttttt
     1621 tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg ctaccagcgg tggtttgttt
     1681 gccggatcaa gagctaccaa ctctttttcc gaaggtaact ggcttcagca gagcgcagat
     1741 accaaatact gttcttctag tgtagccgta gttaggccac cacttcaaga actctgtagc
     1801 accgcctaca tacctcgctc tgctaatcct gttaccagtg gctgctgcca gtggcgataa
     1861 gtcgtgtctt accgggttgg actcaagacg atagttaccg gataaggcgc agcggtcggg
     1921 ctgaacgggg ggttcgtgca cacagcccag cttggagcga acgacctaca ccgaactgag
     1981 atacctacag cgtgagcttt gagaaagcgc cacgcttccc gaagggagaa aggcggacag
     2041 gtatccggta agcggcaggg tcggaacagg agagcgcacg agggagcttc cagggggaaa
     2101 cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc tgacttgagc gtcgattttt
     2161 gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc agcaacgcgg cctttttacg
     2221 gttcctggcc ttttgctggc cttttgctca catgttcttt cctgcgttat cccctgattc
     2281 tgtggataac cgtattaccg cctttgagtg agctgatacc gctcgccgca gccgaacgac
     2341 cgagcgcagc gagtcagtga gcgaggaagc ggaagagcgc ccaatacgca aaccgcctct
     2401 ccccgcgcgt tggccgattc attaatgcag ctggcacgac aggtttcccg actggaaagc
     2461 gggcagtgag cgcaacgcaa ttaatgtgag ttagctcact cattaggcag gcgcgcccag
     2521 ctgtctaggg cggcggattt gtcctactca ggagagcgtt caccgacaaa caacagataa
     2581 aacgaaaggc ccagtctttc gactgagcct ttcgttttat ttgatgcctt taattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P61 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P61, contains a BetI promoter with an upstream Terminator1 and a downstream RiboA",
                    "label": "B-P61_Terminator1_BetI_RiboA",
                },
                {
                    "accessor": "B-P62",
                    "binaryString": """LOCUS       B-P62_Terminator2_Ttg_RiboB 2621 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P62 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P62,
            contains a Ttg promoter with an upstream Terminator2 and a
            downstream RiboB.
ACCESSION   ccb7702fea535c6b23e52d4df65b64ce
VERSION     ccb7702fea535c6b23e52d4df65b64ce
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      135..185
                     /label="Ttg"
     misc_feature    186..260
                     /label="RiboB"
     regulatory      58..114
                     /label="Terminator2"
     misc_feature    115..134
                     /label="SpacerA"
     misc_feature    263..317
                     /label="LMS"
     misc_feature    453..1491
                     /label="SEVA_Ap"
     misc_feature    1565..2493
                     /label="SEVA_pUC"
     misc_feature    324..426
                     /label="SEVA_T0"
     misc_feature    2508..2612
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccctc
       61 ggtaccaaat tccagaaaag agacgctttc gagcgtcttt tttcgttttg gtccgtgcct
      121 actctggaaa atctcaccca gcagtattta caaacaacca tgaatgtaag tatattcctt
      181 agcaaagcgc tcaacgggtg tgcttcccgt tctgatgagt ccgtgaggac gaaagcgcct
      241 ctacaaataa ttttgtttaa ggctcgggag acctatcggt aataacagtc caatctggtg
      301 taacttcgga atcgtccact agtcttggac tcctgttgat agatccagta atgacctcag
      361 aactccatct ggatttgttc agaacgctcg gttgccgccg ggcgtttttt attggtgaga
      421 atccaggggt ccccaataat tacgatttaa attagtagcc cgcctaatga gcgggctttt
      481 ttttaattcc cctatttgtt tatttttcta aatacattca aatatgtatc cgctcatgag
      541 acaataaccc tgataaatgc ttcaataata ttgaaaaagg aagagtatga gcattcagca
      601 ttttcgtgtg gcgctgattc cgttttttgc ggcgttttgc ctgccggtgt ttgcgcatcc
      661 ggaaaccctg gtgaaagtga aagatgcgga agatcaactg ggtgcgcgcg tgggctatat
      721 tgaactggat ctgaacagcg gcaaaattct ggaatctttt cgtccggaag aacgttttcc
      781 gatgatgagc acctttaaag tgctgctgtg cggtgcggtt ctgagccgtg tggatgcggg
      841 ccaggaacaa ctgggccgtc gtattcatta tagccagaac gatctggtgg aatatagccc
      901 ggtgaccgaa aaacatctga ccgatggcat gaccgtgcgt gaactgtgca gcgcggcgat
      961 taccatgagc gataacaccg cggcgaacct gctgctgacg accattggcg gtccgaaaga
     1021 actgaccgcg tttctgcata acatgggcga tcatgtgacc cgtctggatc gttgggaacc
     1081 ggaactgaac gaagcgattc cgaacgatga acgtgatacc accatgccgg cagcaatggc
     1141 gaccaccctg cgtaaactgc tgacgggtga gctgctgacc ctggcaagcc gccagcaact
     1201 gattgattgg atggaagcgg ataaagtggc gggtccgctg ctgcgtagcg cgctgccggc
     1261 tggctggttt attgcggata aaagcggtgc gggcgaacgt ggcagccgtg gcattattgc
     1321 ggcgctgggc ccggatggta aaccgagccg tattgtggtg atttatacca ccggcagcca
     1381 ggcgacgatg gatgaacgta accgtcagat tgcggaaatt ggcgcgagcc tgattaaaca
     1441 ttggtaaacc gatacaatta aaggctcctt ttggagcctt tttttttgga cgacccttgt
     1501 cggctcgacc cacgactatt gactgctctg agaaagttga ttgttacgat tagtccggcc
     1561 ggccccgtag aaaagatcaa aggatcttct tgagatcctt tttttctgcg cgtaatctgc
     1621 tgcttgcaaa caaaaaaacc accgctacca gcggtggttt gtttgccgga tcaagagcta
     1681 ccaactcttt ttccgaaggt aactggcttc agcagagcgc agataccaaa tactgttctt
     1741 ctagtgtagc cgtagttagg ccaccacttc aagaactctg tagcaccgcc tacatacctc
     1801 gctctgctaa tcctgttacc agtggctgct gccagtggcg ataagtcgtg tcttaccggg
     1861 ttggactcaa gacgatagtt accggataag gcgcagcggt cgggctgaac ggggggttcg
     1921 tgcacacagc ccagcttgga gcgaacgacc tacaccgaac tgagatacct acagcgtgag
     1981 ctttgagaaa gcgccacgct tcccgaaggg agaaaggcgg acaggtatcc ggtaagcggc
     2041 agggtcggaa caggagagcg cacgagggag cttccagggg gaaacgcctg gtatctttat
     2101 agtcctgtcg ggtttcgcca cctctgactt gagcgtcgat ttttgtgatg ctcgtcaggg
     2161 gggcggagcc tatggaaaaa cgccagcaac gcggcctttt tacggttcct ggccttttgc
     2221 tggccttttg ctcacatgtt ctttcctgcg ttatcccctg attctgtgga taaccgtatt
     2281 accgcctttg agtgagctga taccgctcgc cgcagccgaa cgaccgagcg cagcgagtca
     2341 gtgagcgagg aagcggaaga gcgcccaata cgcaaaccgc ctctccccgc gcgttggccg
     2401 attcattaat gcagctggca cgacaggttt cccgactgga aagcgggcag tgagcgcaac
     2461 gcaattaatg tgagttagct cactcattag gcaggcgcgc ccagctgtct agggcggcgg
     2521 atttgtccta ctcaggagag cgttcaccga caaacaacag ataaaacgaa aggcccagtc
     2581 tttcgactga gcctttcgtt ttatttgatg cctttaatta a
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P62 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P62, contains a Ttg promoter with an upstream Terminator2 and a downstream RiboB",
                    "label": "B-P62_Terminator2_Ttg_RiboB",
                },
                {
                    "accessor": "B-P63",
                    "binaryString": """LOCUS       B-P63_Terminator3_SaITTC_RiboC 2680 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  B-P63 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P63,
            contains a SaITTC promoter with an upstream Terminator3 and a
            downstream RiboC.
ACCESSION   2efe3b0c9d0a41739866e78d82414a55
VERSION     2efe3b0c9d0a41739866e78d82414a55
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct
            other sequences; artificial sequences.
FEATURES             Location/Qualifiers
     misc_feature    3..57
                     /label="LMP"
     regulatory      58..108
                     /label="Terminator3"
     misc_feature    245..319
                     /label="RiboC"
     misc_feature    109..128
                     /label="SpacerA"
     regulatory      129..244
                     /label="SaITTC"
     misc_feature    322..376
                     /label="LMS"
     misc_feature    512..1550
                     /label="SEVA_Ap"
     misc_feature    1624..2552
                     /label="SEVA_pUC"
     misc_feature    383..485
                     /label="SEVA_T0"
     misc_feature    2567..2671
                     /label="SEVA_T1"
ORIGIN
        1 ggctcgggta agaactcgca cttcgtggaa acactattat ctggtgggtc tctgtccgac
       61 gaacaataag gcctccctaa cggggggcct tttttattga taacaaaagt gcctactctg
      121 gaaaatctgg ggcctcgctt gggttattgc tggtgcccgg ccgggcgcaa tattcatgtt
      181 gatgatttat tatatatcga gtggtgtatt tatttatatt gtttgctccg ttaccgttat
      241 taacagtagt caccggctgt gcttgccggt ctgatgagcc tgtgaaggcg aaactacctc
      301 tacaaataat tttgtttaag gctcgggaga cctatcggta ataacagtcc aatctggtgt
      361 aacttcggaa tcgtccacta gtcttggact cctgttgata gatccagtaa tgacctcaga
      421 actccatctg gatttgttca gaacgctcgg ttgccgccgg gcgtttttta ttggtgagaa
      481 tccaggggtc cccaataatt acgatttaaa ttagtagccc gcctaatgag cgggcttttt
      541 tttaattccc ctatttgttt atttttctaa atacattcaa atatgtatcc gctcatgaga
      601 caataaccct gataaatgct tcaataatat tgaaaaagga agagtatgag cattcagcat
      661 tttcgtgtgg cgctgattcc gttttttgcg gcgttttgcc tgccggtgtt tgcgcatccg
      721 gaaaccctgg tgaaagtgaa agatgcggaa gatcaactgg gtgcgcgcgt gggctatatt
      781 gaactggatc tgaacagcgg caaaattctg gaatcttttc gtccggaaga acgttttccg
      841 atgatgagca cctttaaagt gctgctgtgc ggtgcggttc tgagccgtgt ggatgcgggc
      901 caggaacaac tgggccgtcg tattcattat agccagaacg atctggtgga atatagcccg
      961 gtgaccgaaa aacatctgac cgatggcatg accgtgcgtg aactgtgcag cgcggcgatt
     1021 accatgagcg ataacaccgc ggcgaacctg ctgctgacga ccattggcgg tccgaaagaa
     1081 ctgaccgcgt ttctgcataa catgggcgat catgtgaccc gtctggatcg ttgggaaccg
     1141 gaactgaacg aagcgattcc gaacgatgaa cgtgatacca ccatgccggc agcaatggcg
     1201 accaccctgc gtaaactgct gacgggtgag ctgctgaccc tggcaagccg ccagcaactg
     1261 attgattgga tggaagcgga taaagtggcg ggtccgctgc tgcgtagcgc gctgccggct
     1321 ggctggttta ttgcggataa aagcggtgcg ggcgaacgtg gcagccgtgg cattattgcg
     1381 gcgctgggcc cggatggtaa accgagccgt attgtggtga tttataccac cggcagccag
     1441 gcgacgatgg atgaacgtaa ccgtcagatt gcggaaattg gcgcgagcct gattaaacat
     1501 tggtaaaccg atacaattaa aggctccttt tggagccttt ttttttggac gacccttgtc
     1561 ggctcgaccc acgactattg actgctctga gaaagttgat tgttacgatt agtccggccg
     1621 gccccgtaga aaagatcaaa ggatcttctt gagatccttt ttttctgcgc gtaatctgct
     1681 gcttgcaaac aaaaaaacca ccgctaccag cggtggtttg tttgccggat caagagctac
     1741 caactctttt tccgaaggta actggcttca gcagagcgca gataccaaat actgttcttc
     1801 tagtgtagcc gtagttaggc caccacttca agaactctgt agcaccgcct acatacctcg
     1861 ctctgctaat cctgttacca gtggctgctg ccagtggcga taagtcgtgt cttaccgggt
     1921 tggactcaag acgatagtta ccggataagg cgcagcggtc gggctgaacg gggggttcgt
     1981 gcacacagcc cagcttggag cgaacgacct acaccgaact gagataccta cagcgtgagc
     2041 tttgagaaag cgccacgctt cccgaaggga gaaaggcgga caggtatccg gtaagcggca
     2101 gggtcggaac aggagagcgc acgagggagc ttccaggggg aaacgcctgg tatctttata
     2161 gtcctgtcgg gtttcgccac ctctgacttg agcgtcgatt tttgtgatgc tcgtcagggg
     2221 ggcggagcct atggaaaaac gccagcaacg cggccttttt acggttcctg gccttttgct
     2281 ggccttttgc tcacatgttc tttcctgcgt tatcccctga ttctgtggat aaccgtatta
     2341 ccgcctttga gtgagctgat accgctcgcc gcagccgaac gaccgagcgc agcgagtcag
     2401 tgagcgagga agcggaagag cgcccaatac gcaaaccgcc tctccccgcg cgttggccga
     2461 ttcattaatg cagctggcac gacaggtttc ccgactggaa agcgggcagt gagcgcaacg
     2521 caattaatgt gagttagctc actcattagg caggcgcgcc cagctgtcta gggcggcgga
     2581 tttgtcctac tcaggagagc gttcaccgac aaacaacaga taaaacgaaa ggcccagtct
     2641 ttcgactgag cctttcgttt tatttgatgc ctttaattaa
//
""",
                    "collection": "BASIC_PROMOTER_PARTS",
                    "description": "B-P63 stored in BASIC_SEVA_18. The BASIC insulated promoter B-P63, contains a SaITTC promoter with an upstream Terminator3 and a downstream RiboC",
                    "label": "B-P63_Terminator3_SaITTC_RiboC",
                },
            ],
        },
        {
            "name": "BASIC_SEVA_PARTS",
            "v0.1": [
                {
                    "accessor": "12",
                    "binaryString": """LOCUS       BASIC_SEVA_12           4843 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and RK2
            origin of replication..
ACCESSION   5ffe4dd31e090d490d72196e4137cf82
VERSION     5ffe4dd31e090d490d72196e4137cf82
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3798..3832
                     /label="J23119"
     misc_feature    join(4838..4843,1..51)
                     /label="LMP"
     misc_feature    4705..4833
                     /label="B0015"
     misc_feature    3649..3705
                     /label="LMS"
     CDS             3964..4668
                     /label="mScarlett"
     misc_feature    3535..3639
                     /label="SEVA_T1"
     misc_feature    1299..3520
                     /label="SEVA_RK2"
     misc_feature    187..1225
                     /label="SEVA_Ap"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggccgc gatgcaggtg gctgctgaac
     1321 ccccagccgg aactgacccc acaaggccct agcgtttgca atgcaccagg tcatcattga
     1381 cccaggcgtg ttccaccagg ccgctgcctc gcaactcttc gcaggcttcg ccgacctgct
     1441 cgcgccactt cttcacgcgg gtggaatccg atccgcacat gaggcggaag gtttccagct
     1501 tgagcgggta cggctcccgg tgcgagctga aatagtcgaa catccgtcgg gccgtcggcg
     1561 acagcttgcg gtacttctcc catatgaatt tcgtgtagtg gtcgccagca aacagcacga
     1621 cgatttcctc gtcgatcagg acctggcaac gggacgtttt cttgccacgg tccaggacgc
     1681 ggaagcggtg cagcagcgac accgattcca ggtgcccaac gcggtcggac gtgaagccca
     1741 tcgccgtcgc ctgtaggcgc gacaggcatt cctcggcctt cgtgtaatac cggccattga
     1801 tcgaccagcc caggtcctgg caaagctcgt agaacgtgaa ggtgatcggc tcgccgatag
     1861 gggtgcgctt cgcgtactcc aacacctgct gccacaccag ttcgtcatcg tcggcccgca
     1921 gctcgacgcc ggtgtaggtg atcttcacgt ccttgttgac gtggaaaatg accttgtttt
     1981 gcagcgcctc gcgcgggatt ttcttgttgc gcgtggtgaa cagggcagag cgggccgtgt
     2041 cgtttggcat cgctcgcatc gtgtccggcc acggcgcaat atcgaacaag gaaagctgca
     2101 tttccttgat ctgctgcttc gtgtgtttca gcaacgcggc ctgcttggct tcgctgacct
     2161 gttttgccag gtcctcgccg gcggtttttc gcttcttggt cgtcatagtt cctcgcgtgt
     2221 cgatggtcat cgacttcgcc aaacctgccg cctcctgttc gagacgacgc gaacgctcca
     2281 cggcggccga tggcgcgggc agggcagggg gagccagttg cacgctgtcg cgctcgatct
     2341 tggccgtagc ttgctggact atcgagccga cggactggaa ggtttcgcgg ggcgcacgca
     2401 tgacggtgcg gcttgcgatg gtttcggcat cctcggcgga aaaccccgcg tcgatcagtt
     2461 cttgcctgta tgccttccgg tcaaacgtcc gattcattca ccctccttgc gggattgccc
     2521 cggaattaat tccccggatc gatccgtcga tcttgatccc ctgcgccatc agatccttgg
     2581 cggcaagaaa gccatccagt ttactttgca gggcttccca accttaccag agggcgcccc
     2641 agctggcaat tccggttcgc ttgctgtcca taaaaccgcc cagtctagct atcgccatgt
     2701 aagcccactg caagctacct gctttctctt tgcgcttgcg ttttcccttg tccagatagc
     2761 ccagtagctg acattcatcc ggggtcagca ccgtttctgc ggactggctt tctacgtggc
     2821 tgccattttt ggggtgaggc cgttcgcggc cgaggggcgc agcccctggg gggatgggag
     2881 gcccgcgtta gcgggccggg agggttcgag aagggggggc accccccttc ggcgtgcgcg
     2941 gtcacgcgca cagggcgcag ccctggttaa aaacaaggtt tataaatatt ggtttaaaag
     3001 caggttaaaa gacaggttag cggtggccga aaaacgggcg gaaacccttg caaatgctgg
     3061 attttctgcc tgtggacagc ccctcaaatg tcaataggtg cgcccctcat ctgtcagcac
     3121 tctgcccctc aagtgtcaag gatcgcgccc ctcatctgtc agtagtcgcg cccctcaagt
     3181 gtcaataccg cagggcactt atccccaggc ttgtccacat catctgtggg aaactcgcgt
     3241 aaaatcaggc gttttcgccg atttgcgagg ctggccagct ccacgtcgcc ggccgaaatc
     3301 gagcctgccc ctcatctgtc aacgccgcgc cgggtgagtc ggcccctcaa gtgtcaacgt
     3361 ccgcccctca tctgtcagtg agggccaagt tttccgcgag gtatccacaa cgccggcggc
     3421 cctacatggc tctgctgtag tgagtgggtt gcgctccggc agcggtcctg atcccccgca
     3481 gaaaaaaagg atctcaagaa gatcctttga tcttttctac ggcgcgccca gctgtctagg
     3541 gcggcggatt tgtcctactc aggagagcgt tcaccgacaa acaacagata aaacgaaagg
     3601 cccagtcttt cgactgagcc tttcgtttta tttgatgcct ttaattaagg ctcgggagac
     3661 ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccccaat tattgaacac
     3721 ccttcggggt gtttttttgt ttctggtcta ccatctcgtt gtgataatag acctgaagtg
     3781 cctactctgg aaaatctttg acagctagct cagtcctagg tataatgcta gcagctgtca
     3841 ccggatgtgc tttccggtct gatgagtccg tgaggacgaa acagcctcta caaataattt
     3901 tgtttaaggc tcgctacgag aagattgtta ctttcgcagc gttattatct aaggaggtag
     3961 tccatggtta gcaaaggcga ggcggttatc aaggagttta tgcgttttaa ggttcacatg
     4021 gagggtagca tgaatggtca cgagttcgag atcgagggtg aaggcgaggg tcgtccgtac
     4081 gaaggcaccc agaccgcgaa gctgaaagtg accaagggtg gcccgctgcc gttcagctgg
     4141 gacatcctga gcccgcagtt catgtatggc agccgtgcgt ttaccaaaca cccggcggac
     4201 attccggatt actataagca aagcttcccg gaaggtttta aatgggagcg tgttatgaac
     4261 ttcgaagatg gtggcgcggt gaccgttacc caggacacca gcctggagga tggcaccctg
     4321 atttacaagg tgaaactgcg tggcaccaac tttccgccgg atggtccggt tatgcagaag
     4381 aaaacgatgg gttgggaagc gagcaccgag cgtctgtatc cggaagatgg cgtgctgaag
     4441 ggtgatatca aaatggcgct gcgtctgaag gacggtggcc gttacctggc ggattttaag
     4501 accacctata aagcgaagaa accggtgcaa atgccgggtg cgtacaacgt tgaccgtaaa
     4561 ctggatatta ccagccacaa cgaggattat accgtggttg agcaatatga gcgtagcgag
     4621 ggtcgccaca gcaccggcgg catggacgaa ctgtataagg gatcctaata acgctgatag
     4681 tgctagtgta gatcgctact agagccaggc atcaaataaa acgaaaggct cagtcgaaag
     4741 actgggcctt tcgttttatc tgttgtttgt cggtgaacgc tctctactag agtcacactg
     4801 gctcaccttc gggtgggcct ttctgcgttt atatactggc tcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and RK2 origin of replication.",
                    "label": "BASIC_SEVA_12",
                },
                {
                    "accessor": "13",
                    "binaryString": """LOCUS       BASIC_SEVA_13           4143 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and pBBR1
            origin of replication..
ACCESSION   b0cc681c00c117b6c86cdfbcb050b272
VERSION     b0cc681c00c117b6c86cdfbcb050b272
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     CDS             3264..3968
                     /label="mScarlett"
     misc_feature    4005..4133
                     /label="B0015"
     misc_feature    1299..2820
                     /label="SEVA_pBBR1"
     misc_feature    2949..3005
                     /label="LMS"
     misc_feature    2835..2939
                     /label="SEVA_T1"
     misc_feature    join(4138..4143,1..51)
                     /label="LMP"
     misc_feature    3098..3132
                     /label="J23119"
     misc_feature    187..1225
                     /label="SEVA_Ap"
     misc_feature    58..160
                     /label="SEVA_T0"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggccct accggcgcgg cagcgttacc
     1321 cgtgtcggcg gctccaacgg ctcgccatcg tccagaaaac acggctcatc gggcatcggc
     1381 aggcgctgct gcccgcgccg ttcccattcc tccgtttcgg tcaaggctgg caggtctggt
     1441 tccatgcccg gaatgccggg ctggctgggc ggctcctcgc cggggccggt cggtagttgc
     1501 tgctcgcccg gatacagggt cgggatgcgg cgcaggtcgc catgccccaa cagcgattcg
     1561 tcctggtcgt cgtgatcaac caccacggcg gcactgaaca ccgacaggcg caactggtcg
     1621 cggggctggc cccacgccac gcggtcattg accacgtagg ccgacacggt gccggggccg
     1681 ttgagcttca cgacggagat ccagcgctcg gccaccaagt ccttgactgc gtattggacc
     1741 gtccgcaaag aacgtccgat gagcttggaa agtgtcttct ggctgaccac cacggcgttc
     1801 tggtggccca tctgcgccac gaggtgatgc agcagcattg ccgccgtggg tttcctcgca
     1861 ataagcccgg cccacgcctc atgcgctttg cgttccgttt gcacccagtg accgggcttg
     1921 ttcttggctt gaatgccgat ttctctggac tgcgtggcca tgcttatctc catgcggtag
     1981 gggtgccgca cggttgcggc accatgcgca atcagctgca acttttcggc agcgcgacaa
     2041 caattatgcg ttgcgtaaaa gtggcagtca attacagatt ttctttaacc tacgcaatga
     2101 gctattgcgg ggggtgccgc aatgagctgt tgcgtacccc ccttttttaa gttgttgatt
     2161 tttaagtctt tcgcatttcg ccctatatct agttctttgg tgcccaaaga agggcacccc
     2221 tgcggggttc ccccacgcct tcggcgcggc tccccctccg gcaaaaagtg gcccctccgg
     2281 ggcttgttga tcgactgcgc ggccttcggc cttgcccaag gtggcgctgc ccccttggaa
     2341 cccccgcact cgccgccgtg aggctcgggg ggcaggcggg cgggcttcgc ccttcgactg
     2401 cccccactcg cataggcttg ggtcgttcca ggcgcgtcaa ggccaagccg ctgcgcggtc
     2461 gctgcgcgag ccttgacccg ccttccactt ggtgtccaac cggcaagcga agcgcgcagg
     2521 ccgcaggccg gaggcttttc cccagagaaa attaaaaaaa ttgatggggc aaggccgcag
     2581 gccgcgcagt tggagccggt gggtatgtgg tcgaaggctg ggtagccggt gggcaatccc
     2641 tgtggtcaag ctcgtgggca ggcgcagcct gtccatcagc ttgtccagca gggttgtcca
     2701 cgggccgagc gaagcgagcc agccggtggc cgctcgcggc catcgtccac atatccacgg
     2761 gctggcaagg gagcgcagcg accgcgcagg gcgaagcccg gagagcaagc ccgtaggggg
     2821 ggcgcgccca gctgtctagg gcggcggatt tgtcctactc aggagagcgt tcaccgacaa
     2881 acaacagata aaacgaaagg cccagtcttt cgactgagcc tttcgtttta tttgatgcct
     2941 ttaattaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
     3001 cgtccccaat tattgaacac ccttcggggt gtttttttgt ttctggtcta ccatctcgtt
     3061 gtgataatag acctgaagtg cctactctgg aaaatctttg acagctagct cagtcctagg
     3121 tataatgcta gcagctgtca ccggatgtgc tttccggtct gatgagtccg tgaggacgaa
     3181 acagcctcta caaataattt tgtttaaggc tcgctacgag aagattgtta ctttcgcagc
     3241 gttattatct aaggaggtag tccatggtta gcaaaggcga ggcggttatc aaggagttta
     3301 tgcgttttaa ggttcacatg gagggtagca tgaatggtca cgagttcgag atcgagggtg
     3361 aaggcgaggg tcgtccgtac gaaggcaccc agaccgcgaa gctgaaagtg accaagggtg
     3421 gcccgctgcc gttcagctgg gacatcctga gcccgcagtt catgtatggc agccgtgcgt
     3481 ttaccaaaca cccggcggac attccggatt actataagca aagcttcccg gaaggtttta
     3541 aatgggagcg tgttatgaac ttcgaagatg gtggcgcggt gaccgttacc caggacacca
     3601 gcctggagga tggcaccctg atttacaagg tgaaactgcg tggcaccaac tttccgccgg
     3661 atggtccggt tatgcagaag aaaacgatgg gttgggaagc gagcaccgag cgtctgtatc
     3721 cggaagatgg cgtgctgaag ggtgatatca aaatggcgct gcgtctgaag gacggtggcc
     3781 gttacctggc ggattttaag accacctata aagcgaagaa accggtgcaa atgccgggtg
     3841 cgtacaacgt tgaccgtaaa ctggatatta ccagccacaa cgaggattat accgtggttg
     3901 agcaatatga gcgtagcgag ggtcgccaca gcaccggcgg catggacgaa ctgtataagg
     3961 gatcctaata acgctgatag tgctagtgta gatcgctact agagccaggc atcaaataaa
     4021 acgaaaggct cagtcgaaag actgggcctt tcgttttatc tgttgtttgt cggtgaacgc
     4081 tctctactag agtcacactg gctcaccttc gggtgggcct ttctgcgttt atatactggc
     4141 tcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and pBBR1 origin of replication.",
                    "label": "BASIC_SEVA_13",
                },
                {
                    "accessor": "14",
                    "binaryString": """LOCUS       BASIC_SEVA_14           4394 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and
            pRO1600/ColE1 origin of replication..
ACCESSION   059542022621a0912a9ffdddc40ee292
VERSION     059542022621a0912a9ffdddc40ee292
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3282..3386
                     /label="SEVA_T1"
     misc_feature    3453..3487
                     /label="J23105"
     misc_feature    join(4389..4394,1..51)
                     /label="LMP"
     CDS             3515..4219
                     /label="mScarlett"
     misc_feature    3396..3452
                     /label="LMS"
     misc_feature    187..1225
                     /label="SEVA_Ap"
     misc_feature    1299..3267
                     /label="SEVA_pRO1600/ColE1"
     misc_feature    3496..3507
                     /label="B0034"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    4256..4384
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggccga taatctcatg accaaaatcc
     1321 cttaacgtga gttttcgttc cactgagcgt cagaccccgt agaaaagatc aaaggatctt
     1381 cttgagatcc tttttttctg cgcgtaatct gctgcttgca aacaaaaaaa ccaccgctac
     1441 cagcggtggt ttgtttgccg gatcaagagc taccaactct ttttccgaag gtaactggct
     1501 tcagcagagc gcagatacca aatactgttc ttctagtgta gccgtagtta ggccaccact
     1561 tcaagaactc tgtagcaccg cctacatacc tcgctctgct aatcctgtta ccagtggctg
     1621 ctgccagtgg cgataagtcg tgtcttaccg ggttggactc aagacgatag ttaccggata
     1681 aggcgcagcg gtcgggctga acggggggtt cgtgcacaca gcccagcttg gagcgaacga
     1741 cctacaccga actgagatac ctacagcgtg agctatgaga aagcgccacg cttcccgaag
     1801 ggagaaaggc ggacaggcat ccggtaagcg gcagggtcgg aacaggagag cgcacgaggg
     1861 agcttccagg gggaaacgcc tggtatcttt atagtcctgt cgggtttcgc cacctctgac
     1921 ttgagcgtcg atttttgtga tgctcgtcag gggggcggag cctatggaaa aacgccagca
     1981 acgcggccgt gaaaggcagg ccggtccgtg gtggccacgg cctctaggcc agatccagcg
     2041 gcatctgggt tagtcgagcg cgggccgctt cccatgtctc accagggcga gcctgtttcg
     2101 cgatctcagc atctgaaatc ttcccggcct tgcgcttcgc tggggcctta cccaccgcct
     2161 tggcgggctt cttcggtcca aaactgaaca acagatgtgt gaccttgcgc ccggtctttc
     2221 gctgcgccca ctccacctgt agcgggctgt gctcgttgat ctgcgtcacg gctggatcaa
     2281 gcactcgcaa cttgaagtcc ttgatcgagg gataccggcc ttccagttga aaccactttc
     2341 gcagctggtc aatttctatt tcgcgctggc cgatgctgtc ccattgcatg agcagctcgt
     2401 aaagcctgat cgcgtgggtg ctgtccatct tggccacgtc agccaaggcg tatttggtga
     2461 actgtttggt gagttccgtc aggtacggca gcatgtcttt ggtgaacctg agttctacac
     2521 ggccctcacc ctcccggtag atgattgttt gcacccagcc ggtaatcatc acactcggtc
     2581 ttttcccctt gccattgggc tcttgggtta accggacttc ccgccgtttc aggcgcaggg
     2641 ccgcttcttt gagctggttg taggaagatt cgatagggac acccgccatc gtcgctatgt
     2701 cctccgccgt cactgaatac atcacttcat cggtgacagg ctcgctcctc ttcacctggc
     2761 taatacaggc cagaacgatc cgctgttcct gaacactgag gcgatacgcg gcctcgacca
     2821 gggcattgct tttgtaaacc attgggggtg aggccacgtt cgacattcct tgtgtataag
     2881 gggacactgt atctgcgtcc cacaatacaa caaatccgtc cctttacaac aacaaatccg
     2941 tcccttctta acaacaaatc cgtcccttaa tggcaacaaa tccgtccctt tttaaactct
     3001 acaggccacg gattacgtgg cctgtagacg tcctaaaagg tttaaaaggg aaaaggaaga
     3061 aaagggtgga aacgcaaaaa acgcaccact acgtggcccc gttggggccg catttgtgcc
     3121 cctgaagggg cgggggaggc gtctgggcaa tccccgtttt accagtcccc tatcgccgcc
     3181 tgagagggcg caggaagcga gtaatcaggg tatcgaggcg gattcaccct tggcgtccaa
     3241 ccagcggcac cagcggcgcc tgagaggggc gcgcccagct gtctagggcg gcggatttgt
     3301 cctactcagg agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga
     3361 ctgagccttt cgttttattt gatgccttta attaaggctc gggagaccta tcggtaataa
     3421 cagtccaatc tggtgtaact tcggaatcgt cctttacggc tagctcagtc ctaggtacta
     3481 tgctagctac tagtgaaaga ggagaaatac tagtatggtt agcaaaggcg aggcggttat
     3541 caaggagttt atgcgtttta aggttcacat ggagggtagc atgaatggtc acgagttcga
     3601 gatcgagggt gaaggcgagg gtcgtccgta cgaaggcacc cagaccgcga agctgaaagt
     3661 gaccaagggt ggcccgctgc cgttcagctg ggacatcctg agcccgcagt tcatgtatgg
     3721 cagccgtgcg tttaccaaac acccggcgga cattccggat tactataagc aaagcttccc
     3781 ggaaggtttt aaatgggagc gtgttatgaa cttcgaagat ggtggcgcgg tgaccgttac
     3841 ccaggacacc agcctggagg atggcaccct gatttacaag gtgaaactgc gtggcaccaa
     3901 ctttccgccg gatggtccgg ttatgcagaa gaaaacgatg ggttgggaag cgagcaccga
     3961 gcgtctgtat ccggaagatg gcgtgctgaa gggtgatatc aaaatggcgc tgcgtctgaa
     4021 ggacggtggc cgttacctgg cggattttaa gaccacctat aaagcgaaga aaccggtgca
     4081 aatgccgggt gcgtacaacg ttgaccgtaa actggatatt accagccaca acgaggatta
     4141 taccgtggtt gagcaatatg agcgtagcga gggtcgccac agcaccggcg gcatggacga
     4201 actgtataag ggatcctaat aacgctgata gtgctagtgt agatcgctac tagagccagg
     4261 catcaaataa aacgaaaggc tcagtcgaaa gactgggcct ttcgttttat ctgttgtttg
     4321 tcggtgaacg ctctctacta gagtcacact ggctcacctt cgggtgggcc tttctgcgtt
     4381 tatatactgg ctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and pRO1600/ColE1 origin of replication.",
                    "label": "BASIC_SEVA_14",
                },
                {
                    "accessor": "15",
                    "binaryString": """LOCUS       BASIC_SEVA_15           6099 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and
            RSF1010 origin of replication..
ACCESSION   51f82553488c3a17aacdc55d78b363a8
VERSION     51f82553488c3a17aacdc55d78b363a8
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    5961..6089
                     /label="B0015"
     misc_feature    187..1225
                     /label="SEVA_Ap"
     misc_feature    5201..5212
                     /label="B0034"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    4987..5091
                     /label="SEVA_T1"
     misc_feature    5158..5192
                     /label="J23119"
     misc_feature    5101..5157
                     /label="LMS"
     CDS             5220..5924
                     /label="mScarlett"
     misc_feature    join(6094..6099,1..51)
                     /label="LMP"
     misc_feature    1299..4972
                     /label="SEVA_RSF101"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggcctc agcctgccgc cttgggccgg
     1321 gtgatgtcgt acttgcccgc cgcgaactcg gttaccgtcc agcccagcgc gaccagctcc
     1381 ggcaacgcct cgcgcacccg ctggcggcgc ttgcgcatgg tcgaaccact ggcctctgac
     1441 ggccagacat agccgcacaa ggtatctatg gaagccttgc cggttttgcc ggggtcgatc
     1501 cagccacaca gccgctggtg cagcaggcgg gcggtttcgc tgtccagcgc ccgcacctcg
     1561 tccatgctga tgcgcacatg ctggccgcca cccatgacgg cctgcgcgat caaggggttc
     1621 agggccacgt acaggcgccc gtccgcctcg tcgctggcgt actccgacag cagccgaaac
     1681 ccctgccgct tgcggccatt ctgggcgatg atggatacct tccaaaggcg ctcgatgcag
     1741 tcctgtatgt gcttgagcgc cccaccacta tcgacctctg ccccgatttc ctttgccagc
     1801 gcccgatagc tacctttgac cacatggcat tcagcggtga cggcctccca cttgggttcc
     1861 aggaacagcc ggagctgccg tccgccttcg gtcttgggtt ccgggccaag cactaggcca
     1921 ttaggcccag ccatggccac cagcccttgc aggatgcgca gatcatcagc gcccagcggc
     1981 tccgggccgc tgaactcgat ccgcttgccg tcgccgtagt catacgtcac gtccagcttg
     2041 ctgcgcttgc gctcgccccg cttgagggca cggaacaggc cgggggccag acagtgcgcc
     2101 gggtcgtgcc ggacgtggct gaggctgtgc ttgttcttag gcttcaccac ggggcacccc
     2161 cttgctcttg cgctgcctct ccagcacggc gggcttgagc accccgccgt catgccgcct
     2221 gaaccaccga tcagcgaacg gtgcgccata gttggccttg ctcacaccga agcggacgaa
     2281 gaaccggcgc tggtcgtcgt ccacacccca ttcctcggcc tcggcgctgg tcatgctcga
     2341 caggtaggac tgccagcgga tgttatcgac cagtaccgag ctgccccggc tggcctgctg
     2401 ctggtcgcct gcgcccatca tggccgcgcc cttgctggca tggtgcagga acacgataga
     2461 gcacccggta tcggcggcga tggcctccat gcgaccgatg acctgggcca tggggccgct
     2521 ggcgttttct tcctcgatgt ggaaccggcg cagcgtgtcc agcaccatca ggcggcggcc
     2581 ctcggcggcg cgcttgaggc cgtcgaacca ctccggggcc atgatgttgg gcaggctgcc
     2641 gatcagcggc tggatcagca ggccgtcagc cacggcttgc cgttcctcgg cgctgaggtg
     2701 cgccccaagg gcgtgcaggc ggtgatgaat ggcggtgggc gggtcttcgg cgggcaggta
     2761 gatcaccggg ccggtgggca gttcgcccac ctccagcaga tccggcccgc ctgcaatctg
     2821 tgcggccagt tgcagggcca gcatggattt accggcacca ccgggcgaca ccagcgcccc
     2881 gaccgtaccg gccaccatgt tgggcaaaac gtagtccagc ggtggcggcg ctgctgcgaa
     2941 cgcctccaga atattgatag gcttatgggt agccattgat tgcctccttt gcaggcagtt
     3001 ggtggttagg cgctggcggg gtcactaccc ccgccctgcg ccgctctgag ttcttccagg
     3061 cactcgcgca gcgcctcgta ttcgtcgtcg gtcagccaga acttgcgctg acgcatccct
     3121 ttggccttca tgcgctcggc atatcgcgct tggcgtacag cgtcagggct ggccagcagg
     3181 tcgccggtct gcttgtcctt ttggtctttc atatcagtca ccgagaaact tgccggggcc
     3241 gaaaggcttg tcttcgcgga acaaggacaa ggtgcagccg tcaaggttaa ggctggccat
     3301 atcagcgact gaaaagcggc cagcctcggc cttgtttgac gtataaccaa agccaccggg
     3361 caaccaatag cccttgtcac ttttgatcag gtagaccgac cctgaagcgc ttttttcgta
     3421 ttccataaaa cccccttctg tgcgtgagta ctcatagtat aacaggcgtg agtaccaacg
     3481 caagcactac atgctgaaat ctggcccgcc cctgtccatg cctcgctggc ggggtgccgg
     3541 tgcccgtgcc agctcggccc gcgcaagctg gacgctgggc agacccatga ccttgctgac
     3601 ggtgcgctcg atgtaatccg cttcgtggcc gggcttgcgc tctgccagcg ctgggctggc
     3661 ctcggccatg gccttgccga tttcctcggc actgcggccc cggctggcca gcttctgcgc
     3721 ggcgataaag tcgcacttgc tgaggtcatc accgaagcgc ttgaccagcc cggccatctc
     3781 gctgcggtac tcgtccagcg ccgtgcgccg gtggcggcta agctgccgct cgggcagttc
     3841 gaggctggcc agcctgcggg ccttctcctg ctgccgctgg gcctgctcga tctgctggcc
     3901 agcctgctgc accagcgccg ggccagcggt ggcggtcttg cccttggatt cacgcagcag
     3961 cacccacggc tgataaccgg cgcgggtggt gtgcttgtcc ttgcggttgg tgaagcccgc
     4021 caagcggcca tagtggcggc tgtcggcgct ggccgggtcg gcgtcgtact cgctggccag
     4081 cgtccgggca atctgccccc gaagttcacc gcctgcggcg tcggccacct tgacccatgc
     4141 ctgatagttc ttcgggctgg tttccactac cagggcaggc tcccggccct cggctttcat
     4201 gtcatccagg tcaaactcgc tgaggtcgtc caccagcacc agaccatgcc gctcctgctc
     4261 ggcgggcctg atatacacgt cattgccctg ggcattcatc cgcttgagcc atggcgtgtt
     4321 ctggagcact tcggcggctg accattcccg gttcatcatc tggccggtgg tggcgtccct
     4381 gacgccgata tcgaagcgct cacagcccat ggccttgagc tgtcggccta tggcctgcaa
     4441 agtcctgtcg ttcttcatcg ggccaccaag cgattcccac acattatacg agccggaagc
     4501 ataaagtgta aagcctagat ccgaaggatg agccgggctg aatgatcgac cgagacaggc
     4561 cctgcggggc tgcacacgcg cccccaccct tcgggtaggg ggaaaggccg ctaaagcggc
     4621 taaaagcgct ccagcgtatt tctgcggggt ttggtgtggg gtttagcggg ctttgcccgc
     4681 ctttccccct gccgcgcagc ggtggggcgg tgtgtagcct agcgcagcga atagaccagc
     4741 tatccggcct ctggccgggc atattgggca agggcagcag cgccccacaa gggcgctgat
     4801 aaccgcgcct agtggattat tcttagataa tcatggatgg atttttccaa caccccgcca
     4861 gcccccgccc ctgctgggtt tgcaggtttg ggggcgtgac agttattgca ggggttcgtg
     4921 acagttattg caggggggcg tgacagttat tgcaggggtt cgtgacagtt agggcgcgcc
     4981 cagctgtcta gggcggcgga tttgtcctac tcaggagagc gttcaccgac aaacaacaga
     5041 taaaacgaaa ggcccagtct ttcgactgag cctttcgttt tatttgatgc ctttaattaa
     5101 ggctcgggag acctatcggt aataacagtc caatctggtg taacttcgga atcgtccttg
     5161 acagctagct cagtcctagg tataatgcta gctactagtg aaagaggaga aatactagta
     5221 tggttagcaa aggcgaggcg gttatcaagg agtttatgcg ttttaaggtt cacatggagg
     5281 gtagcatgaa tggtcacgag ttcgagatcg agggtgaagg cgagggtcgt ccgtacgaag
     5341 gcacccagac cgcgaagctg aaagtgacca agggtggccc gctgccgttc agctgggaca
     5401 tcctgagccc gcagttcatg tatggcagcc gtgcgtttac caaacacccg gcggacattc
     5461 cggattacta taagcaaagc ttcccggaag gttttaaatg ggagcgtgtt atgaacttcg
     5521 aagatggtgg cgcggtgacc gttacccagg acaccagcct ggaggatggc accctgattt
     5581 acaaggtgaa actgcgtggc accaactttc cgccggatgg tccggttatg cagaagaaaa
     5641 cgatgggttg ggaagcgagc accgagcgtc tgtatccgga agatggcgtg ctgaagggtg
     5701 atatcaaaat ggcgctgcgt ctgaaggacg gtggccgtta cctggcggat tttaagacca
     5761 cctataaagc gaagaaaccg gtgcaaatgc cgggtgcgta caacgttgac cgtaaactgg
     5821 atattaccag ccacaacgag gattataccg tggttgagca atatgagcgt agcgagggtc
     5881 gccacagcac cggcggcatg gacgaactgt ataagggatc ctaataacgc tgatagtgct
     5941 agtgtagatc gctactagag ccaggcatca aataaaacga aaggctcagt cgaaagactg
     6001 ggcctttcgt tttatctgtt gtttgtcggt gaacgctctc tactagagtc acactggctc
     6061 accttcgggt gggcctttct gcgtttatat actggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and RSF1010 origin of replication.",
                    "label": "BASIC_SEVA_15",
                },
                {
                    "accessor": "16",
                    "binaryString": """LOCUS       BASIC_SEVA_16           3157 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and p15A
            origin of replication..
ACCESSION   f77fb6c59e6995d572ef33db00b9d7b0
VERSION     f77fb6c59e6995d572ef33db00b9d7b0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2159..2215
                     /label="LMS"
     misc_feature    2216..2250
                     /label="J23119"
     misc_feature    2045..2149
                     /label="SEVA_T1"
     misc_feature    2259..2270
                     /label="B0034"
     CDS             2278..2982
                     /label="mScarlett"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    join(3152..3157,1..51)
                     /label="LMP"
     misc_feature    187..1225
                     /label="SEVA_Ap"
     misc_feature    1299..2030
                     /label="SEVA_p15A"
     misc_feature    3019..3147
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggccct agaaatattt tatctgatta
     1321 ataagatgat cttcttgaga tcgttttggt ctgcgcgtaa tctcttgctc tgaaaacgaa
     1381 aaaaccgcct tgcagggcgg tttttcgaag gttctctgag ctaccaactc tttgaaccga
     1441 ggtaactggc ttggaggagc gcagtcacca aaacttgtcc tttcagttta gccttaaccg
     1501 gcgcatgact tcaagactaa ctcctctaaa tcaattacca gtggctgctg ccagtggtgc
     1561 ttttgcatgt ctttccgggt tggactcaag acgatagtta ccggataagg cgcagcggtc
     1621 ggactgaacg gggggttcgt gcatacagtc cagcttggag cgaactgcct acccggaact
     1681 gagtgtcagg cgtggaatga gacaaacgcg gccataacag cggaatgaca ccggtaaacc
     1741 gaaaggcagg aacaggagag cgcacgaggg agccgccagg gggaaacgcc tggtatcttt
     1801 atagtcctgt cgggtttcgc caccactgat ttgagcgtca gatttcgtga tgcttgtcag
     1861 gggggcggag cctatggaaa aacggctttg ccgcggccct ctcacttccc tgttaagtat
     1921 cttcctggca tcttccagga aatctccgcc ccgttcgtaa gccatttccg ctcgccgcag
     1981 tcgaacgacc gagcgtagcg agtcagtgag cgaggaagcg gaatatatcc ggcgcgccca
     2041 gctgtctagg gcggcggatt tgtcctactc aggagagcgt tcaccgacaa acaacagata
     2101 aaacgaaagg cccagtcttt cgactgagcc tttcgtttta tttgatgcct ttaattaagg
     2161 ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat cgtccttgac
     2221 agctagctca gtcctaggta taatgctagc tactagtgaa agaggagaaa tactagtatg
     2281 gttagcaaag gcgaggcggt tatcaaggag tttatgcgtt ttaaggttca catggagggt
     2341 agcatgaatg gtcacgagtt cgagatcgag ggtgaaggcg agggtcgtcc gtacgaaggc
     2401 acccagaccg cgaagctgaa agtgaccaag ggtggcccgc tgccgttcag ctgggacatc
     2461 ctgagcccgc agttcatgta tggcagccgt gcgtttacca aacacccggc ggacattccg
     2521 gattactata agcaaagctt cccggaaggt tttaaatggg agcgtgttat gaacttcgaa
     2581 gatggtggcg cggtgaccgt tacccaggac accagcctgg aggatggcac cctgatttac
     2641 aaggtgaaac tgcgtggcac caactttccg ccggatggtc cggttatgca gaagaaaacg
     2701 atgggttggg aagcgagcac cgagcgtctg tatccggaag atggcgtgct gaagggtgat
     2761 atcaaaatgg cgctgcgtct gaaggacggt ggccgttacc tggcggattt taagaccacc
     2821 tataaagcga agaaaccggt gcaaatgccg ggtgcgtaca acgttgaccg taaactggat
     2881 attaccagcc acaacgagga ttataccgtg gttgagcaat atgagcgtag cgagggtcgc
     2941 cacagcaccg gcggcatgga cgaactgtat aagggatcct aataacgctg atagtgctag
     3001 tgtagatcgc tactagagcc aggcatcaaa taaaacgaaa ggctcagtcg aaagactggg
     3061 cctttcgttt tatctgttgt ttgtcggtga acgctctcta ctagagtcac actggctcac
     3121 cttcgggtgg gcctttctgc gtttatatac tggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and p15A origin of replication.",
                    "label": "BASIC_SEVA_16",
                },
                {
                    "accessor": "17",
                    "binaryString": """LOCUS       BASIC_SEVA_17           4081 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and pSC101
            origin of replication..
ACCESSION   7a602b3ce4e26f30182ccbf045bff782
VERSION     7a602b3ce4e26f30182ccbf045bff782
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3943..4071
                     /label="B0015"
     misc_feature    187..1225
                     /label="SEVA_Ap"
     misc_feature    1299..2758
                     /label="SEVA_pSC101"
     misc_feature    2773..2877
                     /label="SEVA_T1"
     misc_feature    join(4076..4081,1..51)
                     /label="LMP"
     misc_feature    3036..3070
                     /label="J23119"
     misc_feature    2887..2943
                     /label="LMS"
     CDS             3202..3906
                     /label="mScarlett"
     misc_feature    58..160
                     /label="SEVA_T0"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggcctc agatccttcc gtatttagcc
     1321 agtatgttct ctagtgtggt tcgttgtttt tgcgtgagcc atgagaacga accattgaga
     1381 tcatacttac tttgcatgtc actcaaaaat tttgcctcaa aactggtgag ctgaattttt
     1441 gcagttaaag catcgtgtag tgtttttctt agtccgttat gtaggtagga atctgatgta
     1501 atggttgttg gtattttgtc accattcatt tttatctggt tgttctcaag ttcggttacg
     1561 agatccattt gtctatctag ttcaacttgg aaaatcaacg tatcagtcgg gcggcctcgc
     1621 ttatcaacca ccaatttcat attgctgtaa gtgtttaaat ctttacttat tggtttcaaa
     1681 acccattggt taagcctttt aaactcatgg tagttatttt caagcattaa catgaactta
     1741 aattcatcaa ggctaatctc tatatttgcc ttgtgagttt tcttttgtgt tagttctttt
     1801 aataaccact cataaatcct catagagtat ttgttttcaa aagacttaac atgttccaga
     1861 ttatatttta tgaatttttt taactggaaa agataaggca atatctcttc actaaaaact
     1921 aattctaatt tttcgcttga gaacttggca tagtttgtcc actggaaaat ctcaaagcct
     1981 ttaaccaaag gattcctgat ttccacagtt ctcgtcatca gctctctggt tgctttagct
     2041 aatacaccat aagcattttc cctactgatg ttcatcatct gagcgtattg gttataagtg
     2101 aacgataccg tccgttcttt ccttgtaggg ttttcaatcg tggggttgag tagtgccaca
     2161 cagcataaaa ttagcttggt ttcatgctcc gttaagtcat agcgactaat cgctagttca
     2221 tttgctttga aaacaactaa ttcagacata catctcaatt ggtctaggtg attttaatca
     2281 ctataccaat tgagatgggc tagtcaatga taattacatg tccttttcct ttgagttgtg
     2341 ggtatctgta aattctgcta gacctttgct ggaaaacttg taaattctgc tagaccctct
     2401 gtaaattccg ctagaccttt gtgtgttttt tttgtttata ttcaagtggt tataatttat
     2461 agaataaaga aagaataaaa aaagataaaa agaatagatc ccagccctgt gtataactca
     2521 ctactttagt cagttccgca gtattacaaa aggatgtcgc aaacgctgtt tgctcctcta
     2581 caaaacagac cttaaaaccc taaaggctta agtagcaccc tcgcaagctc gggcaaatcg
     2641 ctgaatattc cttttgtctc cgaccatcag gcacctgagt cgctgtcttt ttcgtgacat
     2701 tcagttcgct gcgctcacgg ctctggcagt gaatgggggt aaatggcact acaggcgcgg
     2761 cgcgcccagc tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac
     2821 aacagataaa acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt
     2881 aattaaggct cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg
     2941 tccccaatta ttgaacaccc ttcggggtgt ttttttgttt ctggtctacc atctcgttgt
     3001 gataatagac ctgaagtgcc tactctggaa aatctttgac agctagctca gtcctaggta
     3061 taatgctagc agctgtcacc ggatgtgctt tccggtctga tgagtccgtg aggacgaaac
     3121 agcctctaca aataattttg tttaaggctc gctacgagaa gattgttact ttcgcagcgt
     3181 tattatctaa ggaggtagtc catggttagc aaaggcgagg cggttatcaa ggagtttatg
     3241 cgttttaagg ttcacatgga gggtagcatg aatggtcacg agttcgagat cgagggtgaa
     3301 ggcgagggtc gtccgtacga aggcacccag accgcgaagc tgaaagtgac caagggtggc
     3361 ccgctgccgt tcagctggga catcctgagc ccgcagttca tgtatggcag ccgtgcgttt
     3421 accaaacacc cggcggacat tccggattac tataagcaaa gcttcccgga aggttttaaa
     3481 tgggagcgtg ttatgaactt cgaagatggt ggcgcggtga ccgttaccca ggacaccagc
     3541 ctggaggatg gcaccctgat ttacaaggtg aaactgcgtg gcaccaactt tccgccggat
     3601 ggtccggtta tgcagaagaa aacgatgggt tgggaagcga gcaccgagcg tctgtatccg
     3661 gaagatggcg tgctgaaggg tgatatcaaa atggcgctgc gtctgaagga cggtggccgt
     3721 tacctggcgg attttaagac cacctataaa gcgaagaaac cggtgcaaat gccgggtgcg
     3781 tacaacgttg accgtaaact ggatattacc agccacaacg aggattatac cgtggttgag
     3841 caatatgagc gtagcgaggg tcgccacagc accggcggca tggacgaact gtataaggga
     3901 tcctaataac gctgatagtg ctagtgtaga tcgctactag agccaggcat caaataaaac
     3961 gaaaggctca gtcgaaagac tgggcctttc gttttatctg ttgtttgtcg gtgaacgctc
     4021 tctactagag tcacactggc tcaccttcgg gtgggccttt ctgcgtttat atactggctc
     4081 g
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and pSC101 origin of replication.",
                    "label": "BASIC_SEVA_17",
                },
                {
                    "accessor": "18",
                    "binaryString": """LOCUS       BASIC_SEVA_18           3354 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and pUC
            origin of replication..
ACCESSION   bb90c9b9713d85ff695493fde3f0051a
VERSION     bb90c9b9713d85ff695493fde3f0051a
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     CDS             2475..3179
                     /label="mScarlett"
     misc_feature    187..1225
                     /label="SEVA_Ap"
     misc_feature    1299..2227
                     /label="SEVA_pUC"
     misc_feature    2456..2467
                     /label="B0034"
     misc_feature    2413..2447
                     /label="J23106"
     misc_feature    2356..2412
                     /label="LMS"
     misc_feature    join(3349..3354,1..51)
                     /label="LMP"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3216..3344
                     /label="B0015"
     misc_feature    2242..2346
                     /label="SEVA_T1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga tcaaaggatc
     1321 ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa aaccaccgct
     1381 accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga aggtaactgg
     1441 cttcagcaga gcgcagatac caaatactgt tcttctagtg tagccgtagt taggccacca
     1501 cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt taccagtggc
     1561 tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat agttaccgga
     1621 taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct tggagcgaac
     1681 gacctacacc gaactgagat acctacagcg tgagctttga gaaagcgcca cgcttcccga
     1741 agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag agcgcacgag
     1801 ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc gccacctctg
     1861 acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga aaaacgccag
     1921 caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca tgttctttcc
     1981 tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag ctgataccgc
     2041 tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg aagagcgccc
     2101 aatacgcaaa ccgcctctcc ccgcgcgttg gccgattcat taatgcagct ggcacgacag
     2161 gtttcccgac tggaaagcgg gcagtgagcg caacgcaatt aatgtgagtt agctcactca
     2221 ttaggcaggc gcgcccagct gtctagggcg gcggatttgt cctactcagg agagcgttca
     2281 ccgacaaaca acagataaaa cgaaaggccc agtctttcga ctgagccttt cgttttattt
     2341 gatgccttta attaaggctc gggagaccta tcggtaataa cagtccaatc tggtgtaact
     2401 tcggaatcgt cctttacggc tagctcagtc ctaggtatag tgctagctac tagtgaaaga
     2461 ggagaaatac tagtatggtt agcaaaggcg aggcggttat caaggagttt atgcgtttta
     2521 aggttcacat ggagggtagc atgaatggtc acgagttcga gatcgagggt gaaggcgagg
     2581 gtcgtccgta cgaaggcacc cagaccgcga agctgaaagt gaccaagggt ggcccgctgc
     2641 cgttcagctg ggacatcctg agcccgcagt tcatgtatgg cagccgtgcg tttaccaaac
     2701 acccggcgga cattccggat tactataagc aaagcttccc ggaaggtttt aaatgggagc
     2761 gtgttatgaa cttcgaagat ggtggcgcgg tgaccgttac ccaggacacc agcctggagg
     2821 atggcaccct gatttacaag gtgaaactgc gtggcaccaa ctttccgccg gatggtccgg
     2881 ttatgcagaa gaaaacgatg ggttgggaag cgagcaccga gcgtctgtat ccggaagatg
     2941 gcgtgctgaa gggtgatatc aaaatggcgc tgcgtctgaa ggacggtggc cgttacctgg
     3001 cggattttaa gaccacctat aaagcgaaga aaccggtgca aatgccgggt gcgtacaacg
     3061 ttgaccgtaa actggatatt accagccaca acgaggatta taccgtggtt gagcaatatg
     3121 agcgtagcga gggtcgccac agcaccggcg gcatggacga actgtataag ggatcctaat
     3181 aacgctgata gtgctagtgt agatcgctac tagagccagg catcaaataa aacgaaaggc
     3241 tcagtcgaaa gactgggcct ttcgttttat ctgttgtttg tcggtgaacg ctctctacta
     3301 gagtcacact ggctcacctt cgggtgggcc tttctgcgtt tatatactgg ctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and pUC origin of replication.",
                    "label": "BASIC_SEVA_18",
                },
                {
                    "accessor": "19",
                    "binaryString": """LOCUS       BASIC_SEVA_19           3810 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Ampicillin resistance marker and
            pBR322-ROP origin of replication..
ACCESSION   12485441757bf3c0997b28b53938fa44
VERSION     12485441757bf3c0997b28b53938fa44
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3672..3800
                     /label="B0015"
     misc_feature    join(3805..3810,1..51)
                     /label="LMP"
     misc_feature    2812..2868
                     /label="LMS"
     CDS             2931..3635
                     /label="mScarlett"
     misc_feature    187..1225
                     /label="SEVA_Ap"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2912..2923
                     /label="B0034"
     misc_feature    2698..2802
                     /label="SEVA_T1"
     misc_feature    2869..2903
                     /label="J23119"
     misc_feature    1299..2683
                     /label="SEVA_pBR322-ROP"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattagt agcccgccta atgagcgggc ttttttttaa ttcccctatt tgtttatttt
      241 tctaaataca ttcaaatatg tatccgctca tgagacaata accctgataa atgcttcaat
      301 aatattgaaa aaggaagagt atgagcattc agcattttcg tgtggcgctg attccgtttt
      361 ttgcggcgtt ttgcctgccg gtgtttgcgc atccggaaac cctggtgaaa gtgaaagatg
      421 cggaagatca actgggtgcg cgcgtgggct atattgaact ggatctgaac agcggcaaaa
      481 ttctggaatc ttttcgtccg gaagaacgtt ttccgatgat gagcaccttt aaagtgctgc
      541 tgtgcggtgc ggttctgagc cgtgtggatg cgggccagga acaactgggc cgtcgtattc
      601 attatagcca gaacgatctg gtggaatata gcccggtgac cgaaaaacat ctgaccgatg
      661 gcatgaccgt gcgtgaactg tgcagcgcgg cgattaccat gagcgataac accgcggcga
      721 acctgctgct gacgaccatt ggcggtccga aagaactgac cgcgtttctg cataacatgg
      781 gcgatcatgt gacccgtctg gatcgttggg aaccggaact gaacgaagcg attccgaacg
      841 atgaacgtga taccaccatg ccggcagcaa tggcgaccac cctgcgtaaa ctgctgacgg
      901 gtgagctgct gaccctggca agccgccagc aactgattga ttggatggaa gcggataaag
      961 tggcgggtcc gctgctgcgt agcgcgctgc cggctggctg gtttattgcg gataaaagcg
     1021 gtgcgggcga acgtggcagc cgtggcatta ttgcggcgct gggcccggat ggtaaaccga
     1081 gccgtattgt ggtgatttat accaccggca gccaggcgac gatggatgaa cgtaaccgtc
     1141 agattgcgga aattggcgcg agcctgatta aacattggta aaccgataca attaaaggct
     1201 ccttttggag cctttttttt tggacgaccc ttgtcggctc gacccacgac tattgactgc
     1261 tctgagaaag ttgattgtta cgattagtcc ggccggcccc gtagaaaaga tcaaaggatc
     1321 ttcttgagat cctttttttc tgcgcgtaat ctgctgcttg caaacaaaaa aaccaccgct
     1381 accagcggtg gtttgtttgc cggatcaaga gctaccaact ctttttccga aggtaactgg
     1441 cttcagcaga gcgcagatac caaatactgt ccttctagtg tagccgtagt taggccacca
     1501 cttcaagaac tctgtagcac cgcctacata cctcgctctg ctaatcctgt taccagtggc
     1561 tgctgccagt ggcgataagt cgtgtcttac cgggttggac tcaagacgat agttaccgga
     1621 taaggcgcag cggtcgggct gaacgggggg ttcgtgcaca cagcccagct tggagcgaac
     1681 gacctacacc gaactgagat acctacagcg tgagctatga gaaagcgcca cgcttcccga
     1741 agggagaaag gcggacaggt atccggtaag cggcagggtc ggaacaggag agcgcacgag
     1801 ggagcttcca gggggaaacg cctggtatct ttatagtcct gtcgggtttc gccacctctg
     1861 acttgagcgt cgatttttgt gatgctcgtc aggggggcgg agcctatgga aaaacgccag
     1921 caacgcggcc tttttacggt tcctggcctt ttgctggcct tttgctcaca tgttctttcc
     1981 tgcgttatcc cctgattctg tggataaccg tattaccgcc tttgagtgag ctgataccgc
     2041 tcgccgcagc cgaacgaccg agcgcagcga gtcagtgagc gaggaagcgg aagagcgcct
     2101 gatgcggtat tttctcctta cgcatctgtg cggtatttca caccgcatat ggtgcactct
     2161 cagtacaatc tgctctgatg ccgcatagtt aagccagtat acactccgct atcgctacgt
     2221 gactgggtca tggctgcgcc ccgacacccg ccaacacccg ctgacgcgcc ctgacgggct
     2281 tgtctgctcc cggcatccgc ttacagacaa gctgtgaccg tctccgggag ctgcatgtgt
     2341 cagaggtttt caccgtcatc accgaaacgc gcgaggcagc tgcggtaaag ctcatcagcg
     2401 tggtcgtgca gcgattcaca gatgtctgcc tgttcatccg cgtccagctc gttgagtttc
     2461 tccagaagcg ttaatgtctg gcttctgata aagcgggcca tgttaagggc ggttttttcc
     2521 tgtttggtca ctgatgcctc cgtgtaaggg ggatttctgt tcatgggggt aatgataccg
     2581 atgaaacgag agaggatgct cacgatacgg gttactgatg atgaacatgc ccggttactg
     2641 gaacgttgtg agggtaaaca actggcggta tggatgcggc gggggcgcgc ccagctgtct
     2701 agggcggcgg atttgtccta ctcaggagag cgttcaccga caaacaacag ataaaacgaa
     2761 aggcccagtc tttcgactga gcctttcgtt ttatttgatg cctttaatta aggctcggga
     2821 gacctatcgg taataacagt ccaatctggt gtaacttcgg aatcgtcctt gacagctagc
     2881 tcagtcctag gtataatgct agctactagt gaaagaggag aaatactagt atggttagca
     2941 aaggcgaggc ggttatcaag gagtttatgc gttttaaggt tcacatggag ggtagcatga
     3001 atggtcacga gttcgagatc gagggtgaag gcgagggtcg tccgtacgaa ggcacccaga
     3061 ccgcgaagct gaaagtgacc aagggtggcc cgctgccgtt cagctgggac atcctgagcc
     3121 cgcagttcat gtatggcagc cgtgcgttta ccaaacaccc ggcggacatt ccggattact
     3181 ataagcaaag cttcccggaa ggttttaaat gggagcgtgt tatgaacttc gaagatggtg
     3241 gcgcggtgac cgttacccag gacaccagcc tggaggatgg caccctgatt tacaaggtga
     3301 aactgcgtgg caccaacttt ccgccggatg gtccggttat gcagaagaaa acgatgggtt
     3361 gggaagcgag caccgagcgt ctgtatccgg aagatggcgt gctgaagggt gatatcaaaa
     3421 tggcgctgcg tctgaaggac ggtggccgtt acctggcgga ttttaagacc acctataaag
     3481 cgaagaaacc ggtgcaaatg ccgggtgcgt acaacgttga ccgtaaactg gatattacca
     3541 gccacaacga ggattatacc gtggttgagc aatatgagcg tagcgagggt cgccacagca
     3601 ccggcggcat ggacgaactg tataagggat cctaataacg ctgatagtgc tagtgtagat
     3661 cgctactaga gccaggcatc aaataaaacg aaaggctcag tcgaaagact gggcctttcg
     3721 ttttatctgt tgtttgtcgg tgaacgctct ctactagagt cacactggct caccttcggg
     3781 tgggcctttc tgcgtttata tactggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Ampicillin resistance marker and pBR322-ROP origin of replication.",
                    "label": "BASIC_SEVA_19",
                },
                {
                    "accessor": "22",
                    "binaryString": """LOCUS       BASIC_SEVA_22           4731 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and RK2
            origin of replication..
ACCESSION   d916716736db2b7b6c4ce0a621fc6e9f
VERSION     d916716736db2b7b6c4ce0a621fc6e9f
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    join(4726..4731,1..51)
                     /label="LMP"
     misc_feature    3537..3593
                     /label="LMS"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3686..3720
                     /label="J23119"
     misc_feature    3423..3527
                     /label="SEVA_T1"
     CDS             3852..4556
                     /label="mScarlett"
     misc_feature    1187..3408
                     /label="SEVA_RK2"
     misc_feature    4593..4721
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccgcga tgcaggtggc
     1201 tgctgaaccc ccagccggaa ctgaccccac aaggccctag cgtttgcaat gcaccaggtc
     1261 atcattgacc caggcgtgtt ccaccaggcc gctgcctcgc aactcttcgc aggcttcgcc
     1321 gacctgctcg cgccacttct tcacgcgggt ggaatccgat ccgcacatga ggcggaaggt
     1381 ttccagcttg agcgggtacg gctcccggtg cgagctgaaa tagtcgaaca tccgtcgggc
     1441 cgtcggcgac agcttgcggt acttctccca tatgaatttc gtgtagtggt cgccagcaaa
     1501 cagcacgacg atttcctcgt cgatcaggac ctggcaacgg gacgttttct tgccacggtc
     1561 caggacgcgg aagcggtgca gcagcgacac cgattccagg tgcccaacgc ggtcggacgt
     1621 gaagcccatc gccgtcgcct gtaggcgcga caggcattcc tcggccttcg tgtaataccg
     1681 gccattgatc gaccagccca ggtcctggca aagctcgtag aacgtgaagg tgatcggctc
     1741 gccgataggg gtgcgcttcg cgtactccaa cacctgctgc cacaccagtt cgtcatcgtc
     1801 ggcccgcagc tcgacgccgg tgtaggtgat cttcacgtcc ttgttgacgt ggaaaatgac
     1861 cttgttttgc agcgcctcgc gcgggatttt cttgttgcgc gtggtgaaca gggcagagcg
     1921 ggccgtgtcg tttggcatcg ctcgcatcgt gtccggccac ggcgcaatat cgaacaagga
     1981 aagctgcatt tccttgatct gctgcttcgt gtgtttcagc aacgcggcct gcttggcttc
     2041 gctgacctgt tttgccaggt cctcgccggc ggtttttcgc ttcttggtcg tcatagttcc
     2101 tcgcgtgtcg atggtcatcg acttcgccaa acctgccgcc tcctgttcga gacgacgcga
     2161 acgctccacg gcggccgatg gcgcgggcag ggcaggggga gccagttgca cgctgtcgcg
     2221 ctcgatcttg gccgtagctt gctggactat cgagccgacg gactggaagg tttcgcgggg
     2281 cgcacgcatg acggtgcggc ttgcgatggt ttcggcatcc tcggcggaaa accccgcgtc
     2341 gatcagttct tgcctgtatg ccttccggtc aaacgtccga ttcattcacc ctccttgcgg
     2401 gattgccccg gaattaattc cccggatcga tccgtcgatc ttgatcccct gcgccatcag
     2461 atccttggcg gcaagaaagc catccagttt actttgcagg gcttcccaac cttaccagag
     2521 ggcgccccag ctggcaattc cggttcgctt gctgtccata aaaccgccca gtctagctat
     2581 cgccatgtaa gcccactgca agctacctgc tttctctttg cgcttgcgtt ttcccttgtc
     2641 cagatagccc agtagctgac attcatccgg ggtcagcacc gtttctgcgg actggctttc
     2701 tacgtggctg ccatttttgg ggtgaggccg ttcgcggccg aggggcgcag cccctggggg
     2761 gatgggaggc ccgcgttagc gggccgggag ggttcgagaa gggggggcac cccccttcgg
     2821 cgtgcgcggt cacgcgcaca gggcgcagcc ctggttaaaa acaaggttta taaatattgg
     2881 tttaaaagca ggttaaaaga caggttagcg gtggccgaaa aacgggcgga aacccttgca
     2941 aatgctggat tttctgcctg tggacagccc ctcaaatgtc aataggtgcg cccctcatct
     3001 gtcagcactc tgcccctcaa gtgtcaagga tcgcgcccct catctgtcag tagtcgcgcc
     3061 cctcaagtgt caataccgca gggcacttat ccccaggctt gtccacatca tctgtgggaa
     3121 actcgcgtaa aatcaggcgt tttcgccgat ttgcgaggct ggccagctcc acgtcgccgg
     3181 ccgaaatcga gcctgcccct catctgtcaa cgccgcgccg ggtgagtcgg cccctcaagt
     3241 gtcaacgtcc gcccctcatc tgtcagtgag ggccaagttt tccgcgaggt atccacaacg
     3301 ccggcggccc tacatggctc tgctgtagtg agtgggttgc gctccggcag cggtcctgat
     3361 cccccgcaga aaaaaaggat ctcaagaaga tcctttgatc ttttctacgg cgcgcccagc
     3421 tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac aacagataaa
     3481 acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt aattaaggct
     3541 cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccccaatta
     3601 ttgaacaccc ttcggggtgt ttttttgttt ctggtctacc atctcgttgt gataatagac
     3661 ctgaagtgcc tactctggaa aatctttgac agctagctca gtcctaggta taatgctagc
     3721 agctgtcacc ggatgtgctt tccggtctga tgagtccgtg aggacgaaac agcctctaca
     3781 aataattttg tttaaggctc gctacgagaa gattgttact ttcgcagcgt tattatctaa
     3841 ggaggtagtc catggttagc aaaggcgagg cggttatcaa ggagtttatg cgttttaagg
     3901 ttcacatgga gggtagcatg aatggtcacg agttcgagat cgagggtgaa ggcgagggtc
     3961 gtccgtacga aggcacccag accgcgaagc tgaaagtgac caagggtggc ccgctgccgt
     4021 tcagctggga catcctgagc ccgcagttca tgtatggcag ccgtgcgttt accaaacacc
     4081 cggcggacat tccggattac tataagcaaa gcttcccgga aggttttaaa tgggagcgtg
     4141 ttatgaactt cgaagatggt ggcgcggtga ccgttaccca ggacaccagc ctggaggatg
     4201 gcaccctgat ttacaaggtg aaactgcgtg gcaccaactt tccgccggat ggtccggtta
     4261 tgcagaagaa aacgatgggt tgggaagcga gcaccgagcg tctgtatccg gaagatggcg
     4321 tgctgaaggg tgatatcaaa atggcgctgc gtctgaagga cggtggccgt tacctggcgg
     4381 attttaagac cacctataaa gcgaagaaac cggtgcaaat gccgggtgcg tacaacgttg
     4441 accgtaaact ggatattacc agccacaacg aggattatac cgtggttgag caatatgagc
     4501 gtagcgaggg tcgccacagc accggcggca tggacgaact gtataaggga tcctaataac
     4561 gctgatagtg ctagtgtaga tcgctactag agccaggcat caaataaaac gaaaggctca
     4621 gtcgaaagac tgggcctttc gttttatctg ttgtttgtcg gtgaacgctc tctactagag
     4681 tcacactggc tcaccttcgg gtgggccttt ctgcgtttat atactggctc g
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and RK2 origin of replication.",
                    "label": "BASIC_SEVA_22",
                },
                {
                    "accessor": "23",
                    "binaryString": """LOCUS       BASIC_SEVA_23           4031 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and pBBR1
            origin of replication..
ACCESSION   a883822f7f88a4f12c8e8e93cbc34cc3
VERSION     a883822f7f88a4f12c8e8e93cbc34cc3
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2723..2827
                     /label="SEVA_T1"
     misc_feature    join(4026..4031,1..51)
                     /label="LMP"
     misc_feature    2837..2893
                     /label="LMS"
     CDS             3152..3856
                     /label="mScarlett"
     misc_feature    1187..2708
                     /label="SEVA_pBBR1"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    2986..3020
                     /label="J23119"
     misc_feature    3893..4021
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccctac cggcgcggca
     1201 gcgttacccg tgtcggcggc tccaacggct cgccatcgtc cagaaaacac ggctcatcgg
     1261 gcatcggcag gcgctgctgc ccgcgccgtt cccattcctc cgtttcggtc aaggctggca
     1321 ggtctggttc catgcccgga atgccgggct ggctgggcgg ctcctcgccg gggccggtcg
     1381 gtagttgctg ctcgcccgga tacagggtcg ggatgcggcg caggtcgcca tgccccaaca
     1441 gcgattcgtc ctggtcgtcg tgatcaacca ccacggcggc actgaacacc gacaggcgca
     1501 actggtcgcg gggctggccc cacgccacgc ggtcattgac cacgtaggcc gacacggtgc
     1561 cggggccgtt gagcttcacg acggagatcc agcgctcggc caccaagtcc ttgactgcgt
     1621 attggaccgt ccgcaaagaa cgtccgatga gcttggaaag tgtcttctgg ctgaccacca
     1681 cggcgttctg gtggcccatc tgcgccacga ggtgatgcag cagcattgcc gccgtgggtt
     1741 tcctcgcaat aagcccggcc cacgcctcat gcgctttgcg ttccgtttgc acccagtgac
     1801 cgggcttgtt cttggcttga atgccgattt ctctggactg cgtggccatg cttatctcca
     1861 tgcggtaggg gtgccgcacg gttgcggcac catgcgcaat cagctgcaac ttttcggcag
     1921 cgcgacaaca attatgcgtt gcgtaaaagt ggcagtcaat tacagatttt ctttaaccta
     1981 cgcaatgagc tattgcgggg ggtgccgcaa tgagctgttg cgtacccccc ttttttaagt
     2041 tgttgatttt taagtctttc gcatttcgcc ctatatctag ttctttggtg cccaaagaag
     2101 ggcacccctg cggggttccc ccacgccttc ggcgcggctc cccctccggc aaaaagtggc
     2161 ccctccgggg cttgttgatc gactgcgcgg ccttcggcct tgcccaaggt ggcgctgccc
     2221 ccttggaacc cccgcactcg ccgccgtgag gctcgggggg caggcgggcg ggcttcgccc
     2281 ttcgactgcc cccactcgca taggcttggg tcgttccagg cgcgtcaagg ccaagccgct
     2341 gcgcggtcgc tgcgcgagcc ttgacccgcc ttccacttgg tgtccaaccg gcaagcgaag
     2401 cgcgcaggcc gcaggccgga ggcttttccc cagagaaaat taaaaaaatt gatggggcaa
     2461 ggccgcaggc cgcgcagttg gagccggtgg gtatgtggtc gaaggctggg tagccggtgg
     2521 gcaatccctg tggtcaagct cgtgggcagg cgcagcctgt ccatcagctt gtccagcagg
     2581 gttgtccacg ggccgagcga agcgagccag ccggtggccg ctcgcggcca tcgtccacat
     2641 atccacgggc tggcaaggga gcgcagcgac cgcgcagggc gaagcccgga gagcaagccc
     2701 gtaggggggg cgcgcccagc tgtctagggc ggcggatttg tcctactcag gagagcgttc
     2761 accgacaaac aacagataaa acgaaaggcc cagtctttcg actgagcctt tcgttttatt
     2821 tgatgccttt aattaaggct cgggagacct atcggtaata acagtccaat ctggtgtaac
     2881 ttcggaatcg tccccaatta ttgaacaccc ttcggggtgt ttttttgttt ctggtctacc
     2941 atctcgttgt gataatagac ctgaagtgcc tactctggaa aatctttgac agctagctca
     3001 gtcctaggta taatgctagc agctgtcacc ggatgtgctt tccggtctga tgagtccgtg
     3061 aggacgaaac agcctctaca aataattttg tttaaggctc gctacgagaa gattgttact
     3121 ttcgcagcgt tattatctaa ggaggtagtc catggttagc aaaggcgagg cggttatcaa
     3181 ggagtttatg cgttttaagg ttcacatgga gggtagcatg aatggtcacg agttcgagat
     3241 cgagggtgaa ggcgagggtc gtccgtacga aggcacccag accgcgaagc tgaaagtgac
     3301 caagggtggc ccgctgccgt tcagctggga catcctgagc ccgcagttca tgtatggcag
     3361 ccgtgcgttt accaaacacc cggcggacat tccggattac tataagcaaa gcttcccgga
     3421 aggttttaaa tgggagcgtg ttatgaactt cgaagatggt ggcgcggtga ccgttaccca
     3481 ggacaccagc ctggaggatg gcaccctgat ttacaaggtg aaactgcgtg gcaccaactt
     3541 tccgccggat ggtccggtta tgcagaagaa aacgatgggt tgggaagcga gcaccgagcg
     3601 tctgtatccg gaagatggcg tgctgaaggg tgatatcaaa atggcgctgc gtctgaagga
     3661 cggtggccgt tacctggcgg attttaagac cacctataaa gcgaagaaac cggtgcaaat
     3721 gccgggtgcg tacaacgttg accgtaaact ggatattacc agccacaacg aggattatac
     3781 cgtggttgag caatatgagc gtagcgaggg tcgccacagc accggcggca tggacgaact
     3841 gtataaggga tcctaataac gctgatagtg ctagtgtaga tcgctactag agccaggcat
     3901 caaataaaac gaaaggctca gtcgaaagac tgggcctttc gttttatctg ttgtttgtcg
     3961 gtgaacgctc tctactagag tcacactggc tcaccttcgg gtgggccttt ctgcgtttat
     4021 atactggctc g
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and pBBR1 origin of replication.",
                    "label": "BASIC_SEVA_23",
                },
                {
                    "accessor": "24",
                    "binaryString": """LOCUS       BASIC_SEVA_24           4282 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and
            pRO1600/ColE1 origin of replication..
ACCESSION   9414713dcef3fac873f41a7d881db797
VERSION     9414713dcef3fac873f41a7d881db797
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3170..3274
                     /label="SEVA_T1"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    join(4277..4282,1..51)
                     /label="LMP"
     misc_feature    3284..3340
                     /label="LMS"
     misc_feature    3341..3375
                     /label="J23105"
     misc_feature    3384..3395
                     /label="B0034"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    4144..4272
                     /label="B0015"
     misc_feature    1187..3155
                     /label="SEVA_pRO1600/ColE1"
     CDS             3403..4107
                     /label="mScarlett"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccgata atctcatgac
     1201 caaaatccct taacgtgagt tttcgttcca ctgagcgtca gaccccgtag aaaagatcaa
     1261 aggatcttct tgagatcctt tttttctgcg cgtaatctgc tgcttgcaaa caaaaaaacc
     1321 accgctacca gcggtggttt gtttgccgga tcaagagcta ccaactcttt ttccgaaggt
     1381 aactggcttc agcagagcgc agataccaaa tactgttctt ctagtgtagc cgtagttagg
     1441 ccaccacttc aagaactctg tagcaccgcc tacatacctc gctctgctaa tcctgttacc
     1501 agtggctgct gccagtggcg ataagtcgtg tcttaccggg ttggactcaa gacgatagtt
     1561 accggataag gcgcagcggt cgggctgaac ggggggttcg tgcacacagc ccagcttgga
     1621 gcgaacgacc tacaccgaac tgagatacct acagcgtgag ctatgagaaa gcgccacgct
     1681 tcccgaaggg agaaaggcgg acaggcatcc ggtaagcggc agggtcggaa caggagagcg
     1741 cacgagggag cttccagggg gaaacgcctg gtatctttat agtcctgtcg ggtttcgcca
     1801 cctctgactt gagcgtcgat ttttgtgatg ctcgtcaggg gggcggagcc tatggaaaaa
     1861 cgccagcaac gcggccgtga aaggcaggcc ggtccgtggt ggccacggcc tctaggccag
     1921 atccagcggc atctgggtta gtcgagcgcg ggccgcttcc catgtctcac cagggcgagc
     1981 ctgtttcgcg atctcagcat ctgaaatctt cccggccttg cgcttcgctg gggccttacc
     2041 caccgccttg gcgggcttct tcggtccaaa actgaacaac agatgtgtga ccttgcgccc
     2101 ggtctttcgc tgcgcccact ccacctgtag cgggctgtgc tcgttgatct gcgtcacggc
     2161 tggatcaagc actcgcaact tgaagtcctt gatcgaggga taccggcctt ccagttgaaa
     2221 ccactttcgc agctggtcaa tttctatttc gcgctggccg atgctgtccc attgcatgag
     2281 cagctcgtaa agcctgatcg cgtgggtgct gtccatcttg gccacgtcag ccaaggcgta
     2341 tttggtgaac tgtttggtga gttccgtcag gtacggcagc atgtctttgg tgaacctgag
     2401 ttctacacgg ccctcaccct cccggtagat gattgtttgc acccagccgg taatcatcac
     2461 actcggtctt ttccccttgc cattgggctc ttgggttaac cggacttccc gccgtttcag
     2521 gcgcagggcc gcttctttga gctggttgta ggaagattcg atagggacac ccgccatcgt
     2581 cgctatgtcc tccgccgtca ctgaatacat cacttcatcg gtgacaggct cgctcctctt
     2641 cacctggcta atacaggcca gaacgatccg ctgttcctga acactgaggc gatacgcggc
     2701 ctcgaccagg gcattgcttt tgtaaaccat tgggggtgag gccacgttcg acattccttg
     2761 tgtataaggg gacactgtat ctgcgtccca caatacaaca aatccgtccc tttacaacaa
     2821 caaatccgtc ccttcttaac aacaaatccg tcccttaatg gcaacaaatc cgtccctttt
     2881 taaactctac aggccacgga ttacgtggcc tgtagacgtc ctaaaaggtt taaaagggaa
     2941 aaggaagaaa agggtggaaa cgcaaaaaac gcaccactac gtggccccgt tggggccgca
     3001 tttgtgcccc tgaaggggcg ggggaggcgt ctgggcaatc cccgttttac cagtccccta
     3061 tcgccgcctg agagggcgca ggaagcgagt aatcagggta tcgaggcgga ttcacccttg
     3121 gcgtccaacc agcggcacca gcggcgcctg agaggggcgc gcccagctgt ctagggcggc
     3181 ggatttgtcc tactcaggag agcgttcacc gacaaacaac agataaaacg aaaggcccag
     3241 tctttcgact gagcctttcg ttttatttga tgcctttaat taaggctcgg gagacctatc
     3301 ggtaataaca gtccaatctg gtgtaacttc ggaatcgtcc tttacggcta gctcagtcct
     3361 aggtactatg ctagctacta gtgaaagagg agaaatacta gtatggttag caaaggcgag
     3421 gcggttatca aggagtttat gcgttttaag gttcacatgg agggtagcat gaatggtcac
     3481 gagttcgaga tcgagggtga aggcgagggt cgtccgtacg aaggcaccca gaccgcgaag
     3541 ctgaaagtga ccaagggtgg cccgctgccg ttcagctggg acatcctgag cccgcagttc
     3601 atgtatggca gccgtgcgtt taccaaacac ccggcggaca ttccggatta ctataagcaa
     3661 agcttcccgg aaggttttaa atgggagcgt gttatgaact tcgaagatgg tggcgcggtg
     3721 accgttaccc aggacaccag cctggaggat ggcaccctga tttacaaggt gaaactgcgt
     3781 ggcaccaact ttccgccgga tggtccggtt atgcagaaga aaacgatggg ttgggaagcg
     3841 agcaccgagc gtctgtatcc ggaagatggc gtgctgaagg gtgatatcaa aatggcgctg
     3901 cgtctgaagg acggtggccg ttacctggcg gattttaaga ccacctataa agcgaagaaa
     3961 ccggtgcaaa tgccgggtgc gtacaacgtt gaccgtaaac tggatattac cagccacaac
     4021 gaggattata ccgtggttga gcaatatgag cgtagcgagg gtcgccacag caccggcggc
     4081 atggacgaac tgtataaggg atcctaataa cgctgatagt gctagtgtag atcgctacta
     4141 gagccaggca tcaaataaaa cgaaaggctc agtcgaaaga ctgggccttt cgttttatct
     4201 gttgtttgtc ggtgaacgct ctctactaga gtcacactgg ctcaccttcg ggtgggcctt
     4261 tctgcgttta tatactggct cg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and pRO1600/ColE1 origin of replication.",
                    "label": "BASIC_SEVA_24",
                },
                {
                    "accessor": "25",
                    "binaryString": """LOCUS       BASIC_SEVA_25           5987 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and RSF1010
            origin of replication..
ACCESSION   c4c251994910cc0861fe6324822266fb
VERSION     c4c251994910cc0861fe6324822266fb
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    4875..4979
                     /label="SEVA_T1"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    join(5982..5987,1..51)
                     /label="LMP"
     misc_feature    5849..5977
                     /label="B0015"
     misc_feature    5089..5100
                     /label="B0034"
     CDS             5108..5812
                     /label="mScarlett"
     misc_feature    5046..5080
                     /label="J23119"
     misc_feature    4989..5045
                     /label="LMS"
     misc_feature    1187..4860
                     /label="SEVA_RSF101"
     misc_feature    58..160
                     /label="SEVA_T0"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggcctcag cctgccgcct
     1201 tgggccgggt gatgtcgtac ttgcccgccg cgaactcggt taccgtccag cccagcgcga
     1261 ccagctccgg caacgcctcg cgcacccgct ggcggcgctt gcgcatggtc gaaccactgg
     1321 cctctgacgg ccagacatag ccgcacaagg tatctatgga agccttgccg gttttgccgg
     1381 ggtcgatcca gccacacagc cgctggtgca gcaggcgggc ggtttcgctg tccagcgccc
     1441 gcacctcgtc catgctgatg cgcacatgct ggccgccacc catgacggcc tgcgcgatca
     1501 aggggttcag ggccacgtac aggcgcccgt ccgcctcgtc gctggcgtac tccgacagca
     1561 gccgaaaccc ctgccgcttg cggccattct gggcgatgat ggataccttc caaaggcgct
     1621 cgatgcagtc ctgtatgtgc ttgagcgccc caccactatc gacctctgcc ccgatttcct
     1681 ttgccagcgc ccgatagcta cctttgacca catggcattc agcggtgacg gcctcccact
     1741 tgggttccag gaacagccgg agctgccgtc cgccttcggt cttgggttcc gggccaagca
     1801 ctaggccatt aggcccagcc atggccacca gcccttgcag gatgcgcaga tcatcagcgc
     1861 ccagcggctc cgggccgctg aactcgatcc gcttgccgtc gccgtagtca tacgtcacgt
     1921 ccagcttgct gcgcttgcgc tcgccccgct tgagggcacg gaacaggccg ggggccagac
     1981 agtgcgccgg gtcgtgccgg acgtggctga ggctgtgctt gttcttaggc ttcaccacgg
     2041 ggcaccccct tgctcttgcg ctgcctctcc agcacggcgg gcttgagcac cccgccgtca
     2101 tgccgcctga accaccgatc agcgaacggt gcgccatagt tggccttgct cacaccgaag
     2161 cggacgaaga accggcgctg gtcgtcgtcc acaccccatt cctcggcctc ggcgctggtc
     2221 atgctcgaca ggtaggactg ccagcggatg ttatcgacca gtaccgagct gccccggctg
     2281 gcctgctgct ggtcgcctgc gcccatcatg gccgcgccct tgctggcatg gtgcaggaac
     2341 acgatagagc acccggtatc ggcggcgatg gcctccatgc gaccgatgac ctgggccatg
     2401 gggccgctgg cgttttcttc ctcgatgtgg aaccggcgca gcgtgtccag caccatcagg
     2461 cggcggccct cggcggcgcg cttgaggccg tcgaaccact ccggggccat gatgttgggc
     2521 aggctgccga tcagcggctg gatcagcagg ccgtcagcca cggcttgccg ttcctcggcg
     2581 ctgaggtgcg ccccaagggc gtgcaggcgg tgatgaatgg cggtgggcgg gtcttcggcg
     2641 ggcaggtaga tcaccgggcc ggtgggcagt tcgcccacct ccagcagatc cggcccgcct
     2701 gcaatctgtg cggccagttg cagggccagc atggatttac cggcaccacc gggcgacacc
     2761 agcgccccga ccgtaccggc caccatgttg ggcaaaacgt agtccagcgg tggcggcgct
     2821 gctgcgaacg cctccagaat attgataggc ttatgggtag ccattgattg cctcctttgc
     2881 aggcagttgg tggttaggcg ctggcggggt cactaccccc gccctgcgcc gctctgagtt
     2941 cttccaggca ctcgcgcagc gcctcgtatt cgtcgtcggt cagccagaac ttgcgctgac
     3001 gcatcccttt ggccttcatg cgctcggcat atcgcgcttg gcgtacagcg tcagggctgg
     3061 ccagcaggtc gccggtctgc ttgtcctttt ggtctttcat atcagtcacc gagaaacttg
     3121 ccggggccga aaggcttgtc ttcgcggaac aaggacaagg tgcagccgtc aaggttaagg
     3181 ctggccatat cagcgactga aaagcggcca gcctcggcct tgtttgacgt ataaccaaag
     3241 ccaccgggca accaatagcc cttgtcactt ttgatcaggt agaccgaccc tgaagcgctt
     3301 ttttcgtatt ccataaaacc cccttctgtg cgtgagtact catagtataa caggcgtgag
     3361 taccaacgca agcactacat gctgaaatct ggcccgcccc tgtccatgcc tcgctggcgg
     3421 ggtgccggtg cccgtgccag ctcggcccgc gcaagctgga cgctgggcag acccatgacc
     3481 ttgctgacgg tgcgctcgat gtaatccgct tcgtggccgg gcttgcgctc tgccagcgct
     3541 gggctggcct cggccatggc cttgccgatt tcctcggcac tgcggccccg gctggccagc
     3601 ttctgcgcgg cgataaagtc gcacttgctg aggtcatcac cgaagcgctt gaccagcccg
     3661 gccatctcgc tgcggtactc gtccagcgcc gtgcgccggt ggcggctaag ctgccgctcg
     3721 ggcagttcga ggctggccag cctgcgggcc ttctcctgct gccgctgggc ctgctcgatc
     3781 tgctggccag cctgctgcac cagcgccggg ccagcggtgg cggtcttgcc cttggattca
     3841 cgcagcagca cccacggctg ataaccggcg cgggtggtgt gcttgtcctt gcggttggtg
     3901 aagcccgcca agcggccata gtggcggctg tcggcgctgg ccgggtcggc gtcgtactcg
     3961 ctggccagcg tccgggcaat ctgcccccga agttcaccgc ctgcggcgtc ggccaccttg
     4021 acccatgcct gatagttctt cgggctggtt tccactacca gggcaggctc ccggccctcg
     4081 gctttcatgt catccaggtc aaactcgctg aggtcgtcca ccagcaccag accatgccgc
     4141 tcctgctcgg cgggcctgat atacacgtca ttgccctggg cattcatccg cttgagccat
     4201 ggcgtgttct ggagcacttc ggcggctgac cattcccggt tcatcatctg gccggtggtg
     4261 gcgtccctga cgccgatatc gaagcgctca cagcccatgg ccttgagctg tcggcctatg
     4321 gcctgcaaag tcctgtcgtt cttcatcggg ccaccaagcg attcccacac attatacgag
     4381 ccggaagcat aaagtgtaaa gcctagatcc gaaggatgag ccgggctgaa tgatcgaccg
     4441 agacaggccc tgcggggctg cacacgcgcc cccacccttc gggtaggggg aaaggccgct
     4501 aaagcggcta aaagcgctcc agcgtatttc tgcggggttt ggtgtggggt ttagcgggct
     4561 ttgcccgcct ttccccctgc cgcgcagcgg tggggcggtg tgtagcctag cgcagcgaat
     4621 agaccagcta tccggcctct ggccgggcat attgggcaag ggcagcagcg ccccacaagg
     4681 gcgctgataa ccgcgcctag tggattattc ttagataatc atggatggat ttttccaaca
     4741 ccccgccagc ccccgcccct gctgggtttg caggtttggg ggcgtgacag ttattgcagg
     4801 ggttcgtgac agttattgca ggggggcgtg acagttattg caggggttcg tgacagttag
     4861 ggcgcgccca gctgtctagg gcggcggatt tgtcctactc aggagagcgt tcaccgacaa
     4921 acaacagata aaacgaaagg cccagtcttt cgactgagcc tttcgtttta tttgatgcct
     4981 ttaattaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta acttcggaat
     5041 cgtccttgac agctagctca gtcctaggta taatgctagc tactagtgaa agaggagaaa
     5101 tactagtatg gttagcaaag gcgaggcggt tatcaaggag tttatgcgtt ttaaggttca
     5161 catggagggt agcatgaatg gtcacgagtt cgagatcgag ggtgaaggcg agggtcgtcc
     5221 gtacgaaggc acccagaccg cgaagctgaa agtgaccaag ggtggcccgc tgccgttcag
     5281 ctgggacatc ctgagcccgc agttcatgta tggcagccgt gcgtttacca aacacccggc
     5341 ggacattccg gattactata agcaaagctt cccggaaggt tttaaatggg agcgtgttat
     5401 gaacttcgaa gatggtggcg cggtgaccgt tacccaggac accagcctgg aggatggcac
     5461 cctgatttac aaggtgaaac tgcgtggcac caactttccg ccggatggtc cggttatgca
     5521 gaagaaaacg atgggttggg aagcgagcac cgagcgtctg tatccggaag atggcgtgct
     5581 gaagggtgat atcaaaatgg cgctgcgtct gaaggacggt ggccgttacc tggcggattt
     5641 taagaccacc tataaagcga agaaaccggt gcaaatgccg ggtgcgtaca acgttgaccg
     5701 taaactggat attaccagcc acaacgagga ttataccgtg gttgagcaat atgagcgtag
     5761 cgagggtcgc cacagcaccg gcggcatgga cgaactgtat aagggatcct aataacgctg
     5821 atagtgctag tgtagatcgc tactagagcc aggcatcaaa taaaacgaaa ggctcagtcg
     5881 aaagactggg cctttcgttt tatctgttgt ttgtcggtga acgctctcta ctagagtcac
     5941 actggctcac cttcgggtgg gcctttctgc gtttatatac tggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and RSF1010 origin of replication.",
                    "label": "BASIC_SEVA_25",
                },
                {
                    "accessor": "26",
                    "binaryString": """LOCUS       BASIC_SEVA_26           3045 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and p15A
            origin of replication..
ACCESSION   c92d2eb763c0cd5a28e50d32a195c621
VERSION     c92d2eb763c0cd5a28e50d32a195c621
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    1933..2037
                     /label="SEVA_T1"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    1187..1918
                     /label="SEVA_p15A"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    join(3040..3045,1..51)
                     /label="LMP"
     misc_feature    2147..2158
                     /label="B0034"
     misc_feature    2907..3035
                     /label="B0015"
     CDS             2166..2870
                     /label="mScarlett"
     misc_feature    2104..2138
                     /label="J23119"
     misc_feature    2047..2103
                     /label="LMS"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccctag aaatatttta
     1201 tctgattaat aagatgatct tcttgagatc gttttggtct gcgcgtaatc tcttgctctg
     1261 aaaacgaaaa aaccgccttg cagggcggtt tttcgaaggt tctctgagct accaactctt
     1321 tgaaccgagg taactggctt ggaggagcgc agtcaccaaa acttgtcctt tcagtttagc
     1381 cttaaccggc gcatgacttc aagactaact cctctaaatc aattaccagt ggctgctgcc
     1441 agtggtgctt ttgcatgtct ttccgggttg gactcaagac gatagttacc ggataaggcg
     1501 cagcggtcgg actgaacggg gggttcgtgc atacagtcca gcttggagcg aactgcctac
     1561 ccggaactga gtgtcaggcg tggaatgaga caaacgcggc cataacagcg gaatgacacc
     1621 ggtaaaccga aaggcaggaa caggagagcg cacgagggag ccgccagggg gaaacgcctg
     1681 gtatctttat agtcctgtcg ggtttcgcca ccactgattt gagcgtcaga tttcgtgatg
     1741 cttgtcaggg gggcggagcc tatggaaaaa cggctttgcc gcggccctct cacttccctg
     1801 ttaagtatct tcctggcatc ttccaggaaa tctccgcccc gttcgtaagc catttccgct
     1861 cgccgcagtc gaacgaccga gcgtagcgag tcagtgagcg aggaagcgga atatatccgg
     1921 cgcgcccagc tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac
     1981 aacagataaa acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt
     2041 aattaaggct cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg
     2101 tccttgacag ctagctcagt cctaggtata atgctagcta ctagtgaaag aggagaaata
     2161 ctagtatggt tagcaaaggc gaggcggtta tcaaggagtt tatgcgtttt aaggttcaca
     2221 tggagggtag catgaatggt cacgagttcg agatcgaggg tgaaggcgag ggtcgtccgt
     2281 acgaaggcac ccagaccgcg aagctgaaag tgaccaaggg tggcccgctg ccgttcagct
     2341 gggacatcct gagcccgcag ttcatgtatg gcagccgtgc gtttaccaaa cacccggcgg
     2401 acattccgga ttactataag caaagcttcc cggaaggttt taaatgggag cgtgttatga
     2461 acttcgaaga tggtggcgcg gtgaccgtta cccaggacac cagcctggag gatggcaccc
     2521 tgatttacaa ggtgaaactg cgtggcacca actttccgcc ggatggtccg gttatgcaga
     2581 agaaaacgat gggttgggaa gcgagcaccg agcgtctgta tccggaagat ggcgtgctga
     2641 agggtgatat caaaatggcg ctgcgtctga aggacggtgg ccgttacctg gcggatttta
     2701 agaccaccta taaagcgaag aaaccggtgc aaatgccggg tgcgtacaac gttgaccgta
     2761 aactggatat taccagccac aacgaggatt ataccgtggt tgagcaatat gagcgtagcg
     2821 agggtcgcca cagcaccggc ggcatggacg aactgtataa gggatcctaa taacgctgat
     2881 agtgctagtg tagatcgcta ctagagccag gcatcaaata aaacgaaagg ctcagtcgaa
     2941 agactgggcc tttcgtttta tctgttgttt gtcggtgaac gctctctact agagtcacac
     3001 tggctcacct tcgggtgggc ctttctgcgt ttatatactg gctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and p15A origin of replication.",
                    "label": "BASIC_SEVA_26",
                },
                {
                    "accessor": "27",
                    "binaryString": """LOCUS       BASIC_SEVA_27           3969 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and pSC101
            origin of replication..
ACCESSION   9d3f6c884c90f253ed894bcf0e72b193
VERSION     9d3f6c884c90f253ed894bcf0e72b193
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2775..2831
                     /label="LMS"
     misc_feature    1187..2646
                     /label="SEVA_pSC101"
     misc_feature    join(3964..3969,1..51)
                     /label="LMP"
     misc_feature    2661..2765
                     /label="SEVA_T1"
     misc_feature    2924..2958
                     /label="J23119"
     misc_feature    58..160
                     /label="SEVA_T0"
     CDS             3090..3794
                     /label="mScarlett"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    3831..3959
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggcctcag atccttccgt
     1201 atttagccag tatgttctct agtgtggttc gttgtttttg cgtgagccat gagaacgaac
     1261 cattgagatc atacttactt tgcatgtcac tcaaaaattt tgcctcaaaa ctggtgagct
     1321 gaatttttgc agttaaagca tcgtgtagtg tttttcttag tccgttatgt aggtaggaat
     1381 ctgatgtaat ggttgttggt attttgtcac cattcatttt tatctggttg ttctcaagtt
     1441 cggttacgag atccatttgt ctatctagtt caacttggaa aatcaacgta tcagtcgggc
     1501 ggcctcgctt atcaaccacc aatttcatat tgctgtaagt gtttaaatct ttacttattg
     1561 gtttcaaaac ccattggtta agccttttaa actcatggta gttattttca agcattaaca
     1621 tgaacttaaa ttcatcaagg ctaatctcta tatttgcctt gtgagttttc ttttgtgtta
     1681 gttcttttaa taaccactca taaatcctca tagagtattt gttttcaaaa gacttaacat
     1741 gttccagatt atattttatg aattttttta actggaaaag ataaggcaat atctcttcac
     1801 taaaaactaa ttctaatttt tcgcttgaga acttggcata gtttgtccac tggaaaatct
     1861 caaagccttt aaccaaagga ttcctgattt ccacagttct cgtcatcagc tctctggttg
     1921 ctttagctaa tacaccataa gcattttccc tactgatgtt catcatctga gcgtattggt
     1981 tataagtgaa cgataccgtc cgttctttcc ttgtagggtt ttcaatcgtg gggttgagta
     2041 gtgccacaca gcataaaatt agcttggttt catgctccgt taagtcatag cgactaatcg
     2101 ctagttcatt tgctttgaaa acaactaatt cagacataca tctcaattgg tctaggtgat
     2161 tttaatcact ataccaattg agatgggcta gtcaatgata attacatgtc cttttccttt
     2221 gagttgtggg tatctgtaaa ttctgctaga cctttgctgg aaaacttgta aattctgcta
     2281 gaccctctgt aaattccgct agacctttgt gtgttttttt tgtttatatt caagtggtta
     2341 taatttatag aataaagaaa gaataaaaaa agataaaaag aatagatccc agccctgtgt
     2401 ataactcact actttagtca gttccgcagt attacaaaag gatgtcgcaa acgctgtttg
     2461 ctcctctaca aaacagacct taaaacccta aaggcttaag tagcaccctc gcaagctcgg
     2521 gcaaatcgct gaatattcct tttgtctccg accatcaggc acctgagtcg ctgtcttttt
     2581 cgtgacattc agttcgctgc gctcacggct ctggcagtga atgggggtaa atggcactac
     2641 aggcgcggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga gagcgttcac
     2701 cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc gttttatttg
     2761 atgcctttaa ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt
     2821 cggaatcgtc cccaattatt gaacaccctt cggggtgttt ttttgtttct ggtctaccat
     2881 ctcgttgtga taatagacct gaagtgccta ctctggaaaa tctttgacag ctagctcagt
     2941 cctaggtata atgctagcag ctgtcaccgg atgtgctttc cggtctgatg agtccgtgag
     3001 gacgaaacag cctctacaaa taattttgtt taaggctcgc tacgagaaga ttgttacttt
     3061 cgcagcgtta ttatctaagg aggtagtcca tggttagcaa aggcgaggcg gttatcaagg
     3121 agtttatgcg ttttaaggtt cacatggagg gtagcatgaa tggtcacgag ttcgagatcg
     3181 agggtgaagg cgagggtcgt ccgtacgaag gcacccagac cgcgaagctg aaagtgacca
     3241 agggtggccc gctgccgttc agctgggaca tcctgagccc gcagttcatg tatggcagcc
     3301 gtgcgtttac caaacacccg gcggacattc cggattacta taagcaaagc ttcccggaag
     3361 gttttaaatg ggagcgtgtt atgaacttcg aagatggtgg cgcggtgacc gttacccagg
     3421 acaccagcct ggaggatggc accctgattt acaaggtgaa actgcgtggc accaactttc
     3481 cgccggatgg tccggttatg cagaagaaaa cgatgggttg ggaagcgagc accgagcgtc
     3541 tgtatccgga agatggcgtg ctgaagggtg atatcaaaat ggcgctgcgt ctgaaggacg
     3601 gtggccgtta cctggcggat tttaagacca cctataaagc gaagaaaccg gtgcaaatgc
     3661 cgggtgcgta caacgttgac cgtaaactgg atattaccag ccacaacgag gattataccg
     3721 tggttgagca atatgagcgt agcgagggtc gccacagcac cggcggcatg gacgaactgt
     3781 ataagggatc ctaataacgc tgatagtgct agtgtagatc gctactagag ccaggcatca
     3841 aataaaacga aaggctcagt cgaaagactg ggcctttcgt tttatctgtt gtttgtcggt
     3901 gaacgctctc tactagagtc acactggctc accttcgggt gggcctttct gcgtttatat
     3961 actggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and pSC101 origin of replication.",
                    "label": "BASIC_SEVA_27",
                },
                {
                    "accessor": "28",
                    "binaryString": """LOCUS       BASIC_SEVA_28           3242 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and pUC
            origin of replication..
ACCESSION   e960becd8f97dc2988e5ffd17ad4379f
VERSION     e960becd8f97dc2988e5ffd17ad4379f
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2130..2234
                     /label="SEVA_T1"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    2301..2335
                     /label="J23106"
     misc_feature    2344..2355
                     /label="B0034"
     misc_feature    1187..2115
                     /label="SEVA_pUC"
     misc_feature    join(3237..3242,1..51)
                     /label="LMP"
     misc_feature    2244..2300
                     /label="LMS"
     misc_feature    58..160
                     /label="SEVA_T0"
     CDS             2363..3067
                     /label="mScarlett"
     misc_feature    3104..3232
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccccgt agaaaagatc
     1201 aaaggatctt cttgagatcc tttttttctg cgcgtaatct gctgcttgca aacaaaaaaa
     1261 ccaccgctac cagcggtggt ttgtttgccg gatcaagagc taccaactct ttttccgaag
     1321 gtaactggct tcagcagagc gcagatacca aatactgttc ttctagtgta gccgtagtta
     1381 ggccaccact tcaagaactc tgtagcaccg cctacatacc tcgctctgct aatcctgtta
     1441 ccagtggctg ctgccagtgg cgataagtcg tgtcttaccg ggttggactc aagacgatag
     1501 ttaccggata aggcgcagcg gtcgggctga acggggggtt cgtgcacaca gcccagcttg
     1561 gagcgaacga cctacaccga actgagatac ctacagcgtg agctttgaga aagcgccacg
     1621 cttcccgaag ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg aacaggagag
     1681 cgcacgaggg agcttccagg gggaaacgcc tggtatcttt atagtcctgt cgggtttcgc
     1741 cacctctgac ttgagcgtcg atttttgtga tgctcgtcag gggggcggag cctatggaaa
     1801 aacgccagca acgcggcctt tttacggttc ctggcctttt gctggccttt tgctcacatg
     1861 ttctttcctg cgttatcccc tgattctgtg gataaccgta ttaccgcctt tgagtgagct
     1921 gataccgctc gccgcagccg aacgaccgag cgcagcgagt cagtgagcga ggaagcggaa
     1981 gagcgcccaa tacgcaaacc gcctctcccc gcgcgttggc cgattcatta atgcagctgg
     2041 cacgacaggt ttcccgactg gaaagcgggc agtgagcgca acgcaattaa tgtgagttag
     2101 ctcactcatt aggcaggcgc gcccagctgt ctagggcggc ggatttgtcc tactcaggag
     2161 agcgttcacc gacaaacaac agataaaacg aaaggcccag tctttcgact gagcctttcg
     2221 ttttatttga tgcctttaat taaggctcgg gagacctatc ggtaataaca gtccaatctg
     2281 gtgtaacttc ggaatcgtcc tttacggcta gctcagtcct aggtatagtg ctagctacta
     2341 gtgaaagagg agaaatacta gtatggttag caaaggcgag gcggttatca aggagtttat
     2401 gcgttttaag gttcacatgg agggtagcat gaatggtcac gagttcgaga tcgagggtga
     2461 aggcgagggt cgtccgtacg aaggcaccca gaccgcgaag ctgaaagtga ccaagggtgg
     2521 cccgctgccg ttcagctggg acatcctgag cccgcagttc atgtatggca gccgtgcgtt
     2581 taccaaacac ccggcggaca ttccggatta ctataagcaa agcttcccgg aaggttttaa
     2641 atgggagcgt gttatgaact tcgaagatgg tggcgcggtg accgttaccc aggacaccag
     2701 cctggaggat ggcaccctga tttacaaggt gaaactgcgt ggcaccaact ttccgccgga
     2761 tggtccggtt atgcagaaga aaacgatggg ttgggaagcg agcaccgagc gtctgtatcc
     2821 ggaagatggc gtgctgaagg gtgatatcaa aatggcgctg cgtctgaagg acggtggccg
     2881 ttacctggcg gattttaaga ccacctataa agcgaagaaa ccggtgcaaa tgccgggtgc
     2941 gtacaacgtt gaccgtaaac tggatattac cagccacaac gaggattata ccgtggttga
     3001 gcaatatgag cgtagcgagg gtcgccacag caccggcggc atggacgaac tgtataaggg
     3061 atcctaataa cgctgatagt gctagtgtag atcgctacta gagccaggca tcaaataaaa
     3121 cgaaaggctc agtcgaaaga ctgggccttt cgttttatct gttgtttgtc ggtgaacgct
     3181 ctctactaga gtcacactgg ctcaccttcg ggtgggcctt tctgcgttta tatactggct
     3241 cg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and pUC origin of replication.",
                    "label": "BASIC_SEVA_28",
                },
                {
                    "accessor": "29",
                    "binaryString": """LOCUS       BASIC_SEVA_29           3698 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Kanamycin resistance marker and
            pBR322-ROP origin of replication..
ACCESSION   52c4b95c8cfa7223c166bfa25ccb102f
VERSION     52c4b95c8cfa7223c166bfa25ccb102f
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2800..2811
                     /label="B0034"
     misc_feature    187..1113
                     /label="SEVA_Km"
     misc_feature    join(3693..3698,1..51)
                     /label="LMP"
     misc_feature    2586..2690
                     /label="SEVA_T1"
     misc_feature    2757..2791
                     /label="J23119"
     misc_feature    1187..2571
                     /label="SEVA_pBR322-ROP"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2700..2756
                     /label="LMS"
     CDS             2819..3523
                     /label="mScarlett"
     misc_feature    3560..3688
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttgt gtctcaaaat ctctgatgtt acattgcaca agataaaaat atatcatcat
      241 gaacaataaa actgtctgct tacataaaca gtaatacaag gggtgttatg agccatattc
      301 agcgtgaaac gagctgtagc cgtccgcgtc tgaacagcaa catggatgcg gatctgtatg
      361 gctataaatg ggcgcgtgat aacgtgggtc agagcggcgc gaccatttat cgtctgtatg
      421 gcaaaccgga tgcgccggaa ctgtttctga aacatggcaa aggcagcgtg gcgaacgatg
      481 tgaccgatga aatggtgcgt ctgaactggc tgaccgaatt tatgccgctg ccgaccatta
      541 aacattttat tcgcaccccg gatgatgcgt ggctgctgac caccgcgatt ccgggcaaaa
      601 ccgcgtttca ggtgctggaa gaatatccgg atagcggcga aaacattgtg gatgcgctgg
      661 ccgtgtttct gcgtcgtctg catagcattc cggtgtgcaa ctgcccgttt aacagcgatc
      721 gtgtgtttcg tctggcccag gcgcagagcc gtatgaacaa cggcctggtg gatgcgagcg
      781 attttgatga tgaacgtaac ggctggccgg tggaacaggt gtggaaagaa atgcataaac
      841 tgctgccgtt tagcccggat agcgtggtga cccacggcga ttttagcctg gataacctga
      901 ttttcgatga aggcaaactg attggctgca ttgatgtggg ccgtgtgggc attgcggatc
      961 gttatcagga tctggccatt ctgtggaact gcctgggcga atttagcccg agcctgcaaa
     1021 aacgtctgtt tcagaaatat ggcattgata atccggatat gaacaaactg caatttcatc
     1081 tgatgctgga tgaatttttc taataattaa ttggaccgcg gtcggctcga cccacgacta
     1141 ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccccgt agaaaagatc
     1201 aaaggatctt cttgagatcc tttttttctg cgcgtaatct gctgcttgca aacaaaaaaa
     1261 ccaccgctac cagcggtggt ttgtttgccg gatcaagagc taccaactct ttttccgaag
     1321 gtaactggct tcagcagagc gcagatacca aatactgtcc ttctagtgta gccgtagtta
     1381 ggccaccact tcaagaactc tgtagcaccg cctacatacc tcgctctgct aatcctgtta
     1441 ccagtggctg ctgccagtgg cgataagtcg tgtcttaccg ggttggactc aagacgatag
     1501 ttaccggata aggcgcagcg gtcgggctga acggggggtt cgtgcacaca gcccagcttg
     1561 gagcgaacga cctacaccga actgagatac ctacagcgtg agctatgaga aagcgccacg
     1621 cttcccgaag ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg aacaggagag
     1681 cgcacgaggg agcttccagg gggaaacgcc tggtatcttt atagtcctgt cgggtttcgc
     1741 cacctctgac ttgagcgtcg atttttgtga tgctcgtcag gggggcggag cctatggaaa
     1801 aacgccagca acgcggcctt tttacggttc ctggcctttt gctggccttt tgctcacatg
     1861 ttctttcctg cgttatcccc tgattctgtg gataaccgta ttaccgcctt tgagtgagct
     1921 gataccgctc gccgcagccg aacgaccgag cgcagcgagt cagtgagcga ggaagcggaa
     1981 gagcgcctga tgcggtattt tctccttacg catctgtgcg gtatttcaca ccgcatatgg
     2041 tgcactctca gtacaatctg ctctgatgcc gcatagttaa gccagtatac actccgctat
     2101 cgctacgtga ctgggtcatg gctgcgcccc gacacccgcc aacacccgct gacgcgccct
     2161 gacgggcttg tctgctcccg gcatccgctt acagacaagc tgtgaccgtc tccgggagct
     2221 gcatgtgtca gaggttttca ccgtcatcac cgaaacgcgc gaggcagctg cggtaaagct
     2281 catcagcgtg gtcgtgcagc gattcacaga tgtctgcctg ttcatccgcg tccagctcgt
     2341 tgagtttctc cagaagcgtt aatgtctggc ttctgataaa gcgggccatg ttaagggcgg
     2401 ttttttcctg tttggtcact gatgcctccg tgtaaggggg atttctgttc atgggggtaa
     2461 tgataccgat gaaacgagag aggatgctca cgatacgggt tactgatgat gaacatgccc
     2521 ggttactgga acgttgtgag ggtaaacaac tggcggtatg gatgcggcgg gggcgcgccc
     2581 agctgtctag ggcggcggat ttgtcctact caggagagcg ttcaccgaca aacaacagat
     2641 aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt atttgatgcc tttaattaag
     2701 gctcgggaga cctatcggta ataacagtcc aatctggtgt aacttcggaa tcgtccttga
     2761 cagctagctc agtcctaggt ataatgctag ctactagtga aagaggagaa atactagtat
     2821 ggttagcaaa ggcgaggcgg ttatcaagga gtttatgcgt tttaaggttc acatggaggg
     2881 tagcatgaat ggtcacgagt tcgagatcga gggtgaaggc gagggtcgtc cgtacgaagg
     2941 cacccagacc gcgaagctga aagtgaccaa gggtggcccg ctgccgttca gctgggacat
     3001 cctgagcccg cagttcatgt atggcagccg tgcgtttacc aaacacccgg cggacattcc
     3061 ggattactat aagcaaagct tcccggaagg ttttaaatgg gagcgtgtta tgaacttcga
     3121 agatggtggc gcggtgaccg ttacccagga caccagcctg gaggatggca ccctgattta
     3181 caaggtgaaa ctgcgtggca ccaactttcc gccggatggt ccggttatgc agaagaaaac
     3241 gatgggttgg gaagcgagca ccgagcgtct gtatccggaa gatggcgtgc tgaagggtga
     3301 tatcaaaatg gcgctgcgtc tgaaggacgg tggccgttac ctggcggatt ttaagaccac
     3361 ctataaagcg aagaaaccgg tgcaaatgcc gggtgcgtac aacgttgacc gtaaactgga
     3421 tattaccagc cacaacgagg attataccgt ggttgagcaa tatgagcgta gcgagggtcg
     3481 ccacagcacc ggcggcatgg acgaactgta taagggatcc taataacgct gatagtgcta
     3541 gtgtagatcg ctactagagc caggcatcaa ataaaacgaa aggctcagtc gaaagactgg
     3601 gcctttcgtt ttatctgttg tttgtcggtg aacgctctct actagagtca cactggctca
     3661 ccttcgggtg ggcctttctg cgtttatata ctggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Kanamycin resistance marker and pBR322-ROP origin of replication.",
                    "label": "BASIC_SEVA_29",
                },
                {
                    "accessor": "32",
                    "binaryString": """LOCUS       BASIC_SEVA_32           4587 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            RK2 origin of replication..
ACCESSION   24f70e7cdb2bbdf7e33cd505aa9194e0
VERSION     24f70e7cdb2bbdf7e33cd505aa9194e0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    join(4582..4587,1..51)
                     /label="LMP"
     misc_feature    3542..3576
                     /label="J23119"
     misc_feature    187..969
                     /label="SEVA_Cm"
     misc_feature    3279..3383
                     /label="SEVA_T1"
     CDS             3708..4412
                     /label="mScarlett"
     misc_feature    4449..4577
                     /label="B0015"
     misc_feature    1043..3264
                     /label="SEVA_RK2"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3393..3449
                     /label="LMS"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg ccgcgatgca ggtggctgct gaacccccag ccggaactga
     1081 ccccacaagg ccctagcgtt tgcaatgcac caggtcatca ttgacccagg cgtgttccac
     1141 caggccgctg cctcgcaact cttcgcaggc ttcgccgacc tgctcgcgcc acttcttcac
     1201 gcgggtggaa tccgatccgc acatgaggcg gaaggtttcc agcttgagcg ggtacggctc
     1261 ccggtgcgag ctgaaatagt cgaacatccg tcgggccgtc ggcgacagct tgcggtactt
     1321 ctcccatatg aatttcgtgt agtggtcgcc agcaaacagc acgacgattt cctcgtcgat
     1381 caggacctgg caacgggacg ttttcttgcc acggtccagg acgcggaagc ggtgcagcag
     1441 cgacaccgat tccaggtgcc caacgcggtc ggacgtgaag cccatcgccg tcgcctgtag
     1501 gcgcgacagg cattcctcgg ccttcgtgta ataccggcca ttgatcgacc agcccaggtc
     1561 ctggcaaagc tcgtagaacg tgaaggtgat cggctcgccg ataggggtgc gcttcgcgta
     1621 ctccaacacc tgctgccaca ccagttcgtc atcgtcggcc cgcagctcga cgccggtgta
     1681 ggtgatcttc acgtccttgt tgacgtggaa aatgaccttg ttttgcagcg cctcgcgcgg
     1741 gattttcttg ttgcgcgtgg tgaacagggc agagcgggcc gtgtcgtttg gcatcgctcg
     1801 catcgtgtcc ggccacggcg caatatcgaa caaggaaagc tgcatttcct tgatctgctg
     1861 cttcgtgtgt ttcagcaacg cggcctgctt ggcttcgctg acctgttttg ccaggtcctc
     1921 gccggcggtt tttcgcttct tggtcgtcat agttcctcgc gtgtcgatgg tcatcgactt
     1981 cgccaaacct gccgcctcct gttcgagacg acgcgaacgc tccacggcgg ccgatggcgc
     2041 gggcagggca gggggagcca gttgcacgct gtcgcgctcg atcttggccg tagcttgctg
     2101 gactatcgag ccgacggact ggaaggtttc gcggggcgca cgcatgacgg tgcggcttgc
     2161 gatggtttcg gcatcctcgg cggaaaaccc cgcgtcgatc agttcttgcc tgtatgcctt
     2221 ccggtcaaac gtccgattca ttcaccctcc ttgcgggatt gccccggaat taattccccg
     2281 gatcgatccg tcgatcttga tcccctgcgc catcagatcc ttggcggcaa gaaagccatc
     2341 cagtttactt tgcagggctt cccaacctta ccagagggcg ccccagctgg caattccggt
     2401 tcgcttgctg tccataaaac cgcccagtct agctatcgcc atgtaagccc actgcaagct
     2461 acctgctttc tctttgcgct tgcgttttcc cttgtccaga tagcccagta gctgacattc
     2521 atccggggtc agcaccgttt ctgcggactg gctttctacg tggctgccat ttttggggtg
     2581 aggccgttcg cggccgaggg gcgcagcccc tggggggatg ggaggcccgc gttagcgggc
     2641 cgggagggtt cgagaagggg gggcaccccc cttcggcgtg cgcggtcacg cgcacagggc
     2701 gcagccctgg ttaaaaacaa ggtttataaa tattggttta aaagcaggtt aaaagacagg
     2761 ttagcggtgg ccgaaaaacg ggcggaaacc cttgcaaatg ctggattttc tgcctgtgga
     2821 cagcccctca aatgtcaata ggtgcgcccc tcatctgtca gcactctgcc cctcaagtgt
     2881 caaggatcgc gcccctcatc tgtcagtagt cgcgcccctc aagtgtcaat accgcagggc
     2941 acttatcccc aggcttgtcc acatcatctg tgggaaactc gcgtaaaatc aggcgttttc
     3001 gccgatttgc gaggctggcc agctccacgt cgccggccga aatcgagcct gcccctcatc
     3061 tgtcaacgcc gcgccgggtg agtcggcccc tcaagtgtca acgtccgccc ctcatctgtc
     3121 agtgagggcc aagttttccg cgaggtatcc acaacgccgg cggccctaca tggctctgct
     3181 gtagtgagtg ggttgcgctc cggcagcggt cctgatcccc cgcagaaaaa aaggatctca
     3241 agaagatcct ttgatctttt ctacggcgcg cccagctgtc tagggcggcg gatttgtcct
     3301 actcaggaga gcgttcaccg acaaacaaca gataaaacga aaggcccagt ctttcgactg
     3361 agcctttcgt tttatttgat gcctttaatt aaggctcggg agacctatcg gtaataacag
     3421 tccaatctgg tgtaacttcg gaatcgtccc caattattga acacccttcg gggtgttttt
     3481 ttgtttctgg tctaccatct cgttgtgata atagacctga agtgcctact ctggaaaatc
     3541 tttgacagct agctcagtcc taggtataat gctagcagct gtcaccggat gtgctttccg
     3601 gtctgatgag tccgtgagga cgaaacagcc tctacaaata attttgttta aggctcgcta
     3661 cgagaagatt gttactttcg cagcgttatt atctaaggag gtagtccatg gttagcaaag
     3721 gcgaggcggt tatcaaggag tttatgcgtt ttaaggttca catggagggt agcatgaatg
     3781 gtcacgagtt cgagatcgag ggtgaaggcg agggtcgtcc gtacgaaggc acccagaccg
     3841 cgaagctgaa agtgaccaag ggtggcccgc tgccgttcag ctgggacatc ctgagcccgc
     3901 agttcatgta tggcagccgt gcgtttacca aacacccggc ggacattccg gattactata
     3961 agcaaagctt cccggaaggt tttaaatggg agcgtgttat gaacttcgaa gatggtggcg
     4021 cggtgaccgt tacccaggac accagcctgg aggatggcac cctgatttac aaggtgaaac
     4081 tgcgtggcac caactttccg ccggatggtc cggttatgca gaagaaaacg atgggttggg
     4141 aagcgagcac cgagcgtctg tatccggaag atggcgtgct gaagggtgat atcaaaatgg
     4201 cgctgcgtct gaaggacggt ggccgttacc tggcggattt taagaccacc tataaagcga
     4261 agaaaccggt gcaaatgccg ggtgcgtaca acgttgaccg taaactggat attaccagcc
     4321 acaacgagga ttataccgtg gttgagcaat atgagcgtag cgagggtcgc cacagcaccg
     4381 gcggcatgga cgaactgtat aagggatcct aataacgctg atagtgctag tgtagatcgc
     4441 tactagagcc aggcatcaaa taaaacgaaa ggctcagtcg aaagactggg cctttcgttt
     4501 tatctgttgt ttgtcggtga acgctctcta ctagagtcac actggctcac cttcgggtgg
     4561 gcctttctgc gtttatatac tggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and RK2 origin of replication.",
                    "label": "BASIC_SEVA_32",
                },
                {
                    "accessor": "33",
                    "binaryString": """LOCUS       BASIC_SEVA_33           3887 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            pBBR1 origin of replication..
ACCESSION   7e861708c72a18b544e5574679749a31
VERSION     7e861708c72a18b544e5574679749a31
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2842..2876
                     /label="J23119"
     misc_feature    187..969
                     /label="SEVA_Cm"
     misc_feature    3749..3877
                     /label="B0015"
     misc_feature    join(3882..3887,1..51)
                     /label="LMP"
     misc_feature    2693..2749
                     /label="LMS"
     misc_feature    2579..2683
                     /label="SEVA_T1"
     misc_feature    58..160
                     /label="SEVA_T0"
     CDS             3008..3712
                     /label="mScarlett"
     misc_feature    1043..2564
                     /label="SEVA_pBBR1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg ccctaccggc gcggcagcgt tacccgtgtc ggcggctcca
     1081 acggctcgcc atcgtccaga aaacacggct catcgggcat cggcaggcgc tgctgcccgc
     1141 gccgttccca ttcctccgtt tcggtcaagg ctggcaggtc tggttccatg cccggaatgc
     1201 cgggctggct gggcggctcc tcgccggggc cggtcggtag ttgctgctcg cccggataca
     1261 gggtcgggat gcggcgcagg tcgccatgcc ccaacagcga ttcgtcctgg tcgtcgtgat
     1321 caaccaccac ggcggcactg aacaccgaca ggcgcaactg gtcgcggggc tggccccacg
     1381 ccacgcggtc attgaccacg taggccgaca cggtgccggg gccgttgagc ttcacgacgg
     1441 agatccagcg ctcggccacc aagtccttga ctgcgtattg gaccgtccgc aaagaacgtc
     1501 cgatgagctt ggaaagtgtc ttctggctga ccaccacggc gttctggtgg cccatctgcg
     1561 ccacgaggtg atgcagcagc attgccgccg tgggtttcct cgcaataagc ccggcccacg
     1621 cctcatgcgc tttgcgttcc gtttgcaccc agtgaccggg cttgttcttg gcttgaatgc
     1681 cgatttctct ggactgcgtg gccatgctta tctccatgcg gtaggggtgc cgcacggttg
     1741 cggcaccatg cgcaatcagc tgcaactttt cggcagcgcg acaacaatta tgcgttgcgt
     1801 aaaagtggca gtcaattaca gattttcttt aacctacgca atgagctatt gcggggggtg
     1861 ccgcaatgag ctgttgcgta cccccctttt ttaagttgtt gatttttaag tctttcgcat
     1921 ttcgccctat atctagttct ttggtgccca aagaagggca cccctgcggg gttcccccac
     1981 gccttcggcg cggctccccc tccggcaaaa agtggcccct ccggggcttg ttgatcgact
     2041 gcgcggcctt cggccttgcc caaggtggcg ctgccccctt ggaacccccg cactcgccgc
     2101 cgtgaggctc ggggggcagg cgggcgggct tcgcccttcg actgccccca ctcgcatagg
     2161 cttgggtcgt tccaggcgcg tcaaggccaa gccgctgcgc ggtcgctgcg cgagccttga
     2221 cccgccttcc acttggtgtc caaccggcaa gcgaagcgcg caggccgcag gccggaggct
     2281 tttccccaga gaaaattaaa aaaattgatg gggcaaggcc gcaggccgcg cagttggagc
     2341 cggtgggtat gtggtcgaag gctgggtagc cggtgggcaa tccctgtggt caagctcgtg
     2401 ggcaggcgca gcctgtccat cagcttgtcc agcagggttg tccacgggcc gagcgaagcg
     2461 agccagccgg tggccgctcg cggccatcgt ccacatatcc acgggctggc aagggagcgc
     2521 agcgaccgcg cagggcgaag cccggagagc aagcccgtag ggggggcgcg cccagctgtc
     2581 tagggcggcg gatttgtcct actcaggaga gcgttcaccg acaaacaaca gataaaacga
     2641 aaggcccagt ctttcgactg agcctttcgt tttatttgat gcctttaatt aaggctcggg
     2701 agacctatcg gtaataacag tccaatctgg tgtaacttcg gaatcgtccc caattattga
     2761 acacccttcg gggtgttttt ttgtttctgg tctaccatct cgttgtgata atagacctga
     2821 agtgcctact ctggaaaatc tttgacagct agctcagtcc taggtataat gctagcagct
     2881 gtcaccggat gtgctttccg gtctgatgag tccgtgagga cgaaacagcc tctacaaata
     2941 attttgttta aggctcgcta cgagaagatt gttactttcg cagcgttatt atctaaggag
     3001 gtagtccatg gttagcaaag gcgaggcggt tatcaaggag tttatgcgtt ttaaggttca
     3061 catggagggt agcatgaatg gtcacgagtt cgagatcgag ggtgaaggcg agggtcgtcc
     3121 gtacgaaggc acccagaccg cgaagctgaa agtgaccaag ggtggcccgc tgccgttcag
     3181 ctgggacatc ctgagcccgc agttcatgta tggcagccgt gcgtttacca aacacccggc
     3241 ggacattccg gattactata agcaaagctt cccggaaggt tttaaatggg agcgtgttat
     3301 gaacttcgaa gatggtggcg cggtgaccgt tacccaggac accagcctgg aggatggcac
     3361 cctgatttac aaggtgaaac tgcgtggcac caactttccg ccggatggtc cggttatgca
     3421 gaagaaaacg atgggttggg aagcgagcac cgagcgtctg tatccggaag atggcgtgct
     3481 gaagggtgat atcaaaatgg cgctgcgtct gaaggacggt ggccgttacc tggcggattt
     3541 taagaccacc tataaagcga agaaaccggt gcaaatgccg ggtgcgtaca acgttgaccg
     3601 taaactggat attaccagcc acaacgagga ttataccgtg gttgagcaat atgagcgtag
     3661 cgagggtcgc cacagcaccg gcggcatgga cgaactgtat aagggatcct aataacgctg
     3721 atagtgctag tgtagatcgc tactagagcc aggcatcaaa taaaacgaaa ggctcagtcg
     3781 aaagactggg cctttcgttt tatctgttgt ttgtcggtga acgctctcta ctagagtcac
     3841 actggctcac cttcgggtgg gcctttctgc gtttatatac tggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and pBBR1 origin of replication.",
                    "label": "BASIC_SEVA_33",
                },
                {
                    "accessor": "34",
                    "binaryString": """LOCUS       BASIC_SEVA_34           4138 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            pRO1600/ColE1 origin of replication..
ACCESSION   1d0cfeeca882a775fadb595d2db6c0a4
VERSION     1d0cfeeca882a775fadb595d2db6c0a4
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3197..3231
                     /label="J23105"
     misc_feature    join(4133..4138,1..51)
                     /label="LMP"
     CDS             3259..3963
                     /label="mScarlett"
     misc_feature    187..969
                     /label="SEVA_Cm"
     misc_feature    3240..3251
                     /label="B0034"
     misc_feature    3140..3196
                     /label="LMS"
     misc_feature    4000..4128
                     /label="B0015"
     misc_feature    3026..3130
                     /label="SEVA_T1"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    1043..3011
                     /label="SEVA_pRO1600/ColE1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg ccgataatct catgaccaaa atcccttaac gtgagttttc
     1081 gttccactga gcgtcagacc ccgtagaaaa gatcaaagga tcttcttgag atcctttttt
     1141 tctgcgcgta atctgctgct tgcaaacaaa aaaaccaccg ctaccagcgg tggtttgttt
     1201 gccggatcaa gagctaccaa ctctttttcc gaaggtaact ggcttcagca gagcgcagat
     1261 accaaatact gttcttctag tgtagccgta gttaggccac cacttcaaga actctgtagc
     1321 accgcctaca tacctcgctc tgctaatcct gttaccagtg gctgctgcca gtggcgataa
     1381 gtcgtgtctt accgggttgg actcaagacg atagttaccg gataaggcgc agcggtcggg
     1441 ctgaacgggg ggttcgtgca cacagcccag cttggagcga acgacctaca ccgaactgag
     1501 atacctacag cgtgagctat gagaaagcgc cacgcttccc gaagggagaa aggcggacag
     1561 gcatccggta agcggcaggg tcggaacagg agagcgcacg agggagcttc cagggggaaa
     1621 cgcctggtat ctttatagtc ctgtcgggtt tcgccacctc tgacttgagc gtcgattttt
     1681 gtgatgctcg tcaggggggc ggagcctatg gaaaaacgcc agcaacgcgg ccgtgaaagg
     1741 caggccggtc cgtggtggcc acggcctcta ggccagatcc agcggcatct gggttagtcg
     1801 agcgcgggcc gcttcccatg tctcaccagg gcgagcctgt ttcgcgatct cagcatctga
     1861 aatcttcccg gccttgcgct tcgctggggc cttacccacc gccttggcgg gcttcttcgg
     1921 tccaaaactg aacaacagat gtgtgacctt gcgcccggtc tttcgctgcg cccactccac
     1981 ctgtagcggg ctgtgctcgt tgatctgcgt cacggctgga tcaagcactc gcaacttgaa
     2041 gtccttgatc gagggatacc ggccttccag ttgaaaccac tttcgcagct ggtcaatttc
     2101 tatttcgcgc tggccgatgc tgtcccattg catgagcagc tcgtaaagcc tgatcgcgtg
     2161 ggtgctgtcc atcttggcca cgtcagccaa ggcgtatttg gtgaactgtt tggtgagttc
     2221 cgtcaggtac ggcagcatgt ctttggtgaa cctgagttct acacggccct caccctcccg
     2281 gtagatgatt gtttgcaccc agccggtaat catcacactc ggtcttttcc ccttgccatt
     2341 gggctcttgg gttaaccgga cttcccgccg tttcaggcgc agggccgctt ctttgagctg
     2401 gttgtaggaa gattcgatag ggacacccgc catcgtcgct atgtcctccg ccgtcactga
     2461 atacatcact tcatcggtga caggctcgct cctcttcacc tggctaatac aggccagaac
     2521 gatccgctgt tcctgaacac tgaggcgata cgcggcctcg accagggcat tgcttttgta
     2581 aaccattggg ggtgaggcca cgttcgacat tccttgtgta taaggggaca ctgtatctgc
     2641 gtcccacaat acaacaaatc cgtcccttta caacaacaaa tccgtccctt cttaacaaca
     2701 aatccgtccc ttaatggcaa caaatccgtc cctttttaaa ctctacaggc cacggattac
     2761 gtggcctgta gacgtcctaa aaggtttaaa agggaaaagg aagaaaaggg tggaaacgca
     2821 aaaaacgcac cactacgtgg ccccgttggg gccgcatttg tgcccctgaa ggggcggggg
     2881 aggcgtctgg gcaatccccg ttttaccagt cccctatcgc cgcctgagag ggcgcaggaa
     2941 gcgagtaatc agggtatcga ggcggattca cccttggcgt ccaaccagcg gcaccagcgg
     3001 cgcctgagag gggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg
     3061 ttcaccgaca aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt
     3121 atttgatgcc tttaattaag gctcgggaga cctatcggta ataacagtcc aatctggtgt
     3181 aacttcggaa tcgtccttta cggctagctc agtcctaggt actatgctag ctactagtga
     3241 aagaggagaa atactagtat ggttagcaaa ggcgaggcgg ttatcaagga gtttatgcgt
     3301 tttaaggttc acatggaggg tagcatgaat ggtcacgagt tcgagatcga gggtgaaggc
     3361 gagggtcgtc cgtacgaagg cacccagacc gcgaagctga aagtgaccaa gggtggcccg
     3421 ctgccgttca gctgggacat cctgagcccg cagttcatgt atggcagccg tgcgtttacc
     3481 aaacacccgg cggacattcc ggattactat aagcaaagct tcccggaagg ttttaaatgg
     3541 gagcgtgtta tgaacttcga agatggtggc gcggtgaccg ttacccagga caccagcctg
     3601 gaggatggca ccctgattta caaggtgaaa ctgcgtggca ccaactttcc gccggatggt
     3661 ccggttatgc agaagaaaac gatgggttgg gaagcgagca ccgagcgtct gtatccggaa
     3721 gatggcgtgc tgaagggtga tatcaaaatg gcgctgcgtc tgaaggacgg tggccgttac
     3781 ctggcggatt ttaagaccac ctataaagcg aagaaaccgg tgcaaatgcc gggtgcgtac
     3841 aacgttgacc gtaaactgga tattaccagc cacaacgagg attataccgt ggttgagcaa
     3901 tatgagcgta gcgagggtcg ccacagcacc ggcggcatgg acgaactgta taagggatcc
     3961 taataacgct gatagtgcta gtgtagatcg ctactagagc caggcatcaa ataaaacgaa
     4021 aggctcagtc gaaagactgg gcctttcgtt ttatctgttg tttgtcggtg aacgctctct
     4081 actagagtca cactggctca ccttcgggtg ggcctttctg cgtttatata ctggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and pRO1600/ColE1 origin of replication.",
                    "label": "BASIC_SEVA_34",
                },
                {
                    "accessor": "35",
                    "binaryString": """LOCUS       BASIC_SEVA_35           5843 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            RSF1010 origin of replication..
ACCESSION   e0003a4d55dabf27305128b65167bf44
VERSION     e0003a4d55dabf27305128b65167bf44
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     CDS             4964..5668
                     /label="mScarlett"
     misc_feature    4902..4936
                     /label="J23119"
     misc_feature    1043..4716
                     /label="SEVA_RSF101"
     misc_feature    4945..4956
                     /label="B0034"
     misc_feature    join(5838..5843,1..51)
                     /label="LMP"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    5705..5833
                     /label="B0015"
     misc_feature    187..969
                     /label="SEVA_Cm"
     misc_feature    4845..4901
                     /label="LMS"
     misc_feature    4731..4835
                     /label="SEVA_T1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg cctcagcctg ccgccttggg ccgggtgatg tcgtacttgc
     1081 ccgccgcgaa ctcggttacc gtccagccca gcgcgaccag ctccggcaac gcctcgcgca
     1141 cccgctggcg gcgcttgcgc atggtcgaac cactggcctc tgacggccag acatagccgc
     1201 acaaggtatc tatggaagcc ttgccggttt tgccggggtc gatccagcca cacagccgct
     1261 ggtgcagcag gcgggcggtt tcgctgtcca gcgcccgcac ctcgtccatg ctgatgcgca
     1321 catgctggcc gccacccatg acggcctgcg cgatcaaggg gttcagggcc acgtacaggc
     1381 gcccgtccgc ctcgtcgctg gcgtactccg acagcagccg aaacccctgc cgcttgcggc
     1441 cattctgggc gatgatggat accttccaaa ggcgctcgat gcagtcctgt atgtgcttga
     1501 gcgccccacc actatcgacc tctgccccga tttcctttgc cagcgcccga tagctacctt
     1561 tgaccacatg gcattcagcg gtgacggcct cccacttggg ttccaggaac agccggagct
     1621 gccgtccgcc ttcggtcttg ggttccgggc caagcactag gccattaggc ccagccatgg
     1681 ccaccagccc ttgcaggatg cgcagatcat cagcgcccag cggctccggg ccgctgaact
     1741 cgatccgctt gccgtcgccg tagtcatacg tcacgtccag cttgctgcgc ttgcgctcgc
     1801 cccgcttgag ggcacggaac aggccggggg ccagacagtg cgccgggtcg tgccggacgt
     1861 ggctgaggct gtgcttgttc ttaggcttca ccacggggca cccccttgct cttgcgctgc
     1921 ctctccagca cggcgggctt gagcaccccg ccgtcatgcc gcctgaacca ccgatcagcg
     1981 aacggtgcgc catagttggc cttgctcaca ccgaagcgga cgaagaaccg gcgctggtcg
     2041 tcgtccacac cccattcctc ggcctcggcg ctggtcatgc tcgacaggta ggactgccag
     2101 cggatgttat cgaccagtac cgagctgccc cggctggcct gctgctggtc gcctgcgccc
     2161 atcatggccg cgcccttgct ggcatggtgc aggaacacga tagagcaccc ggtatcggcg
     2221 gcgatggcct ccatgcgacc gatgacctgg gccatggggc cgctggcgtt ttcttcctcg
     2281 atgtggaacc ggcgcagcgt gtccagcacc atcaggcggc ggccctcggc ggcgcgcttg
     2341 aggccgtcga accactccgg ggccatgatg ttgggcaggc tgccgatcag cggctggatc
     2401 agcaggccgt cagccacggc ttgccgttcc tcggcgctga ggtgcgcccc aagggcgtgc
     2461 aggcggtgat gaatggcggt gggcgggtct tcggcgggca ggtagatcac cgggccggtg
     2521 ggcagttcgc ccacctccag cagatccggc ccgcctgcaa tctgtgcggc cagttgcagg
     2581 gccagcatgg atttaccggc accaccgggc gacaccagcg ccccgaccgt accggccacc
     2641 atgttgggca aaacgtagtc cagcggtggc ggcgctgctg cgaacgcctc cagaatattg
     2701 ataggcttat gggtagccat tgattgcctc ctttgcaggc agttggtggt taggcgctgg
     2761 cggggtcact acccccgccc tgcgccgctc tgagttcttc caggcactcg cgcagcgcct
     2821 cgtattcgtc gtcggtcagc cagaacttgc gctgacgcat ccctttggcc ttcatgcgct
     2881 cggcatatcg cgcttggcgt acagcgtcag ggctggccag caggtcgccg gtctgcttgt
     2941 ccttttggtc tttcatatca gtcaccgaga aacttgccgg ggccgaaagg cttgtcttcg
     3001 cggaacaagg acaaggtgca gccgtcaagg ttaaggctgg ccatatcagc gactgaaaag
     3061 cggccagcct cggccttgtt tgacgtataa ccaaagccac cgggcaacca atagcccttg
     3121 tcacttttga tcaggtagac cgaccctgaa gcgctttttt cgtattccat aaaaccccct
     3181 tctgtgcgtg agtactcata gtataacagg cgtgagtacc aacgcaagca ctacatgctg
     3241 aaatctggcc cgcccctgtc catgcctcgc tggcggggtg ccggtgcccg tgccagctcg
     3301 gcccgcgcaa gctggacgct gggcagaccc atgaccttgc tgacggtgcg ctcgatgtaa
     3361 tccgcttcgt ggccgggctt gcgctctgcc agcgctgggc tggcctcggc catggccttg
     3421 ccgatttcct cggcactgcg gccccggctg gccagcttct gcgcggcgat aaagtcgcac
     3481 ttgctgaggt catcaccgaa gcgcttgacc agcccggcca tctcgctgcg gtactcgtcc
     3541 agcgccgtgc gccggtggcg gctaagctgc cgctcgggca gttcgaggct ggccagcctg
     3601 cgggccttct cctgctgccg ctgggcctgc tcgatctgct ggccagcctg ctgcaccagc
     3661 gccgggccag cggtggcggt cttgcccttg gattcacgca gcagcaccca cggctgataa
     3721 ccggcgcggg tggtgtgctt gtccttgcgg ttggtgaagc ccgccaagcg gccatagtgg
     3781 cggctgtcgg cgctggccgg gtcggcgtcg tactcgctgg ccagcgtccg ggcaatctgc
     3841 ccccgaagtt caccgcctgc ggcgtcggcc accttgaccc atgcctgata gttcttcggg
     3901 ctggtttcca ctaccagggc aggctcccgg ccctcggctt tcatgtcatc caggtcaaac
     3961 tcgctgaggt cgtccaccag caccagacca tgccgctcct gctcggcggg cctgatatac
     4021 acgtcattgc cctgggcatt catccgcttg agccatggcg tgttctggag cacttcggcg
     4081 gctgaccatt cccggttcat catctggccg gtggtggcgt ccctgacgcc gatatcgaag
     4141 cgctcacagc ccatggcctt gagctgtcgg cctatggcct gcaaagtcct gtcgttcttc
     4201 atcgggccac caagcgattc ccacacatta tacgagccgg aagcataaag tgtaaagcct
     4261 agatccgaag gatgagccgg gctgaatgat cgaccgagac aggccctgcg gggctgcaca
     4321 cgcgccccca cccttcgggt agggggaaag gccgctaaag cggctaaaag cgctccagcg
     4381 tatttctgcg gggtttggtg tggggtttag cgggctttgc ccgcctttcc ccctgccgcg
     4441 cagcggtggg gcggtgtgta gcctagcgca gcgaatagac cagctatccg gcctctggcc
     4501 gggcatattg ggcaagggca gcagcgcccc acaagggcgc tgataaccgc gcctagtgga
     4561 ttattcttag ataatcatgg atggattttt ccaacacccc gccagccccc gcccctgctg
     4621 ggtttgcagg tttgggggcg tgacagttat tgcaggggtt cgtgacagtt attgcagggg
     4681 ggcgtgacag ttattgcagg ggttcgtgac agttagggcg cgcccagctg tctagggcgg
     4741 cggatttgtc ctactcagga gagcgttcac cgacaaacaa cagataaaac gaaaggccca
     4801 gtctttcgac tgagcctttc gttttatttg atgcctttaa ttaaggctcg ggagacctat
     4861 cggtaataac agtccaatct ggtgtaactt cggaatcgtc cttgacagct agctcagtcc
     4921 taggtataat gctagctact agtgaaagag gagaaatact agtatggtta gcaaaggcga
     4981 ggcggttatc aaggagttta tgcgttttaa ggttcacatg gagggtagca tgaatggtca
     5041 cgagttcgag atcgagggtg aaggcgaggg tcgtccgtac gaaggcaccc agaccgcgaa
     5101 gctgaaagtg accaagggtg gcccgctgcc gttcagctgg gacatcctga gcccgcagtt
     5161 catgtatggc agccgtgcgt ttaccaaaca cccggcggac attccggatt actataagca
     5221 aagcttcccg gaaggtttta aatgggagcg tgttatgaac ttcgaagatg gtggcgcggt
     5281 gaccgttacc caggacacca gcctggagga tggcaccctg atttacaagg tgaaactgcg
     5341 tggcaccaac tttccgccgg atggtccggt tatgcagaag aaaacgatgg gttgggaagc
     5401 gagcaccgag cgtctgtatc cggaagatgg cgtgctgaag ggtgatatca aaatggcgct
     5461 gcgtctgaag gacggtggcc gttacctggc ggattttaag accacctata aagcgaagaa
     5521 accggtgcaa atgccgggtg cgtacaacgt tgaccgtaaa ctggatatta ccagccacaa
     5581 cgaggattat accgtggttg agcaatatga gcgtagcgag ggtcgccaca gcaccggcgg
     5641 catggacgaa ctgtataagg gatcctaata acgctgatag tgctagtgta gatcgctact
     5701 agagccaggc atcaaataaa acgaaaggct cagtcgaaag actgggcctt tcgttttatc
     5761 tgttgtttgt cggtgaacgc tctctactag agtcacactg gctcaccttc gggtgggcct
     5821 ttctgcgttt atatactggc tcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and RSF1010 origin of replication.",
                    "label": "BASIC_SEVA_35",
                },
                {
                    "accessor": "36",
                    "binaryString": """LOCUS       BASIC_SEVA_36           2901 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            p15A origin of replication..
ACCESSION   817f6b5c8cecf3151314b28b98a2a2e3
VERSION     817f6b5c8cecf3151314b28b98a2a2e3
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    1043..1774
                     /label="SEVA_p15A"
     CDS             2022..2726
                     /label="mScarlett"
     misc_feature    187..969
                     /label="SEVA_Cm"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2003..2014
                     /label="B0034"
     misc_feature    1789..1893
                     /label="SEVA_T1"
     misc_feature    1960..1994
                     /label="J23119"
     misc_feature    1903..1959
                     /label="LMS"
     misc_feature    2763..2891
                     /label="B0015"
     misc_feature    join(2896..2901,1..51)
                     /label="LMP"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg ccctagaaat attttatctg attaataaga tgatcttctt
     1081 gagatcgttt tggtctgcgc gtaatctctt gctctgaaaa cgaaaaaacc gccttgcagg
     1141 gcggtttttc gaaggttctc tgagctacca actctttgaa ccgaggtaac tggcttggag
     1201 gagcgcagtc accaaaactt gtcctttcag tttagcctta accggcgcat gacttcaaga
     1261 ctaactcctc taaatcaatt accagtggct gctgccagtg gtgcttttgc atgtctttcc
     1321 gggttggact caagacgata gttaccggat aaggcgcagc ggtcggactg aacggggggt
     1381 tcgtgcatac agtccagctt ggagcgaact gcctacccgg aactgagtgt caggcgtgga
     1441 atgagacaaa cgcggccata acagcggaat gacaccggta aaccgaaagg caggaacagg
     1501 agagcgcacg agggagccgc cagggggaaa cgcctggtat ctttatagtc ctgtcgggtt
     1561 tcgccaccac tgatttgagc gtcagatttc gtgatgcttg tcaggggggc ggagcctatg
     1621 gaaaaacggc tttgccgcgg ccctctcact tccctgttaa gtatcttcct ggcatcttcc
     1681 aggaaatctc cgccccgttc gtaagccatt tccgctcgcc gcagtcgaac gaccgagcgt
     1741 agcgagtcag tgagcgagga agcggaatat atccggcgcg cccagctgtc tagggcggcg
     1801 gatttgtcct actcaggaga gcgttcaccg acaaacaaca gataaaacga aaggcccagt
     1861 ctttcgactg agcctttcgt tttatttgat gcctttaatt aaggctcggg agacctatcg
     1921 gtaataacag tccaatctgg tgtaacttcg gaatcgtcct tgacagctag ctcagtccta
     1981 ggtataatgc tagctactag tgaaagagga gaaatactag tatggttagc aaaggcgagg
     2041 cggttatcaa ggagtttatg cgttttaagg ttcacatgga gggtagcatg aatggtcacg
     2101 agttcgagat cgagggtgaa ggcgagggtc gtccgtacga aggcacccag accgcgaagc
     2161 tgaaagtgac caagggtggc ccgctgccgt tcagctggga catcctgagc ccgcagttca
     2221 tgtatggcag ccgtgcgttt accaaacacc cggcggacat tccggattac tataagcaaa
     2281 gcttcccgga aggttttaaa tgggagcgtg ttatgaactt cgaagatggt ggcgcggtga
     2341 ccgttaccca ggacaccagc ctggaggatg gcaccctgat ttacaaggtg aaactgcgtg
     2401 gcaccaactt tccgccggat ggtccggtta tgcagaagaa aacgatgggt tgggaagcga
     2461 gcaccgagcg tctgtatccg gaagatggcg tgctgaaggg tgatatcaaa atggcgctgc
     2521 gtctgaagga cggtggccgt tacctggcgg attttaagac cacctataaa gcgaagaaac
     2581 cggtgcaaat gccgggtgcg tacaacgttg accgtaaact ggatattacc agccacaacg
     2641 aggattatac cgtggttgag caatatgagc gtagcgaggg tcgccacagc accggcggca
     2701 tggacgaact gtataaggga tcctaataac gctgatagtg ctagtgtaga tcgctactag
     2761 agccaggcat caaataaaac gaaaggctca gtcgaaagac tgggcctttc gttttatctg
     2821 ttgtttgtcg gtgaacgctc tctactagag tcacactggc tcaccttcgg gtgggccttt
     2881 ctgcgtttat atactggctc g
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and p15A origin of replication.",
                    "label": "BASIC_SEVA_36",
                },
                {
                    "accessor": "37",
                    "binaryString": """LOCUS       BASIC_SEVA_37           3825 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            pSC101 origin of replication..
ACCESSION   58617d197d0335ce9ace1bb3a0402c30
VERSION     58617d197d0335ce9ace1bb3a0402c30
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     CDS             2946..3650
                     /label="mScarlett"
     misc_feature    join(3820..3825,1..51)
                     /label="LMP"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3687..3815
                     /label="B0015"
     misc_feature    2780..2814
                     /label="J23119"
     misc_feature    2631..2687
                     /label="LMS"
     misc_feature    2517..2621
                     /label="SEVA_T1"
     misc_feature    1043..2502
                     /label="SEVA_pSC101"
     misc_feature    187..969
                     /label="SEVA_Cm"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg cctcagatcc ttccgtattt agccagtatg ttctctagtg
     1081 tggttcgttg tttttgcgtg agccatgaga acgaaccatt gagatcatac ttactttgca
     1141 tgtcactcaa aaattttgcc tcaaaactgg tgagctgaat ttttgcagtt aaagcatcgt
     1201 gtagtgtttt tcttagtccg ttatgtaggt aggaatctga tgtaatggtt gttggtattt
     1261 tgtcaccatt catttttatc tggttgttct caagttcggt tacgagatcc atttgtctat
     1321 ctagttcaac ttggaaaatc aacgtatcag tcgggcggcc tcgcttatca accaccaatt
     1381 tcatattgct gtaagtgttt aaatctttac ttattggttt caaaacccat tggttaagcc
     1441 ttttaaactc atggtagtta ttttcaagca ttaacatgaa cttaaattca tcaaggctaa
     1501 tctctatatt tgccttgtga gttttctttt gtgttagttc ttttaataac cactcataaa
     1561 tcctcataga gtatttgttt tcaaaagact taacatgttc cagattatat tttatgaatt
     1621 tttttaactg gaaaagataa ggcaatatct cttcactaaa aactaattct aatttttcgc
     1681 ttgagaactt ggcatagttt gtccactgga aaatctcaaa gcctttaacc aaaggattcc
     1741 tgatttccac agttctcgtc atcagctctc tggttgcttt agctaataca ccataagcat
     1801 tttccctact gatgttcatc atctgagcgt attggttata agtgaacgat accgtccgtt
     1861 ctttccttgt agggttttca atcgtggggt tgagtagtgc cacacagcat aaaattagct
     1921 tggtttcatg ctccgttaag tcatagcgac taatcgctag ttcatttgct ttgaaaacaa
     1981 ctaattcaga catacatctc aattggtcta ggtgatttta atcactatac caattgagat
     2041 gggctagtca atgataatta catgtccttt tcctttgagt tgtgggtatc tgtaaattct
     2101 gctagacctt tgctggaaaa cttgtaaatt ctgctagacc ctctgtaaat tccgctagac
     2161 ctttgtgtgt tttttttgtt tatattcaag tggttataat ttatagaata aagaaagaat
     2221 aaaaaaagat aaaaagaata gatcccagcc ctgtgtataa ctcactactt tagtcagttc
     2281 cgcagtatta caaaaggatg tcgcaaacgc tgtttgctcc tctacaaaac agaccttaaa
     2341 accctaaagg cttaagtagc accctcgcaa gctcgggcaa atcgctgaat attccttttg
     2401 tctccgacca tcaggcacct gagtcgctgt ctttttcgtg acattcagtt cgctgcgctc
     2461 acggctctgg cagtgaatgg gggtaaatgg cactacaggc gcggcgcgcc cagctgtcta
     2521 gggcggcgga tttgtcctac tcaggagagc gttcaccgac aaacaacaga taaaacgaaa
     2581 ggcccagtct ttcgactgag cctttcgttt tatttgatgc ctttaattaa ggctcgggag
     2641 acctatcggt aataacagtc caatctggtg taacttcgga atcgtcccca attattgaac
     2701 acccttcggg gtgttttttt gtttctggtc taccatctcg ttgtgataat agacctgaag
     2761 tgcctactct ggaaaatctt tgacagctag ctcagtccta ggtataatgc tagcagctgt
     2821 caccggatgt gctttccggt ctgatgagtc cgtgaggacg aaacagcctc tacaaataat
     2881 tttgtttaag gctcgctacg agaagattgt tactttcgca gcgttattat ctaaggaggt
     2941 agtccatggt tagcaaaggc gaggcggtta tcaaggagtt tatgcgtttt aaggttcaca
     3001 tggagggtag catgaatggt cacgagttcg agatcgaggg tgaaggcgag ggtcgtccgt
     3061 acgaaggcac ccagaccgcg aagctgaaag tgaccaaggg tggcccgctg ccgttcagct
     3121 gggacatcct gagcccgcag ttcatgtatg gcagccgtgc gtttaccaaa cacccggcgg
     3181 acattccgga ttactataag caaagcttcc cggaaggttt taaatgggag cgtgttatga
     3241 acttcgaaga tggtggcgcg gtgaccgtta cccaggacac cagcctggag gatggcaccc
     3301 tgatttacaa ggtgaaactg cgtggcacca actttccgcc ggatggtccg gttatgcaga
     3361 agaaaacgat gggttgggaa gcgagcaccg agcgtctgta tccggaagat ggcgtgctga
     3421 agggtgatat caaaatggcg ctgcgtctga aggacggtgg ccgttacctg gcggatttta
     3481 agaccaccta taaagcgaag aaaccggtgc aaatgccggg tgcgtacaac gttgaccgta
     3541 aactggatat taccagccac aacgaggatt ataccgtggt tgagcaatat gagcgtagcg
     3601 agggtcgcca cagcaccggc ggcatggacg aactgtataa gggatcctaa taacgctgat
     3661 agtgctagtg tagatcgcta ctagagccag gcatcaaata aaacgaaagg ctcagtcgaa
     3721 agactgggcc tttcgtttta tctgttgttt gtcggtgaac gctctctact agagtcacac
     3781 tggctcacct tcgggtgggc ctttctgcgt ttatatactg gctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and pSC101 origin of replication.",
                    "label": "BASIC_SEVA_37",
                },
                {
                    "accessor": "38",
                    "binaryString": """LOCUS       BASIC_SEVA_38           3098 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            pUC origin of replication..
ACCESSION   dcf87eb4a87a61d8963500c2c5b854b4
VERSION     dcf87eb4a87a61d8963500c2c5b854b4
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    1986..2090
                     /label="SEVA_T1"
     misc_feature    join(3093..3098,1..51)
                     /label="LMP"
     misc_feature    2200..2211
                     /label="B0034"
     misc_feature    187..969
                     /label="SEVA_Cm"
     CDS             2219..2923
                     /label="mScarlett"
     misc_feature    2157..2191
                     /label="J23106"
     misc_feature    2100..2156
                     /label="LMS"
     misc_feature    1043..1971
                     /label="SEVA_pUC"
     misc_feature    2960..3088
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg ccccgtagaa aagatcaaag gatcttcttg agatcctttt
     1081 tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac cgctaccagc ggtggtttgt
     1141 ttgccggatc aagagctacc aactcttttt ccgaaggtaa ctggcttcag cagagcgcag
     1201 ataccaaata ctgttcttct agtgtagccg tagttaggcc accacttcaa gaactctgta
     1261 gcaccgccta catacctcgc tctgctaatc ctgttaccag tggctgctgc cagtggcgat
     1321 aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac cggataaggc gcagcggtcg
     1381 ggctgaacgg ggggttcgtg cacacagccc agcttggagc gaacgaccta caccgaactg
     1441 agatacctac agcgtgagct ttgagaaagc gccacgcttc ccgaagggag aaaggcggac
     1501 aggtatccgg taagcggcag ggtcggaaca ggagagcgca cgagggagct tccaggggga
     1561 aacgcctggt atctttatag tcctgtcggg tttcgccacc tctgacttga gcgtcgattt
     1621 ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg ccagcaacgc ggccttttta
     1681 cggttcctgg ccttttgctg gccttttgct cacatgttct ttcctgcgtt atcccctgat
     1741 tctgtggata accgtattac cgcctttgag tgagctgata ccgctcgccg cagccgaacg
     1801 accgagcgca gcgagtcagt gagcgaggaa gcggaagagc gcccaatacg caaaccgcct
     1861 ctccccgcgc gttggccgat tcattaatgc agctggcacg acaggtttcc cgactggaaa
     1921 gcgggcagtg agcgcaacgc aattaatgtg agttagctca ctcattaggc aggcgcgccc
     1981 agctgtctag ggcggcggat ttgtcctact caggagagcg ttcaccgaca aacaacagat
     2041 aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt atttgatgcc tttaattaag
     2101 gctcgggaga cctatcggta ataacagtcc aatctggtgt aacttcggaa tcgtccttta
     2161 cggctagctc agtcctaggt atagtgctag ctactagtga aagaggagaa atactagtat
     2221 ggttagcaaa ggcgaggcgg ttatcaagga gtttatgcgt tttaaggttc acatggaggg
     2281 tagcatgaat ggtcacgagt tcgagatcga gggtgaaggc gagggtcgtc cgtacgaagg
     2341 cacccagacc gcgaagctga aagtgaccaa gggtggcccg ctgccgttca gctgggacat
     2401 cctgagcccg cagttcatgt atggcagccg tgcgtttacc aaacacccgg cggacattcc
     2461 ggattactat aagcaaagct tcccggaagg ttttaaatgg gagcgtgtta tgaacttcga
     2521 agatggtggc gcggtgaccg ttacccagga caccagcctg gaggatggca ccctgattta
     2581 caaggtgaaa ctgcgtggca ccaactttcc gccggatggt ccggttatgc agaagaaaac
     2641 gatgggttgg gaagcgagca ccgagcgtct gtatccggaa gatggcgtgc tgaagggtga
     2701 tatcaaaatg gcgctgcgtc tgaaggacgg tggccgttac ctggcggatt ttaagaccac
     2761 ctataaagcg aagaaaccgg tgcaaatgcc gggtgcgtac aacgttgacc gtaaactgga
     2821 tattaccagc cacaacgagg attataccgt ggttgagcaa tatgagcgta gcgagggtcg
     2881 ccacagcacc ggcggcatgg acgaactgta taagggatcc taataacgct gatagtgcta
     2941 gtgtagatcg ctactagagc caggcatcaa ataaaacgaa aggctcagtc gaaagactgg
     3001 gcctttcgtt ttatctgttg tttgtcggtg aacgctctct actagagtca cactggctca
     3061 ccttcgggtg ggcctttctg cgtttatata ctggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and pUC origin of replication.",
                    "label": "BASIC_SEVA_38",
                },
                {
                    "accessor": "39",
                    "binaryString": """LOCUS       BASIC_SEVA_39           3554 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Chloramphenicol resistance marker and
            pBR322-ROP origin of replication..
ACCESSION   3d2aca52c1ccb2400dd9ca26546e5b40
VERSION     3d2aca52c1ccb2400dd9ca26546e5b40
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    join(3549..3554,1..51)
                     /label="LMP"
     misc_feature    2656..2667
                     /label="B0034"
     misc_feature    1043..2427
                     /label="SEVA_pBR322-ROP"
     CDS             2675..3379
                     /label="mScarlett"
     misc_feature    3416..3544
                     /label="B0015"
     misc_feature    2442..2546
                     /label="SEVA_T1"
     misc_feature    2613..2647
                     /label="J23119"
     misc_feature    187..969
                     /label="SEVA_Cm"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2556..2612
                     /label="LMS"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaattggc gaaaatgaga cgttgatcgg cacgtaagag gttccaactt tcaccataat
      241 gaaataagat cactaccggg cgtatttttt gagttatcga gattttcagg agctaaggaa
      301 gctaaaatgg agaaaaaaat cactggatat accaccgttg atatatccca atggcatcgt
      361 aaagaacatt ttgaggcatt tcagtcagtt gctcaatgta cctataacca gaccgttcag
      421 ctggatatta cggccttttt aaagaccgta aagaaaaata agcacaagtt ttatccggcc
      481 tttattcaca ttcttgcccg cctgatgaat gctcatccgg aatttcgtat ggcaatgaaa
      541 gacggtgagc tggtgatatg ggatagtgtt cacccttgtt acaccgtttt ccatgagcaa
      601 actgaaacgt tttcatcgct ctggagtgaa taccacgacg atttccggca gtttctacac
      661 atatattcgc aagatgtggc gtgttacggt gaaaacctgg cctatttccc taaagggttt
      721 attgagaata tgtttttcgt ctcagccaat ccctgggtga gtttcaccag ttttgattta
      781 aacgtggcca atatggacaa cttcttcgcc cccgttttca ccatgggcaa atattatacg
      841 caaggcgaca aggtgctgat gccgctggcg attcaggttc atcatgccgt ttgtgatggc
      901 ttccatgtcg gcagaatgct taatgaatta caacagtact gcgatgagtg gcagggcggg
      961 gcgtaatttg acttttgtcg gctcgaccca cgactattga ctgctctgag aaagttgatt
     1021 gttacgatta gtccggccgg ccccgtagaa aagatcaaag gatcttcttg agatcctttt
     1081 tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac cgctaccagc ggtggtttgt
     1141 ttgccggatc aagagctacc aactcttttt ccgaaggtaa ctggcttcag cagagcgcag
     1201 ataccaaata ctgtccttct agtgtagccg tagttaggcc accacttcaa gaactctgta
     1261 gcaccgccta catacctcgc tctgctaatc ctgttaccag tggctgctgc cagtggcgat
     1321 aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac cggataaggc gcagcggtcg
     1381 ggctgaacgg ggggttcgtg cacacagccc agcttggagc gaacgaccta caccgaactg
     1441 agatacctac agcgtgagct atgagaaagc gccacgcttc ccgaagggag aaaggcggac
     1501 aggtatccgg taagcggcag ggtcggaaca ggagagcgca cgagggagct tccaggggga
     1561 aacgcctggt atctttatag tcctgtcggg tttcgccacc tctgacttga gcgtcgattt
     1621 ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg ccagcaacgc ggccttttta
     1681 cggttcctgg ccttttgctg gccttttgct cacatgttct ttcctgcgtt atcccctgat
     1741 tctgtggata accgtattac cgcctttgag tgagctgata ccgctcgccg cagccgaacg
     1801 accgagcgca gcgagtcagt gagcgaggaa gcggaagagc gcctgatgcg gtattttctc
     1861 cttacgcatc tgtgcggtat ttcacaccgc atatggtgca ctctcagtac aatctgctct
     1921 gatgccgcat agttaagcca gtatacactc cgctatcgct acgtgactgg gtcatggctg
     1981 cgccccgaca cccgccaaca cccgctgacg cgccctgacg ggcttgtctg ctcccggcat
     2041 ccgcttacag acaagctgtg accgtctccg ggagctgcat gtgtcagagg ttttcaccgt
     2101 catcaccgaa acgcgcgagg cagctgcggt aaagctcatc agcgtggtcg tgcagcgatt
     2161 cacagatgtc tgcctgttca tccgcgtcca gctcgttgag tttctccaga agcgttaatg
     2221 tctggcttct gataaagcgg gccatgttaa gggcggtttt ttcctgtttg gtcactgatg
     2281 cctccgtgta agggggattt ctgttcatgg gggtaatgat accgatgaaa cgagagagga
     2341 tgctcacgat acgggttact gatgatgaac atgcccggtt actggaacgt tgtgagggta
     2401 aacaactggc ggtatggatg cggcgggggc gcgcccagct gtctagggcg gcggatttgt
     2461 cctactcagg agagcgttca ccgacaaaca acagataaaa cgaaaggccc agtctttcga
     2521 ctgagccttt cgttttattt gatgccttta attaaggctc gggagaccta tcggtaataa
     2581 cagtccaatc tggtgtaact tcggaatcgt ccttgacagc tagctcagtc ctaggtataa
     2641 tgctagctac tagtgaaaga ggagaaatac tagtatggtt agcaaaggcg aggcggttat
     2701 caaggagttt atgcgtttta aggttcacat ggagggtagc atgaatggtc acgagttcga
     2761 gatcgagggt gaaggcgagg gtcgtccgta cgaaggcacc cagaccgcga agctgaaagt
     2821 gaccaagggt ggcccgctgc cgttcagctg ggacatcctg agcccgcagt tcatgtatgg
     2881 cagccgtgcg tttaccaaac acccggcgga cattccggat tactataagc aaagcttccc
     2941 ggaaggtttt aaatgggagc gtgttatgaa cttcgaagat ggtggcgcgg tgaccgttac
     3001 ccaggacacc agcctggagg atggcaccct gatttacaag gtgaaactgc gtggcaccaa
     3061 ctttccgccg gatggtccgg ttatgcagaa gaaaacgatg ggttgggaag cgagcaccga
     3121 gcgtctgtat ccggaagatg gcgtgctgaa gggtgatatc aaaatggcgc tgcgtctgaa
     3181 ggacggtggc cgttacctgg cggattttaa gaccacctat aaagcgaaga aaccggtgca
     3241 aatgccgggt gcgtacaacg ttgaccgtaa actggatatt accagccaca acgaggatta
     3301 taccgtggtt gagcaatatg agcgtagcga gggtcgccac agcaccggcg gcatggacga
     3361 actgtataag ggatcctaat aacgctgata gtgctagtgt agatcgctac tagagccagg
     3421 catcaaataa aacgaaaggc tcagtcgaaa gactgggcct ttcgttttat ctgttgtttg
     3481 tcggtgaacg ctctctacta gagtcacact ggctcacctt cgggtgggcc tttctgcgtt
     3541 tatatactgg ctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Chloramphenicol resistance marker and pBR322-ROP origin of replication.",
                    "label": "BASIC_SEVA_39",
                },
                {
                    "accessor": "42",
                    "binaryString": """LOCUS       BASIC_SEVA_42           4801 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and RK2
            origin of replication..
ACCESSION   7c8d98d5b6b2effbc1c68261c8afdd63
VERSION     7c8d98d5b6b2effbc1c68261c8afdd63
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    1257..3478
                     /label="SEVA_RK2"
     misc_feature    4663..4791
                     /label="B0015"
     misc_feature    3756..3790
                     /label="J23119"
     misc_feature    3607..3663
                     /label="LMS"
     misc_feature    3493..3597
                     /label="SEVA_T1"
     CDS             3922..4626
                     /label="mScarlett"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
     misc_feature    join(4796..4801,1..51)
                     /label="LMP"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccgcga
     1261 tgcaggtggc tgctgaaccc ccagccggaa ctgaccccac aaggccctag cgtttgcaat
     1321 gcaccaggtc atcattgacc caggcgtgtt ccaccaggcc gctgcctcgc aactcttcgc
     1381 aggcttcgcc gacctgctcg cgccacttct tcacgcgggt ggaatccgat ccgcacatga
     1441 ggcggaaggt ttccagcttg agcgggtacg gctcccggtg cgagctgaaa tagtcgaaca
     1501 tccgtcgggc cgtcggcgac agcttgcggt acttctccca tatgaatttc gtgtagtggt
     1561 cgccagcaaa cagcacgacg atttcctcgt cgatcaggac ctggcaacgg gacgttttct
     1621 tgccacggtc caggacgcgg aagcggtgca gcagcgacac cgattccagg tgcccaacgc
     1681 ggtcggacgt gaagcccatc gccgtcgcct gtaggcgcga caggcattcc tcggccttcg
     1741 tgtaataccg gccattgatc gaccagccca ggtcctggca aagctcgtag aacgtgaagg
     1801 tgatcggctc gccgataggg gtgcgcttcg cgtactccaa cacctgctgc cacaccagtt
     1861 cgtcatcgtc ggcccgcagc tcgacgccgg tgtaggtgat cttcacgtcc ttgttgacgt
     1921 ggaaaatgac cttgttttgc agcgcctcgc gcgggatttt cttgttgcgc gtggtgaaca
     1981 gggcagagcg ggccgtgtcg tttggcatcg ctcgcatcgt gtccggccac ggcgcaatat
     2041 cgaacaagga aagctgcatt tccttgatct gctgcttcgt gtgtttcagc aacgcggcct
     2101 gcttggcttc gctgacctgt tttgccaggt cctcgccggc ggtttttcgc ttcttggtcg
     2161 tcatagttcc tcgcgtgtcg atggtcatcg acttcgccaa acctgccgcc tcctgttcga
     2221 gacgacgcga acgctccacg gcggccgatg gcgcgggcag ggcaggggga gccagttgca
     2281 cgctgtcgcg ctcgatcttg gccgtagctt gctggactat cgagccgacg gactggaagg
     2341 tttcgcgggg cgcacgcatg acggtgcggc ttgcgatggt ttcggcatcc tcggcggaaa
     2401 accccgcgtc gatcagttct tgcctgtatg ccttccggtc aaacgtccga ttcattcacc
     2461 ctccttgcgg gattgccccg gaattaattc cccggatcga tccgtcgatc ttgatcccct
     2521 gcgccatcag atccttggcg gcaagaaagc catccagttt actttgcagg gcttcccaac
     2581 cttaccagag ggcgccccag ctggcaattc cggttcgctt gctgtccata aaaccgccca
     2641 gtctagctat cgccatgtaa gcccactgca agctacctgc tttctctttg cgcttgcgtt
     2701 ttcccttgtc cagatagccc agtagctgac attcatccgg ggtcagcacc gtttctgcgg
     2761 actggctttc tacgtggctg ccatttttgg ggtgaggccg ttcgcggccg aggggcgcag
     2821 cccctggggg gatgggaggc ccgcgttagc gggccgggag ggttcgagaa gggggggcac
     2881 cccccttcgg cgtgcgcggt cacgcgcaca gggcgcagcc ctggttaaaa acaaggttta
     2941 taaatattgg tttaaaagca ggttaaaaga caggttagcg gtggccgaaa aacgggcgga
     3001 aacccttgca aatgctggat tttctgcctg tggacagccc ctcaaatgtc aataggtgcg
     3061 cccctcatct gtcagcactc tgcccctcaa gtgtcaagga tcgcgcccct catctgtcag
     3121 tagtcgcgcc cctcaagtgt caataccgca gggcacttat ccccaggctt gtccacatca
     3181 tctgtgggaa actcgcgtaa aatcaggcgt tttcgccgat ttgcgaggct ggccagctcc
     3241 acgtcgccgg ccgaaatcga gcctgcccct catctgtcaa cgccgcgccg ggtgagtcgg
     3301 cccctcaagt gtcaacgtcc gcccctcatc tgtcagtgag ggccaagttt tccgcgaggt
     3361 atccacaacg ccggcggccc tacatggctc tgctgtagtg agtgggttgc gctccggcag
     3421 cggtcctgat cccccgcaga aaaaaaggat ctcaagaaga tcctttgatc ttttctacgg
     3481 cgcgcccagc tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac
     3541 aacagataaa acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt
     3601 aattaaggct cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg
     3661 tccccaatta ttgaacaccc ttcggggtgt ttttttgttt ctggtctacc atctcgttgt
     3721 gataatagac ctgaagtgcc tactctggaa aatctttgac agctagctca gtcctaggta
     3781 taatgctagc agctgtcacc ggatgtgctt tccggtctga tgagtccgtg aggacgaaac
     3841 agcctctaca aataattttg tttaaggctc gctacgagaa gattgttact ttcgcagcgt
     3901 tattatctaa ggaggtagtc catggttagc aaaggcgagg cggttatcaa ggagtttatg
     3961 cgttttaagg ttcacatgga gggtagcatg aatggtcacg agttcgagat cgagggtgaa
     4021 ggcgagggtc gtccgtacga aggcacccag accgcgaagc tgaaagtgac caagggtggc
     4081 ccgctgccgt tcagctggga catcctgagc ccgcagttca tgtatggcag ccgtgcgttt
     4141 accaaacacc cggcggacat tccggattac tataagcaaa gcttcccgga aggttttaaa
     4201 tgggagcgtg ttatgaactt cgaagatggt ggcgcggtga ccgttaccca ggacaccagc
     4261 ctggaggatg gcaccctgat ttacaaggtg aaactgcgtg gcaccaactt tccgccggat
     4321 ggtccggtta tgcagaagaa aacgatgggt tgggaagcga gcaccgagcg tctgtatccg
     4381 gaagatggcg tgctgaaggg tgatatcaaa atggcgctgc gtctgaagga cggtggccgt
     4441 tacctggcgg attttaagac cacctataaa gcgaagaaac cggtgcaaat gccgggtgcg
     4501 tacaacgttg accgtaaact ggatattacc agccacaacg aggattatac cgtggttgag
     4561 caatatgagc gtagcgaggg tcgccacagc accggcggca tggacgaact gtataaggga
     4621 tcctaataac gctgatagtg ctagtgtaga tcgctactag agccaggcat caaataaaac
     4681 gaaaggctca gtcgaaagac tgggcctttc gttttatctg ttgtttgtcg gtgaacgctc
     4741 tctactagag tcacactggc tcaccttcgg gtgggccttt ctgcgtttat atactggctc
     4801 g
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and RK2 origin of replication.",
                    "label": "BASIC_SEVA_42",
                },
                {
                    "accessor": "43",
                    "binaryString": """LOCUS       BASIC_SEVA_43           4101 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and
            pBBR1 origin of replication..
ACCESSION   1164f71e44b124d61f996b31340de6b0
VERSION     1164f71e44b124d61f996b31340de6b0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2793..2897
                     /label="SEVA_T1"
     misc_feature    2907..2963
                     /label="LMS"
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
     misc_feature    3056..3090
                     /label="J23119"
     misc_feature    3963..4091
                     /label="B0015"
     misc_feature    join(4096..4101,1..51)
                     /label="LMP"
     misc_feature    1257..2778
                     /label="SEVA_pBBR1"
     CDS             3222..3926
                     /label="mScarlett"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccctac
     1261 cggcgcggca gcgttacccg tgtcggcggc tccaacggct cgccatcgtc cagaaaacac
     1321 ggctcatcgg gcatcggcag gcgctgctgc ccgcgccgtt cccattcctc cgtttcggtc
     1381 aaggctggca ggtctggttc catgcccgga atgccgggct ggctgggcgg ctcctcgccg
     1441 gggccggtcg gtagttgctg ctcgcccgga tacagggtcg ggatgcggcg caggtcgcca
     1501 tgccccaaca gcgattcgtc ctggtcgtcg tgatcaacca ccacggcggc actgaacacc
     1561 gacaggcgca actggtcgcg gggctggccc cacgccacgc ggtcattgac cacgtaggcc
     1621 gacacggtgc cggggccgtt gagcttcacg acggagatcc agcgctcggc caccaagtcc
     1681 ttgactgcgt attggaccgt ccgcaaagaa cgtccgatga gcttggaaag tgtcttctgg
     1741 ctgaccacca cggcgttctg gtggcccatc tgcgccacga ggtgatgcag cagcattgcc
     1801 gccgtgggtt tcctcgcaat aagcccggcc cacgcctcat gcgctttgcg ttccgtttgc
     1861 acccagtgac cgggcttgtt cttggcttga atgccgattt ctctggactg cgtggccatg
     1921 cttatctcca tgcggtaggg gtgccgcacg gttgcggcac catgcgcaat cagctgcaac
     1981 ttttcggcag cgcgacaaca attatgcgtt gcgtaaaagt ggcagtcaat tacagatttt
     2041 ctttaaccta cgcaatgagc tattgcgggg ggtgccgcaa tgagctgttg cgtacccccc
     2101 ttttttaagt tgttgatttt taagtctttc gcatttcgcc ctatatctag ttctttggtg
     2161 cccaaagaag ggcacccctg cggggttccc ccacgccttc ggcgcggctc cccctccggc
     2221 aaaaagtggc ccctccgggg cttgttgatc gactgcgcgg ccttcggcct tgcccaaggt
     2281 ggcgctgccc ccttggaacc cccgcactcg ccgccgtgag gctcgggggg caggcgggcg
     2341 ggcttcgccc ttcgactgcc cccactcgca taggcttggg tcgttccagg cgcgtcaagg
     2401 ccaagccgct gcgcggtcgc tgcgcgagcc ttgacccgcc ttccacttgg tgtccaaccg
     2461 gcaagcgaag cgcgcaggcc gcaggccgga ggcttttccc cagagaaaat taaaaaaatt
     2521 gatggggcaa ggccgcaggc cgcgcagttg gagccggtgg gtatgtggtc gaaggctggg
     2581 tagccggtgg gcaatccctg tggtcaagct cgtgggcagg cgcagcctgt ccatcagctt
     2641 gtccagcagg gttgtccacg ggccgagcga agcgagccag ccggtggccg ctcgcggcca
     2701 tcgtccacat atccacgggc tggcaaggga gcgcagcgac cgcgcagggc gaagcccgga
     2761 gagcaagccc gtaggggggg cgcgcccagc tgtctagggc ggcggatttg tcctactcag
     2821 gagagcgttc accgacaaac aacagataaa acgaaaggcc cagtctttcg actgagcctt
     2881 tcgttttatt tgatgccttt aattaaggct cgggagacct atcggtaata acagtccaat
     2941 ctggtgtaac ttcggaatcg tccccaatta ttgaacaccc ttcggggtgt ttttttgttt
     3001 ctggtctacc atctcgttgt gataatagac ctgaagtgcc tactctggaa aatctttgac
     3061 agctagctca gtcctaggta taatgctagc agctgtcacc ggatgtgctt tccggtctga
     3121 tgagtccgtg aggacgaaac agcctctaca aataattttg tttaaggctc gctacgagaa
     3181 gattgttact ttcgcagcgt tattatctaa ggaggtagtc catggttagc aaaggcgagg
     3241 cggttatcaa ggagtttatg cgttttaagg ttcacatgga gggtagcatg aatggtcacg
     3301 agttcgagat cgagggtgaa ggcgagggtc gtccgtacga aggcacccag accgcgaagc
     3361 tgaaagtgac caagggtggc ccgctgccgt tcagctggga catcctgagc ccgcagttca
     3421 tgtatggcag ccgtgcgttt accaaacacc cggcggacat tccggattac tataagcaaa
     3481 gcttcccgga aggttttaaa tgggagcgtg ttatgaactt cgaagatggt ggcgcggtga
     3541 ccgttaccca ggacaccagc ctggaggatg gcaccctgat ttacaaggtg aaactgcgtg
     3601 gcaccaactt tccgccggat ggtccggtta tgcagaagaa aacgatgggt tgggaagcga
     3661 gcaccgagcg tctgtatccg gaagatggcg tgctgaaggg tgatatcaaa atggcgctgc
     3721 gtctgaagga cggtggccgt tacctggcgg attttaagac cacctataaa gcgaagaaac
     3781 cggtgcaaat gccgggtgcg tacaacgttg accgtaaact ggatattacc agccacaacg
     3841 aggattatac cgtggttgag caatatgagc gtagcgaggg tcgccacagc accggcggca
     3901 tggacgaact gtataaggga tcctaataac gctgatagtg ctagtgtaga tcgctactag
     3961 agccaggcat caaataaaac gaaaggctca gtcgaaagac tgggcctttc gttttatctg
     4021 ttgtttgtcg gtgaacgctc tctactagag tcacactggc tcaccttcgg gtgggccttt
     4081 ctgcgtttat atactggctc g
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and pBBR1 origin of replication.",
                    "label": "BASIC_SEVA_43",
                },
                {
                    "accessor": "44",
                    "binaryString": """LOCUS       BASIC_SEVA_44           4352 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and
            pRO1600/ColE1 origin of replication..
ACCESSION   89e355d5c4ac3b3b96310ac1b3cb7412
VERSION     89e355d5c4ac3b3b96310ac1b3cb7412
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     CDS             3473..4177
                     /label="mScarlett"
     misc_feature    3240..3344
                     /label="SEVA_T1"
     misc_feature    3454..3465
                     /label="B0034"
     misc_feature    3411..3445
                     /label="J23105"
     misc_feature    3354..3410
                     /label="LMS"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    join(4347..4352,1..51)
                     /label="LMP"
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
     misc_feature    1257..3225
                     /label="SEVA_pRO1600/ColE1"
     misc_feature    4214..4342
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccgata
     1261 atctcatgac caaaatccct taacgtgagt tttcgttcca ctgagcgtca gaccccgtag
     1321 aaaagatcaa aggatcttct tgagatcctt tttttctgcg cgtaatctgc tgcttgcaaa
     1381 caaaaaaacc accgctacca gcggtggttt gtttgccgga tcaagagcta ccaactcttt
     1441 ttccgaaggt aactggcttc agcagagcgc agataccaaa tactgttctt ctagtgtagc
     1501 cgtagttagg ccaccacttc aagaactctg tagcaccgcc tacatacctc gctctgctaa
     1561 tcctgttacc agtggctgct gccagtggcg ataagtcgtg tcttaccggg ttggactcaa
     1621 gacgatagtt accggataag gcgcagcggt cgggctgaac ggggggttcg tgcacacagc
     1681 ccagcttgga gcgaacgacc tacaccgaac tgagatacct acagcgtgag ctatgagaaa
     1741 gcgccacgct tcccgaaggg agaaaggcgg acaggcatcc ggtaagcggc agggtcggaa
     1801 caggagagcg cacgagggag cttccagggg gaaacgcctg gtatctttat agtcctgtcg
     1861 ggtttcgcca cctctgactt gagcgtcgat ttttgtgatg ctcgtcaggg gggcggagcc
     1921 tatggaaaaa cgccagcaac gcggccgtga aaggcaggcc ggtccgtggt ggccacggcc
     1981 tctaggccag atccagcggc atctgggtta gtcgagcgcg ggccgcttcc catgtctcac
     2041 cagggcgagc ctgtttcgcg atctcagcat ctgaaatctt cccggccttg cgcttcgctg
     2101 gggccttacc caccgccttg gcgggcttct tcggtccaaa actgaacaac agatgtgtga
     2161 ccttgcgccc ggtctttcgc tgcgcccact ccacctgtag cgggctgtgc tcgttgatct
     2221 gcgtcacggc tggatcaagc actcgcaact tgaagtcctt gatcgaggga taccggcctt
     2281 ccagttgaaa ccactttcgc agctggtcaa tttctatttc gcgctggccg atgctgtccc
     2341 attgcatgag cagctcgtaa agcctgatcg cgtgggtgct gtccatcttg gccacgtcag
     2401 ccaaggcgta tttggtgaac tgtttggtga gttccgtcag gtacggcagc atgtctttgg
     2461 tgaacctgag ttctacacgg ccctcaccct cccggtagat gattgtttgc acccagccgg
     2521 taatcatcac actcggtctt ttccccttgc cattgggctc ttgggttaac cggacttccc
     2581 gccgtttcag gcgcagggcc gcttctttga gctggttgta ggaagattcg atagggacac
     2641 ccgccatcgt cgctatgtcc tccgccgtca ctgaatacat cacttcatcg gtgacaggct
     2701 cgctcctctt cacctggcta atacaggcca gaacgatccg ctgttcctga acactgaggc
     2761 gatacgcggc ctcgaccagg gcattgcttt tgtaaaccat tgggggtgag gccacgttcg
     2821 acattccttg tgtataaggg gacactgtat ctgcgtccca caatacaaca aatccgtccc
     2881 tttacaacaa caaatccgtc ccttcttaac aacaaatccg tcccttaatg gcaacaaatc
     2941 cgtccctttt taaactctac aggccacgga ttacgtggcc tgtagacgtc ctaaaaggtt
     3001 taaaagggaa aaggaagaaa agggtggaaa cgcaaaaaac gcaccactac gtggccccgt
     3061 tggggccgca tttgtgcccc tgaaggggcg ggggaggcgt ctgggcaatc cccgttttac
     3121 cagtccccta tcgccgcctg agagggcgca ggaagcgagt aatcagggta tcgaggcgga
     3181 ttcacccttg gcgtccaacc agcggcacca gcggcgcctg agaggggcgc gcccagctgt
     3241 ctagggcggc ggatttgtcc tactcaggag agcgttcacc gacaaacaac agataaaacg
     3301 aaaggcccag tctttcgact gagcctttcg ttttatttga tgcctttaat taaggctcgg
     3361 gagacctatc ggtaataaca gtccaatctg gtgtaacttc ggaatcgtcc tttacggcta
     3421 gctcagtcct aggtactatg ctagctacta gtgaaagagg agaaatacta gtatggttag
     3481 caaaggcgag gcggttatca aggagtttat gcgttttaag gttcacatgg agggtagcat
     3541 gaatggtcac gagttcgaga tcgagggtga aggcgagggt cgtccgtacg aaggcaccca
     3601 gaccgcgaag ctgaaagtga ccaagggtgg cccgctgccg ttcagctggg acatcctgag
     3661 cccgcagttc atgtatggca gccgtgcgtt taccaaacac ccggcggaca ttccggatta
     3721 ctataagcaa agcttcccgg aaggttttaa atgggagcgt gttatgaact tcgaagatgg
     3781 tggcgcggtg accgttaccc aggacaccag cctggaggat ggcaccctga tttacaaggt
     3841 gaaactgcgt ggcaccaact ttccgccgga tggtccggtt atgcagaaga aaacgatggg
     3901 ttgggaagcg agcaccgagc gtctgtatcc ggaagatggc gtgctgaagg gtgatatcaa
     3961 aatggcgctg cgtctgaagg acggtggccg ttacctggcg gattttaaga ccacctataa
     4021 agcgaagaaa ccggtgcaaa tgccgggtgc gtacaacgtt gaccgtaaac tggatattac
     4081 cagccacaac gaggattata ccgtggttga gcaatatgag cgtagcgagg gtcgccacag
     4141 caccggcggc atggacgaac tgtataaggg atcctaataa cgctgatagt gctagtgtag
     4201 atcgctacta gagccaggca tcaaataaaa cgaaaggctc agtcgaaaga ctgggccttt
     4261 cgttttatct gttgtttgtc ggtgaacgct ctctactaga gtcacactgg ctcaccttcg
     4321 ggtgggcctt tctgcgttta tatactggct cg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and pRO1600/ColE1 origin of replication.",
                    "label": "BASIC_SEVA_44",
                },
                {
                    "accessor": "45",
                    "binaryString": """LOCUS       BASIC_SEVA_45           6057 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and
            RSF1010 origin of replication..
ACCESSION   7072310bb13203707bb813b628eff9b7
VERSION     7072310bb13203707bb813b628eff9b7
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    5919..6047
                     /label="B0015"
     misc_feature    5159..5170
                     /label="B0034"
     misc_feature    join(6052..6057,1..51)
                     /label="LMP"
     misc_feature    5059..5115
                     /label="LMS"
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
     misc_feature    5116..5150
                     /label="J23119"
     CDS             5178..5882
                     /label="mScarlett"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    4945..5049
                     /label="SEVA_T1"
     misc_feature    1257..4930
                     /label="SEVA_RSF101"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggcctcag
     1261 cctgccgcct tgggccgggt gatgtcgtac ttgcccgccg cgaactcggt taccgtccag
     1321 cccagcgcga ccagctccgg caacgcctcg cgcacccgct ggcggcgctt gcgcatggtc
     1381 gaaccactgg cctctgacgg ccagacatag ccgcacaagg tatctatgga agccttgccg
     1441 gttttgccgg ggtcgatcca gccacacagc cgctggtgca gcaggcgggc ggtttcgctg
     1501 tccagcgccc gcacctcgtc catgctgatg cgcacatgct ggccgccacc catgacggcc
     1561 tgcgcgatca aggggttcag ggccacgtac aggcgcccgt ccgcctcgtc gctggcgtac
     1621 tccgacagca gccgaaaccc ctgccgcttg cggccattct gggcgatgat ggataccttc
     1681 caaaggcgct cgatgcagtc ctgtatgtgc ttgagcgccc caccactatc gacctctgcc
     1741 ccgatttcct ttgccagcgc ccgatagcta cctttgacca catggcattc agcggtgacg
     1801 gcctcccact tgggttccag gaacagccgg agctgccgtc cgccttcggt cttgggttcc
     1861 gggccaagca ctaggccatt aggcccagcc atggccacca gcccttgcag gatgcgcaga
     1921 tcatcagcgc ccagcggctc cgggccgctg aactcgatcc gcttgccgtc gccgtagtca
     1981 tacgtcacgt ccagcttgct gcgcttgcgc tcgccccgct tgagggcacg gaacaggccg
     2041 ggggccagac agtgcgccgg gtcgtgccgg acgtggctga ggctgtgctt gttcttaggc
     2101 ttcaccacgg ggcaccccct tgctcttgcg ctgcctctcc agcacggcgg gcttgagcac
     2161 cccgccgtca tgccgcctga accaccgatc agcgaacggt gcgccatagt tggccttgct
     2221 cacaccgaag cggacgaaga accggcgctg gtcgtcgtcc acaccccatt cctcggcctc
     2281 ggcgctggtc atgctcgaca ggtaggactg ccagcggatg ttatcgacca gtaccgagct
     2341 gccccggctg gcctgctgct ggtcgcctgc gcccatcatg gccgcgccct tgctggcatg
     2401 gtgcaggaac acgatagagc acccggtatc ggcggcgatg gcctccatgc gaccgatgac
     2461 ctgggccatg gggccgctgg cgttttcttc ctcgatgtgg aaccggcgca gcgtgtccag
     2521 caccatcagg cggcggccct cggcggcgcg cttgaggccg tcgaaccact ccggggccat
     2581 gatgttgggc aggctgccga tcagcggctg gatcagcagg ccgtcagcca cggcttgccg
     2641 ttcctcggcg ctgaggtgcg ccccaagggc gtgcaggcgg tgatgaatgg cggtgggcgg
     2701 gtcttcggcg ggcaggtaga tcaccgggcc ggtgggcagt tcgcccacct ccagcagatc
     2761 cggcccgcct gcaatctgtg cggccagttg cagggccagc atggatttac cggcaccacc
     2821 gggcgacacc agcgccccga ccgtaccggc caccatgttg ggcaaaacgt agtccagcgg
     2881 tggcggcgct gctgcgaacg cctccagaat attgataggc ttatgggtag ccattgattg
     2941 cctcctttgc aggcagttgg tggttaggcg ctggcggggt cactaccccc gccctgcgcc
     3001 gctctgagtt cttccaggca ctcgcgcagc gcctcgtatt cgtcgtcggt cagccagaac
     3061 ttgcgctgac gcatcccttt ggccttcatg cgctcggcat atcgcgcttg gcgtacagcg
     3121 tcagggctgg ccagcaggtc gccggtctgc ttgtcctttt ggtctttcat atcagtcacc
     3181 gagaaacttg ccggggccga aaggcttgtc ttcgcggaac aaggacaagg tgcagccgtc
     3241 aaggttaagg ctggccatat cagcgactga aaagcggcca gcctcggcct tgtttgacgt
     3301 ataaccaaag ccaccgggca accaatagcc cttgtcactt ttgatcaggt agaccgaccc
     3361 tgaagcgctt ttttcgtatt ccataaaacc cccttctgtg cgtgagtact catagtataa
     3421 caggcgtgag taccaacgca agcactacat gctgaaatct ggcccgcccc tgtccatgcc
     3481 tcgctggcgg ggtgccggtg cccgtgccag ctcggcccgc gcaagctgga cgctgggcag
     3541 acccatgacc ttgctgacgg tgcgctcgat gtaatccgct tcgtggccgg gcttgcgctc
     3601 tgccagcgct gggctggcct cggccatggc cttgccgatt tcctcggcac tgcggccccg
     3661 gctggccagc ttctgcgcgg cgataaagtc gcacttgctg aggtcatcac cgaagcgctt
     3721 gaccagcccg gccatctcgc tgcggtactc gtccagcgcc gtgcgccggt ggcggctaag
     3781 ctgccgctcg ggcagttcga ggctggccag cctgcgggcc ttctcctgct gccgctgggc
     3841 ctgctcgatc tgctggccag cctgctgcac cagcgccggg ccagcggtgg cggtcttgcc
     3901 cttggattca cgcagcagca cccacggctg ataaccggcg cgggtggtgt gcttgtcctt
     3961 gcggttggtg aagcccgcca agcggccata gtggcggctg tcggcgctgg ccgggtcggc
     4021 gtcgtactcg ctggccagcg tccgggcaat ctgcccccga agttcaccgc ctgcggcgtc
     4081 ggccaccttg acccatgcct gatagttctt cgggctggtt tccactacca gggcaggctc
     4141 ccggccctcg gctttcatgt catccaggtc aaactcgctg aggtcgtcca ccagcaccag
     4201 accatgccgc tcctgctcgg cgggcctgat atacacgtca ttgccctggg cattcatccg
     4261 cttgagccat ggcgtgttct ggagcacttc ggcggctgac cattcccggt tcatcatctg
     4321 gccggtggtg gcgtccctga cgccgatatc gaagcgctca cagcccatgg ccttgagctg
     4381 tcggcctatg gcctgcaaag tcctgtcgtt cttcatcggg ccaccaagcg attcccacac
     4441 attatacgag ccggaagcat aaagtgtaaa gcctagatcc gaaggatgag ccgggctgaa
     4501 tgatcgaccg agacaggccc tgcggggctg cacacgcgcc cccacccttc gggtaggggg
     4561 aaaggccgct aaagcggcta aaagcgctcc agcgtatttc tgcggggttt ggtgtggggt
     4621 ttagcgggct ttgcccgcct ttccccctgc cgcgcagcgg tggggcggtg tgtagcctag
     4681 cgcagcgaat agaccagcta tccggcctct ggccgggcat attgggcaag ggcagcagcg
     4741 ccccacaagg gcgctgataa ccgcgcctag tggattattc ttagataatc atggatggat
     4801 ttttccaaca ccccgccagc ccccgcccct gctgggtttg caggtttggg ggcgtgacag
     4861 ttattgcagg ggttcgtgac agttattgca ggggggcgtg acagttattg caggggttcg
     4921 tgacagttag ggcgcgccca gctgtctagg gcggcggatt tgtcctactc aggagagcgt
     4981 tcaccgacaa acaacagata aaacgaaagg cccagtcttt cgactgagcc tttcgtttta
     5041 tttgatgcct ttaattaagg ctcgggagac ctatcggtaa taacagtcca atctggtgta
     5101 acttcggaat cgtccttgac agctagctca gtcctaggta taatgctagc tactagtgaa
     5161 agaggagaaa tactagtatg gttagcaaag gcgaggcggt tatcaaggag tttatgcgtt
     5221 ttaaggttca catggagggt agcatgaatg gtcacgagtt cgagatcgag ggtgaaggcg
     5281 agggtcgtcc gtacgaaggc acccagaccg cgaagctgaa agtgaccaag ggtggcccgc
     5341 tgccgttcag ctgggacatc ctgagcccgc agttcatgta tggcagccgt gcgtttacca
     5401 aacacccggc ggacattccg gattactata agcaaagctt cccggaaggt tttaaatggg
     5461 agcgtgttat gaacttcgaa gatggtggcg cggtgaccgt tacccaggac accagcctgg
     5521 aggatggcac cctgatttac aaggtgaaac tgcgtggcac caactttccg ccggatggtc
     5581 cggttatgca gaagaaaacg atgggttggg aagcgagcac cgagcgtctg tatccggaag
     5641 atggcgtgct gaagggtgat atcaaaatgg cgctgcgtct gaaggacggt ggccgttacc
     5701 tggcggattt taagaccacc tataaagcga agaaaccggt gcaaatgccg ggtgcgtaca
     5761 acgttgaccg taaactggat attaccagcc acaacgagga ttataccgtg gttgagcaat
     5821 atgagcgtag cgagggtcgc cacagcaccg gcggcatgga cgaactgtat aagggatcct
     5881 aataacgctg atagtgctag tgtagatcgc tactagagcc aggcatcaaa taaaacgaaa
     5941 ggctcagtcg aaagactggg cctttcgttt tatctgttgt ttgtcggtga acgctctcta
     6001 ctagagtcac actggctcac cttcgggtgg gcctttctgc gtttatatac tggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and RSF1010 origin of replication.",
                    "label": "BASIC_SEVA_45",
                },
                {
                    "accessor": "46",
                    "binaryString": """LOCUS       BASIC_SEVA_46           3115 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and p15A
            origin of replication..
ACCESSION   9d55b6bfb91e90bb21e6acb4fdb1915d
VERSION     9d55b6bfb91e90bb21e6acb4fdb1915d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2217..2228
                     /label="B0034"
     misc_feature    join(3110..3115,1..51)
                     /label="LMP"
     misc_feature    2117..2173
                     /label="LMS"
     misc_feature    2174..2208
                     /label="J23119"
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
     misc_feature    2977..3105
                     /label="B0015"
     misc_feature    2003..2107
                     /label="SEVA_T1"
     misc_feature    1257..1988
                     /label="SEVA_p15A"
     misc_feature    58..160
                     /label="SEVA_T0"
     CDS             2236..2940
                     /label="mScarlett"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccctag
     1261 aaatatttta tctgattaat aagatgatct tcttgagatc gttttggtct gcgcgtaatc
     1321 tcttgctctg aaaacgaaaa aaccgccttg cagggcggtt tttcgaaggt tctctgagct
     1381 accaactctt tgaaccgagg taactggctt ggaggagcgc agtcaccaaa acttgtcctt
     1441 tcagtttagc cttaaccggc gcatgacttc aagactaact cctctaaatc aattaccagt
     1501 ggctgctgcc agtggtgctt ttgcatgtct ttccgggttg gactcaagac gatagttacc
     1561 ggataaggcg cagcggtcgg actgaacggg gggttcgtgc atacagtcca gcttggagcg
     1621 aactgcctac ccggaactga gtgtcaggcg tggaatgaga caaacgcggc cataacagcg
     1681 gaatgacacc ggtaaaccga aaggcaggaa caggagagcg cacgagggag ccgccagggg
     1741 gaaacgcctg gtatctttat agtcctgtcg ggtttcgcca ccactgattt gagcgtcaga
     1801 tttcgtgatg cttgtcaggg gggcggagcc tatggaaaaa cggctttgcc gcggccctct
     1861 cacttccctg ttaagtatct tcctggcatc ttccaggaaa tctccgcccc gttcgtaagc
     1921 catttccgct cgccgcagtc gaacgaccga gcgtagcgag tcagtgagcg aggaagcgga
     1981 atatatccgg cgcgcccagc tgtctagggc ggcggatttg tcctactcag gagagcgttc
     2041 accgacaaac aacagataaa acgaaaggcc cagtctttcg actgagcctt tcgttttatt
     2101 tgatgccttt aattaaggct cgggagacct atcggtaata acagtccaat ctggtgtaac
     2161 ttcggaatcg tccttgacag ctagctcagt cctaggtata atgctagcta ctagtgaaag
     2221 aggagaaata ctagtatggt tagcaaaggc gaggcggtta tcaaggagtt tatgcgtttt
     2281 aaggttcaca tggagggtag catgaatggt cacgagttcg agatcgaggg tgaaggcgag
     2341 ggtcgtccgt acgaaggcac ccagaccgcg aagctgaaag tgaccaaggg tggcccgctg
     2401 ccgttcagct gggacatcct gagcccgcag ttcatgtatg gcagccgtgc gtttaccaaa
     2461 cacccggcgg acattccgga ttactataag caaagcttcc cggaaggttt taaatgggag
     2521 cgtgttatga acttcgaaga tggtggcgcg gtgaccgtta cccaggacac cagcctggag
     2581 gatggcaccc tgatttacaa ggtgaaactg cgtggcacca actttccgcc ggatggtccg
     2641 gttatgcaga agaaaacgat gggttgggaa gcgagcaccg agcgtctgta tccggaagat
     2701 ggcgtgctga agggtgatat caaaatggcg ctgcgtctga aggacggtgg ccgttacctg
     2761 gcggatttta agaccaccta taaagcgaag aaaccggtgc aaatgccggg tgcgtacaac
     2821 gttgaccgta aactggatat taccagccac aacgaggatt ataccgtggt tgagcaatat
     2881 gagcgtagcg agggtcgcca cagcaccggc ggcatggacg aactgtataa gggatcctaa
     2941 taacgctgat agtgctagtg tagatcgcta ctagagccag gcatcaaata aaacgaaagg
     3001 ctcagtcgaa agactgggcc tttcgtttta tctgttgttt gtcggtgaac gctctctact
     3061 agagtcacac tggctcacct tcgggtgggc ctttctgcgt ttatatactg gctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and p15A origin of replication.",
                    "label": "BASIC_SEVA_46",
                },
                {
                    "accessor": "47",
                    "binaryString": """LOCUS       BASIC_SEVA_47           4039 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and
            pSC101 origin of replication..
ACCESSION   e276798c3ebd5ffdc016fbead7d37903
VERSION     e276798c3ebd5ffdc016fbead7d37903
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
     misc_feature    2731..2835
                     /label="SEVA_T1"
     CDS             3160..3864
                     /label="mScarlett"
     misc_feature    1257..2716
                     /label="SEVA_pSC101"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2994..3028
                     /label="J23119"
     misc_feature    3901..4029
                     /label="B0015"
     misc_feature    join(4034..4039,1..51)
                     /label="LMP"
     misc_feature    2845..2901
                     /label="LMS"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggcctcag
     1261 atccttccgt atttagccag tatgttctct agtgtggttc gttgtttttg cgtgagccat
     1321 gagaacgaac cattgagatc atacttactt tgcatgtcac tcaaaaattt tgcctcaaaa
     1381 ctggtgagct gaatttttgc agttaaagca tcgtgtagtg tttttcttag tccgttatgt
     1441 aggtaggaat ctgatgtaat ggttgttggt attttgtcac cattcatttt tatctggttg
     1501 ttctcaagtt cggttacgag atccatttgt ctatctagtt caacttggaa aatcaacgta
     1561 tcagtcgggc ggcctcgctt atcaaccacc aatttcatat tgctgtaagt gtttaaatct
     1621 ttacttattg gtttcaaaac ccattggtta agccttttaa actcatggta gttattttca
     1681 agcattaaca tgaacttaaa ttcatcaagg ctaatctcta tatttgcctt gtgagttttc
     1741 ttttgtgtta gttcttttaa taaccactca taaatcctca tagagtattt gttttcaaaa
     1801 gacttaacat gttccagatt atattttatg aattttttta actggaaaag ataaggcaat
     1861 atctcttcac taaaaactaa ttctaatttt tcgcttgaga acttggcata gtttgtccac
     1921 tggaaaatct caaagccttt aaccaaagga ttcctgattt ccacagttct cgtcatcagc
     1981 tctctggttg ctttagctaa tacaccataa gcattttccc tactgatgtt catcatctga
     2041 gcgtattggt tataagtgaa cgataccgtc cgttctttcc ttgtagggtt ttcaatcgtg
     2101 gggttgagta gtgccacaca gcataaaatt agcttggttt catgctccgt taagtcatag
     2161 cgactaatcg ctagttcatt tgctttgaaa acaactaatt cagacataca tctcaattgg
     2221 tctaggtgat tttaatcact ataccaattg agatgggcta gtcaatgata attacatgtc
     2281 cttttccttt gagttgtggg tatctgtaaa ttctgctaga cctttgctgg aaaacttgta
     2341 aattctgcta gaccctctgt aaattccgct agacctttgt gtgttttttt tgtttatatt
     2401 caagtggtta taatttatag aataaagaaa gaataaaaaa agataaaaag aatagatccc
     2461 agccctgtgt ataactcact actttagtca gttccgcagt attacaaaag gatgtcgcaa
     2521 acgctgtttg ctcctctaca aaacagacct taaaacccta aaggcttaag tagcaccctc
     2581 gcaagctcgg gcaaatcgct gaatattcct tttgtctccg accatcaggc acctgagtcg
     2641 ctgtcttttt cgtgacattc agttcgctgc gctcacggct ctggcagtga atgggggtaa
     2701 atggcactac aggcgcggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga
     2761 gagcgttcac cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc
     2821 gttttatttg atgcctttaa ttaaggctcg ggagacctat cggtaataac agtccaatct
     2881 ggtgtaactt cggaatcgtc cccaattatt gaacaccctt cggggtgttt ttttgtttct
     2941 ggtctaccat ctcgttgtga taatagacct gaagtgccta ctctggaaaa tctttgacag
     3001 ctagctcagt cctaggtata atgctagcag ctgtcaccgg atgtgctttc cggtctgatg
     3061 agtccgtgag gacgaaacag cctctacaaa taattttgtt taaggctcgc tacgagaaga
     3121 ttgttacttt cgcagcgtta ttatctaagg aggtagtcca tggttagcaa aggcgaggcg
     3181 gttatcaagg agtttatgcg ttttaaggtt cacatggagg gtagcatgaa tggtcacgag
     3241 ttcgagatcg agggtgaagg cgagggtcgt ccgtacgaag gcacccagac cgcgaagctg
     3301 aaagtgacca agggtggccc gctgccgttc agctgggaca tcctgagccc gcagttcatg
     3361 tatggcagcc gtgcgtttac caaacacccg gcggacattc cggattacta taagcaaagc
     3421 ttcccggaag gttttaaatg ggagcgtgtt atgaacttcg aagatggtgg cgcggtgacc
     3481 gttacccagg acaccagcct ggaggatggc accctgattt acaaggtgaa actgcgtggc
     3541 accaactttc cgccggatgg tccggttatg cagaagaaaa cgatgggttg ggaagcgagc
     3601 accgagcgtc tgtatccgga agatggcgtg ctgaagggtg atatcaaaat ggcgctgcgt
     3661 ctgaaggacg gtggccgtta cctggcggat tttaagacca cctataaagc gaagaaaccg
     3721 gtgcaaatgc cgggtgcgta caacgttgac cgtaaactgg atattaccag ccacaacgag
     3781 gattataccg tggttgagca atatgagcgt agcgagggtc gccacagcac cggcggcatg
     3841 gacgaactgt ataagggatc ctaataacgc tgatagtgct agtgtagatc gctactagag
     3901 ccaggcatca aataaaacga aaggctcagt cgaaagactg ggcctttcgt tttatctgtt
     3961 gtttgtcggt gaacgctctc tactagagtc acactggctc accttcgggt gggcctttct
     4021 gcgtttatat actggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and pSC101 origin of replication.",
                    "label": "BASIC_SEVA_47",
                },
                {
                    "accessor": "48",
                    "binaryString": """LOCUS       BASIC_SEVA_48           3312 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and pUC
            origin of replication..
ACCESSION   72bca0fe0dc27fa1db1bd0a753193aca
VERSION     72bca0fe0dc27fa1db1bd0a753193aca
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    join(3307..3312,1..51)
                     /label="LMP"
     misc_feature    2371..2405
                     /label="J23106"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2200..2304
                     /label="SEVA_T1"
     misc_feature    2314..2370
                     /label="LMS"
     CDS             2433..3137
                     /label="mScarlett"
     misc_feature    1257..2185
                     /label="SEVA_pUC"
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
     misc_feature    2414..2425
                     /label="B0034"
     misc_feature    3174..3302
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccccgt
     1261 agaaaagatc aaaggatctt cttgagatcc tttttttctg cgcgtaatct gctgcttgca
     1321 aacaaaaaaa ccaccgctac cagcggtggt ttgtttgccg gatcaagagc taccaactct
     1381 ttttccgaag gtaactggct tcagcagagc gcagatacca aatactgttc ttctagtgta
     1441 gccgtagtta ggccaccact tcaagaactc tgtagcaccg cctacatacc tcgctctgct
     1501 aatcctgtta ccagtggctg ctgccagtgg cgataagtcg tgtcttaccg ggttggactc
     1561 aagacgatag ttaccggata aggcgcagcg gtcgggctga acggggggtt cgtgcacaca
     1621 gcccagcttg gagcgaacga cctacaccga actgagatac ctacagcgtg agctttgaga
     1681 aagcgccacg cttcccgaag ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg
     1741 aacaggagag cgcacgaggg agcttccagg gggaaacgcc tggtatcttt atagtcctgt
     1801 cgggtttcgc cacctctgac ttgagcgtcg atttttgtga tgctcgtcag gggggcggag
     1861 cctatggaaa aacgccagca acgcggcctt tttacggttc ctggcctttt gctggccttt
     1921 tgctcacatg ttctttcctg cgttatcccc tgattctgtg gataaccgta ttaccgcctt
     1981 tgagtgagct gataccgctc gccgcagccg aacgaccgag cgcagcgagt cagtgagcga
     2041 ggaagcggaa gagcgcccaa tacgcaaacc gcctctcccc gcgcgttggc cgattcatta
     2101 atgcagctgg cacgacaggt ttcccgactg gaaagcgggc agtgagcgca acgcaattaa
     2161 tgtgagttag ctcactcatt aggcaggcgc gcccagctgt ctagggcggc ggatttgtcc
     2221 tactcaggag agcgttcacc gacaaacaac agataaaacg aaaggcccag tctttcgact
     2281 gagcctttcg ttttatttga tgcctttaat taaggctcgg gagacctatc ggtaataaca
     2341 gtccaatctg gtgtaacttc ggaatcgtcc tttacggcta gctcagtcct aggtatagtg
     2401 ctagctacta gtgaaagagg agaaatacta gtatggttag caaaggcgag gcggttatca
     2461 aggagtttat gcgttttaag gttcacatgg agggtagcat gaatggtcac gagttcgaga
     2521 tcgagggtga aggcgagggt cgtccgtacg aaggcaccca gaccgcgaag ctgaaagtga
     2581 ccaagggtgg cccgctgccg ttcagctggg acatcctgag cccgcagttc atgtatggca
     2641 gccgtgcgtt taccaaacac ccggcggaca ttccggatta ctataagcaa agcttcccgg
     2701 aaggttttaa atgggagcgt gttatgaact tcgaagatgg tggcgcggtg accgttaccc
     2761 aggacaccag cctggaggat ggcaccctga tttacaaggt gaaactgcgt ggcaccaact
     2821 ttccgccgga tggtccggtt atgcagaaga aaacgatggg ttgggaagcg agcaccgagc
     2881 gtctgtatcc ggaagatggc gtgctgaagg gtgatatcaa aatggcgctg cgtctgaagg
     2941 acggtggccg ttacctggcg gattttaaga ccacctataa agcgaagaaa ccggtgcaaa
     3001 tgccgggtgc gtacaacgtt gaccgtaaac tggatattac cagccacaac gaggattata
     3061 ccgtggttga gcaatatgag cgtagcgagg gtcgccacag caccggcggc atggacgaac
     3121 tgtataaggg atcctaataa cgctgatagt gctagtgtag atcgctacta gagccaggca
     3181 tcaaataaaa cgaaaggctc agtcgaaaga ctgggccttt cgttttatct gttgtttgtc
     3241 ggtgaacgct ctctactaga gtcacactgg ctcaccttcg ggtgggcctt tctgcgttta
     3301 tatactggct cg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and pUC origin of replication.",
                    "label": "BASIC_SEVA_48",
                },
                {
                    "accessor": "49",
                    "binaryString": """LOCUS       BASIC_SEVA_49           3768 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Streptomycin resistance marker and
            pBR322-ROP origin of replication..
ACCESSION   e089de570a552d5c35715270486c48cc
VERSION     e089de570a552d5c35715270486c48cc
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3630..3758
                     /label="B0015"
     misc_feature    2827..2861
                     /label="J23119"
     misc_feature    2770..2826
                     /label="LMS"
     misc_feature    join(3763..3768,1..51)
                     /label="LMP"
     CDS             2889..3593
                     /label="mScarlett"
     misc_feature    2870..2881
                     /label="B0034"
     misc_feature    2656..2760
                     /label="SEVA_T1"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    1257..2641
                     /label="SEVA_pBR322-ROP"
     misc_feature    195..1183
                     /label="SEVA_Sm/Sp"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatgaacct tgaccgaacg cagcggtggt aacggcgcag tggcggtttt
      241 catggcttgt tatgactgtt tttttggggt acagtctatg cctcgggcat ccaagcagca
      301 agcgcgttac gccgtgggtc gatgtttgat gttatggagc agcaacgatg ttacgcagca
      361 gggcagtcgc cctaaaacaa agttaaacat catgagggaa gcggtgatcg ccgaagtatc
      421 gactcaacta tcagaggtag ttggcgtcat cgagcgccat ctcgaaccga cgttgctggc
      481 cgtacatttg tacggctccg cagtggatgg cggcctgaag ccacacagtg atattgattt
      541 gctggttacg gtgaccgtaa ggcttgatga aacaacgcgg cgagctttga tcaacgacct
      601 tttggaaact tcggcttccc ctggagagag cgagattctc cgcgctgtag aagtcaccat
      661 tgttgtgcac gacgacatca ttccgtggcg ttatccagct aagcgcgaac tgcaatttgg
      721 agaatggcag cgcaatgaca ttcttgcagg tatcttcgag ccagccacga tcgacattga
      781 tctggctatc ttgctgacaa aagcaagaga acatagcgtt gccttggtag gtccagcggc
      841 ggaggaactc tttgatccgg ttcctgaaca ggatctattt gaggcgctaa atgaaacctt
      901 aacgctatgg aactcgccgc ccgactgggc tggcgatgag cgaaatgtag tgcttacgtt
      961 gtcccgcatt tggtacagcg cagtaaccgg caaaatcgcg ccgaaggatg tcgctgccga
     1021 ctgggcaatg gagcgcctgc cggcccagta tcagcccgtc atacttgaag ctagacaggc
     1081 ttatcttgga caagaagaag atcgcttggc ctcgcgcgca gatcagttgg aagaatttgt
     1141 ccactacgtg aaaggcgaga tcaccaaggt agtcggcaaa taagacaatt gtcggctcga
     1201 cccacgacta ttgactgctc tgagaaagtt gattgttacg attagtccgg ccggccccgt
     1261 agaaaagatc aaaggatctt cttgagatcc tttttttctg cgcgtaatct gctgcttgca
     1321 aacaaaaaaa ccaccgctac cagcggtggt ttgtttgccg gatcaagagc taccaactct
     1381 ttttccgaag gtaactggct tcagcagagc gcagatacca aatactgtcc ttctagtgta
     1441 gccgtagtta ggccaccact tcaagaactc tgtagcaccg cctacatacc tcgctctgct
     1501 aatcctgtta ccagtggctg ctgccagtgg cgataagtcg tgtcttaccg ggttggactc
     1561 aagacgatag ttaccggata aggcgcagcg gtcgggctga acggggggtt cgtgcacaca
     1621 gcccagcttg gagcgaacga cctacaccga actgagatac ctacagcgtg agctatgaga
     1681 aagcgccacg cttcccgaag ggagaaaggc ggacaggtat ccggtaagcg gcagggtcgg
     1741 aacaggagag cgcacgaggg agcttccagg gggaaacgcc tggtatcttt atagtcctgt
     1801 cgggtttcgc cacctctgac ttgagcgtcg atttttgtga tgctcgtcag gggggcggag
     1861 cctatggaaa aacgccagca acgcggcctt tttacggttc ctggcctttt gctggccttt
     1921 tgctcacatg ttctttcctg cgttatcccc tgattctgtg gataaccgta ttaccgcctt
     1981 tgagtgagct gataccgctc gccgcagccg aacgaccgag cgcagcgagt cagtgagcga
     2041 ggaagcggaa gagcgcctga tgcggtattt tctccttacg catctgtgcg gtatttcaca
     2101 ccgcatatgg tgcactctca gtacaatctg ctctgatgcc gcatagttaa gccagtatac
     2161 actccgctat cgctacgtga ctgggtcatg gctgcgcccc gacacccgcc aacacccgct
     2221 gacgcgccct gacgggcttg tctgctcccg gcatccgctt acagacaagc tgtgaccgtc
     2281 tccgggagct gcatgtgtca gaggttttca ccgtcatcac cgaaacgcgc gaggcagctg
     2341 cggtaaagct catcagcgtg gtcgtgcagc gattcacaga tgtctgcctg ttcatccgcg
     2401 tccagctcgt tgagtttctc cagaagcgtt aatgtctggc ttctgataaa gcgggccatg
     2461 ttaagggcgg ttttttcctg tttggtcact gatgcctccg tgtaaggggg atttctgttc
     2521 atgggggtaa tgataccgat gaaacgagag aggatgctca cgatacgggt tactgatgat
     2581 gaacatgccc ggttactgga acgttgtgag ggtaaacaac tggcggtatg gatgcggcgg
     2641 gggcgcgccc agctgtctag ggcggcggat ttgtcctact caggagagcg ttcaccgaca
     2701 aacaacagat aaaacgaaag gcccagtctt tcgactgagc ctttcgtttt atttgatgcc
     2761 tttaattaag gctcgggaga cctatcggta ataacagtcc aatctggtgt aacttcggaa
     2821 tcgtccttga cagctagctc agtcctaggt ataatgctag ctactagtga aagaggagaa
     2881 atactagtat ggttagcaaa ggcgaggcgg ttatcaagga gtttatgcgt tttaaggttc
     2941 acatggaggg tagcatgaat ggtcacgagt tcgagatcga gggtgaaggc gagggtcgtc
     3001 cgtacgaagg cacccagacc gcgaagctga aagtgaccaa gggtggcccg ctgccgttca
     3061 gctgggacat cctgagcccg cagttcatgt atggcagccg tgcgtttacc aaacacccgg
     3121 cggacattcc ggattactat aagcaaagct tcccggaagg ttttaaatgg gagcgtgtta
     3181 tgaacttcga agatggtggc gcggtgaccg ttacccagga caccagcctg gaggatggca
     3241 ccctgattta caaggtgaaa ctgcgtggca ccaactttcc gccggatggt ccggttatgc
     3301 agaagaaaac gatgggttgg gaagcgagca ccgagcgtct gtatccggaa gatggcgtgc
     3361 tgaagggtga tatcaaaatg gcgctgcgtc tgaaggacgg tggccgttac ctggcggatt
     3421 ttaagaccac ctataaagcg aagaaaccgg tgcaaatgcc gggtgcgtac aacgttgacc
     3481 gtaaactgga tattaccagc cacaacgagg attataccgt ggttgagcaa tatgagcgta
     3541 gcgagggtcg ccacagcacc ggcggcatgg acgaactgta taagggatcc taataacgct
     3601 gatagtgcta gtgtagatcg ctactagagc caggcatcaa ataaaacgaa aggctcagtc
     3661 gaaagactgg gcctttcgtt ttatctgttg tttgtcggtg aacgctctct actagagtca
     3721 cactggctca ccttcgggtg ggcctttctg cgtttatata ctggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Streptomycin resistance marker and pBR322-ROP origin of replication.",
                    "label": "BASIC_SEVA_49",
                },
                {
                    "accessor": "52",
                    "binaryString": """LOCUS       BASIC_SEVA_52           5079 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and RK2
            origin of replication..
ACCESSION   8a6b275731b465403c0420f195ce90cb
VERSION     8a6b275731b465403c0420f195ce90cb
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3771..3875
                     /label="SEVA_T1"
     misc_feature    195..1461
                     /label="SEVA_Tet"
     misc_feature    1535..3756
                     /label="SEVA_RK2"
     misc_feature    4034..4068
                     /label="J23119"
     CDS             4200..4904
                     /label="mScarlett"
     misc_feature    join(5074..5079,1..51)
                     /label="LMP"
     misc_feature    4941..5069
                     /label="B0015"
     misc_feature    3885..3941
                     /label="LMS"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggccgcgatg caggtggctg ctgaaccccc
     1561 agccggaact gaccccacaa ggccctagcg tttgcaatgc accaggtcat cattgaccca
     1621 ggcgtgttcc accaggccgc tgcctcgcaa ctcttcgcag gcttcgccga cctgctcgcg
     1681 ccacttcttc acgcgggtgg aatccgatcc gcacatgagg cggaaggttt ccagcttgag
     1741 cgggtacggc tcccggtgcg agctgaaata gtcgaacatc cgtcgggccg tcggcgacag
     1801 cttgcggtac ttctcccata tgaatttcgt gtagtggtcg ccagcaaaca gcacgacgat
     1861 ttcctcgtcg atcaggacct ggcaacggga cgttttcttg ccacggtcca ggacgcggaa
     1921 gcggtgcagc agcgacaccg attccaggtg cccaacgcgg tcggacgtga agcccatcgc
     1981 cgtcgcctgt aggcgcgaca ggcattcctc ggccttcgtg taataccggc cattgatcga
     2041 ccagcccagg tcctggcaaa gctcgtagaa cgtgaaggtg atcggctcgc cgataggggt
     2101 gcgcttcgcg tactccaaca cctgctgcca caccagttcg tcatcgtcgg cccgcagctc
     2161 gacgccggtg taggtgatct tcacgtcctt gttgacgtgg aaaatgacct tgttttgcag
     2221 cgcctcgcgc gggattttct tgttgcgcgt ggtgaacagg gcagagcggg ccgtgtcgtt
     2281 tggcatcgct cgcatcgtgt ccggccacgg cgcaatatcg aacaaggaaa gctgcatttc
     2341 cttgatctgc tgcttcgtgt gtttcagcaa cgcggcctgc ttggcttcgc tgacctgttt
     2401 tgccaggtcc tcgccggcgg tttttcgctt cttggtcgtc atagttcctc gcgtgtcgat
     2461 ggtcatcgac ttcgccaaac ctgccgcctc ctgttcgaga cgacgcgaac gctccacggc
     2521 ggccgatggc gcgggcaggg cagggggagc cagttgcacg ctgtcgcgct cgatcttggc
     2581 cgtagcttgc tggactatcg agccgacgga ctggaaggtt tcgcggggcg cacgcatgac
     2641 ggtgcggctt gcgatggttt cggcatcctc ggcggaaaac cccgcgtcga tcagttcttg
     2701 cctgtatgcc ttccggtcaa acgtccgatt cattcaccct ccttgcggga ttgccccgga
     2761 attaattccc cggatcgatc cgtcgatctt gatcccctgc gccatcagat ccttggcggc
     2821 aagaaagcca tccagtttac tttgcagggc ttcccaacct taccagaggg cgccccagct
     2881 ggcaattccg gttcgcttgc tgtccataaa accgcccagt ctagctatcg ccatgtaagc
     2941 ccactgcaag ctacctgctt tctctttgcg cttgcgtttt cccttgtcca gatagcccag
     3001 tagctgacat tcatccgggg tcagcaccgt ttctgcggac tggctttcta cgtggctgcc
     3061 atttttgggg tgaggccgtt cgcggccgag gggcgcagcc cctgggggga tgggaggccc
     3121 gcgttagcgg gccgggaggg ttcgagaagg gggggcaccc cccttcggcg tgcgcggtca
     3181 cgcgcacagg gcgcagccct ggttaaaaac aaggtttata aatattggtt taaaagcagg
     3241 ttaaaagaca ggttagcggt ggccgaaaaa cgggcggaaa cccttgcaaa tgctggattt
     3301 tctgcctgtg gacagcccct caaatgtcaa taggtgcgcc cctcatctgt cagcactctg
     3361 cccctcaagt gtcaaggatc gcgcccctca tctgtcagta gtcgcgcccc tcaagtgtca
     3421 ataccgcagg gcacttatcc ccaggcttgt ccacatcatc tgtgggaaac tcgcgtaaaa
     3481 tcaggcgttt tcgccgattt gcgaggctgg ccagctccac gtcgccggcc gaaatcgagc
     3541 ctgcccctca tctgtcaacg ccgcgccggg tgagtcggcc cctcaagtgt caacgtccgc
     3601 ccctcatctg tcagtgaggg ccaagttttc cgcgaggtat ccacaacgcc ggcggcccta
     3661 catggctctg ctgtagtgag tgggttgcgc tccggcagcg gtcctgatcc cccgcagaaa
     3721 aaaaggatct caagaagatc ctttgatctt ttctacggcg cgcccagctg tctagggcgg
     3781 cggatttgtc ctactcagga gagcgttcac cgacaaacaa cagataaaac gaaaggccca
     3841 gtctttcgac tgagcctttc gttttatttg atgcctttaa ttaaggctcg ggagacctat
     3901 cggtaataac agtccaatct ggtgtaactt cggaatcgtc cccaattatt gaacaccctt
     3961 cggggtgttt ttttgtttct ggtctaccat ctcgttgtga taatagacct gaagtgccta
     4021 ctctggaaaa tctttgacag ctagctcagt cctaggtata atgctagcag ctgtcaccgg
     4081 atgtgctttc cggtctgatg agtccgtgag gacgaaacag cctctacaaa taattttgtt
     4141 taaggctcgc tacgagaaga ttgttacttt cgcagcgtta ttatctaagg aggtagtcca
     4201 tggttagcaa aggcgaggcg gttatcaagg agtttatgcg ttttaaggtt cacatggagg
     4261 gtagcatgaa tggtcacgag ttcgagatcg agggtgaagg cgagggtcgt ccgtacgaag
     4321 gcacccagac cgcgaagctg aaagtgacca agggtggccc gctgccgttc agctgggaca
     4381 tcctgagccc gcagttcatg tatggcagcc gtgcgtttac caaacacccg gcggacattc
     4441 cggattacta taagcaaagc ttcccggaag gttttaaatg ggagcgtgtt atgaacttcg
     4501 aagatggtgg cgcggtgacc gttacccagg acaccagcct ggaggatggc accctgattt
     4561 acaaggtgaa actgcgtggc accaactttc cgccggatgg tccggttatg cagaagaaaa
     4621 cgatgggttg ggaagcgagc accgagcgtc tgtatccgga agatggcgtg ctgaagggtg
     4681 atatcaaaat ggcgctgcgt ctgaaggacg gtggccgtta cctggcggat tttaagacca
     4741 cctataaagc gaagaaaccg gtgcaaatgc cgggtgcgta caacgttgac cgtaaactgg
     4801 atattaccag ccacaacgag gattataccg tggttgagca atatgagcgt agcgagggtc
     4861 gccacagcac cggcggcatg gacgaactgt ataagggatc ctaataacgc tgatagtgct
     4921 agtgtagatc gctactagag ccaggcatca aataaaacga aaggctcagt cgaaagactg
     4981 ggcctttcgt tttatctgtt gtttgtcggt gaacgctctc tactagagtc acactggctc
     5041 accttcgggt gggcctttct gcgtttatat actggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and RK2 origin of replication.",
                    "label": "BASIC_SEVA_52",
                },
                {
                    "accessor": "53",
                    "binaryString": """LOCUS       BASIC_SEVA_53           4379 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and
            pBBR1 origin of replication..
ACCESSION   b1c8b9f61d00f7f91859a0aaabe94db6
VERSION     b1c8b9f61d00f7f91859a0aaabe94db6
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3185..3241
                     /label="LMS"
     misc_feature    195..1461
                     /label="SEVA_Tet"
     misc_feature    3334..3368
                     /label="J23119"
     CDS             3500..4204
                     /label="mScarlett"
     misc_feature    4241..4369
                     /label="B0015"
     misc_feature    3071..3175
                     /label="SEVA_T1"
     misc_feature    1535..3056
                     /label="SEVA_pBBR1"
     misc_feature    join(4374..4379,1..51)
                     /label="LMP"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggccctaccg gcgcggcagc gttacccgtg
     1561 tcggcggctc caacggctcg ccatcgtcca gaaaacacgg ctcatcgggc atcggcaggc
     1621 gctgctgccc gcgccgttcc cattcctccg tttcggtcaa ggctggcagg tctggttcca
     1681 tgcccggaat gccgggctgg ctgggcggct cctcgccggg gccggtcggt agttgctgct
     1741 cgcccggata cagggtcggg atgcggcgca ggtcgccatg ccccaacagc gattcgtcct
     1801 ggtcgtcgtg atcaaccacc acggcggcac tgaacaccga caggcgcaac tggtcgcggg
     1861 gctggcccca cgccacgcgg tcattgacca cgtaggccga cacggtgccg gggccgttga
     1921 gcttcacgac ggagatccag cgctcggcca ccaagtcctt gactgcgtat tggaccgtcc
     1981 gcaaagaacg tccgatgagc ttggaaagtg tcttctggct gaccaccacg gcgttctggt
     2041 ggcccatctg cgccacgagg tgatgcagca gcattgccgc cgtgggtttc ctcgcaataa
     2101 gcccggccca cgcctcatgc gctttgcgtt ccgtttgcac ccagtgaccg ggcttgttct
     2161 tggcttgaat gccgatttct ctggactgcg tggccatgct tatctccatg cggtaggggt
     2221 gccgcacggt tgcggcacca tgcgcaatca gctgcaactt ttcggcagcg cgacaacaat
     2281 tatgcgttgc gtaaaagtgg cagtcaatta cagattttct ttaacctacg caatgagcta
     2341 ttgcgggggg tgccgcaatg agctgttgcg tacccccctt ttttaagttg ttgattttta
     2401 agtctttcgc atttcgccct atatctagtt ctttggtgcc caaagaaggg cacccctgcg
     2461 gggttccccc acgccttcgg cgcggctccc cctccggcaa aaagtggccc ctccggggct
     2521 tgttgatcga ctgcgcggcc ttcggccttg cccaaggtgg cgctgccccc ttggaacccc
     2581 cgcactcgcc gccgtgaggc tcggggggca ggcgggcggg cttcgccctt cgactgcccc
     2641 cactcgcata ggcttgggtc gttccaggcg cgtcaaggcc aagccgctgc gcggtcgctg
     2701 cgcgagcctt gacccgcctt ccacttggtg tccaaccggc aagcgaagcg cgcaggccgc
     2761 aggccggagg cttttcccca gagaaaatta aaaaaattga tggggcaagg ccgcaggccg
     2821 cgcagttgga gccggtgggt atgtggtcga aggctgggta gccggtgggc aatccctgtg
     2881 gtcaagctcg tgggcaggcg cagcctgtcc atcagcttgt ccagcagggt tgtccacggg
     2941 ccgagcgaag cgagccagcc ggtggccgct cgcggccatc gtccacatat ccacgggctg
     3001 gcaagggagc gcagcgaccg cgcagggcga agcccggaga gcaagcccgt agggggggcg
     3061 cgcccagctg tctagggcgg cggatttgtc ctactcagga gagcgttcac cgacaaacaa
     3121 cagataaaac gaaaggccca gtctttcgac tgagcctttc gttttatttg atgcctttaa
     3181 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
     3241 cccaattatt gaacaccctt cggggtgttt ttttgtttct ggtctaccat ctcgttgtga
     3301 taatagacct gaagtgccta ctctggaaaa tctttgacag ctagctcagt cctaggtata
     3361 atgctagcag ctgtcaccgg atgtgctttc cggtctgatg agtccgtgag gacgaaacag
     3421 cctctacaaa taattttgtt taaggctcgc tacgagaaga ttgttacttt cgcagcgtta
     3481 ttatctaagg aggtagtcca tggttagcaa aggcgaggcg gttatcaagg agtttatgcg
     3541 ttttaaggtt cacatggagg gtagcatgaa tggtcacgag ttcgagatcg agggtgaagg
     3601 cgagggtcgt ccgtacgaag gcacccagac cgcgaagctg aaagtgacca agggtggccc
     3661 gctgccgttc agctgggaca tcctgagccc gcagttcatg tatggcagcc gtgcgtttac
     3721 caaacacccg gcggacattc cggattacta taagcaaagc ttcccggaag gttttaaatg
     3781 ggagcgtgtt atgaacttcg aagatggtgg cgcggtgacc gttacccagg acaccagcct
     3841 ggaggatggc accctgattt acaaggtgaa actgcgtggc accaactttc cgccggatgg
     3901 tccggttatg cagaagaaaa cgatgggttg ggaagcgagc accgagcgtc tgtatccgga
     3961 agatggcgtg ctgaagggtg atatcaaaat ggcgctgcgt ctgaaggacg gtggccgtta
     4021 cctggcggat tttaagacca cctataaagc gaagaaaccg gtgcaaatgc cgggtgcgta
     4081 caacgttgac cgtaaactgg atattaccag ccacaacgag gattataccg tggttgagca
     4141 atatgagcgt agcgagggtc gccacagcac cggcggcatg gacgaactgt ataagggatc
     4201 ctaataacgc tgatagtgct agtgtagatc gctactagag ccaggcatca aataaaacga
     4261 aaggctcagt cgaaagactg ggcctttcgt tttatctgtt gtttgtcggt gaacgctctc
     4321 tactagagtc acactggctc accttcgggt gggcctttct gcgtttatat actggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and pBBR1 origin of replication.",
                    "label": "BASIC_SEVA_53",
                },
                {
                    "accessor": "54",
                    "binaryString": """LOCUS       BASIC_SEVA_54           4630 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and
            pRO1600/ColE1 origin of replication..
ACCESSION   15433d91d38015969dce8c44b3dd1736
VERSION     15433d91d38015969dce8c44b3dd1736
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    195..1461
                     /label="SEVA_Tet"
     misc_feature    1535..3503
                     /label="SEVA_pRO1600/ColE1"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    join(4625..4630,1..51)
                     /label="LMP"
     misc_feature    3632..3688
                     /label="LMS"
     misc_feature    3689..3723
                     /label="J23105"
     misc_feature    4492..4620
                     /label="B0015"
     misc_feature    3732..3743
                     /label="B0034"
     CDS             3751..4455
                     /label="mScarlett"
     misc_feature    3518..3622
                     /label="SEVA_T1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggccgataat ctcatgacca aaatccctta
     1561 acgtgagttt tcgttccact gagcgtcaga ccccgtagaa aagatcaaag gatcttcttg
     1621 agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac cgctaccagc
     1681 ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa ctggcttcag
     1741 cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc accacttcaa
     1801 gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag tggctgctgc
     1861 cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac cggataaggc
     1921 gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc gaacgaccta
     1981 caccgaactg agatacctac agcgtgagct atgagaaagc gccacgcttc ccgaagggag
     2041 aaaggcggac aggcatccgg taagcggcag ggtcggaaca ggagagcgca cgagggagct
     2101 tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc tctgacttga
     2161 gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg ccagcaacgc
     2221 ggccgtgaaa ggcaggccgg tccgtggtgg ccacggcctc taggccagat ccagcggcat
     2281 ctgggttagt cgagcgcggg ccgcttccca tgtctcacca gggcgagcct gtttcgcgat
     2341 ctcagcatct gaaatcttcc cggccttgcg cttcgctggg gccttaccca ccgccttggc
     2401 gggcttcttc ggtccaaaac tgaacaacag atgtgtgacc ttgcgcccgg tctttcgctg
     2461 cgcccactcc acctgtagcg ggctgtgctc gttgatctgc gtcacggctg gatcaagcac
     2521 tcgcaacttg aagtccttga tcgagggata ccggccttcc agttgaaacc actttcgcag
     2581 ctggtcaatt tctatttcgc gctggccgat gctgtcccat tgcatgagca gctcgtaaag
     2641 cctgatcgcg tgggtgctgt ccatcttggc cacgtcagcc aaggcgtatt tggtgaactg
     2701 tttggtgagt tccgtcaggt acggcagcat gtctttggtg aacctgagtt ctacacggcc
     2761 ctcaccctcc cggtagatga ttgtttgcac ccagccggta atcatcacac tcggtctttt
     2821 ccccttgcca ttgggctctt gggttaaccg gacttcccgc cgtttcaggc gcagggccgc
     2881 ttctttgagc tggttgtagg aagattcgat agggacaccc gccatcgtcg ctatgtcctc
     2941 cgccgtcact gaatacatca cttcatcggt gacaggctcg ctcctcttca cctggctaat
     3001 acaggccaga acgatccgct gttcctgaac actgaggcga tacgcggcct cgaccagggc
     3061 attgcttttg taaaccattg ggggtgaggc cacgttcgac attccttgtg tataagggga
     3121 cactgtatct gcgtcccaca atacaacaaa tccgtccctt tacaacaaca aatccgtccc
     3181 ttcttaacaa caaatccgtc ccttaatggc aacaaatccg tcccttttta aactctacag
     3241 gccacggatt acgtggcctg tagacgtcct aaaaggttta aaagggaaaa ggaagaaaag
     3301 ggtggaaacg caaaaaacgc accactacgt ggccccgttg gggccgcatt tgtgcccctg
     3361 aaggggcggg ggaggcgtct gggcaatccc cgttttacca gtcccctatc gccgcctgag
     3421 agggcgcagg aagcgagtaa tcagggtatc gaggcggatt cacccttggc gtccaaccag
     3481 cggcaccagc ggcgcctgag aggggcgcgc ccagctgtct agggcggcgg atttgtccta
     3541 ctcaggagag cgttcaccga caaacaacag ataaaacgaa aggcccagtc tttcgactga
     3601 gcctttcgtt ttatttgatg cctttaatta aggctcggga gacctatcgg taataacagt
     3661 ccaatctggt gtaacttcgg aatcgtcctt tacggctagc tcagtcctag gtactatgct
     3721 agctactagt gaaagaggag aaatactagt atggttagca aaggcgaggc ggttatcaag
     3781 gagtttatgc gttttaaggt tcacatggag ggtagcatga atggtcacga gttcgagatc
     3841 gagggtgaag gcgagggtcg tccgtacgaa ggcacccaga ccgcgaagct gaaagtgacc
     3901 aagggtggcc cgctgccgtt cagctgggac atcctgagcc cgcagttcat gtatggcagc
     3961 cgtgcgttta ccaaacaccc ggcggacatt ccggattact ataagcaaag cttcccggaa
     4021 ggttttaaat gggagcgtgt tatgaacttc gaagatggtg gcgcggtgac cgttacccag
     4081 gacaccagcc tggaggatgg caccctgatt tacaaggtga aactgcgtgg caccaacttt
     4141 ccgccggatg gtccggttat gcagaagaaa acgatgggtt gggaagcgag caccgagcgt
     4201 ctgtatccgg aagatggcgt gctgaagggt gatatcaaaa tggcgctgcg tctgaaggac
     4261 ggtggccgtt acctggcgga ttttaagacc acctataaag cgaagaaacc ggtgcaaatg
     4321 ccgggtgcgt acaacgttga ccgtaaactg gatattacca gccacaacga ggattatacc
     4381 gtggttgagc aatatgagcg tagcgagggt cgccacagca ccggcggcat ggacgaactg
     4441 tataagggat cctaataacg ctgatagtgc tagtgtagat cgctactaga gccaggcatc
     4501 aaataaaacg aaaggctcag tcgaaagact gggcctttcg ttttatctgt tgtttgtcgg
     4561 tgaacgctct ctactagagt cacactggct caccttcggg tgggcctttc tgcgtttata
     4621 tactggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and pRO1600/ColE1 origin of replication.",
                    "label": "BASIC_SEVA_54",
                },
                {
                    "accessor": "55",
                    "binaryString": """LOCUS       BASIC_SEVA_55           6335 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and
            RSF1010 origin of replication..
ACCESSION   958bce75e4cb6c99ecf451f888f9fd07
VERSION     958bce75e4cb6c99ecf451f888f9fd07
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    5437..5448
                     /label="B0034"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    5337..5393
                     /label="LMS"
     misc_feature    join(6330..6335,1..51)
                     /label="LMP"
     misc_feature    195..1461
                     /label="SEVA_Tet"
     CDS             5456..6160
                     /label="mScarlett"
     misc_feature    6197..6325
                     /label="B0015"
     misc_feature    5394..5428
                     /label="J23119"
     misc_feature    1535..5208
                     /label="SEVA_RSF101"
     misc_feature    5223..5327
                     /label="SEVA_T1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggcctcagcc tgccgccttg ggccgggtga
     1561 tgtcgtactt gcccgccgcg aactcggtta ccgtccagcc cagcgcgacc agctccggca
     1621 acgcctcgcg cacccgctgg cggcgcttgc gcatggtcga accactggcc tctgacggcc
     1681 agacatagcc gcacaaggta tctatggaag ccttgccggt tttgccgggg tcgatccagc
     1741 cacacagccg ctggtgcagc aggcgggcgg tttcgctgtc cagcgcccgc acctcgtcca
     1801 tgctgatgcg cacatgctgg ccgccaccca tgacggcctg cgcgatcaag gggttcaggg
     1861 ccacgtacag gcgcccgtcc gcctcgtcgc tggcgtactc cgacagcagc cgaaacccct
     1921 gccgcttgcg gccattctgg gcgatgatgg ataccttcca aaggcgctcg atgcagtcct
     1981 gtatgtgctt gagcgcccca ccactatcga cctctgcccc gatttccttt gccagcgccc
     2041 gatagctacc tttgaccaca tggcattcag cggtgacggc ctcccacttg ggttccagga
     2101 acagccggag ctgccgtccg ccttcggtct tgggttccgg gccaagcact aggccattag
     2161 gcccagccat ggccaccagc ccttgcagga tgcgcagatc atcagcgccc agcggctccg
     2221 ggccgctgaa ctcgatccgc ttgccgtcgc cgtagtcata cgtcacgtcc agcttgctgc
     2281 gcttgcgctc gccccgcttg agggcacgga acaggccggg ggccagacag tgcgccgggt
     2341 cgtgccggac gtggctgagg ctgtgcttgt tcttaggctt caccacgggg cacccccttg
     2401 ctcttgcgct gcctctccag cacggcgggc ttgagcaccc cgccgtcatg ccgcctgaac
     2461 caccgatcag cgaacggtgc gccatagttg gccttgctca caccgaagcg gacgaagaac
     2521 cggcgctggt cgtcgtccac accccattcc tcggcctcgg cgctggtcat gctcgacagg
     2581 taggactgcc agcggatgtt atcgaccagt accgagctgc cccggctggc ctgctgctgg
     2641 tcgcctgcgc ccatcatggc cgcgcccttg ctggcatggt gcaggaacac gatagagcac
     2701 ccggtatcgg cggcgatggc ctccatgcga ccgatgacct gggccatggg gccgctggcg
     2761 ttttcttcct cgatgtggaa ccggcgcagc gtgtccagca ccatcaggcg gcggccctcg
     2821 gcggcgcgct tgaggccgtc gaaccactcc ggggccatga tgttgggcag gctgccgatc
     2881 agcggctgga tcagcaggcc gtcagccacg gcttgccgtt cctcggcgct gaggtgcgcc
     2941 ccaagggcgt gcaggcggtg atgaatggcg gtgggcgggt cttcggcggg caggtagatc
     3001 accgggccgg tgggcagttc gcccacctcc agcagatccg gcccgcctgc aatctgtgcg
     3061 gccagttgca gggccagcat ggatttaccg gcaccaccgg gcgacaccag cgccccgacc
     3121 gtaccggcca ccatgttggg caaaacgtag tccagcggtg gcggcgctgc tgcgaacgcc
     3181 tccagaatat tgataggctt atgggtagcc attgattgcc tcctttgcag gcagttggtg
     3241 gttaggcgct ggcggggtca ctacccccgc cctgcgccgc tctgagttct tccaggcact
     3301 cgcgcagcgc ctcgtattcg tcgtcggtca gccagaactt gcgctgacgc atccctttgg
     3361 ccttcatgcg ctcggcatat cgcgcttggc gtacagcgtc agggctggcc agcaggtcgc
     3421 cggtctgctt gtccttttgg tctttcatat cagtcaccga gaaacttgcc ggggccgaaa
     3481 ggcttgtctt cgcggaacaa ggacaaggtg cagccgtcaa ggttaaggct ggccatatca
     3541 gcgactgaaa agcggccagc ctcggccttg tttgacgtat aaccaaagcc accgggcaac
     3601 caatagccct tgtcactttt gatcaggtag accgaccctg aagcgctttt ttcgtattcc
     3661 ataaaacccc cttctgtgcg tgagtactca tagtataaca ggcgtgagta ccaacgcaag
     3721 cactacatgc tgaaatctgg cccgcccctg tccatgcctc gctggcgggg tgccggtgcc
     3781 cgtgccagct cggcccgcgc aagctggacg ctgggcagac ccatgacctt gctgacggtg
     3841 cgctcgatgt aatccgcttc gtggccgggc ttgcgctctg ccagcgctgg gctggcctcg
     3901 gccatggcct tgccgatttc ctcggcactg cggccccggc tggccagctt ctgcgcggcg
     3961 ataaagtcgc acttgctgag gtcatcaccg aagcgcttga ccagcccggc catctcgctg
     4021 cggtactcgt ccagcgccgt gcgccggtgg cggctaagct gccgctcggg cagttcgagg
     4081 ctggccagcc tgcgggcctt ctcctgctgc cgctgggcct gctcgatctg ctggccagcc
     4141 tgctgcacca gcgccgggcc agcggtggcg gtcttgccct tggattcacg cagcagcacc
     4201 cacggctgat aaccggcgcg ggtggtgtgc ttgtccttgc ggttggtgaa gcccgccaag
     4261 cggccatagt ggcggctgtc ggcgctggcc gggtcggcgt cgtactcgct ggccagcgtc
     4321 cgggcaatct gcccccgaag ttcaccgcct gcggcgtcgg ccaccttgac ccatgcctga
     4381 tagttcttcg ggctggtttc cactaccagg gcaggctccc ggccctcggc tttcatgtca
     4441 tccaggtcaa actcgctgag gtcgtccacc agcaccagac catgccgctc ctgctcggcg
     4501 ggcctgatat acacgtcatt gccctgggca ttcatccgct tgagccatgg cgtgttctgg
     4561 agcacttcgg cggctgacca ttcccggttc atcatctggc cggtggtggc gtccctgacg
     4621 ccgatatcga agcgctcaca gcccatggcc ttgagctgtc ggcctatggc ctgcaaagtc
     4681 ctgtcgttct tcatcgggcc accaagcgat tcccacacat tatacgagcc ggaagcataa
     4741 agtgtaaagc ctagatccga aggatgagcc gggctgaatg atcgaccgag acaggccctg
     4801 cggggctgca cacgcgcccc cacccttcgg gtagggggaa aggccgctaa agcggctaaa
     4861 agcgctccag cgtatttctg cggggtttgg tgtggggttt agcgggcttt gcccgccttt
     4921 ccccctgccg cgcagcggtg gggcggtgtg tagcctagcg cagcgaatag accagctatc
     4981 cggcctctgg ccgggcatat tgggcaaggg cagcagcgcc ccacaagggc gctgataacc
     5041 gcgcctagtg gattattctt agataatcat ggatggattt ttccaacacc ccgccagccc
     5101 ccgcccctgc tgggtttgca ggtttggggg cgtgacagtt attgcagggg ttcgtgacag
     5161 ttattgcagg ggggcgtgac agttattgca ggggttcgtg acagttaggg cgcgcccagc
     5221 tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac aacagataaa
     5281 acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt aattaaggct
     5341 cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg tccttgacag
     5401 ctagctcagt cctaggtata atgctagcta ctagtgaaag aggagaaata ctagtatggt
     5461 tagcaaaggc gaggcggtta tcaaggagtt tatgcgtttt aaggttcaca tggagggtag
     5521 catgaatggt cacgagttcg agatcgaggg tgaaggcgag ggtcgtccgt acgaaggcac
     5581 ccagaccgcg aagctgaaag tgaccaaggg tggcccgctg ccgttcagct gggacatcct
     5641 gagcccgcag ttcatgtatg gcagccgtgc gtttaccaaa cacccggcgg acattccgga
     5701 ttactataag caaagcttcc cggaaggttt taaatgggag cgtgttatga acttcgaaga
     5761 tggtggcgcg gtgaccgtta cccaggacac cagcctggag gatggcaccc tgatttacaa
     5821 ggtgaaactg cgtggcacca actttccgcc ggatggtccg gttatgcaga agaaaacgat
     5881 gggttgggaa gcgagcaccg agcgtctgta tccggaagat ggcgtgctga agggtgatat
     5941 caaaatggcg ctgcgtctga aggacggtgg ccgttacctg gcggatttta agaccaccta
     6001 taaagcgaag aaaccggtgc aaatgccggg tgcgtacaac gttgaccgta aactggatat
     6061 taccagccac aacgaggatt ataccgtggt tgagcaatat gagcgtagcg agggtcgcca
     6121 cagcaccggc ggcatggacg aactgtataa gggatcctaa taacgctgat agtgctagtg
     6181 tagatcgcta ctagagccag gcatcaaata aaacgaaagg ctcagtcgaa agactgggcc
     6241 tttcgtttta tctgttgttt gtcggtgaac gctctctact agagtcacac tggctcacct
     6301 tcgggtgggc ctttctgcgt ttatatactg gctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and RSF1010 origin of replication.",
                    "label": "BASIC_SEVA_55",
                },
                {
                    "accessor": "56",
                    "binaryString": """LOCUS       BASIC_SEVA_56           3393 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and p15A
            origin of replication..
ACCESSION   51852c5b59b43f6944de097f3ccb6d8e
VERSION     51852c5b59b43f6944de097f3ccb6d8e
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2395..2451
                     /label="LMS"
     misc_feature    join(3388..3393,1..51)
                     /label="LMP"
     misc_feature    195..1461
                     /label="SEVA_Tet"
     CDS             2514..3218
                     /label="mScarlett"
     misc_feature    3255..3383
                     /label="B0015"
     misc_feature    2281..2385
                     /label="SEVA_T1"
     misc_feature    2495..2506
                     /label="B0034"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2452..2486
                     /label="J23119"
     misc_feature    1535..2266
                     /label="SEVA_p15A"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggccctagaa atattttatc tgattaataa
     1561 gatgatcttc ttgagatcgt tttggtctgc gcgtaatctc ttgctctgaa aacgaaaaaa
     1621 ccgccttgca gggcggtttt tcgaaggttc tctgagctac caactctttg aaccgaggta
     1681 actggcttgg aggagcgcag tcaccaaaac ttgtcctttc agtttagcct taaccggcgc
     1741 atgacttcaa gactaactcc tctaaatcaa ttaccagtgg ctgctgccag tggtgctttt
     1801 gcatgtcttt ccgggttgga ctcaagacga tagttaccgg ataaggcgca gcggtcggac
     1861 tgaacggggg gttcgtgcat acagtccagc ttggagcgaa ctgcctaccc ggaactgagt
     1921 gtcaggcgtg gaatgagaca aacgcggcca taacagcgga atgacaccgg taaaccgaaa
     1981 ggcaggaaca ggagagcgca cgagggagcc gccaggggga aacgcctggt atctttatag
     2041 tcctgtcggg tttcgccacc actgatttga gcgtcagatt tcgtgatgct tgtcaggggg
     2101 gcggagccta tggaaaaacg gctttgccgc ggccctctca cttccctgtt aagtatcttc
     2161 ctggcatctt ccaggaaatc tccgccccgt tcgtaagcca tttccgctcg ccgcagtcga
     2221 acgaccgagc gtagcgagtc agtgagcgag gaagcggaat atatccggcg cgcccagctg
     2281 tctagggcgg cggatttgtc ctactcagga gagcgttcac cgacaaacaa cagataaaac
     2341 gaaaggccca gtctttcgac tgagcctttc gttttatttg atgcctttaa ttaaggctcg
     2401 ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc cttgacagct
     2461 agctcagtcc taggtataat gctagctact agtgaaagag gagaaatact agtatggtta
     2521 gcaaaggcga ggcggttatc aaggagttta tgcgttttaa ggttcacatg gagggtagca
     2581 tgaatggtca cgagttcgag atcgagggtg aaggcgaggg tcgtccgtac gaaggcaccc
     2641 agaccgcgaa gctgaaagtg accaagggtg gcccgctgcc gttcagctgg gacatcctga
     2701 gcccgcagtt catgtatggc agccgtgcgt ttaccaaaca cccggcggac attccggatt
     2761 actataagca aagcttcccg gaaggtttta aatgggagcg tgttatgaac ttcgaagatg
     2821 gtggcgcggt gaccgttacc caggacacca gcctggagga tggcaccctg atttacaagg
     2881 tgaaactgcg tggcaccaac tttccgccgg atggtccggt tatgcagaag aaaacgatgg
     2941 gttgggaagc gagcaccgag cgtctgtatc cggaagatgg cgtgctgaag ggtgatatca
     3001 aaatggcgct gcgtctgaag gacggtggcc gttacctggc ggattttaag accacctata
     3061 aagcgaagaa accggtgcaa atgccgggtg cgtacaacgt tgaccgtaaa ctggatatta
     3121 ccagccacaa cgaggattat accgtggttg agcaatatga gcgtagcgag ggtcgccaca
     3181 gcaccggcgg catggacgaa ctgtataagg gatcctaata acgctgatag tgctagtgta
     3241 gatcgctact agagccaggc atcaaataaa acgaaaggct cagtcgaaag actgggcctt
     3301 tcgttttatc tgttgtttgt cggtgaacgc tctctactag agtcacactg gctcaccttc
     3361 gggtgggcct ttctgcgttt atatactggc tcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and p15A origin of replication.",
                    "label": "BASIC_SEVA_56",
                },
                {
                    "accessor": "57",
                    "binaryString": """LOCUS       BASIC_SEVA_57           4317 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and
            pSC101 origin of replication..
ACCESSION   1717a522fb5416a5f5f9666578dee856
VERSION     1717a522fb5416a5f5f9666578dee856
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3123..3179
                     /label="LMS"
     misc_feature    195..1461
                     /label="SEVA_Tet"
     CDS             3438..4142
                     /label="mScarlett"
     misc_feature    join(4312..4317,1..51)
                     /label="LMP"
     misc_feature    4179..4307
                     /label="B0015"
     misc_feature    3272..3306
                     /label="J23119"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    1535..2994
                     /label="SEVA_pSC101"
     misc_feature    3009..3113
                     /label="SEVA_T1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggcctcagat ccttccgtat ttagccagta
     1561 tgttctctag tgtggttcgt tgtttttgcg tgagccatga gaacgaacca ttgagatcat
     1621 acttactttg catgtcactc aaaaattttg cctcaaaact ggtgagctga atttttgcag
     1681 ttaaagcatc gtgtagtgtt tttcttagtc cgttatgtag gtaggaatct gatgtaatgg
     1741 ttgttggtat tttgtcacca ttcattttta tctggttgtt ctcaagttcg gttacgagat
     1801 ccatttgtct atctagttca acttggaaaa tcaacgtatc agtcgggcgg cctcgcttat
     1861 caaccaccaa tttcatattg ctgtaagtgt ttaaatcttt acttattggt ttcaaaaccc
     1921 attggttaag ccttttaaac tcatggtagt tattttcaag cattaacatg aacttaaatt
     1981 catcaaggct aatctctata tttgccttgt gagttttctt ttgtgttagt tcttttaata
     2041 accactcata aatcctcata gagtatttgt tttcaaaaga cttaacatgt tccagattat
     2101 attttatgaa tttttttaac tggaaaagat aaggcaatat ctcttcacta aaaactaatt
     2161 ctaatttttc gcttgagaac ttggcatagt ttgtccactg gaaaatctca aagcctttaa
     2221 ccaaaggatt cctgatttcc acagttctcg tcatcagctc tctggttgct ttagctaata
     2281 caccataagc attttcccta ctgatgttca tcatctgagc gtattggtta taagtgaacg
     2341 ataccgtccg ttctttcctt gtagggtttt caatcgtggg gttgagtagt gccacacagc
     2401 ataaaattag cttggtttca tgctccgtta agtcatagcg actaatcgct agttcatttg
     2461 ctttgaaaac aactaattca gacatacatc tcaattggtc taggtgattt taatcactat
     2521 accaattgag atgggctagt caatgataat tacatgtcct tttcctttga gttgtgggta
     2581 tctgtaaatt ctgctagacc tttgctggaa aacttgtaaa ttctgctaga ccctctgtaa
     2641 attccgctag acctttgtgt gttttttttg tttatattca agtggttata atttatagaa
     2701 taaagaaaga ataaaaaaag ataaaaagaa tagatcccag ccctgtgtat aactcactac
     2761 tttagtcagt tccgcagtat tacaaaagga tgtcgcaaac gctgtttgct cctctacaaa
     2821 acagacctta aaaccctaaa ggcttaagta gcaccctcgc aagctcgggc aaatcgctga
     2881 atattccttt tgtctccgac catcaggcac ctgagtcgct gtctttttcg tgacattcag
     2941 ttcgctgcgc tcacggctct ggcagtgaat gggggtaaat ggcactacag gcgcggcgcg
     3001 cccagctgtc tagggcggcg gatttgtcct actcaggaga gcgttcaccg acaaacaaca
     3061 gataaaacga aaggcccagt ctttcgactg agcctttcgt tttatttgat gcctttaatt
     3121 aaggctcggg agacctatcg gtaataacag tccaatctgg tgtaacttcg gaatcgtccc
     3181 caattattga acacccttcg gggtgttttt ttgtttctgg tctaccatct cgttgtgata
     3241 atagacctga agtgcctact ctggaaaatc tttgacagct agctcagtcc taggtataat
     3301 gctagcagct gtcaccggat gtgctttccg gtctgatgag tccgtgagga cgaaacagcc
     3361 tctacaaata attttgttta aggctcgcta cgagaagatt gttactttcg cagcgttatt
     3421 atctaaggag gtagtccatg gttagcaaag gcgaggcggt tatcaaggag tttatgcgtt
     3481 ttaaggttca catggagggt agcatgaatg gtcacgagtt cgagatcgag ggtgaaggcg
     3541 agggtcgtcc gtacgaaggc acccagaccg cgaagctgaa agtgaccaag ggtggcccgc
     3601 tgccgttcag ctgggacatc ctgagcccgc agttcatgta tggcagccgt gcgtttacca
     3661 aacacccggc ggacattccg gattactata agcaaagctt cccggaaggt tttaaatggg
     3721 agcgtgttat gaacttcgaa gatggtggcg cggtgaccgt tacccaggac accagcctgg
     3781 aggatggcac cctgatttac aaggtgaaac tgcgtggcac caactttccg ccggatggtc
     3841 cggttatgca gaagaaaacg atgggttggg aagcgagcac cgagcgtctg tatccggaag
     3901 atggcgtgct gaagggtgat atcaaaatgg cgctgcgtct gaaggacggt ggccgttacc
     3961 tggcggattt taagaccacc tataaagcga agaaaccggt gcaaatgccg ggtgcgtaca
     4021 acgttgaccg taaactggat attaccagcc acaacgagga ttataccgtg gttgagcaat
     4081 atgagcgtag cgagggtcgc cacagcaccg gcggcatgga cgaactgtat aagggatcct
     4141 aataacgctg atagtgctag tgtagatcgc tactagagcc aggcatcaaa taaaacgaaa
     4201 ggctcagtcg aaagactggg cctttcgttt tatctgttgt ttgtcggtga acgctctcta
     4261 ctagagtcac actggctcac cttcgggtgg gcctttctgc gtttatatac tggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and pSC101 origin of replication.",
                    "label": "BASIC_SEVA_57",
                },
                {
                    "accessor": "58",
                    "binaryString": """LOCUS       BASIC_SEVA_58           3590 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and pUC
            origin of replication..
ACCESSION   477b1d2b812116bc6151f3e4a1a0c635
VERSION     477b1d2b812116bc6151f3e4a1a0c635
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    1535..2463
                     /label="SEVA_pUC"
     misc_feature    2478..2582
                     /label="SEVA_T1"
     misc_feature    195..1461
                     /label="SEVA_Tet"
     misc_feature    join(3585..3590,1..51)
                     /label="LMP"
     misc_feature    2649..2683
                     /label="J23106"
     misc_feature    2692..2703
                     /label="B0034"
     CDS             2711..3415
                     /label="mScarlett"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2592..2648
                     /label="LMS"
     misc_feature    3452..3580
                     /label="B0015"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggccccgtag aaaagatcaa aggatcttct
     1561 tgagatcctt tttttctgcg cgtaatctgc tgcttgcaaa caaaaaaacc accgctacca
     1621 gcggtggttt gtttgccgga tcaagagcta ccaactcttt ttccgaaggt aactggcttc
     1681 agcagagcgc agataccaaa tactgttctt ctagtgtagc cgtagttagg ccaccacttc
     1741 aagaactctg tagcaccgcc tacatacctc gctctgctaa tcctgttacc agtggctgct
     1801 gccagtggcg ataagtcgtg tcttaccggg ttggactcaa gacgatagtt accggataag
     1861 gcgcagcggt cgggctgaac ggggggttcg tgcacacagc ccagcttgga gcgaacgacc
     1921 tacaccgaac tgagatacct acagcgtgag ctttgagaaa gcgccacgct tcccgaaggg
     1981 agaaaggcgg acaggtatcc ggtaagcggc agggtcggaa caggagagcg cacgagggag
     2041 cttccagggg gaaacgcctg gtatctttat agtcctgtcg ggtttcgcca cctctgactt
     2101 gagcgtcgat ttttgtgatg ctcgtcaggg gggcggagcc tatggaaaaa cgccagcaac
     2161 gcggcctttt tacggttcct ggccttttgc tggccttttg ctcacatgtt ctttcctgcg
     2221 ttatcccctg attctgtgga taaccgtatt accgcctttg agtgagctga taccgctcgc
     2281 cgcagccgaa cgaccgagcg cagcgagtca gtgagcgagg aagcggaaga gcgcccaata
     2341 cgcaaaccgc ctctccccgc gcgttggccg attcattaat gcagctggca cgacaggttt
     2401 cccgactgga aagcgggcag tgagcgcaac gcaattaatg tgagttagct cactcattag
     2461 gcaggcgcgc ccagctgtct agggcggcgg atttgtccta ctcaggagag cgttcaccga
     2521 caaacaacag ataaaacgaa aggcccagtc tttcgactga gcctttcgtt ttatttgatg
     2581 cctttaatta aggctcggga gacctatcgg taataacagt ccaatctggt gtaacttcgg
     2641 aatcgtcctt tacggctagc tcagtcctag gtatagtgct agctactagt gaaagaggag
     2701 aaatactagt atggttagca aaggcgaggc ggttatcaag gagtttatgc gttttaaggt
     2761 tcacatggag ggtagcatga atggtcacga gttcgagatc gagggtgaag gcgagggtcg
     2821 tccgtacgaa ggcacccaga ccgcgaagct gaaagtgacc aagggtggcc cgctgccgtt
     2881 cagctgggac atcctgagcc cgcagttcat gtatggcagc cgtgcgttta ccaaacaccc
     2941 ggcggacatt ccggattact ataagcaaag cttcccggaa ggttttaaat gggagcgtgt
     3001 tatgaacttc gaagatggtg gcgcggtgac cgttacccag gacaccagcc tggaggatgg
     3061 caccctgatt tacaaggtga aactgcgtgg caccaacttt ccgccggatg gtccggttat
     3121 gcagaagaaa acgatgggtt gggaagcgag caccgagcgt ctgtatccgg aagatggcgt
     3181 gctgaagggt gatatcaaaa tggcgctgcg tctgaaggac ggtggccgtt acctggcgga
     3241 ttttaagacc acctataaag cgaagaaacc ggtgcaaatg ccgggtgcgt acaacgttga
     3301 ccgtaaactg gatattacca gccacaacga ggattatacc gtggttgagc aatatgagcg
     3361 tagcgagggt cgccacagca ccggcggcat ggacgaactg tataagggat cctaataacg
     3421 ctgatagtgc tagtgtagat cgctactaga gccaggcatc aaataaaacg aaaggctcag
     3481 tcgaaagact gggcctttcg ttttatctgt tgtttgtcgg tgaacgctct ctactagagt
     3541 cacactggct caccttcggg tgggcctttc tgcgtttata tactggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and pUC origin of replication.",
                    "label": "BASIC_SEVA_58",
                },
                {
                    "accessor": "59",
                    "binaryString": """LOCUS       BASIC_SEVA_59           4046 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Tetracycline resistance marker and
            pBR322-ROP origin of replication..
ACCESSION   c169e83a91a8e4453627ae72c10f6bf0
VERSION     c169e83a91a8e4453627ae72c10f6bf0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    1535..2919
                     /label="SEVA_pBR322-ROP"
     misc_feature    3908..4036
                     /label="B0015"
     misc_feature    join(4041..4046,1..51)
                     /label="LMP"
     misc_feature    3105..3139
                     /label="J23119"
     misc_feature    3148..3159
                     /label="B0034"
     misc_feature    3048..3104
                     /label="LMS"
     misc_feature    2934..3038
                     /label="SEVA_T1"
     CDS             3167..3871
                     /label="mScarlett"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    195..1461
                     /label="SEVA_Tet"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttacgtattt aaatttgaca gcttatcatc gataaactgt aatgcggtag tttatcacag
      241 ttaaattgct aacgcagtca ggcaccgtgt atgaaatcta acaatgcgct catcgtcatc
      301 ctcggcaccg tcaccctgga tgctgtaggc ataggcttgg ttatgccggt actgccgggc
      361 ctcttgcggg atatcgtcca ttccgacagc atcgccagtc actatggcgt gctgctagcg
      421 ctatatgcgt tgatgcaatt tctatgcgca cccgttctcg gagcactgtc cgaccgcttt
      481 ggccgccgcc cagtcctgct cgcttcgcta cttggagcca ctatcgacta cgcgatcatg
      541 gcgaccacac ccgtcctgtg gattctctac gccggacgca tcgtggccgg catcaccggc
      601 gccacaggtg cggttgctgg cgcctatatc gccgacatca ccgatgggga agatcgggct
      661 cgccacttcg ggctcatgag cgcttgtttc ggcgtgggta tggtggcagg ccccgtggcc
      721 gggggactgt tgggcgccat ctccctgcac gcaccattcc ttgcggcggc ggtgctcaac
      781 ggcctcaacc tactactggg ctgcttccta atgcaggagt cgcataaggg agagcgccgt
      841 ccgatgccct tgagagcctt caacccagtc agctccttcc ggtgggcgcg gggcatgacc
      901 attgtggccg cacttatgac tgtcttcttt atcatgcaac tcgtaggaca ggtgccggca
      961 gcgctctggg tcattttcgg cgaggaccgc tttcgctgga gcgcgacgat gatcggcctg
     1021 tcgcttgcgg tattcggaat cttgcacgcc ctcgctcaag ccttcgtcac tggtcccgcc
     1081 accaaacgtt tcggcgagaa gcaggccatt atcgccggca tggcggccga cgcgctgggc
     1141 tacgtcttgc tggcgttcgc gacgcgaggc tggatggcct tccccattat gattcttctc
     1201 gcttccggcg gcatcgggat gcccgcgttg caggccatgc tgtccaggca ggtagatgac
     1261 gaccatcagg gacagcttca aggatcgctc gcggctctta ccagcctaac ttcgatcact
     1321 ggaccgctga tcgtcacggc gatttatgcc gcctcggcga gcacatggaa cgggttggca
     1381 tggattgtag gcgccgccct ataccttgtc tgcctccccg cgttgcgtcg cggtgcatgg
     1441 agccgggcca cctcgacctg agacaattgt cggctcgacc cacgactatt gactgctctg
     1501 agaaagttga ttgttacgat tagtccggcc ggccccgtag aaaagatcaa aggatcttct
     1561 tgagatcctt tttttctgcg cgtaatctgc tgcttgcaaa caaaaaaacc accgctacca
     1621 gcggtggttt gtttgccgga tcaagagcta ccaactcttt ttccgaaggt aactggcttc
     1681 agcagagcgc agataccaaa tactgtcctt ctagtgtagc cgtagttagg ccaccacttc
     1741 aagaactctg tagcaccgcc tacatacctc gctctgctaa tcctgttacc agtggctgct
     1801 gccagtggcg ataagtcgtg tcttaccggg ttggactcaa gacgatagtt accggataag
     1861 gcgcagcggt cgggctgaac ggggggttcg tgcacacagc ccagcttgga gcgaacgacc
     1921 tacaccgaac tgagatacct acagcgtgag ctatgagaaa gcgccacgct tcccgaaggg
     1981 agaaaggcgg acaggtatcc ggtaagcggc agggtcggaa caggagagcg cacgagggag
     2041 cttccagggg gaaacgcctg gtatctttat agtcctgtcg ggtttcgcca cctctgactt
     2101 gagcgtcgat ttttgtgatg ctcgtcaggg gggcggagcc tatggaaaaa cgccagcaac
     2161 gcggcctttt tacggttcct ggccttttgc tggccttttg ctcacatgtt ctttcctgcg
     2221 ttatcccctg attctgtgga taaccgtatt accgcctttg agtgagctga taccgctcgc
     2281 cgcagccgaa cgaccgagcg cagcgagtca gtgagcgagg aagcggaaga gcgcctgatg
     2341 cggtattttc tccttacgca tctgtgcggt atttcacacc gcatatggtg cactctcagt
     2401 acaatctgct ctgatgccgc atagttaagc cagtatacac tccgctatcg ctacgtgact
     2461 gggtcatggc tgcgccccga cacccgccaa cacccgctga cgcgccctga cgggcttgtc
     2521 tgctcccggc atccgcttac agacaagctg tgaccgtctc cgggagctgc atgtgtcaga
     2581 ggttttcacc gtcatcaccg aaacgcgcga ggcagctgcg gtaaagctca tcagcgtggt
     2641 cgtgcagcga ttcacagatg tctgcctgtt catccgcgtc cagctcgttg agtttctcca
     2701 gaagcgttaa tgtctggctt ctgataaagc gggccatgtt aagggcggtt ttttcctgtt
     2761 tggtcactga tgcctccgtg taagggggat ttctgttcat gggggtaatg ataccgatga
     2821 aacgagagag gatgctcacg atacgggtta ctgatgatga acatgcccgg ttactggaac
     2881 gttgtgaggg taaacaactg gcggtatgga tgcggcgggg gcgcgcccag ctgtctaggg
     2941 cggcggattt gtcctactca ggagagcgtt caccgacaaa caacagataa aacgaaaggc
     3001 ccagtctttc gactgagcct ttcgttttat ttgatgcctt taattaaggc tcgggagacc
     3061 tatcggtaat aacagtccaa tctggtgtaa cttcggaatc gtccttgaca gctagctcag
     3121 tcctaggtat aatgctagct actagtgaaa gaggagaaat actagtatgg ttagcaaagg
     3181 cgaggcggtt atcaaggagt ttatgcgttt taaggttcac atggagggta gcatgaatgg
     3241 tcacgagttc gagatcgagg gtgaaggcga gggtcgtccg tacgaaggca cccagaccgc
     3301 gaagctgaaa gtgaccaagg gtggcccgct gccgttcagc tgggacatcc tgagcccgca
     3361 gttcatgtat ggcagccgtg cgtttaccaa acacccggcg gacattccgg attactataa
     3421 gcaaagcttc ccggaaggtt ttaaatggga gcgtgttatg aacttcgaag atggtggcgc
     3481 ggtgaccgtt acccaggaca ccagcctgga ggatggcacc ctgatttaca aggtgaaact
     3541 gcgtggcacc aactttccgc cggatggtcc ggttatgcag aagaaaacga tgggttggga
     3601 agcgagcacc gagcgtctgt atccggaaga tggcgtgctg aagggtgata tcaaaatggc
     3661 gctgcgtctg aaggacggtg gccgttacct ggcggatttt aagaccacct ataaagcgaa
     3721 gaaaccggtg caaatgccgg gtgcgtacaa cgttgaccgt aaactggata ttaccagcca
     3781 caacgaggat tataccgtgg ttgagcaata tgagcgtagc gagggtcgcc acagcaccgg
     3841 cggcatggac gaactgtata agggatccta ataacgctga tagtgctagt gtagatcgct
     3901 actagagcca ggcatcaaat aaaacgaaag gctcagtcga aagactgggc ctttcgtttt
     3961 atctgttgtt tgtcggtgaa cgctctctac tagagtcaca ctggctcacc ttcgggtggg
     4021 cctttctgcg tttatatact ggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Tetracycline resistance marker and pBR322-ROP origin of replication.",
                    "label": "BASIC_SEVA_59",
                },
                {
                    "accessor": "62",
                    "binaryString": """LOCUS       BASIC_SEVA_62           4609 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and RK2
            origin of replication..
ACCESSION   d5cb5debc69f624ccc0d12b627816666
VERSION     d5cb5debc69f624ccc0d12b627816666
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    187..991
                     /label="SEVA_Gm"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3564..3598
                     /label="J23119"
     CDS             3730..4434
                     /label="mScarlett"
     misc_feature    3301..3405
                     /label="SEVA_T1"
     misc_feature    4471..4599
                     /label="B0015"
     misc_feature    1065..3286
                     /label="SEVA_RK2"
     misc_feature    join(4604..4609,1..51)
                     /label="LMP"
     misc_feature    3415..3471
                     /label="LMS"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggccgcgatg caggtggctg
     1081 ctgaaccccc agccggaact gaccccacaa ggccctagcg tttgcaatgc accaggtcat
     1141 cattgaccca ggcgtgttcc accaggccgc tgcctcgcaa ctcttcgcag gcttcgccga
     1201 cctgctcgcg ccacttcttc acgcgggtgg aatccgatcc gcacatgagg cggaaggttt
     1261 ccagcttgag cgggtacggc tcccggtgcg agctgaaata gtcgaacatc cgtcgggccg
     1321 tcggcgacag cttgcggtac ttctcccata tgaatttcgt gtagtggtcg ccagcaaaca
     1381 gcacgacgat ttcctcgtcg atcaggacct ggcaacggga cgttttcttg ccacggtcca
     1441 ggacgcggaa gcggtgcagc agcgacaccg attccaggtg cccaacgcgg tcggacgtga
     1501 agcccatcgc cgtcgcctgt aggcgcgaca ggcattcctc ggccttcgtg taataccggc
     1561 cattgatcga ccagcccagg tcctggcaaa gctcgtagaa cgtgaaggtg atcggctcgc
     1621 cgataggggt gcgcttcgcg tactccaaca cctgctgcca caccagttcg tcatcgtcgg
     1681 cccgcagctc gacgccggtg taggtgatct tcacgtcctt gttgacgtgg aaaatgacct
     1741 tgttttgcag cgcctcgcgc gggattttct tgttgcgcgt ggtgaacagg gcagagcggg
     1801 ccgtgtcgtt tggcatcgct cgcatcgtgt ccggccacgg cgcaatatcg aacaaggaaa
     1861 gctgcatttc cttgatctgc tgcttcgtgt gtttcagcaa cgcggcctgc ttggcttcgc
     1921 tgacctgttt tgccaggtcc tcgccggcgg tttttcgctt cttggtcgtc atagttcctc
     1981 gcgtgtcgat ggtcatcgac ttcgccaaac ctgccgcctc ctgttcgaga cgacgcgaac
     2041 gctccacggc ggccgatggc gcgggcaggg cagggggagc cagttgcacg ctgtcgcgct
     2101 cgatcttggc cgtagcttgc tggactatcg agccgacgga ctggaaggtt tcgcggggcg
     2161 cacgcatgac ggtgcggctt gcgatggttt cggcatcctc ggcggaaaac cccgcgtcga
     2221 tcagttcttg cctgtatgcc ttccggtcaa acgtccgatt cattcaccct ccttgcggga
     2281 ttgccccgga attaattccc cggatcgatc cgtcgatctt gatcccctgc gccatcagat
     2341 ccttggcggc aagaaagcca tccagtttac tttgcagggc ttcccaacct taccagaggg
     2401 cgccccagct ggcaattccg gttcgcttgc tgtccataaa accgcccagt ctagctatcg
     2461 ccatgtaagc ccactgcaag ctacctgctt tctctttgcg cttgcgtttt cccttgtcca
     2521 gatagcccag tagctgacat tcatccgggg tcagcaccgt ttctgcggac tggctttcta
     2581 cgtggctgcc atttttgggg tgaggccgtt cgcggccgag gggcgcagcc cctgggggga
     2641 tgggaggccc gcgttagcgg gccgggaggg ttcgagaagg gggggcaccc cccttcggcg
     2701 tgcgcggtca cgcgcacagg gcgcagccct ggttaaaaac aaggtttata aatattggtt
     2761 taaaagcagg ttaaaagaca ggttagcggt ggccgaaaaa cgggcggaaa cccttgcaaa
     2821 tgctggattt tctgcctgtg gacagcccct caaatgtcaa taggtgcgcc cctcatctgt
     2881 cagcactctg cccctcaagt gtcaaggatc gcgcccctca tctgtcagta gtcgcgcccc
     2941 tcaagtgtca ataccgcagg gcacttatcc ccaggcttgt ccacatcatc tgtgggaaac
     3001 tcgcgtaaaa tcaggcgttt tcgccgattt gcgaggctgg ccagctccac gtcgccggcc
     3061 gaaatcgagc ctgcccctca tctgtcaacg ccgcgccggg tgagtcggcc cctcaagtgt
     3121 caacgtccgc ccctcatctg tcagtgaggg ccaagttttc cgcgaggtat ccacaacgcc
     3181 ggcggcccta catggctctg ctgtagtgag tgggttgcgc tccggcagcg gtcctgatcc
     3241 cccgcagaaa aaaaggatct caagaagatc ctttgatctt ttctacggcg cgcccagctg
     3301 tctagggcgg cggatttgtc ctactcagga gagcgttcac cgacaaacaa cagataaaac
     3361 gaaaggccca gtctttcgac tgagcctttc gttttatttg atgcctttaa ttaaggctcg
     3421 ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc cccaattatt
     3481 gaacaccctt cggggtgttt ttttgtttct ggtctaccat ctcgttgtga taatagacct
     3541 gaagtgccta ctctggaaaa tctttgacag ctagctcagt cctaggtata atgctagcag
     3601 ctgtcaccgg atgtgctttc cggtctgatg agtccgtgag gacgaaacag cctctacaaa
     3661 taattttgtt taaggctcgc tacgagaaga ttgttacttt cgcagcgtta ttatctaagg
     3721 aggtagtcca tggttagcaa aggcgaggcg gttatcaagg agtttatgcg ttttaaggtt
     3781 cacatggagg gtagcatgaa tggtcacgag ttcgagatcg agggtgaagg cgagggtcgt
     3841 ccgtacgaag gcacccagac cgcgaagctg aaagtgacca agggtggccc gctgccgttc
     3901 agctgggaca tcctgagccc gcagttcatg tatggcagcc gtgcgtttac caaacacccg
     3961 gcggacattc cggattacta taagcaaagc ttcccggaag gttttaaatg ggagcgtgtt
     4021 atgaacttcg aagatggtgg cgcggtgacc gttacccagg acaccagcct ggaggatggc
     4081 accctgattt acaaggtgaa actgcgtggc accaactttc cgccggatgg tccggttatg
     4141 cagaagaaaa cgatgggttg ggaagcgagc accgagcgtc tgtatccgga agatggcgtg
     4201 ctgaagggtg atatcaaaat ggcgctgcgt ctgaaggacg gtggccgtta cctggcggat
     4261 tttaagacca cctataaagc gaagaaaccg gtgcaaatgc cgggtgcgta caacgttgac
     4321 cgtaaactgg atattaccag ccacaacgag gattataccg tggttgagca atatgagcgt
     4381 agcgagggtc gccacagcac cggcggcatg gacgaactgt ataagggatc ctaataacgc
     4441 tgatagtgct agtgtagatc gctactagag ccaggcatca aataaaacga aaggctcagt
     4501 cgaaagactg ggcctttcgt tttatctgtt gtttgtcggt gaacgctctc tactagagtc
     4561 acactggctc accttcgggt gggcctttct gcgtttatat actggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and RK2 origin of replication.",
                    "label": "BASIC_SEVA_62",
                },
                {
                    "accessor": "63",
                    "binaryString": """LOCUS       BASIC_SEVA_63           3909 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and pBBR1
            origin of replication..
ACCESSION   dc4b1f3d7ce456eea715d1cf35deecc0
VERSION     dc4b1f3d7ce456eea715d1cf35deecc0
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2864..2898
                     /label="J23119"
     misc_feature    1065..2586
                     /label="SEVA_pBBR1"
     misc_feature    187..991
                     /label="SEVA_Gm"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    3771..3899
                     /label="B0015"
     misc_feature    2715..2771
                     /label="LMS"
     misc_feature    2601..2705
                     /label="SEVA_T1"
     CDS             3030..3734
                     /label="mScarlett"
     misc_feature    join(3904..3909,1..51)
                     /label="LMP"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggccctaccg gcgcggcagc
     1081 gttacccgtg tcggcggctc caacggctcg ccatcgtcca gaaaacacgg ctcatcgggc
     1141 atcggcaggc gctgctgccc gcgccgttcc cattcctccg tttcggtcaa ggctggcagg
     1201 tctggttcca tgcccggaat gccgggctgg ctgggcggct cctcgccggg gccggtcggt
     1261 agttgctgct cgcccggata cagggtcggg atgcggcgca ggtcgccatg ccccaacagc
     1321 gattcgtcct ggtcgtcgtg atcaaccacc acggcggcac tgaacaccga caggcgcaac
     1381 tggtcgcggg gctggcccca cgccacgcgg tcattgacca cgtaggccga cacggtgccg
     1441 gggccgttga gcttcacgac ggagatccag cgctcggcca ccaagtcctt gactgcgtat
     1501 tggaccgtcc gcaaagaacg tccgatgagc ttggaaagtg tcttctggct gaccaccacg
     1561 gcgttctggt ggcccatctg cgccacgagg tgatgcagca gcattgccgc cgtgggtttc
     1621 ctcgcaataa gcccggccca cgcctcatgc gctttgcgtt ccgtttgcac ccagtgaccg
     1681 ggcttgttct tggcttgaat gccgatttct ctggactgcg tggccatgct tatctccatg
     1741 cggtaggggt gccgcacggt tgcggcacca tgcgcaatca gctgcaactt ttcggcagcg
     1801 cgacaacaat tatgcgttgc gtaaaagtgg cagtcaatta cagattttct ttaacctacg
     1861 caatgagcta ttgcgggggg tgccgcaatg agctgttgcg tacccccctt ttttaagttg
     1921 ttgattttta agtctttcgc atttcgccct atatctagtt ctttggtgcc caaagaaggg
     1981 cacccctgcg gggttccccc acgccttcgg cgcggctccc cctccggcaa aaagtggccc
     2041 ctccggggct tgttgatcga ctgcgcggcc ttcggccttg cccaaggtgg cgctgccccc
     2101 ttggaacccc cgcactcgcc gccgtgaggc tcggggggca ggcgggcggg cttcgccctt
     2161 cgactgcccc cactcgcata ggcttgggtc gttccaggcg cgtcaaggcc aagccgctgc
     2221 gcggtcgctg cgcgagcctt gacccgcctt ccacttggtg tccaaccggc aagcgaagcg
     2281 cgcaggccgc aggccggagg cttttcccca gagaaaatta aaaaaattga tggggcaagg
     2341 ccgcaggccg cgcagttgga gccggtgggt atgtggtcga aggctgggta gccggtgggc
     2401 aatccctgtg gtcaagctcg tgggcaggcg cagcctgtcc atcagcttgt ccagcagggt
     2461 tgtccacggg ccgagcgaag cgagccagcc ggtggccgct cgcggccatc gtccacatat
     2521 ccacgggctg gcaagggagc gcagcgaccg cgcagggcga agcccggaga gcaagcccgt
     2581 agggggggcg cgcccagctg tctagggcgg cggatttgtc ctactcagga gagcgttcac
     2641 cgacaaacaa cagataaaac gaaaggccca gtctttcgac tgagcctttc gttttatttg
     2701 atgcctttaa ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt
     2761 cggaatcgtc cccaattatt gaacaccctt cggggtgttt ttttgtttct ggtctaccat
     2821 ctcgttgtga taatagacct gaagtgccta ctctggaaaa tctttgacag ctagctcagt
     2881 cctaggtata atgctagcag ctgtcaccgg atgtgctttc cggtctgatg agtccgtgag
     2941 gacgaaacag cctctacaaa taattttgtt taaggctcgc tacgagaaga ttgttacttt
     3001 cgcagcgtta ttatctaagg aggtagtcca tggttagcaa aggcgaggcg gttatcaagg
     3061 agtttatgcg ttttaaggtt cacatggagg gtagcatgaa tggtcacgag ttcgagatcg
     3121 agggtgaagg cgagggtcgt ccgtacgaag gcacccagac cgcgaagctg aaagtgacca
     3181 agggtggccc gctgccgttc agctgggaca tcctgagccc gcagttcatg tatggcagcc
     3241 gtgcgtttac caaacacccg gcggacattc cggattacta taagcaaagc ttcccggaag
     3301 gttttaaatg ggagcgtgtt atgaacttcg aagatggtgg cgcggtgacc gttacccagg
     3361 acaccagcct ggaggatggc accctgattt acaaggtgaa actgcgtggc accaactttc
     3421 cgccggatgg tccggttatg cagaagaaaa cgatgggttg ggaagcgagc accgagcgtc
     3481 tgtatccgga agatggcgtg ctgaagggtg atatcaaaat ggcgctgcgt ctgaaggacg
     3541 gtggccgtta cctggcggat tttaagacca cctataaagc gaagaaaccg gtgcaaatgc
     3601 cgggtgcgta caacgttgac cgtaaactgg atattaccag ccacaacgag gattataccg
     3661 tggttgagca atatgagcgt agcgagggtc gccacagcac cggcggcatg gacgaactgt
     3721 ataagggatc ctaataacgc tgatagtgct agtgtagatc gctactagag ccaggcatca
     3781 aataaaacga aaggctcagt cgaaagactg ggcctttcgt tttatctgtt gtttgtcggt
     3841 gaacgctctc tactagagtc acactggctc accttcgggt gggcctttct gcgtttatat
     3901 actggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and pBBR1 origin of replication.",
                    "label": "BASIC_SEVA_63",
                },
                {
                    "accessor": "64",
                    "binaryString": """LOCUS       BASIC_SEVA_64           4160 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and
            pRO1600/ColE1 origin of replication..
ACCESSION   5bcbfec04b54bcc37a17ba5bd5d6776d
VERSION     5bcbfec04b54bcc37a17ba5bd5d6776d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    3162..3218
                     /label="LMS"
     misc_feature    join(4155..4160,1..51)
                     /label="LMP"
     misc_feature    1065..3033
                     /label="SEVA_pRO1600/ColE1"
     misc_feature    3219..3253
                     /label="J23105"
     misc_feature    4022..4150
                     /label="B0015"
     misc_feature    3262..3273
                     /label="B0034"
     misc_feature    3048..3152
                     /label="SEVA_T1"
     misc_feature    187..991
                     /label="SEVA_Gm"
     CDS             3281..3985
                     /label="mScarlett"
     misc_feature    58..160
                     /label="SEVA_T0"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggccgataat ctcatgacca
     1081 aaatccctta acgtgagttt tcgttccact gagcgtcaga ccccgtagaa aagatcaaag
     1141 gatcttcttg agatcctttt tttctgcgcg taatctgctg cttgcaaaca aaaaaaccac
     1201 cgctaccagc ggtggtttgt ttgccggatc aagagctacc aactcttttt ccgaaggtaa
     1261 ctggcttcag cagagcgcag ataccaaata ctgttcttct agtgtagccg tagttaggcc
     1321 accacttcaa gaactctgta gcaccgccta catacctcgc tctgctaatc ctgttaccag
     1381 tggctgctgc cagtggcgat aagtcgtgtc ttaccgggtt ggactcaaga cgatagttac
     1441 cggataaggc gcagcggtcg ggctgaacgg ggggttcgtg cacacagccc agcttggagc
     1501 gaacgaccta caccgaactg agatacctac agcgtgagct atgagaaagc gccacgcttc
     1561 ccgaagggag aaaggcggac aggcatccgg taagcggcag ggtcggaaca ggagagcgca
     1621 cgagggagct tccaggggga aacgcctggt atctttatag tcctgtcggg tttcgccacc
     1681 tctgacttga gcgtcgattt ttgtgatgct cgtcaggggg gcggagccta tggaaaaacg
     1741 ccagcaacgc ggccgtgaaa ggcaggccgg tccgtggtgg ccacggcctc taggccagat
     1801 ccagcggcat ctgggttagt cgagcgcggg ccgcttccca tgtctcacca gggcgagcct
     1861 gtttcgcgat ctcagcatct gaaatcttcc cggccttgcg cttcgctggg gccttaccca
     1921 ccgccttggc gggcttcttc ggtccaaaac tgaacaacag atgtgtgacc ttgcgcccgg
     1981 tctttcgctg cgcccactcc acctgtagcg ggctgtgctc gttgatctgc gtcacggctg
     2041 gatcaagcac tcgcaacttg aagtccttga tcgagggata ccggccttcc agttgaaacc
     2101 actttcgcag ctggtcaatt tctatttcgc gctggccgat gctgtcccat tgcatgagca
     2161 gctcgtaaag cctgatcgcg tgggtgctgt ccatcttggc cacgtcagcc aaggcgtatt
     2221 tggtgaactg tttggtgagt tccgtcaggt acggcagcat gtctttggtg aacctgagtt
     2281 ctacacggcc ctcaccctcc cggtagatga ttgtttgcac ccagccggta atcatcacac
     2341 tcggtctttt ccccttgcca ttgggctctt gggttaaccg gacttcccgc cgtttcaggc
     2401 gcagggccgc ttctttgagc tggttgtagg aagattcgat agggacaccc gccatcgtcg
     2461 ctatgtcctc cgccgtcact gaatacatca cttcatcggt gacaggctcg ctcctcttca
     2521 cctggctaat acaggccaga acgatccgct gttcctgaac actgaggcga tacgcggcct
     2581 cgaccagggc attgcttttg taaaccattg ggggtgaggc cacgttcgac attccttgtg
     2641 tataagggga cactgtatct gcgtcccaca atacaacaaa tccgtccctt tacaacaaca
     2701 aatccgtccc ttcttaacaa caaatccgtc ccttaatggc aacaaatccg tcccttttta
     2761 aactctacag gccacggatt acgtggcctg tagacgtcct aaaaggttta aaagggaaaa
     2821 ggaagaaaag ggtggaaacg caaaaaacgc accactacgt ggccccgttg gggccgcatt
     2881 tgtgcccctg aaggggcggg ggaggcgtct gggcaatccc cgttttacca gtcccctatc
     2941 gccgcctgag agggcgcagg aagcgagtaa tcagggtatc gaggcggatt cacccttggc
     3001 gtccaaccag cggcaccagc ggcgcctgag aggggcgcgc ccagctgtct agggcggcgg
     3061 atttgtccta ctcaggagag cgttcaccga caaacaacag ataaaacgaa aggcccagtc
     3121 tttcgactga gcctttcgtt ttatttgatg cctttaatta aggctcggga gacctatcgg
     3181 taataacagt ccaatctggt gtaacttcgg aatcgtcctt tacggctagc tcagtcctag
     3241 gtactatgct agctactagt gaaagaggag aaatactagt atggttagca aaggcgaggc
     3301 ggttatcaag gagtttatgc gttttaaggt tcacatggag ggtagcatga atggtcacga
     3361 gttcgagatc gagggtgaag gcgagggtcg tccgtacgaa ggcacccaga ccgcgaagct
     3421 gaaagtgacc aagggtggcc cgctgccgtt cagctgggac atcctgagcc cgcagttcat
     3481 gtatggcagc cgtgcgttta ccaaacaccc ggcggacatt ccggattact ataagcaaag
     3541 cttcccggaa ggttttaaat gggagcgtgt tatgaacttc gaagatggtg gcgcggtgac
     3601 cgttacccag gacaccagcc tggaggatgg caccctgatt tacaaggtga aactgcgtgg
     3661 caccaacttt ccgccggatg gtccggttat gcagaagaaa acgatgggtt gggaagcgag
     3721 caccgagcgt ctgtatccgg aagatggcgt gctgaagggt gatatcaaaa tggcgctgcg
     3781 tctgaaggac ggtggccgtt acctggcgga ttttaagacc acctataaag cgaagaaacc
     3841 ggtgcaaatg ccgggtgcgt acaacgttga ccgtaaactg gatattacca gccacaacga
     3901 ggattatacc gtggttgagc aatatgagcg tagcgagggt cgccacagca ccggcggcat
     3961 ggacgaactg tataagggat cctaataacg ctgatagtgc tagtgtagat cgctactaga
     4021 gccaggcatc aaataaaacg aaaggctcag tcgaaagact gggcctttcg ttttatctgt
     4081 tgtttgtcgg tgaacgctct ctactagagt cacactggct caccttcggg tgggcctttc
     4141 tgcgtttata tactggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and pRO1600/ColE1 origin of replication.",
                    "label": "BASIC_SEVA_64",
                },
                {
                    "accessor": "65",
                    "binaryString": """LOCUS       BASIC_SEVA_65           5865 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and
            RSF1010 origin of replication..
ACCESSION   4b8862f782d04fa17f10ec9484b1f945
VERSION     4b8862f782d04fa17f10ec9484b1f945
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    5727..5855
                     /label="B0015"
     CDS             4986..5690
                     /label="mScarlett"
     misc_feature    187..991
                     /label="SEVA_Gm"
     misc_feature    1065..4738
                     /label="SEVA_RSF101"
     misc_feature    4967..4978
                     /label="B0034"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    4867..4923
                     /label="LMS"
     misc_feature    join(5860..5865,1..51)
                     /label="LMP"
     misc_feature    4924..4958
                     /label="J23119"
     misc_feature    4753..4857
                     /label="SEVA_T1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggcctcagcc tgccgccttg
     1081 ggccgggtga tgtcgtactt gcccgccgcg aactcggtta ccgtccagcc cagcgcgacc
     1141 agctccggca acgcctcgcg cacccgctgg cggcgcttgc gcatggtcga accactggcc
     1201 tctgacggcc agacatagcc gcacaaggta tctatggaag ccttgccggt tttgccgggg
     1261 tcgatccagc cacacagccg ctggtgcagc aggcgggcgg tttcgctgtc cagcgcccgc
     1321 acctcgtcca tgctgatgcg cacatgctgg ccgccaccca tgacggcctg cgcgatcaag
     1381 gggttcaggg ccacgtacag gcgcccgtcc gcctcgtcgc tggcgtactc cgacagcagc
     1441 cgaaacccct gccgcttgcg gccattctgg gcgatgatgg ataccttcca aaggcgctcg
     1501 atgcagtcct gtatgtgctt gagcgcccca ccactatcga cctctgcccc gatttccttt
     1561 gccagcgccc gatagctacc tttgaccaca tggcattcag cggtgacggc ctcccacttg
     1621 ggttccagga acagccggag ctgccgtccg ccttcggtct tgggttccgg gccaagcact
     1681 aggccattag gcccagccat ggccaccagc ccttgcagga tgcgcagatc atcagcgccc
     1741 agcggctccg ggccgctgaa ctcgatccgc ttgccgtcgc cgtagtcata cgtcacgtcc
     1801 agcttgctgc gcttgcgctc gccccgcttg agggcacgga acaggccggg ggccagacag
     1861 tgcgccgggt cgtgccggac gtggctgagg ctgtgcttgt tcttaggctt caccacgggg
     1921 cacccccttg ctcttgcgct gcctctccag cacggcgggc ttgagcaccc cgccgtcatg
     1981 ccgcctgaac caccgatcag cgaacggtgc gccatagttg gccttgctca caccgaagcg
     2041 gacgaagaac cggcgctggt cgtcgtccac accccattcc tcggcctcgg cgctggtcat
     2101 gctcgacagg taggactgcc agcggatgtt atcgaccagt accgagctgc cccggctggc
     2161 ctgctgctgg tcgcctgcgc ccatcatggc cgcgcccttg ctggcatggt gcaggaacac
     2221 gatagagcac ccggtatcgg cggcgatggc ctccatgcga ccgatgacct gggccatggg
     2281 gccgctggcg ttttcttcct cgatgtggaa ccggcgcagc gtgtccagca ccatcaggcg
     2341 gcggccctcg gcggcgcgct tgaggccgtc gaaccactcc ggggccatga tgttgggcag
     2401 gctgccgatc agcggctgga tcagcaggcc gtcagccacg gcttgccgtt cctcggcgct
     2461 gaggtgcgcc ccaagggcgt gcaggcggtg atgaatggcg gtgggcgggt cttcggcggg
     2521 caggtagatc accgggccgg tgggcagttc gcccacctcc agcagatccg gcccgcctgc
     2581 aatctgtgcg gccagttgca gggccagcat ggatttaccg gcaccaccgg gcgacaccag
     2641 cgccccgacc gtaccggcca ccatgttggg caaaacgtag tccagcggtg gcggcgctgc
     2701 tgcgaacgcc tccagaatat tgataggctt atgggtagcc attgattgcc tcctttgcag
     2761 gcagttggtg gttaggcgct ggcggggtca ctacccccgc cctgcgccgc tctgagttct
     2821 tccaggcact cgcgcagcgc ctcgtattcg tcgtcggtca gccagaactt gcgctgacgc
     2881 atccctttgg ccttcatgcg ctcggcatat cgcgcttggc gtacagcgtc agggctggcc
     2941 agcaggtcgc cggtctgctt gtccttttgg tctttcatat cagtcaccga gaaacttgcc
     3001 ggggccgaaa ggcttgtctt cgcggaacaa ggacaaggtg cagccgtcaa ggttaaggct
     3061 ggccatatca gcgactgaaa agcggccagc ctcggccttg tttgacgtat aaccaaagcc
     3121 accgggcaac caatagccct tgtcactttt gatcaggtag accgaccctg aagcgctttt
     3181 ttcgtattcc ataaaacccc cttctgtgcg tgagtactca tagtataaca ggcgtgagta
     3241 ccaacgcaag cactacatgc tgaaatctgg cccgcccctg tccatgcctc gctggcgggg
     3301 tgccggtgcc cgtgccagct cggcccgcgc aagctggacg ctgggcagac ccatgacctt
     3361 gctgacggtg cgctcgatgt aatccgcttc gtggccgggc ttgcgctctg ccagcgctgg
     3421 gctggcctcg gccatggcct tgccgatttc ctcggcactg cggccccggc tggccagctt
     3481 ctgcgcggcg ataaagtcgc acttgctgag gtcatcaccg aagcgcttga ccagcccggc
     3541 catctcgctg cggtactcgt ccagcgccgt gcgccggtgg cggctaagct gccgctcggg
     3601 cagttcgagg ctggccagcc tgcgggcctt ctcctgctgc cgctgggcct gctcgatctg
     3661 ctggccagcc tgctgcacca gcgccgggcc agcggtggcg gtcttgccct tggattcacg
     3721 cagcagcacc cacggctgat aaccggcgcg ggtggtgtgc ttgtccttgc ggttggtgaa
     3781 gcccgccaag cggccatagt ggcggctgtc ggcgctggcc gggtcggcgt cgtactcgct
     3841 ggccagcgtc cgggcaatct gcccccgaag ttcaccgcct gcggcgtcgg ccaccttgac
     3901 ccatgcctga tagttcttcg ggctggtttc cactaccagg gcaggctccc ggccctcggc
     3961 tttcatgtca tccaggtcaa actcgctgag gtcgtccacc agcaccagac catgccgctc
     4021 ctgctcggcg ggcctgatat acacgtcatt gccctgggca ttcatccgct tgagccatgg
     4081 cgtgttctgg agcacttcgg cggctgacca ttcccggttc atcatctggc cggtggtggc
     4141 gtccctgacg ccgatatcga agcgctcaca gcccatggcc ttgagctgtc ggcctatggc
     4201 ctgcaaagtc ctgtcgttct tcatcgggcc accaagcgat tcccacacat tatacgagcc
     4261 ggaagcataa agtgtaaagc ctagatccga aggatgagcc gggctgaatg atcgaccgag
     4321 acaggccctg cggggctgca cacgcgcccc cacccttcgg gtagggggaa aggccgctaa
     4381 agcggctaaa agcgctccag cgtatttctg cggggtttgg tgtggggttt agcgggcttt
     4441 gcccgccttt ccccctgccg cgcagcggtg gggcggtgtg tagcctagcg cagcgaatag
     4501 accagctatc cggcctctgg ccgggcatat tgggcaaggg cagcagcgcc ccacaagggc
     4561 gctgataacc gcgcctagtg gattattctt agataatcat ggatggattt ttccaacacc
     4621 ccgccagccc ccgcccctgc tgggtttgca ggtttggggg cgtgacagtt attgcagggg
     4681 ttcgtgacag ttattgcagg ggggcgtgac agttattgca ggggttcgtg acagttaggg
     4741 cgcgcccagc tgtctagggc ggcggatttg tcctactcag gagagcgttc accgacaaac
     4801 aacagataaa acgaaaggcc cagtctttcg actgagcctt tcgttttatt tgatgccttt
     4861 aattaaggct cgggagacct atcggtaata acagtccaat ctggtgtaac ttcggaatcg
     4921 tccttgacag ctagctcagt cctaggtata atgctagcta ctagtgaaag aggagaaata
     4981 ctagtatggt tagcaaaggc gaggcggtta tcaaggagtt tatgcgtttt aaggttcaca
     5041 tggagggtag catgaatggt cacgagttcg agatcgaggg tgaaggcgag ggtcgtccgt
     5101 acgaaggcac ccagaccgcg aagctgaaag tgaccaaggg tggcccgctg ccgttcagct
     5161 gggacatcct gagcccgcag ttcatgtatg gcagccgtgc gtttaccaaa cacccggcgg
     5221 acattccgga ttactataag caaagcttcc cggaaggttt taaatgggag cgtgttatga
     5281 acttcgaaga tggtggcgcg gtgaccgtta cccaggacac cagcctggag gatggcaccc
     5341 tgatttacaa ggtgaaactg cgtggcacca actttccgcc ggatggtccg gttatgcaga
     5401 agaaaacgat gggttgggaa gcgagcaccg agcgtctgta tccggaagat ggcgtgctga
     5461 agggtgatat caaaatggcg ctgcgtctga aggacggtgg ccgttacctg gcggatttta
     5521 agaccaccta taaagcgaag aaaccggtgc aaatgccggg tgcgtacaac gttgaccgta
     5581 aactggatat taccagccac aacgaggatt ataccgtggt tgagcaatat gagcgtagcg
     5641 agggtcgcca cagcaccggc ggcatggacg aactgtataa gggatcctaa taacgctgat
     5701 agtgctagtg tagatcgcta ctagagccag gcatcaaata aaacgaaagg ctcagtcgaa
     5761 agactgggcc tttcgtttta tctgttgttt gtcggtgaac gctctctact agagtcacac
     5821 tggctcacct tcgggtgggc ctttctgcgt ttatatactg gctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and RSF1010 origin of replication.",
                    "label": "BASIC_SEVA_65",
                },
                {
                    "accessor": "66",
                    "binaryString": """LOCUS       BASIC_SEVA_66           2923 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and p15A
            origin of replication..
ACCESSION   c4086f1150c7096ada36e3445f07bc74
VERSION     c4086f1150c7096ada36e3445f07bc74
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    187..991
                     /label="SEVA_Gm"
     misc_feature    join(2918..2923,1..51)
                     /label="LMP"
     misc_feature    1925..1981
                     /label="LMS"
     misc_feature    1982..2016
                     /label="J23119"
     misc_feature    1065..1796
                     /label="SEVA_p15A"
     misc_feature    2025..2036
                     /label="B0034"
     CDS             2044..2748
                     /label="mScarlett"
     misc_feature    2785..2913
                     /label="B0015"
     misc_feature    1811..1915
                     /label="SEVA_T1"
     misc_feature    58..160
                     /label="SEVA_T0"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggccctagaa atattttatc
     1081 tgattaataa gatgatcttc ttgagatcgt tttggtctgc gcgtaatctc ttgctctgaa
     1141 aacgaaaaaa ccgccttgca gggcggtttt tcgaaggttc tctgagctac caactctttg
     1201 aaccgaggta actggcttgg aggagcgcag tcaccaaaac ttgtcctttc agtttagcct
     1261 taaccggcgc atgacttcaa gactaactcc tctaaatcaa ttaccagtgg ctgctgccag
     1321 tggtgctttt gcatgtcttt ccgggttgga ctcaagacga tagttaccgg ataaggcgca
     1381 gcggtcggac tgaacggggg gttcgtgcat acagtccagc ttggagcgaa ctgcctaccc
     1441 ggaactgagt gtcaggcgtg gaatgagaca aacgcggcca taacagcgga atgacaccgg
     1501 taaaccgaaa ggcaggaaca ggagagcgca cgagggagcc gccaggggga aacgcctggt
     1561 atctttatag tcctgtcggg tttcgccacc actgatttga gcgtcagatt tcgtgatgct
     1621 tgtcaggggg gcggagccta tggaaaaacg gctttgccgc ggccctctca cttccctgtt
     1681 aagtatcttc ctggcatctt ccaggaaatc tccgccccgt tcgtaagcca tttccgctcg
     1741 ccgcagtcga acgaccgagc gtagcgagtc agtgagcgag gaagcggaat atatccggcg
     1801 cgcccagctg tctagggcgg cggatttgtc ctactcagga gagcgttcac cgacaaacaa
     1861 cagataaaac gaaaggccca gtctttcgac tgagcctttc gttttatttg atgcctttaa
     1921 ttaaggctcg ggagacctat cggtaataac agtccaatct ggtgtaactt cggaatcgtc
     1981 cttgacagct agctcagtcc taggtataat gctagctact agtgaaagag gagaaatact
     2041 agtatggtta gcaaaggcga ggcggttatc aaggagttta tgcgttttaa ggttcacatg
     2101 gagggtagca tgaatggtca cgagttcgag atcgagggtg aaggcgaggg tcgtccgtac
     2161 gaaggcaccc agaccgcgaa gctgaaagtg accaagggtg gcccgctgcc gttcagctgg
     2221 gacatcctga gcccgcagtt catgtatggc agccgtgcgt ttaccaaaca cccggcggac
     2281 attccggatt actataagca aagcttcccg gaaggtttta aatgggagcg tgttatgaac
     2341 ttcgaagatg gtggcgcggt gaccgttacc caggacacca gcctggagga tggcaccctg
     2401 atttacaagg tgaaactgcg tggcaccaac tttccgccgg atggtccggt tatgcagaag
     2461 aaaacgatgg gttgggaagc gagcaccgag cgtctgtatc cggaagatgg cgtgctgaag
     2521 ggtgatatca aaatggcgct gcgtctgaag gacggtggcc gttacctggc ggattttaag
     2581 accacctata aagcgaagaa accggtgcaa atgccgggtg cgtacaacgt tgaccgtaaa
     2641 ctggatatta ccagccacaa cgaggattat accgtggttg agcaatatga gcgtagcgag
     2701 ggtcgccaca gcaccggcgg catggacgaa ctgtataagg gatcctaata acgctgatag
     2761 tgctagtgta gatcgctact agagccaggc atcaaataaa acgaaaggct cagtcgaaag
     2821 actgggcctt tcgttttatc tgttgtttgt cggtgaacgc tctctactag agtcacactg
     2881 gctcaccttc gggtgggcct ttctgcgttt atatactggc tcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and p15A origin of replication.",
                    "label": "BASIC_SEVA_66",
                },
                {
                    "accessor": "67",
                    "binaryString": """LOCUS       BASIC_SEVA_67           3847 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and pSC101
            origin of replication..
ACCESSION   2ec5633c7edef85d47632723006c365c
VERSION     2ec5633c7edef85d47632723006c365c
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2653..2709
                     /label="LMS"
     misc_feature    3709..3837
                     /label="B0015"
     misc_feature    187..991
                     /label="SEVA_Gm"
     misc_feature    2802..2836
                     /label="J23119"
     misc_feature    1065..2524
                     /label="SEVA_pSC101"
     misc_feature    join(3842..3847,1..51)
                     /label="LMP"
     CDS             2968..3672
                     /label="mScarlett"
     misc_feature    2539..2643
                     /label="SEVA_T1"
     misc_feature    58..160
                     /label="SEVA_T0"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggcctcagat ccttccgtat
     1081 ttagccagta tgttctctag tgtggttcgt tgtttttgcg tgagccatga gaacgaacca
     1141 ttgagatcat acttactttg catgtcactc aaaaattttg cctcaaaact ggtgagctga
     1201 atttttgcag ttaaagcatc gtgtagtgtt tttcttagtc cgttatgtag gtaggaatct
     1261 gatgtaatgg ttgttggtat tttgtcacca ttcattttta tctggttgtt ctcaagttcg
     1321 gttacgagat ccatttgtct atctagttca acttggaaaa tcaacgtatc agtcgggcgg
     1381 cctcgcttat caaccaccaa tttcatattg ctgtaagtgt ttaaatcttt acttattggt
     1441 ttcaaaaccc attggttaag ccttttaaac tcatggtagt tattttcaag cattaacatg
     1501 aacttaaatt catcaaggct aatctctata tttgccttgt gagttttctt ttgtgttagt
     1561 tcttttaata accactcata aatcctcata gagtatttgt tttcaaaaga cttaacatgt
     1621 tccagattat attttatgaa tttttttaac tggaaaagat aaggcaatat ctcttcacta
     1681 aaaactaatt ctaatttttc gcttgagaac ttggcatagt ttgtccactg gaaaatctca
     1741 aagcctttaa ccaaaggatt cctgatttcc acagttctcg tcatcagctc tctggttgct
     1801 ttagctaata caccataagc attttcccta ctgatgttca tcatctgagc gtattggtta
     1861 taagtgaacg ataccgtccg ttctttcctt gtagggtttt caatcgtggg gttgagtagt
     1921 gccacacagc ataaaattag cttggtttca tgctccgtta agtcatagcg actaatcgct
     1981 agttcatttg ctttgaaaac aactaattca gacatacatc tcaattggtc taggtgattt
     2041 taatcactat accaattgag atgggctagt caatgataat tacatgtcct tttcctttga
     2101 gttgtgggta tctgtaaatt ctgctagacc tttgctggaa aacttgtaaa ttctgctaga
     2161 ccctctgtaa attccgctag acctttgtgt gttttttttg tttatattca agtggttata
     2221 atttatagaa taaagaaaga ataaaaaaag ataaaaagaa tagatcccag ccctgtgtat
     2281 aactcactac tttagtcagt tccgcagtat tacaaaagga tgtcgcaaac gctgtttgct
     2341 cctctacaaa acagacctta aaaccctaaa ggcttaagta gcaccctcgc aagctcgggc
     2401 aaatcgctga atattccttt tgtctccgac catcaggcac ctgagtcgct gtctttttcg
     2461 tgacattcag ttcgctgcgc tcacggctct ggcagtgaat gggggtaaat ggcactacag
     2521 gcgcggcgcg cccagctgtc tagggcggcg gatttgtcct actcaggaga gcgttcaccg
     2581 acaaacaaca gataaaacga aaggcccagt ctttcgactg agcctttcgt tttatttgat
     2641 gcctttaatt aaggctcggg agacctatcg gtaataacag tccaatctgg tgtaacttcg
     2701 gaatcgtccc caattattga acacccttcg gggtgttttt ttgtttctgg tctaccatct
     2761 cgttgtgata atagacctga agtgcctact ctggaaaatc tttgacagct agctcagtcc
     2821 taggtataat gctagcagct gtcaccggat gtgctttccg gtctgatgag tccgtgagga
     2881 cgaaacagcc tctacaaata attttgttta aggctcgcta cgagaagatt gttactttcg
     2941 cagcgttatt atctaaggag gtagtccatg gttagcaaag gcgaggcggt tatcaaggag
     3001 tttatgcgtt ttaaggttca catggagggt agcatgaatg gtcacgagtt cgagatcgag
     3061 ggtgaaggcg agggtcgtcc gtacgaaggc acccagaccg cgaagctgaa agtgaccaag
     3121 ggtggcccgc tgccgttcag ctgggacatc ctgagcccgc agttcatgta tggcagccgt
     3181 gcgtttacca aacacccggc ggacattccg gattactata agcaaagctt cccggaaggt
     3241 tttaaatggg agcgtgttat gaacttcgaa gatggtggcg cggtgaccgt tacccaggac
     3301 accagcctgg aggatggcac cctgatttac aaggtgaaac tgcgtggcac caactttccg
     3361 ccggatggtc cggttatgca gaagaaaacg atgggttggg aagcgagcac cgagcgtctg
     3421 tatccggaag atggcgtgct gaagggtgat atcaaaatgg cgctgcgtct gaaggacggt
     3481 ggccgttacc tggcggattt taagaccacc tataaagcga agaaaccggt gcaaatgccg
     3541 ggtgcgtaca acgttgaccg taaactggat attaccagcc acaacgagga ttataccgtg
     3601 gttgagcaat atgagcgtag cgagggtcgc cacagcaccg gcggcatgga cgaactgtat
     3661 aagggatcct aataacgctg atagtgctag tgtagatcgc tactagagcc aggcatcaaa
     3721 taaaacgaaa ggctcagtcg aaagactggg cctttcgttt tatctgttgt ttgtcggtga
     3781 acgctctcta ctagagtcac actggctcac cttcgggtgg gcctttctgc gtttatatac
     3841 tggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and pSC101 origin of replication.",
                    "label": "BASIC_SEVA_67",
                },
                {
                    "accessor": "68",
                    "binaryString": """LOCUS       BASIC_SEVA_68           3120 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and pUC
            origin of replication..
ACCESSION   6c867b6cbf05361d09da7c1ecca28613
VERSION     6c867b6cbf05361d09da7c1ecca28613
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    2222..2233
                     /label="B0034"
     CDS             2241..2945
                     /label="mScarlett"
     misc_feature    join(3115..3120,1..51)
                     /label="LMP"
     misc_feature    2982..3110
                     /label="B0015"
     misc_feature    187..991
                     /label="SEVA_Gm"
     misc_feature    1065..1993
                     /label="SEVA_pUC"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2179..2213
                     /label="J23106"
     misc_feature    2122..2178
                     /label="LMS"
     misc_feature    2008..2112
                     /label="SEVA_T1"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggccccgtag aaaagatcaa
     1081 aggatcttct tgagatcctt tttttctgcg cgtaatctgc tgcttgcaaa caaaaaaacc
     1141 accgctacca gcggtggttt gtttgccgga tcaagagcta ccaactcttt ttccgaaggt
     1201 aactggcttc agcagagcgc agataccaaa tactgttctt ctagtgtagc cgtagttagg
     1261 ccaccacttc aagaactctg tagcaccgcc tacatacctc gctctgctaa tcctgttacc
     1321 agtggctgct gccagtggcg ataagtcgtg tcttaccggg ttggactcaa gacgatagtt
     1381 accggataag gcgcagcggt cgggctgaac ggggggttcg tgcacacagc ccagcttgga
     1441 gcgaacgacc tacaccgaac tgagatacct acagcgtgag ctttgagaaa gcgccacgct
     1501 tcccgaaggg agaaaggcgg acaggtatcc ggtaagcggc agggtcggaa caggagagcg
     1561 cacgagggag cttccagggg gaaacgcctg gtatctttat agtcctgtcg ggtttcgcca
     1621 cctctgactt gagcgtcgat ttttgtgatg ctcgtcaggg gggcggagcc tatggaaaaa
     1681 cgccagcaac gcggcctttt tacggttcct ggccttttgc tggccttttg ctcacatgtt
     1741 ctttcctgcg ttatcccctg attctgtgga taaccgtatt accgcctttg agtgagctga
     1801 taccgctcgc cgcagccgaa cgaccgagcg cagcgagtca gtgagcgagg aagcggaaga
     1861 gcgcccaata cgcaaaccgc ctctccccgc gcgttggccg attcattaat gcagctggca
     1921 cgacaggttt cccgactgga aagcgggcag tgagcgcaac gcaattaatg tgagttagct
     1981 cactcattag gcaggcgcgc ccagctgtct agggcggcgg atttgtccta ctcaggagag
     2041 cgttcaccga caaacaacag ataaaacgaa aggcccagtc tttcgactga gcctttcgtt
     2101 ttatttgatg cctttaatta aggctcggga gacctatcgg taataacagt ccaatctggt
     2161 gtaacttcgg aatcgtcctt tacggctagc tcagtcctag gtatagtgct agctactagt
     2221 gaaagaggag aaatactagt atggttagca aaggcgaggc ggttatcaag gagtttatgc
     2281 gttttaaggt tcacatggag ggtagcatga atggtcacga gttcgagatc gagggtgaag
     2341 gcgagggtcg tccgtacgaa ggcacccaga ccgcgaagct gaaagtgacc aagggtggcc
     2401 cgctgccgtt cagctgggac atcctgagcc cgcagttcat gtatggcagc cgtgcgttta
     2461 ccaaacaccc ggcggacatt ccggattact ataagcaaag cttcccggaa ggttttaaat
     2521 gggagcgtgt tatgaacttc gaagatggtg gcgcggtgac cgttacccag gacaccagcc
     2581 tggaggatgg caccctgatt tacaaggtga aactgcgtgg caccaacttt ccgccggatg
     2641 gtccggttat gcagaagaaa acgatgggtt gggaagcgag caccgagcgt ctgtatccgg
     2701 aagatggcgt gctgaagggt gatatcaaaa tggcgctgcg tctgaaggac ggtggccgtt
     2761 acctggcgga ttttaagacc acctataaag cgaagaaacc ggtgcaaatg ccgggtgcgt
     2821 acaacgttga ccgtaaactg gatattacca gccacaacga ggattatacc gtggttgagc
     2881 aatatgagcg tagcgagggt cgccacagca ccggcggcat ggacgaactg tataagggat
     2941 cctaataacg ctgatagtgc tagtgtagat cgctactaga gccaggcatc aaataaaacg
     3001 aaaggctcag tcgaaagact gggcctttcg ttttatctgt tgtttgtcgg tgaacgctct
     3061 ctactagagt cacactggct caccttcggg tgggcctttc tgcgtttata tactggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and pUC origin of replication.",
                    "label": "BASIC_SEVA_68",
                },
                {
                    "accessor": "69",
                    "binaryString": """LOCUS       BASIC_SEVA_69           3576 bp    DNA     circular UNK 03-SEP-2020
DEFINITION  BASIC SEVA vector containing Gentamicin resistance marker and
            pBR322-ROP origin of replication..
ACCESSION   c24ab786cffd654c2a89c82048dce73d
VERSION     c24ab786cffd654c2a89c82048dce73d
KEYWORDS    .
SOURCE      synthetic construct
  ORGANISM  synthetic construct other sequences; artificial sequences.
            .
FEATURES             Location/Qualifiers
     misc_feature    join(3571..3576,1..51)
                     /label="LMP"
     misc_feature    2635..2669
                     /label="J23119"
     misc_feature    58..160
                     /label="SEVA_T0"
     misc_feature    2578..2634
                     /label="LMS"
     misc_feature    1065..2449
                     /label="SEVA_pBR322-ROP"
     misc_feature    3438..3566
                     /label="B0015"
     misc_feature    2464..2568
                     /label="SEVA_T1"
     misc_feature    187..991
                     /label="SEVA_Gm"
     misc_feature    2678..2689
                     /label="B0034"
     CDS             2697..3401
                     /label="mScarlett"
ORIGIN
        1 ggtaagaact cgcacttcgt ggaaacacta ttatctggtg ggtctctgtc cactagtctt
       61 ggactcctgt tgatagatcc agtaatgacc tcagaactcc atctggattt gttcagaacg
      121 ctcggttgcc gccgggcgtt ttttattggt gagaatccag gggtccccaa taattacgat
      181 ttaaatttga cataagcctg ttcggttcgt aaactgtaat gcaagtagcg tatgcgctca
      241 cgcaactggt ccagaacctt gaccgaacgc agcggtggta acggcgcagt ggcggttttc
      301 atggcttgtt atgactgttt ttttgtacag cctatgcctc gggcatccaa gcagcaagcg
      361 cgttacgccg tgggtcgatg tttgatgtta tggagcagca acgatgttac gcagcagcaa
      421 cgatgttacg cagcagggca gtcgccctaa aacaaagtta ggtggctcaa gtatgggcat
      481 cattcgcaca tgtaggctcg gccctgacca agtcaaatcc atgcgggctg ctcttgatct
      541 tttcggtcgt gagttcggag acgtagccac ctactcccaa catcagccgg actccgatta
      601 cctcgggaac ttgctccgta gtaagacatt catcgcgctt gctgccttcg accaagaagc
      661 ggttgttggc gctctcgcgg cttacgttct gcccaagttt gagcagccgc gtagtgagat
      721 ctatatctat gatctcgcag tctccggaga gcaccggagg cagggcattg ccaccgcgct
      781 catcaatctc ctcaagcatg aggccaacgc gcttggtgct tatgtgatct acgtgcaagc
      841 agattacggt gacgatcccg cagtggctct ctatacaaag ttgggcatac gggaagaagt
      901 gatgcacttt gatatcgacc caagtaccgc cacctaacaa ttcgttcaag ccgagatcgg
      961 cttcccggcc gcggagttgt tcggtaaatt ggacaacggt cggctcgacc cacgactatt
     1021 gactgctctg agaaagttga ttgttacgat tagtccggcc ggccccgtag aaaagatcaa
     1081 aggatcttct tgagatcctt tttttctgcg cgtaatctgc tgcttgcaaa caaaaaaacc
     1141 accgctacca gcggtggttt gtttgccgga tcaagagcta ccaactcttt ttccgaaggt
     1201 aactggcttc agcagagcgc agataccaaa tactgtcctt ctagtgtagc cgtagttagg
     1261 ccaccacttc aagaactctg tagcaccgcc tacatacctc gctctgctaa tcctgttacc
     1321 agtggctgct gccagtggcg ataagtcgtg tcttaccggg ttggactcaa gacgatagtt
     1381 accggataag gcgcagcggt cgggctgaac ggggggttcg tgcacacagc ccagcttgga
     1441 gcgaacgacc tacaccgaac tgagatacct acagcgtgag ctatgagaaa gcgccacgct
     1501 tcccgaaggg agaaaggcgg acaggtatcc ggtaagcggc agggtcggaa caggagagcg
     1561 cacgagggag cttccagggg gaaacgcctg gtatctttat agtcctgtcg ggtttcgcca
     1621 cctctgactt gagcgtcgat ttttgtgatg ctcgtcaggg gggcggagcc tatggaaaaa
     1681 cgccagcaac gcggcctttt tacggttcct ggccttttgc tggccttttg ctcacatgtt
     1741 ctttcctgcg ttatcccctg attctgtgga taaccgtatt accgcctttg agtgagctga
     1801 taccgctcgc cgcagccgaa cgaccgagcg cagcgagtca gtgagcgagg aagcggaaga
     1861 gcgcctgatg cggtattttc tccttacgca tctgtgcggt atttcacacc gcatatggtg
     1921 cactctcagt acaatctgct ctgatgccgc atagttaagc cagtatacac tccgctatcg
     1981 ctacgtgact gggtcatggc tgcgccccga cacccgccaa cacccgctga cgcgccctga
     2041 cgggcttgtc tgctcccggc atccgcttac agacaagctg tgaccgtctc cgggagctgc
     2101 atgtgtcaga ggttttcacc gtcatcaccg aaacgcgcga ggcagctgcg gtaaagctca
     2161 tcagcgtggt cgtgcagcga ttcacagatg tctgcctgtt catccgcgtc cagctcgttg
     2221 agtttctcca gaagcgttaa tgtctggctt ctgataaagc gggccatgtt aagggcggtt
     2281 ttttcctgtt tggtcactga tgcctccgtg taagggggat ttctgttcat gggggtaatg
     2341 ataccgatga aacgagagag gatgctcacg atacgggtta ctgatgatga acatgcccgg
     2401 ttactggaac gttgtgaggg taaacaactg gcggtatgga tgcggcgggg gcgcgcccag
     2461 ctgtctaggg cggcggattt gtcctactca ggagagcgtt caccgacaaa caacagataa
     2521 aacgaaaggc ccagtctttc gactgagcct ttcgttttat ttgatgcctt taattaaggc
     2581 tcgggagacc tatcggtaat aacagtccaa tctggtgtaa cttcggaatc gtccttgaca
     2641 gctagctcag tcctaggtat aatgctagct actagtgaaa gaggagaaat actagtatgg
     2701 ttagcaaagg cgaggcggtt atcaaggagt ttatgcgttt taaggttcac atggagggta
     2761 gcatgaatgg tcacgagttc gagatcgagg gtgaaggcga gggtcgtccg tacgaaggca
     2821 cccagaccgc gaagctgaaa gtgaccaagg gtggcccgct gccgttcagc tgggacatcc
     2881 tgagcccgca gttcatgtat ggcagccgtg cgtttaccaa acacccggcg gacattccgg
     2941 attactataa gcaaagcttc ccggaaggtt ttaaatggga gcgtgttatg aacttcgaag
     3001 atggtggcgc ggtgaccgtt acccaggaca ccagcctgga ggatggcacc ctgatttaca
     3061 aggtgaaact gcgtggcacc aactttccgc cggatggtcc ggttatgcag aagaaaacga
     3121 tgggttggga agcgagcacc gagcgtctgt atccggaaga tggcgtgctg aagggtgata
     3181 tcaaaatggc gctgcgtctg aaggacggtg gccgttacct ggcggatttt aagaccacct
     3241 ataaagcgaa gaaaccggtg caaatgccgg gtgcgtacaa cgttgaccgt aaactggata
     3301 ttaccagcca caacgaggat tataccgtgg ttgagcaata tgagcgtagc gagggtcgcc
     3361 acagcaccgg cggcatggac gaactgtata agggatccta ataacgctga tagtgctagt
     3421 gtagatcgct actagagcca ggcatcaaat aaaacgaaag gctcagtcga aagactgggc
     3481 ctttcgtttt atctgttgtt tgtcggtgaa cgctctctac tagagtcaca ctggctcacc
     3541 ttcgggtggg cctttctgcg tttatatact ggctcg
//
""",
                    "collection": "BASIC_SEVA_PARTS",
                    "description": "BASIC SEVA vector containing Gentamicin resistance marker and pBR322-ROP origin of replication.",
                    "label": "BASIC_SEVA_69",
                },
            ],
        },
    ]
}

snapshots["test_collection_names 1"] = 200

snapshots["test_collection_names 2"] = {
    "data": [
        "BASIC_BIOLEGIO_LINKERS",
        "BASIC_CDS_PARTS",
        "BASIC_PROMOTER_PARTS",
        "BASIC_SEVA_PARTS",
    ]
}

snapshots["test_get_seq_labels 1"] = 200

snapshots["test_get_seq_labels 2"] = ["label", "Feature"]

snapshots["test_root_hello_world 1"] = 200

snapshots["test_root_hello_world 2"] = {"message": "Hello World"}

snapshots["test_singular_build_PDF_instructions 1"] = 200

snapshots["test_singular_build_csvs 1"] = 200

snapshots["test_singular_build_echo_instructions 1"] = 200

snapshots["test_singular_build_json 1"] = 200

snapshots["test_singular_file_upload 1"] = 200

snapshots["test_singular_file_upload 2"] = {
    "result": "success",
    "seq": "TCTGGTGGGTCTCTGTCCatgcgtaaaggcgaagaactgttcacgggcgtagttccgattctggtcgagctggacggcgatgtgaacggtcataagtttagcgttcgcggtgaaggtgagggcgacgcgaccaacggcaaactgaccctgaagttcatctgcaccaccggtaaactgccggtgccttggccgaccttggtgacgacgttgacgtatggcgtgcagtgttttgcgcgttatccggaccacatgaaacaacacgatttcttcaaatctgcgatgccggagggttacgtccaggagcgtaccatttccttcaaggatgatggcacttacaaaactcgcgcagaggttaagtttgaaggtgacacgctggtcaatcgtatcgaattgaagggtatcgactttaaagaggatggtaacattctgggccataaactggagtataacttcaacagccataatgtttacattacggcagacaagcaaaagaacggcatcaaggccaatttcaagattcgccacaatgttgaggacggtagcgtccaactggccgaccattaccagcagaacaccccaattggtgacggtccggttttgctgccggataatcactatctgagcacccaaagcgtgctgagcaaagatccgaacgaaaaacgtgatcacatggtcctgctggaatttgtgaccgctgcgggcatcacccacggtatggacgagctgtataagcgtccgtaaGGCTCGGGAGACCTATCG",
}

snapshots["test_singular_file_upload 3"] = 200

snapshots["test_singular_file_upload 4"] = {
    "error": "BASIC_sfGFP_ORF lacks iP sequence"
}

snapshots["test_singular_file_upload 5"] = 200

snapshots["test_singular_file_upload 6"] = {
    "result": "success",
    "seq": "TCTGGTGGGTCTCTGTCCATGCGTAAAGGCGAAGAACTGTTCACGGGCGTAGTTCCGATTCTGGTCGAGCTGGACGGCGATGTGAACGGTCATAAGTTTAGCGTTCGCGGTGAAGGTGAGGGCGACGCGACCAACGGCAAACTGACCCTGAAGTTCATCTGCACCACCGGTAAACTGCCGGTGCCTTGGCCGACCTTGGTGACGACGTTGACGTATGGCGTGCAGTGTTTTGCGCGTTATCCGGACCACATGAAACAACACGATTTCTTCAAATCTGCGATGCCGGAGGGTTACGTCCAGGAGCGTACCATTTCCTTCAAGGATGATGGCACTTACAAAACTCGCGCAGAGGTTAAGTTTGAAGGTGACACGCTGGTCAATCGTATCGAATTGAAGGGTATCGACTTTAAAGAGGATGGTAACATTCTGGGCCATAAACTGGAGTATAACTTCAACAGCCATAATGTTTACATTACGGCAGACAAGCAAAAGAACGGCATCAAGGCCAATTTCAAGATTCGCCACAATGTTGAGGACGGTAGCGTCCAACTGGCCGACCATTACCAGCAGAACACCCCAATTGGTGACGGTCCGGTTTTGCTGCCGGATAATCACTATCTGAGCACCCAAAGCGTGCTGAGCAAAGATCCGAACGAAAAACGTGATCACATGGTCCTGCTGGAATTTGTGACCGCTGCGGGCATCACCCACGGTATGGACGAGCTGTATAAGCGTCCGTAAGGCTCGGGAGACCTATCG",
}

snapshots["test_singular_file_upload 7"] = 200

snapshots["test_singular_file_upload 8"] = {
    "error": "BASIC_sfGFP_ORF_[52-774] lacks iP sequence"
}

snapshots["test_singular_unique_assemblies_genbank 1"] = 200

snapshots["test_singular_unique_parts_genbank 1"] = 200

snapshots["test_validate_failure 1"] = 200

snapshots["test_validate_failure 2"] = {
    "detail": "Alternating BasicPart, BasicLinker instances required: 00d898637a50a35f638cd3c4bc3ef744 is preceeded by <class 'basicsynbio.main.BasicLinker'> and is of type <class 'basicsynbio.main.BasicLinker'>.",
    "result": "failed",
}

snapshots["test_validate_success 1"] = 200

snapshots["test_validate_success 2"] = {"result": "success"}
