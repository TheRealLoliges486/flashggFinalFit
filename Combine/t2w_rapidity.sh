#!/bin/bash

text2workspace.py Datacard_rapidity.txt -o Datacard_rapidity.root -m 125.38 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO "map=.*/ggh_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]" --PO "map=.*/tth_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]" --PO "map=.*/vh_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]" --PO "map=.*/vbf_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]" --PO "map=.*/ggh_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]" --PO "map=.*/tth_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]" --PO "map=.*/vh_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]" --PO "map=.*/vbf_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]" --PO "map=.*/ggh_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]" --PO "map=.*/tth_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]" --PO "map=.*/vh_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]" --PO "map=.*/vbf_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]" --PO "map=.*/ggh_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]" --PO "map=.*/tth_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]" --PO "map=.*/vh_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]" --PO "map=.*/vbf_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]" --PO "map=.*/ggh_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]" --PO "map=.*/tth_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]" --PO "map=.*/vh_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]" --PO "map=.*/vbf_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]"