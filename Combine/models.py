models = {
  "mu_inclusive":"",

  "mu_inclusive_wsyst":"",

  "mu_fiducial":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggh_in.*:r[1,0,2]\" \
--PO \"map=.*/vbf_in.*:r[1,0,2]\" \
--PO \"map=.*/vh_in.*:r[1,0,2]\" \
--PO \"map=.*/tth_in.*:r[1,0,2]\"",

  "mu_fiducial_observed":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/ggh_in.*:r[1,0,2]\" \
  --PO \"map=.*/vbf_in.*:r[1,0,2]\" \
  --PO \"map=.*/vh_in.*:r[1,0,2]\" \
  --PO \"map=.*/tth_in.*:r[1,0,2]\"",

  "mu":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/bbH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/qqH.*:r_VBF[1,0,3]\" \
--PO \"map=.*/WH_had.*:r_VH[1,0,3]\" \
--PO \"map=.*/ZH_had.*:r_VH[1,0,3]\" \
--PO \"map=.*/ggZH_had.*:r_VH[1,0,3]\" \
--PO \"map=.*/WH_lep.*:r_VH[1,0,3]\" \
--PO \"map=.*/ZH_lep.*:r_VH[1,0,3]\" \
--PO \"map=.*/ggZH_ll.*:r_VH[1,0,3]\" \
--PO \"map=.*/ggZH_nunu.*:r_VH[1,0,3]\" \
--PO \"map=.*/ttH.*:r_top[1,0,3]\" \
--PO \"map=.*/tHq.*:r_top[1,0,3]\" \
--PO \"map=.*/tHW.*:r_top[1,0,3]\"",

  "stage0":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/bbH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/qqH.*:r_qqH[1,0,3]\" \
--PO \"map=.*/WH_had.*:r_qqH[1,0,3]\" \
--PO \"map=.*/ZH_had.*:r_qqH[1,0,3]\" \
--PO \"map=.*/ggZH_had.*:r_ggH[1,0,2]\" \
--PO \"map=.*/WH_lep.*:r_WH_lep[1,0,5]\" \
--PO \"map=.*/ZH_lep.*:r_ZH_lep[1,0,5]\" \
--PO \"map=.*/ggZH_ll.*:r_ZH_lep[1,0,5]\" \
--PO \"map=.*/ggZH_nunu.*:r_ZH_lep[1,0,5]\" \
--PO \"map=.*/ttH.*:r_ttH[1,0,3]\" \
--PO \"map=.*/tHq.*:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*:r_tH[1,0,15]\"",

  "stage1p2_maximal":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=RECO_0J_PTH_0_10_Tag.*/bbH.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggH_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggZH_had_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=RECO_0J_PTH_GT10_Tag.*/bbH.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggH_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=RECO_1J_PTH_0_60_Tag.*/bbH.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=RECO_1J_PTH_60_120_Tag.*/bbH.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=RECO_1J_PTH_120_200_Tag.*/bbH.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_0_60_Tag.*/bbH.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_60_120_Tag.*/bbH.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_120_200_Tag.*/bbH.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_.*:r_ggH_BSM[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_.*:r_ggH_BSM[1,0,4]\" \
--PO \"map=RECO_PTH.*/bbH.*:r_ggH_BSM[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/qqH_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/WH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/ZH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/qqH_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_lep.*hgg:r_WH_lep[1,0,6]\" \
--PO \"map=.*/ZH_lep.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_ll.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_nunu.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ttH.*hgg:r_ttH[1,0,3]\" \
--PO \"map=.*/tHq.*hgg:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*hgg:r_tH[1,0,15]\"",

  "stage1p2_minimal":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=RECO_0J_PTH_0_10_Tag.*/bbH.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggH_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggZH_had_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=RECO_0J_PTH_GT10_Tag.*/bbH.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggH_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=RECO_1J_PTH_0_60_Tag.*/bbH.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=RECO_1J_PTH_60_120_Tag.*/bbH.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=RECO_1J_PTH_120_200_Tag.*/bbH.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_0_60_Tag.*/bbH.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_60_120_Tag.*/bbH.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_120_200_Tag.*/bbH.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=RECO_PTH_200_300_Tag.*/bbH.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggH_PTH_300_450.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_300_450.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=RECO_PTH_300_450_Tag.*/bbH.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_450_650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_450_650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=RECO_PTH_450_650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_GT650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_GT650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=RECO_PTH_GT650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/WH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/ZH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/qqH_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_0_75.*hgg:r_WH_lep_low[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_75_150.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_150_250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_GT250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/ZH_lep.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_ll.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_nunu.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ttH_PTH_0_60.*hgg:r_ttH_low[1,0,5]\" \
--PO \"map=.*/ttH_PTH_60_120.*hgg:r_ttH_medlow[1,0,3]\" \
--PO \"map=.*/ttH_PTH_120_200.*hgg:r_ttH_medhigh[1,0,4]\" \
--PO \"map=.*/ttH_PTH_200_300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/ttH_PTH_GT300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/tHq.*hgg:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*hgg:r_tH[1,0,15]\"",

  "stage1p2_extended":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=RECO_0J_PTH_0_10_Tag.*/bbH.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggH_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggZH_had_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=RECO_0J_PTH_GT10_Tag.*/bbH.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggH_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=RECO_1J_PTH_0_60_Tag.*/bbH.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=RECO_1J_PTH_60_120_Tag.*/bbH.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=RECO_1J_PTH_120_200_Tag.*/bbH.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_0_60_Tag.*/bbH.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_60_120_Tag.*/bbH.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_120_200_Tag.*/bbH.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=RECO_PTH_200_300_Tag.*/bbH.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggH_PTH_300_450.*:r_ggH_BSM_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_300_450.*:r_ggH_BSM_med[1,0,4]\" \
--PO \"map=RECO_PTH_300_450_Tag.*/bbH.*:r_ggH_BSM_med[1,0,4]\" \
--PO \"map=.*/ggH_PTH_450_650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggZH_had_PTH_450_650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=RECO_PTH_450_650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggH_PTH_GT650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggZH_had_PTH_GT650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=RECO_PTH_GT650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/WH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/ZH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/qqH_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_0_75.*hgg:r_WH_lep_low[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_75_150.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_150_250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_GT250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/ZH_lep.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_ll.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_nunu.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ttH_PTH_0_60.*hgg:r_ttH_low[1,0,5]\" \
--PO \"map=.*/ttH_PTH_60_120.*hgg:r_ttH_medlow[1,0,3]\" \
--PO \"map=.*/ttH_PTH_120_200.*hgg:r_ttH_medhigh[1,0,4]\" \
--PO \"map=.*/ttH_PTH_200_300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/ttH_PTH_GT300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/tHq.*hgg:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*hgg:r_tH[1,0,15]\"",


  "PTH":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggh_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_0p0_15p0.*:r_PTH_0p0_15p0[1,-3,3]\" \
--PO \"map=.*/ggh_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_15p0_30p0.*:r_PTH_15p0_30p0[1,-3,3]\" \
--PO \"map=.*/ggh_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_30p0_45p0.*:r_PTH_30p0_45p0[1,-3,3]\" \
--PO \"map=.*/ggh_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_45p0_80p0.*:r_PTH_45p0_80p0[1,-3,3]\" \
--PO \"map=.*/ggh_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_80p0_120p0.*:r_PTH_80p0_120p0[1,-3,3]\" \
--PO \"map=.*/ggh_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_120p0_200p0.*:r_PTH_120p0_200p0[1,-3,3]\" \
--PO \"map=.*/ggh_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_200p0_350p0.*:r_PTH_200p0_350p0[1,-3,3]\" \
--PO \"map=.*/ggh_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,-3,3]\" \
--PO \"map=.*/tth_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,-3,3]\" \
--PO \"map=.*/vh_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,-3,3]\" \
--PO \"map=.*/vbf_PTH_350p0_10000p0.*:r_PTH_350p0_10000p0[1,-3,3]\"",

  "rapidity":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggh_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]\" \
--PO \"map=.*/tth_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]\" \
--PO \"map=.*/vh_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]\" \
--PO \"map=.*/vbf_YH_0p0_0p15.*:r_YH_0p0_0p15[1,0,3]\" \
--PO \"map=.*/ggh_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]\" \
--PO \"map=.*/tth_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]\" \
--PO \"map=.*/vh_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]\" \
--PO \"map=.*/vbf_YH_0p15_0p3.*:r_YH_0p15_0p3[1,0,3]\" \
--PO \"map=.*/ggh_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]\" \
--PO \"map=.*/tth_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]\" \
--PO \"map=.*/vh_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]\" \
--PO \"map=.*/vbf_YH_0p3_0p6.*:r_YH_0p3_0p6[1,0,3]\" \
--PO \"map=.*/ggh_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]\" \
--PO \"map=.*/tth_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]\" \
--PO \"map=.*/vh_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]\" \
--PO \"map=.*/vbf_YH_0p6_0p9.*:r_YH_0p6_0p9[1,0,3]\" \
--PO \"map=.*/ggh_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]\" \
--PO \"map=.*/tth_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]\" \
--PO \"map=.*/vh_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]\" \
--PO \"map=.*/vbf_YH_0p9_2p5.*:r_YH_0p9_2p5[1,0,3]\"",

  "Njets2p5_5bin":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggh_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/ggh_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/ggh_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/ggh_NJ_3p0_4p0.*:r_NJ_3p0_4p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_3p0_4p0.*:r_NJ_3p0_4p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_3p0_4p0.*:r_NJ_3p0_4p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_3p0_4p0.*:r_NJ_3p0_4p0[1,0,3]\" \
--PO \"map=.*/ggh_NJ_4p0_100p0.*:r_NJ_4p0_100p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_4p0_100p0.*:r_NJ_4p0_100p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_4p0_100p0.*:r_NJ_4p0_100p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_4p0_100p0.*:r_NJ_4p0_100p0[1,0,3]\"",

  "Njets2p5":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggh_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_0p0_1p0.*:r_NJ_0p0_1p0[1,0,3]\" \
--PO \"map=.*/ggh_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_1p0_2p0.*:r_NJ_1p0_2p0[1,0,3]\" \
--PO \"map=.*/ggh_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_2p0_3p0.*:r_NJ_2p0_3p0[1,0,3]\" \
--PO \"map=.*/ggh_NJ_3p0_100p0.*:r_NJ_3p0_100p0[1,0,3]\" \
--PO \"map=.*/tth_NJ_3p0_100p0.*:r_NJ_3p0_100p0[1,0,3]\" \
--PO \"map=.*/vh_NJ_3p0_100p0.*:r_NJ_3p0_100p0[1,0,3]\" \
--PO \"map=.*/vbf_NJ_3p0_100p0.*:r_NJ_3p0_100p0[1,0,3]\"",

  "PTJ0":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggh_PTJ0_0p0_30p0.*:r_PTJ0_0p0_30p0[1,0,3]\" \
--PO \"map=.*/tth_PTJ0_0p0_30p0.*:r_PTJ0_0p0_30p0[1,0,3]\" \
--PO \"map=.*/vh_PTJ0_0p0_30p0.*:r_PTJ0_0p0_30p0[1,0,3]\" \
--PO \"map=.*/vbf_PTJ0_0p0_30p0.*:r_PTJ0_0p0_30p0[1,0,3]\" \
--PO \"map=.*/ggh_PTJ0_30p0_45p0.*:r_PTJ0_30p0_45p0[1,0,3]\" \
--PO \"map=.*/tth_PTJ0_30p0_45p0.*:r_PTJ0_30p0_45p0[1,0,3]\" \
--PO \"map=.*/vh_PTJ0_30p0_45p0.*:r_PTJ0_30p0_45p0[1,0,3]\" \
--PO \"map=.*/vbf_PTJ0_30p0_45p0.*:r_PTJ0_30p0_45p0[1,0,3]\" \
--PO \"map=.*/ggh_PTJ0_45p0_70p0.*:r_PTJ0_45p0_70p0[1,0,3]\" \
--PO \"map=.*/tth_PTJ0_45p0_70p0.*:r_PTJ0_45p0_70p0[1,0,3]\" \
--PO \"map=.*/vh_PTJ0_45p0_70p0.*:r_PTJ0_45p0_70p0[1,0,3]\" \
--PO \"map=.*/vbf_PTJ0_45p0_70p0.*:r_PTJ0_45p0_70p0[1,0,3]\" \
--PO \"map=.*/ggh_PTJ0_70p0_110p0.*:r_PTJ0_70p0_110p0[1,0,3]\" \
--PO \"map=.*/tth_PTJ0_70p0_110p0.*:r_PTJ0_70p0_110p0[1,0,3]\" \
--PO \"map=.*/vh_PTJ0_70p0_110p0.*:r_PTJ0_70p0_110p0[1,0,3]\" \
--PO \"map=.*/vbf_PTJ0_70p0_110p0.*:r_PTJ0_70p0_110p0[1,0,3]\" \
--PO \"map=.*/ggh_PTJ0_110p0_200p0.*:r_PTJ0_110p0_200p0[1,0,3]\" \
--PO \"map=.*/tth_PTJ0_110p0_200p0.*:r_PTJ0_110p0_200p0[1,0,3]\" \
--PO \"map=.*/vh_PTJ0_110p0_200p0.*:r_PTJ0_110p0_200p0[1,0,3]\" \
--PO \"map=.*/vbf_PTJ0_110p0_200p0.*:r_PTJ0_110p0_200p0[1,0,3]\" \
--PO \"map=.*/ggh_PTJ0_200p0_10000p0.*:r_PTJ0_200p0_10000p0[1,0,3]\" \
--PO \"map=.*/tth_PTJ0_200p0_10000p0.*:r_PTJ0_200p0_10000p0[1,0,3]\" \
--PO \"map=.*/vh_PTJ0_200p0_10000p0.*:r_PTJ0_200p0_10000p0[1,0,3]\" \
--PO \"map=.*/vbf_PTJ0_200p0_10000p0.*:r_PTJ0_200p0_10000p0[1,0,3]\"",



  "kappas_resolved":"-P HiggsAnalysis.CombinedLimit.LHCHCGModels:K1 --PO BRU=0",

  "kappas":"-P HiggsAnalysis.CombinedLimit.LHCHCGModels:K2 --PO BRU=0",

  "kVkF":"-P HiggsAnalysis.CombinedLimit.LHCHCGModels:K3 --PO BRU=0"
}
