# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_collection_data 1"] = 200

snapshots["test_collection_data 2"] = {
    "data": [
        {
            "availableVersions": ["v0.1"],
            "name": "BASIC_SEVA_PARTS",
            "versions": [
                {
                    "name": "v0.1",
                    "parts": [
                        {
                            "accessor": "12",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_12",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "13",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_13",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "14",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_14",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "15",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_15",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "16",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_16",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "17",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_17",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "18",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_18",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "19",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_19",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "22",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_22",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "23",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_23",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "24",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_24",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "25",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_25",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "26",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_26",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "27",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_27",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "28",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_28",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "29",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_29",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "32",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_32",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "33",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_33",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "34",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_34",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "35",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_35",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "36",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_36",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "37",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_37",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "38",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_38",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "39",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_39",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "42",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_42",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "43",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_43",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "44",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_44",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "45",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_45",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "46",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_46",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "47",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_47",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "48",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_48",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "49",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_49",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "52",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_52",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "53",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_53",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "54",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_54",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "55",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_55",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "56",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_56",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "57",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_57",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "58",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_58",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "59",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_59",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "62",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_62",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "63",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_63",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "64",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_64",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "65",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_65",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "66",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_66",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "67",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_67",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "68",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_68",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                        {
                            "accessor": "69",
                            "base64": None,
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
                            "id": None,
                            "index": None,
                            "label": "BASIC_SEVA_69",
                            "multiple": None,
                            "type": None,
                            "version": "v0.1",
                        },
                    ],
                }
            ],
        }
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

snapshots["test_dna_feature_viewer 1"] = 200

snapshots["test_dna_feature_viewer 2"] = {
    "base64image": "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",
    "success": True,
}

snapshots["test_dna_feature_viewer_assembly 1"] = 200

snapshots["test_dna_feature_viewer_assembly 2"] = {
    "base64image": "iVBORw0KGgoAAAANSUhEUgAAA+gAAAEECAYAAAC7uh40AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAA9hAAAPYQGoP6dpAABQyElEQVR4nO3dZ1wU1/4G8GeXpfdeBFSaXQE19oYldqzR5CZGkxiTmJjkn5ube9NuetPElJtEU9TkJsYGggW7YsdeAMUKghSVXhe2zP8F19V1Kbu4sLP4fD+ffcHsOWfOcHbmzG/mzBmJIAgCiIiIiIiIiMikpKauABERERERERExQCciIiIiIiISBQboRERERERERCLAAJ2IiIiIiIhIBBigExEREREREYkAA3QiIiIiIiIiEWCATkRERERERCQCDNCJiIiIiIiIRIABOhEREREREZEIMEAnIiIiIiIiEgEG6EREREREREQiwACdiIiIiIiISAQYoBMRERERERGJAAN0IiIiIiIiIhFggE5EREREREQkAgzQiYiIiIiIiESAAToRERERERGRCDBAJyIiIiIiIhIBBuhEREREREREIsAAnYiIiIiIiEgEGKATERERERERiQADdCIiIiIiIiIRYIBOREREREREJAIM0ImIiIiIiIhEgAE6ERERERERkQgwQCciIiIiIiISAQboRERERERERCLAAJ2IiIiIiIhIBBigExEREREREYkAA3QiIiIiIiIiEWCATkRERERERCQCDNCJiIiIiIiIRIABOhEREREREZEIMEAnIiIiIiIiEgEG6EREREREREQiwACdiIiIiIiISAQYoBMRERERERGJAAN0IiIiIiIiIhFggE5EREREREQkAgzQiYiIiIiIiESAAToRERERERGRCDBAJyIiIiIiIhIBBuhEREREREREIsAAnYiIiIiIiEgEGKATERERERERiQADdCIiIiIiIiIRYIBOREREREREJAIyU1eAiIiIxE8ul+PSxcsor6iABBJTV0dvgiDAwsICgW394e3tDYnEfOpOREQPHokgCIKpK0FERETiJAgCkpKOAioZAgOCYWdrb3ZBrkqlQk5uJm7cuo7efSLh7Oxs6ioRERHViQE6ERER1evkidNwcfSBm6uHqaty3wRBwLFT+zFi5FBIpXzKj4iIxIe9ExEREdWrvKyyVQTnACCR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wNPLAwEBAfyBEhFRq6RUKpGeno7i4lKoVQ0Pe29K32xoHlP3/xKJBPb2dggOCYKNDW9YENGDpbq6GlcuX0V5eYXJJxNtiT6nMVILKZycHBEcHASZrOkvS2tygC4mEydOxIYNG0xdDSIiIvqfpvTNhuZh/09EREDL9DktheOwiIiIiIiIiESAAToRERERERGRCDBAJyIiIiIiIhIBBuhEREREREREIsAAnYiIiIiIiEgEGKATERERERERiQADdCIiIiIiIiIRYIBOREREREREJAIM0ImIiIiIiIhEgAE6ERERERERkQgwQCciIiIiIiISAQboRERERERERCLAAJ2IiIiIiIhIBBigExEREREREYkAA3QiIiIiIiIiEWCATkRERERERCQCDNCJiIiIiIiIRIABOhEREREREZEIMEAnIiIiIiIiEgEG6EREREREREQiIDN1BfShVqtRVlZW53eOjo56lyMIAkpLS41VLWolJBIJnJycjF5udXU15HK50cslIjI2R0dHSKWGXbOv7xgnlUr16puVSiUqKio0fzs4OOikqaiogFKp1FlubW0NGxsbvetaWVkJhUKhd3p6MNjZ2cHS0tKoZfJck6hxVlZWsLW1NShPQ/uWnZ2dXmWUl5dDpVIBgNH3faMSzMCcOXMEAHV+Bg4YJIwdO1avcl555ZV6y+Hnwf5MnTJNKC8vN9pvVqlUCp4eXibfLn744YcffT49ukcI165d0/sYV1VVJTg7u9Rb3ksvvSSMHz++wTKGR43QytOvb3+tPMePHxekUmmd5dva2gm7du0SJkyY0Ghd09LSBJlMZvL/MT/i+3h5+ggHDx7U+3evj/fee8/k28UPP2L/WFpaCUuWLDFo33r77bfrLc/P118YPnx4g/m3bNmilUcqlQoDBgy4n9292ZjFHfScnFz4OPdAr7ZPay2vVpQh8ciH8PB0g1qtbvTqf05ODjwdO6BP+/nNWV0yMxXV+di4cREG9B+ETZs3wN/f/77LVKlUuJV/Ez0CHkeA60NGqCURUfNQqmuQdGUxevV8CPEb1qNfv36N5pHL5SgpKUbPwKfg6xKu9V1++SV899136NSpU4NlZGfnoL3HUHTxm4Liyms4kPSl1rpv3LgBtVqNEZ0+go2l9iin5OxVmDRpCnr2jGi0rrdu3YJSqcTQsLfgYOPdaHp6MAiCgLPZf2Do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",
    "success": True,
}

snapshots["test_get_part_labels 1"] = 200

snapshots["test_get_part_labels 2"] = {
    "annotated": [
        {"direction": 1, "end": 160, "name": "SEVA_T0", "start": 57},
        {"direction": 1, "end": 3832, "name": "J23119", "start": 3797},
        {"direction": 1, "end": 4843, "name": "LMP", "start": 4837},
        {"direction": 1, "end": 4833, "name": "B0015", "start": 4704},
        {"direction": 1, "end": 3705, "name": "LMS", "start": 3648},
        {"direction": 1, "end": 4668, "name": "mScarlett", "start": 3963},
        {"direction": 1, "end": 3639, "name": "SEVA_T1", "start": 3534},
        {"direction": 1, "end": 3520, "name": "SEVA_RK2", "start": 1298},
        {"direction": 1, "end": 1225, "name": "SEVA_Ap", "start": 186},
    ],
    "seq": "GGTAAGAACTCGCACTTCGTGGAAACACTATTATCTGGTGGGTCTCTGTCCACTAGTCTTGGACTCCTGTTGATAGATCCAGTAATGACCTCAGAACTCCATCTGGATTTGTTCAGAACGCTCGGTTGCCGCCGGGCGTTTTTTATTGGTGAGAATCCAGGGGTCCCCAATAATTACGATTTAAATTAGTAGCCCGCCTAATGAGCGGGCTTTTTTTTAATTCCCCTATTTGTTTATTTTTCTAAATACATTCAAATATGTATCCGCTCATGAGACAATAACCCTGATAAATGCTTCAATAATATTGAAAAAGGAAGAGTATGAGCATTCAGCATTTTCGTGTGGCGCTGATTCCGTTTTTTGCGGCGTTTTGCCTGCCGGTGTTTGCGCATCCGGAAACCCTGGTGAAAGTGAAAGATGCGGAAGATCAACTGGGTGCGCGCGTGGGCTATATTGAACTGGATCTGAACAGCGGCAAAATTCTGGAATCTTTTCGTCCGGAAGAACGTTTTCCGATGATGAGCACCTTTAAAGTGCTGCTGTGCGGTGCGGTTCTGAGCCGTGTGGATGCGGGCCAGGAACAACTGGGCCGTCGTATTCATTATAGCCAGAACGATCTGGTGGAATATAGCCCGGTGACCGAAAAACATCTGACCGATGGCATGACCGTGCGTGAACTGTGCAGCGCGGCGATTACCATGAGCGATAACACCGCGGCGAACCTGCTGCTGACGACCATTGGCGGTCCGAAAGAACTGACCGCGTTTCTGCATAACATGGGCGATCATGTGACCCGTCTGGATCGTTGGGAACCGGAACTGAACGAAGCGATTCCGAACGATGAACGTGATACCACCATGCCGGCAGCAATGGCGACCACCCTGCGTAAACTGCTGACGGGTGAGCTGCTGACCCTGGCAAGCCGCCAGCAACTGATTGATTGGATGGAAGCGGATAAAGTGGCGGGTCCGCTGCTGCGTAGCGCGCTGCCGGCTGGCTGGTTTATTGCGGATAAAAGCGGTGCGGGCGAACGTGGCAGCCGTGGCATTATTGCGGCGCTGGGCCCGGATGGTAAACCGAGCCGTATTGTGGTGATTTATACCACCGGCAGCCAGGCGACGATGGATGAACGTAACCGTCAGATTGCGGAAATTGGCGCGAGCCTGATTAAACATTGGTAAACCGATACAATTAAAGGCTCCTTTTGGAGCCTTTTTTTTTGGACGACCCTTGTCGGCTCGACCCACGACTATTGACTGCTCTGAGAAAGTTGATTGTTACGATTAGTCCGGCCGGCCGCGATGCAGGTGGCTGCTGAACCCCCAGCCGGAACTGACCCCACAAGGCCCTAGCGTTTGCAATGCACCAGGTCATCATTGACCCAGGCGTGTTCCACCAGGCCGCTGCCTCGCAACTCTTCGCAGGCTTCGCCGACCTGCTCGCGCCACTTCTTCACGCGGGTGGAATCCGATCCGCACATGAGGCGGAAGGTTTCCAGCTTGAGCGGGTACGGCTCCCGGTGCGAGCTGAAATAGTCGAACATCCGTCGGGCCGTCGGCGACAGCTTGCGGTACTTCTCCCATATGAATTTCGTGTAGTGGTCGCCAGCAAACAGCACGACGATTTCCTCGTCGATCAGGACCTGGCAACGGGACGTTTTCTTGCCACGGTCCAGGACGCGGAAGCGGTGCAGCAGCGACACCGATTCCAGGTGCCCAACGCGGTCGGACGTGAAGCCCATCGCCGTCGCCTGTAGGCGCGACAGGCATTCCTCGGCCTTCGTGTAATACCGGCCATTGATCGACCAGCCCAGGTCCTGGCAAAGCTCGTAGAACGTGAAGGTGATCGGCTCGCCGATAGGGGTGCGCTTCGCGTACTCCAACACCTGCTGCCACACCAGTTCGTCATCGTCGGCCCGCAGCTCGACGCCGGTGTAGGTGATCTTCACGTCCTTGTTGACGTGGAAAATGACCTTGTTTTGCAGCGCCTCGCGCGGGATTTTCTTGTTGCGCGTGGTGAACAGGGCAGAGCGGGCCGTGTCGTTTGGCATCGCTCGCATCGTGTCCGGCCACGGCGCAATATCGAACAAGGAAAGCTGCATTTCCTTGATCTGCTGCTTCGTGTGTTTCAGCAACGCGGCCTGCTTGGCTTCGCTGACCTGTTTTGCCAGGTCCTCGCCGGCGGTTTTTCGCTTCTTGGTCGTCATAGTTCCTCGCGTGTCGATGGTCATCGACTTCGCCAAACCTGCCGCCTCCTGTTCGAGACGACGCGAACGCTCCACGGCGGCCGATGGCGCGGGCAGGGCAGGGGGAGCCAGTTGCACGCTGTCGCGCTCGATCTTGGCCGTAGCTTGCTGGACTATCGAGCCGACGGACTGGAAGGTTTCGCGGGGCGCACGCATGACGGTGCGGCTTGCGATGGTTTCGGCATCCTCGGCGGAAAACCCCGCGTCGATCAGTTCTTGCCTGTATGCCTTCCGGTCAAACGTCCGATTCATTCACCCTCCTTGCGGGATTGCCCCGGAATTAATTCCCCGGATCGATCCGTCGATCTTGATCCCCTGCGCCATCAGATCCTTGGCGGCAAGAAAGCCATCCAGTTTACTTTGCAGGGCTTCCCAACCTTACCAGAGGGCGCCCCAGCTGGCAATTCCGGTTCGCTTGCTGTCCATAAAACCGCCCAGTCTAGCTATCGCCATGTAAGCCCACTGCAAGCTACCTGCTTTCTCTTTGCGCTTGCGTTTTCCCTTGTCCAGATAGCCCAGTAGCTGACATTCATCCGGGGTCAGCACCGTTTCTGCGGACTGGCTTTCTACGTGGCTGCCATTTTTGGGGTGAGGCCGTTCGCGGCCGAGGGGCGCAGCCCCTGGGGGGATGGGAGGCCCGCGTTAGCGGGCCGGGAGGGTTCGAGAAGGGGGGGCACCCCCCTTCGGCGTGCGCGGTCACGCGCACAGGGCGCAGCCCTGGTTAAAAACAAGGTTTATAAATATTGGTTTAAAAGCAGGTTAAAAGACAGGTTAGCGGTGGCCGAAAAACGGGCGGAAACCCTTGCAAATGCTGGATTTTCTGCCTGTGGACAGCCCCTCAAATGTCAATAGGTGCGCCCCTCATCTGTCAGCACTCTGCCCCTCAAGTGTCAAGGATCGCGCCCCTCATCTGTCAGTAGTCGCGCCCCTCAAGTGTCAATACCGCAGGGCACTTATCCCCAGGCTTGTCCACATCATCTGTGGGAAACTCGCGTAAAATCAGGCGTTTTCGCCGATTTGCGAGGCTGGCCAGCTCCACGTCGCCGGCCGAAATCGAGCCTGCCCCTCATCTGTCAACGCCGCGCCGGGTGAGTCGGCCCCTCAAGTGTCAACGTCCGCCCCTCATCTGTCAGTGAGGGCCAAGTTTTCCGCGAGGTATCCACAACGCCGGCGGCCCTACATGGCTCTGCTGTAGTGAGTGGGTTGCGCTCCGGCAGCGGTCCTGATCCCCCGCAGAAAAAAAGGATCTCAAGAAGATCCTTTGATCTTTTCTACGGCGCGCCCAGCTGTCTAGGGCGGCGGATTTGTCCTACTCAGGAGAGCGTTCACCGACAAACAACAGATAAAACGAAAGGCCCAGTCTTTCGACTGAGCCTTTCGTTTTATTTGATGCCTTTAATTAAGGCTCGGGAGACCTATCGGTAATAACAGTCCAATCTGGTGTAACTTCGGAATCGTCCCCAATTATTGAACACCCTTCGGGGTGTTTTTTTGTTTCTGGTCTACCATCTCGTTGTGATAATAGACCTGAAGTGCCTACTCTGGAAAATCTTTGACAGCTAGCTCAGTCCTAGGTATAATGCTAGCAGCTGTCACCGGATGTGCTTTCCGGTCTGATGAGTCCGTGAGGACGAAACAGCCTCTACAAATAATTTTGTTTAAGGCTCGCTACGAGAAGATTGTTACTTTCGCAGCGTTATTATCTAAGGAGGTAGTCCATGGTTAGCAAAGGCGAGGCGGTTATCAAGGAGTTTATGCGTTTTAAGGTTCACATGGAGGGTAGCATGAATGGTCACGAGTTCGAGATCGAGGGTGAAGGCGAGGGTCGTCCGTACGAAGGCACCCAGACCGCGAAGCTGAAAGTGACCAAGGGTGGCCCGCTGCCGTTCAGCTGGGACATCCTGAGCCCGCAGTTCATGTATGGCAGCCGTGCGTTTACCAAACACCCGGCGGACATTCCGGATTACTATAAGCAAAGCTTCCCGGAAGGTTTTAAATGGGAGCGTGTTATGAACTTCGAAGATGGTGGCGCGGTGACCGTTACCCAGGACACCAGCCTGGAGGATGGCACCCTGATTTACAAGGTGAAACTGCGTGGCACCAACTTTCCGCCGGATGGTCCGGTTATGCAGAAGAAAACGATGGGTTGGGAAGCGAGCACCGAGCGTCTGTATCCGGAAGATGGCGTGCTGAAGGGTGATATCAAAATGGCGCTGCGTCTGAAGGACGGTGGCCGTTACCTGGCGGATTTTAAGACCACCTATAAAGCGAAGAAACCGGTGCAAATGCCGGGTGCGTACAACGTTGACCGTAAACTGGATATTACCAGCCACAACGAGGATTATACCGTGGTTGAGCAATATGAGCGTAGCGAGGGTCGCCACAGCACCGGCGGCATGGACGAACTGTATAAGGGATCCTAATAACGCTGATAGTGCTAGTGTAGATCGCTACTAGAGCCAGGCATCAAATAAAACGAAAGGCTCAGTCGAAAGACTGGGCCTTTCGTTTTATCTGTTGTTTGTCGGTGAACGCTCTCTACTAGAGTCACACTGGCTCACCTTCGGGTGGGCCTTTCTGCGTTTATATACTGGCTCG",
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
