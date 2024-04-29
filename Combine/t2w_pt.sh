#!/bin/bash

text2workspace.py Datacard_pt.txt -o Datacard_pt.root -m 125.38 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO "map=.*/ggh_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,0,3]" --PO "map=.*/tth_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,0,3]" --PO "map=.*/vh_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,0,3]" --PO "map=.*/vbf_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,0,3]" --PO "map=.*/ggh_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,0,3]" --PO "map=.*/tth_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,0,3]" --PO "map=.*/vh_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,0,3]" --PO "map=.*/vbf_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,0,3]" --PO "map=.*/ggh_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,0,3]" --PO "map=.*/tth_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,0,3]" --PO "map=.*/vh_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,0,3]" --PO "map=.*/vbf_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,0,3]" --PO "map=.*/ggh_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,0,3]" --PO "map=.*/tth_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,0,3]" --PO "map=.*/vh_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,0,3]" --PO "map=.*/vbf_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,0,3]" --PO "map=.*/ggh_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,0,3]" --PO "map=.*/tth_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,0,3]" --PO "map=.*/vh_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,0,3]" --PO "map=.*/vbf_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,0,3]" --PO "map=.*/ggh_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,0,3]" --PO "map=.*/tth_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,0,3]" --PO "map=.*/vh_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,0,3]" --PO "map=.*/vbf_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,0,3]" --PO "map=.*/ggh_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,0,3]" --PO "map=.*/tth_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,0,3]" --PO "map=.*/vh_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,0,3]" --PO "map=.*/vbf_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,0,3]" --PO "map=.*/ggh_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,0,3]" --PO "map=.*/tth_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,0,3]" --PO "map=.*/vh_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,0,3]" --PO "map=.*/vbf_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,0,3]"