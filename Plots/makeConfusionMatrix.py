# Script to make migration + purity matrices and output yields table
#  * Read in PANDAS dataframe

import os, sys
import re
from optparse import OptionParser
import ROOT
import pandas as pd
import glob
import pickle
import json
# Scripts for plotting
from usefulStyle import setCanvas, drawCMS, drawEnPu, drawEnYear, formatHisto
from shanePalette import set_color_palette

print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG YIELDS RUN II ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
def leave():
  print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG YIELDS RUN II (END) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
  exit(0)

ROOT.gROOT.SetBatch(True)

# Define processes
productionModes = ['ggH','qqH','WH_had','ZH_had','ggZH_had','WH_lep','ZH_lep','ggZH_ll','ggZH_nunu','ttH','tHq','tHW','bbH']
#productionModes = ['ggH','qqH','WH_had','ZH_had','WH_lep','ZH_lep','ttH']#,'tHq']
#productionModes = ['ggH']
stxsBins = {
  "ggH":['ggH_0J_PTH_0_10','ggH_0J_PTH_GT10','ggH_1J_PTH_0_60','ggH_1J_PTH_60_120','ggH_1J_PTH_120_200','ggH_GE2J_MJJ_0_350_PTH_0_60','ggH_GE2J_MJJ_0_350_PTH_60_120','ggH_GE2J_MJJ_0_350_PTH_120_200','ggH_PTH_200_300','ggH_PTH_300_450','ggH_PTH_450_650','ggH_PTH_GT650','ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
  "ggZH_had":['ggZH_had_0J_PTH_0_10','ggZH_had_0J_PTH_GT10','ggZH_had_1J_PTH_0_60','ggZH_had_1J_PTH_60_120','ggZH_had_1J_PTH_120_200','ggZH_had_GE2J_MJJ_0_350_PTH_0_60','ggZH_had_GE2J_MJJ_0_350_PTH_60_120','ggZH_had_GE2J_MJJ_0_350_PTH_120_200','ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ggZH_had_PTH_200_300','ggZH_had_PTH_300_450','ggZH_had_PTH_450_650','ggZH_had_PTH_GT650'],
  "qqH":['qqH_0J','qqH_1J','qqH_GE2J_MJJ_0_60','qqH_GE2J_MJJ_60_120','qqH_GE2J_MJJ_120_350','qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','qqH_GE2J_MJJ_GT350_PTH_GT200'],
  "WH_had":['WH_had_0J','WH_had_1J','WH_had_GE2J_MJJ_0_60','WH_had_GE2J_MJJ_60_120','WH_had_GE2J_MJJ_120_350','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_GT350_PTH_GT200'],
  "ZH_had":['ZH_had_0J','ZH_had_1J','ZH_had_GE2J_MJJ_0_60','ZH_had_GE2J_MJJ_60_120','ZH_had_GE2J_MJJ_120_350','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_GT350_PTH_GT200'],
  "WH_lep":['WH_lep_PTV_0_75','WH_lep_PTV_75_150','WH_lep_PTV_150_250_0J','WH_lep_PTV_150_250_GE1J','WH_lep_PTV_GT250'],
  "ZH_lep":['ZH_lep_PTV_0_75','ZH_lep_PTV_75_150','ZH_lep_PTV_150_250_0J','ZH_lep_PTV_150_250_GE1J','ZH_lep_PTV_GT250'],
  "ggZH_ll":['ggZH_ll_PTV_0_75','ggZH_ll_PTV_75_150','ggZH_ll_PTV_150_250_0J','ggZH_ll_PTV_150_250_GE1J','ggZH_ll_PTV_GT250'],
  "ggZH_nunu":['ggZH_nunu_PTV_0_75','ggZH_nunu_PTV_75_150','ggZH_nunu_PTV_150_250_0J','ggZH_nunu_PTV_150_250_GE1J','ggZH_nunu_PTV_GT250'],
  "ttH":['ttH_PTH_0_60','ttH_PTH_60_120','ttH_PTH_120_200','ttH_PTH_200_300','ttH_PTH_GT300'],
  "bbH":['bbH'],
  "tHq":['tHq'],
  "tHW":['tHW']
} 

# Define parameter merging scheme
paramMergingSchemes = {
  "stage1p2_new":{
    "ggH_0J_low":['ggH_0J_PTH_0_10','ggZH_had_0J_PTH_0_10'],
    "ggH_0J_high":['ggH_0J_PTH_GT10','ggZH_had_0J_PTH_GT10','bbH'],
    "ggH_1J_low":['ggH_1J_PTH_0_60','ggZH_had_1J_PTH_0_60'],
    "ggH_1J_med":['ggH_1J_PTH_60_120','ggZH_had_1J_PTH_60_120'],
    "ggH_1J_high":['ggH_1J_PTH_120_200','ggZH_had_1J_PTH_120_200'],
    "ggH_2J_low":['ggH_GE2J_MJJ_0_350_PTH_0_60','ggZH_had_GE2J_MJJ_0_350_PTH_0_60'],
    "ggH_2J_med":['ggH_GE2J_MJJ_0_350_PTH_60_120','ggZH_had_GE2J_MJJ_0_350_PTH_60_120'],
    "ggH_2J_high":['ggH_GE2J_MJJ_0_350_PTH_120_200','ggZH_had_GE2J_MJJ_0_350_PTH_120_200'],
    "ggH_BSM_low":['ggH_PTH_200_300','ggZH_had_PTH_200_300'],
    "ggH_BSM_medlow":['ggH_PTH_300_450','ggZH_had_PTH_300_450'],
    "ggH_BSM_medhigh":['ggH_PTH_450_650','ggZH_had_PTH_450_650'],
    "ggH_BSM_high":['ggH_PTH_GT650','ggZH_had_PTH_GT650'],
    "ggH_VBF_like":['ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    "qqH_other":['qqH_0J','qqH_1J','qqH_GE2J_MJJ_0_60','qqH_GE2J_MJJ_120_350','WH_had_0J','WH_had_1J','WH_had_GE2J_MJJ_0_60','WH_had_GE2J_MJJ_120_350','ZH_had_0J','ZH_had_1J','ZH_had_GE2J_MJJ_0_60','ZH_had_GE2J_MJJ_120_350'],
    "qqH_VH_like":['qqH_GE2J_MJJ_60_120','WH_had_GE2J_MJJ_60_120','ZH_had_GE2J_MJJ_60_120'],
    "qqH_low_mjj_low_pthjj":['qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'],
    "qqH_low_mjj_high_pthjj":['qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'],
    "qqH_high_mjj_low_pthjj":['qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'],
    "qqH_high_mjj_high_pthjj":['qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    "qqH_BSM":['qqH_GE2J_MJJ_GT350_PTH_GT200','WH_had_GE2J_MJJ_GT350_PTH_GT200','ZH_had_GE2J_MJJ_GT350_PTH_GT200'],
    "WH_lep_low":['WH_lep_PTV_0_75'],
    "WH_lep_med":['WH_lep_PTV_75_150'],
    "WH_lep_high":['WH_lep_PTV_150_250_0J','WH_lep_PTV_150_250_GE1J','WH_lep_PTV_GT250'],
    "ZH_lep":['ZH_lep_PTV_0_75','ZH_lep_PTV_75_150','ZH_lep_PTV_150_250_0J','ZH_lep_PTV_150_250_GE1J','ZH_lep_PTV_GT250'],
    "ggZH_lep":['ggZH_ll_PTV_0_75','ggZH_ll_PTV_75_150','ggZH_ll_PTV_150_250_0J','ggZH_ll_PTV_150_250_GE1J','ggZH_ll_PTV_GT250','ggZH_nunu_PTV_0_75','ggZH_nunu_PTV_75_150','ggZH_nunu_PTV_150_250_0J','ggZH_nunu_PTV_150_250_GE1J','ggZH_nunu_PTV_GT250'],
    "ttH_PTH_0_60":['ttH_PTH_0_60'],
    "ttH_PTH_60_120":['ttH_PTH_60_120'],
    "ttH_PTH_120_200":['ttH_PTH_120_200'],
    "ttH_PTH_200_300":['ttH_PTH_200_300'],
    "ttH_PTH_GT300":['ttH_PTH_GT300']
  },

  "stage1p2_minimal":{
    "ggH_0J_low":['ggH_0J_PTH_0_10','ggZH_had_0J_PTH_0_10'],
    "ggH_0J_high":['ggH_0J_PTH_GT10','ggZH_had_0J_PTH_GT10'],
    "ggH_1J_low":['ggH_1J_PTH_0_60','ggZH_had_1J_PTH_0_60'],
    "ggH_1J_med":['ggH_1J_PTH_60_120','ggZH_had_1J_PTH_60_120'],
    "ggH_1J_high":['ggH_1J_PTH_120_200','ggZH_had_1J_PTH_120_200'],
    "ggH_2J_low":['ggH_GE2J_MJJ_0_350_PTH_0_60','ggZH_had_GE2J_MJJ_0_350_PTH_0_60'],
    "ggH_2J_med":['ggH_GE2J_MJJ_0_350_PTH_60_120','ggZH_had_GE2J_MJJ_0_350_PTH_60_120'],
    "ggH_2J_high":['ggH_GE2J_MJJ_0_350_PTH_120_200','ggZH_had_GE2J_MJJ_0_350_PTH_120_200'],
    "ggH_BSM_low":['ggH_PTH_200_300','ggZH_had_PTH_200_300'],
    "ggH_BSM_high":['ggH_PTH_300_450','ggH_PTH_450_650','ggH_PTH_GT650','ggZH_had_PTH_300_450','ggZH_had_PTH_450_650','ggZH_had_PTH_GT650'],
    "ggH_VBF_like":['ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    "qqH_other":['qqH_0J','qqH_1J','qqH_GE2J_MJJ_0_60','qqH_GE2J_MJJ_120_350','WH_had_0J','WH_had_1J','WH_had_GE2J_MJJ_0_60','WH_had_GE2J_MJJ_120_350','ZH_had_0J','ZH_had_1J','ZH_had_GE2J_MJJ_0_60','ZH_had_GE2J_MJJ_120_350'],
    "qqH_VH_like":['qqH_GE2J_MJJ_60_120','WH_had_GE2J_MJJ_60_120','ZH_had_GE2J_MJJ_60_120'],
    "qqH_low_mjj_low_pthjj":['qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'],
    "qqH_low_mjj_high_pthjj":['qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'],
    "qqH_high_mjj_low_pthjj":['qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'],
    "qqH_high_mjj_high_pthjj":['qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    "qqH_BSM":['qqH_GE2J_MJJ_GT350_PTH_GT200','WH_had_GE2J_MJJ_GT350_PTH_GT200','ZH_had_GE2J_MJJ_GT350_PTH_GT200'],
    "WH_lep_low":['WH_lep_PTV_0_75'],
    "WH_lep_high":['WH_lep_PTV_75_150','WH_lep_PTV_150_250_0J','WH_lep_PTV_150_250_GE1J','WH_lep_PTV_GT250'],
    "ZH_lep":['ZH_lep_PTV_0_75','ZH_lep_PTV_75_150','ZH_lep_PTV_150_250_0J','ZH_lep_PTV_150_250_GE1J','ZH_lep_PTV_GT250'],
    "ggZH_lep":['ggZH_ll_PTV_0_75','ggZH_ll_PTV_75_150','ggZH_ll_PTV_150_250_0J','ggZH_ll_PTV_150_250_GE1J','ggZH_ll_PTV_GT250','ggZH_nunu_PTV_0_75','ggZH_nunu_PTV_75_150','ggZH_nunu_PTV_150_250_0J','ggZH_nunu_PTV_150_250_GE1J','ggZH_nunu_PTV_GT250'],
    "ttH_low":['ttH_PTH_0_60'],
    "ttH_medlow":['ttH_PTH_60_120'],
    "ttH_medhigh":['ttH_PTH_120_200'],
    "ttH_high":['ttH_PTH_200_300','ttH_PTH_GT300']
  },

  "stage1p2_intermediate":{
    "ggH_BSM_low":['ggH_PTH_200_300'],
    "ggH_BSM_high":['ggH_PTH_300_450','ggH_PTH_450_650','ggH_PTH_GT650'],
    "ggH_VBF_like":['ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    "qqH_VH_like":['qqH_GE2J_MJJ_60_120','WH_had_GE2J_MJJ_60_120','ZH_had_GE2J_MJJ_60_120'],
    "qqH_MJJ_350_700":['qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'],
    "qqH_MJJ_GT700":['qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'], 
    "qqH_BSM":['qqH_GE2J_MJJ_GT350_PTH_GT200','WH_had_GE2J_MJJ_GT350_PTH_GT200','ZH_had_GE2J_MJJ_GT350_PTH_GT200'],
    "qqH_other":['qqH_0J','qqH_1J','qqH_GE2J_MJJ_0_60','qqH_GE2J_MJJ_120_350','WH_had_0J','WH_had_1J','WH_had_GE2J_MJJ_0_60','WH_had_GE2J_MJJ_120_350','ZH_had_0J','ZH_had_1J','ZH_had_GE2J_MJJ_0_60','ZH_had_GE2J_MJJ_120_350'],
    "WH_lep_low":['WH_lep_PTV_0_75'],
    "WH_lep_high":['WH_lep_PTV_75_150','WH_lep_PTV_150_250_0J','WH_lep_PTV_150_250_GE1J','WH_lep_PTV_GT250'],
    "ZH_lep":['ZH_lep_PTV_0_75','ZH_lep_PTV_75_150','ZH_lep_PTV_150_250_0J','ZH_lep_PTV_150_250_GE1J','ZH_lep_PTV_GT250'],
    "ttH_low":['ttH_PTH_0_60','ttH_PTH_60_120'],
    "ttH_high":['ttH_PTH_120_200','ttH_PTH_200_300','ttH_PTH_GT300']
  },

  "stage1p2_maximal":{
    "ggH_BSM":['ggH_PTH_200_300','ggH_PTH_300_450','ggH_PTH_450_650','ggH_PTH_GT650'],
    "ggH_VBF_like":['ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    "qqH_VH_like":['qqH_GE2J_MJJ_60_120','WH_had_GE2J_MJJ_60_120','ZH_had_GE2J_MJJ_60_120'],
    "qqH_MJJ_350_700":['qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'],
    "qqH_MJJ_GT700":['qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25','ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'], 
    "qqH_BSM":['qqH_GE2J_MJJ_GT350_PTH_GT200','WH_had_GE2J_MJJ_GT350_PTH_GT200','ZH_had_GE2J_MJJ_GT350_PTH_GT200'],
    "qqH_other":['qqH_0J','qqH_1J','qqH_GE2J_MJJ_0_60','qqH_GE2J_MJJ_120_350','WH_had_0J','WH_had_1J','WH_had_GE2J_MJJ_0_60','WH_had_GE2J_MJJ_120_350','ZH_had_0J','ZH_had_1J','ZH_had_GE2J_MJJ_0_60','ZH_had_GE2J_MJJ_120_350'],
    "WH_lep":['WH_lep_PTV_0_75','WH_lep_PTV_75_150','WH_lep_PTV_150_250_0J','WH_lep_PTV_150_250_GE1J','WH_lep_PTV_GT250'],
    "ZH_lep":['ZH_lep_PTV_0_75','ZH_lep_PTV_75_150','ZH_lep_PTV_150_250_0J','ZH_lep_PTV_150_250_GE1J','ZH_lep_PTV_GT250'],
    "ttH":['ttH_PTH_0_60','ttH_PTH_60_120','ttH_PTH_120_200','ttH_PTH_200_300','ttH_PTH_GT300']
  }
}

cats = ['RECO_0J_PTH_0_10_Tag0', 'RECO_0J_PTH_0_10_Tag1', 'RECO_0J_PTH_0_10_Tag2', 'RECO_0J_PTH_GT10_Tag0', 'RECO_0J_PTH_GT10_Tag1', 'RECO_0J_PTH_GT10_Tag2', 'RECO_1J_PTH_0_60_Tag0', 'RECO_1J_PTH_0_60_Tag1', 'RECO_1J_PTH_0_60_Tag2', 'RECO_1J_PTH_60_120_Tag0', 'RECO_1J_PTH_60_120_Tag1', 'RECO_1J_PTH_60_120_Tag2', 'RECO_1J_PTH_120_200_Tag0', 'RECO_1J_PTH_120_200_Tag1', 'RECO_1J_PTH_120_200_Tag2', 'RECO_GE2J_PTH_0_60_Tag0', 'RECO_GE2J_PTH_0_60_Tag1', 'RECO_GE2J_PTH_0_60_Tag2', 'RECO_GE2J_PTH_60_120_Tag0', 'RECO_GE2J_PTH_60_120_Tag1', 'RECO_GE2J_PTH_60_120_Tag2', 'RECO_GE2J_PTH_120_200_Tag0', 'RECO_GE2J_PTH_120_200_Tag1', 'RECO_GE2J_PTH_120_200_Tag2', 'RECO_PTH_200_300_Tag0', 'RECO_PTH_200_300_Tag1', 'RECO_PTH_300_450_Tag0', 'RECO_PTH_300_450_Tag1', 'RECO_PTH_450_650_Tag0', 'RECO_PTH_GT650_Tag0','RECO_VBFLIKEGGH_Tag0', 'RECO_VBFLIKEGGH_Tag1', 'RECO_VBFTOPO_VHHAD_Tag0', 'RECO_VBFTOPO_VHHAD_Tag1', 'RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0', 'RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1', 'RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0', 'RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1', 'RECO_VBFTOPO_JET3_LOWMJJ_Tag0', 'RECO_VBFTOPO_JET3_LOWMJJ_Tag1', 'RECO_VBFTOPO_JET3_HIGHMJJ_Tag0', 'RECO_VBFTOPO_JET3_HIGHMJJ_Tag1', 'RECO_VBFTOPO_BSM_Tag0', 'RECO_VBFTOPO_BSM_Tag1', 'RECO_VBFTOPO_VHHAD_Tag0', 'RECO_VBFTOPO_VHHAD_Tag1','RECO_VH_MET_Tag0', 'RECO_VH_MET_Tag1', 'RECO_VH_MET_Tag2', 'RECO_WH_LEP_PTV_0_75_Tag0', 'RECO_WH_LEP_PTV_0_75_Tag1', 'RECO_WH_LEP_PTV_75_150_Tag0', 'RECO_WH_LEP_PTV_75_150_Tag1', 'RECO_WH_LEP_PTV_GT150_Tag0', 'RECO_ZH_LEP_Tag0', 'RECO_ZH_LEP_Tag1','RECO_TTH_HAD_PTH_0_60_Tag0', 'RECO_TTH_HAD_PTH_0_60_Tag1', 'RECO_TTH_HAD_PTH_0_60_Tag2', 'RECO_TTH_HAD_PTH_60_120_Tag0', 'RECO_TTH_HAD_PTH_60_120_Tag1', 'RECO_TTH_HAD_PTH_60_120_Tag2', 'RECO_TTH_HAD_PTH_120_200_Tag0', 'RECO_TTH_HAD_PTH_120_200_Tag1', 'RECO_TTH_HAD_PTH_120_200_Tag2', 'RECO_TTH_HAD_PTH_120_200_Tag3', 'RECO_TTH_HAD_PTH_200_300_Tag0', 'RECO_TTH_HAD_PTH_200_300_Tag1', 'RECO_TTH_HAD_PTH_200_300_Tag2', 'RECO_TTH_HAD_PTH_GT300_Tag0', 'RECO_TTH_HAD_PTH_GT300_Tag1', 'RECO_TTH_LEP_PTH_0_60_Tag0', 'RECO_TTH_LEP_PTH_0_60_Tag1', 'RECO_TTH_LEP_PTH_0_60_Tag2', 'RECO_TTH_LEP_PTH_60_120_Tag0', 'RECO_TTH_LEP_PTH_60_120_Tag1', 'RECO_TTH_LEP_PTH_60_120_Tag2', 'RECO_TTH_LEP_PTH_120_200_Tag0', 'RECO_TTH_LEP_PTH_120_200_Tag1', 'RECO_TTH_LEP_PTH_200_300_Tag0', 'RECO_TTH_LEP_PTH_GT300_Tag0', 'RECO_THQ_LEP']


def get_options():
  parser = OptionParser()
  parser.add_option('--paramMergingScheme', dest='paramMergingScheme', default='none', help="Parameter merging scenario e.g. maximal_mjj")
  parser.add_option('--mode', dest='mode', default='purity', help="Composition matrix. Purity = norm by RECO category, migration = norm by process")
  parser.add_option("--inputPkl", dest="inputPkl", default='', help="Input pickle file")
  parser.add_option("--threshold", dest="threshold", default=1.0, type='float', help="Threshold (in %%)")
  parser.add_option("--year", dest="year", default='2016', help="Used only for migration (norm by proc)")
  parser.add_option("--ext", dest="ext", default='', help="Extension for saving")
  parser.add_option("--translateCats", dest="translateCats", default=None, help="JSON to store cat translations")
  parser.add_option("--translateProcs", dest="translateProcs", default=None, help="JSON to store proc translations")
  parser.add_option("--yieldVar", dest="yieldVar", default='nominal_yield', help="Name of yield column in dataframe")
  return parser.parse_args()
(opt,args) = get_options()

def Translate(name, ndict):
    return ndict[name] if name in ndict else name

def LoadTranslations(jsonfilename):
    with open(jsonfilename) as jsonfile:
        return json.load(jsonfile)

translateCats = {} if opt.translateCats is None else LoadTranslations(opt.translateCats)
translateProcs = {} if opt.translateProcs is None else LoadTranslations(opt.translateProcs)

# If norm by proc: add NoTag
#if opt.mode == 'migration': cats.insert(0,"NOTAG_%s"%opt.year)
if opt.mode == 'migration': cats.insert(0,"NOTAG")

# Load input dataFrame from pickle file
if not os.path.exists( opt.inputPkl ): 
  print(" --> [ERROR] Input pickle file does not exist. Leaving")
  leave()
with open( opt.inputPkl, "rb" ) as fin: idata = pickle.load(fin)

# Initiate pandas dataframe
_columns = ['proc','param','cat',opt.yieldVar]
data = pd.DataFrame(columns=_columns)

# Fill frame
for pm in productionModes:
  for stxsBin in stxsBins[pm]:
    _proc = stxsBin
    paramFound = False
    if opt.paramMergingScheme in paramMergingSchemes:
      for p, mergeBins in paramMergingSchemes[opt.paramMergingScheme].items():
        if paramFound: continue
        if _proc in mergeBins: 
          _param = p
          paramFound = True
    if not paramFound: _param = stxsBin
    
    for cat in cats:
      _cat = cat
      # Extract yield from input pickle file
      if opt.mode == 'purity': mask = (idata['cat']==cat)&(idata['proc'].str.contains(_proc))
      elif opt.mode == 'migration': mask = (idata['cat']==cat)&(idata['proc'].str.contains(_proc))&(idata['year']==opt.year)
      _yield = idata[mask][opt.yieldVar].sum()
      data.loc[len(data)] = [_proc,_param,_cat,_yield]

# Add column to dataFrame: normalised yield (depending on mode)
data['norm_yield'] = 0
if opt.mode == 'purity':
  catYields = {}
  for cat in cats: 
    mask = data['cat']==cat
    catYields[cat] = data[mask][opt.yieldVar].sum()
    data.loc[mask,'norm_yield'] = data[mask].apply(lambda x: x[opt.yieldVar]/catYields[cat], axis=1)
elif opt.mode == 'migration':
  paramYields = {}
  for param in data['param'].unique():
    mask = data['param']==param
    paramYields[param] = data[mask][opt.yieldVar].sum()
    data.loc[mask,'norm_yield'] = data[mask].apply(lambda x: x[opt.yieldVar]/paramYields[param], axis=1)

# Make 2D histogram to store yields
params = list(data['param'].unique())
nParams = len(params)
nCats = len(cats)
h_matrix = ROOT.TH2F("h_matrix","", nParams, 0, nParams, nCats, 0, nCats)
h_notag = ROOT.TH2F("h_notag","", nParams, 0, nParams, nCats, 0, nCats)
if opt.mode == 'purity': h_matrix.SetMaximum(100)
#elif opt.mode == 'migration': h_matrix.SetMaximum(25)
elif opt.mode == 'migration': h_matrix.SetMaximum(50)
h_matrix.SetMinimum(0)
# Set bin labels
for xbin_idx in range(1,h_matrix.GetNbinsX()+1): h_matrix.GetXaxis().SetBinLabel( xbin_idx, Translate(params[xbin_idx-1],translateProcs) ) 
for ybin_idx in range(1,h_matrix.GetNbinsY()+1): 
  c = cats[ybin_idx-1]
  if "Tag" in c: 
    c, t = c.split("_Tag")[0], c[-1]
    cstr = "%s Tag %s"%(Translate(c,translateCats),t)
  else:
    cstr = "%s"%Translate(c,translateCats)
  h_matrix.GetYaxis().SetBinLabel( ybin_idx, cstr ) 

# Fill bins of histogram with normalised values
for pidx in range(nParams):
  for cidx in range(nCats):
    p, c = params[pidx], cats[cidx]
    mask = (data['param']==p)&(data['cat']==c)
    norm_y = data[mask].norm_yield.sum()*100
    if norm_y > opt.threshold: 
      if "NOTAG" in c: h_notag.SetBinContent( pidx+1, cidx+1, norm_y )
      else: h_matrix.SetBinContent( pidx+1, cidx+1, norm_y )
   
# Plotting
if opt.mode == 'purity': set_color_palette('ed_noice')
#if opt.mode == 'purity': set_color_palette('ed_noice_ggh')
#if opt.mode == 'purity': set_color_palette('ed_noice_qqh')
elif opt.mode == 'migration': set_color_palette('ed_noice_mig')
canv = ROOT.TCanvas("c","c",1400,1800)
#canv = ROOT.TCanvas("c","c",1200,800)
canv.SetLeftMargin(0.18)
canv.SetRightMargin(0.15)
canv.SetBottomMargin(0.2)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetNumberContours(500)
ROOT.gStyle.SetTextFont(42)
ROOT.gStyle.SetPaintTextFormat('.0f')
if opt.threshold < 0.049: ROOT.gStyle.SetPaintTextFormat('.2f')
elif opt.threshold < 0.99: ROOT.gStyle.SetPaintTextFormat('.1f')
else: ROOT.gStyle.SetPaintTextFormat('.0f')


# Formatting
h_matrix.GetXaxis().LabelsOption("v")
#h_matrix.GetXaxis().SetLabelSize(0.02)
h_matrix.GetXaxis().SetLabelSize(0.024)
h_matrix.GetXaxis().SetLabelOffset(0.0025)
h_matrix.GetXaxis().SetTitle("STXS stage 1.2 bins (reduced)")
h_matrix.GetXaxis().SetTitleOffset(3.2)
h_matrix.GetXaxis().SetTickLength(0.)
h_matrix.GetYaxis().SetLabelOffset(0.0025)
h_matrix.GetYaxis().SetLabelSize(0.015)
#h_matrix.GetYaxis().SetLabelSize(0.025)
h_matrix.GetYaxis().SetTitle("Event category")
h_matrix.GetYaxis().SetTitleOffset(2.8)
#h_matrix.GetYaxis().SetTitleOffset(3.2)
h_matrix.GetYaxis().SetTickLength(0.)
if opt.mode == 'purity': h_matrix.GetZaxis().SetTitle("Category signal composition (%)")
#elif opt.mode == 'migration': h_matrix.GetZaxis().SetTitle("Process distribution (%)")
elif opt.mode == 'migration': h_matrix.GetZaxis().SetTitle("#varepsilon^{i,#gamma#gamma}_{k} (%)")
h_matrix.GetZaxis().SetTitleSize(0.03)
h_matrix.GetZaxis().SetTitleOffset(1.25)
h_matrix.GetZaxis().SetLabelSize(0.025)
#h_matrix.SetMarkerSize(0.375)
h_matrix.SetMarkerSize(0.45)
#h_matrix.SetMarkerSize(0.55)
h_matrix.Draw("COLZ TEXT")
if opt.mode == 'migration':
  h_notag.SetMarkerSize(0.45)
  h_notag.SetMarkerColor(2)
  h_notag.Draw("TEXT SAME")

# Lines
lines = {}
for pidx in range(1,nParams): 
  lines["l_proc_%g"%pidx] = ROOT.TLine(pidx,0,pidx,nCats)
  lines["l_proc_%g"%pidx].SetLineColorAlpha(ROOT.kGray,0.5)
  lines["l_proc_%g"%pidx].SetLineWidth(1)
#pm_lines = []#'qqH_other','WH_lep','ZH_lep','ttH']#,'tHq']
#pm_lines = ['qqH_other','WH_lep','ZH_lep','ttH']#,'tHq']
#pm_lines = ['qqH_other','WH_lep','ZH_lep','ttH','tHq']
pm_lines = ['qqH_other','WH_lep_low','ZH_lep','ttH_PTH_0_60','tHq']#,'bbH']
#pm_lines = ['qqH_other','WH_lep_low','ZH_lep','ttH_low','tHq']
for pm in pm_lines:
  pidx = params.index(pm)
  lines["l_pm_%g"%pidx] = ROOT.TLine(pidx,0,pidx,nCats)
  lines["l_pm_%g"%pidx].SetLineColorAlpha(ROOT.kBlack,0.5)
  lines["l_pm_%g"%pidx].SetLineWidth(2)
tag_lines = []
for cat in cats:
  if "Tag0" in cat: tag_lines.append(cat)
for tag in tag_lines:
  tidx = cats.index(tag)
  lines["l_tag_%g"%tidx] = ROOT.TLine(0,tidx,nParams,tidx)
  lines["l_tag_%g"%tidx].SetLineColorAlpha(ROOT.kGray,0.5)
  lines["l_tag_%g"%tidx].SetLineWidth(1)
#cat_lines = ['RECO_0J_PTH_0_10_Tag0','RECO_VBFTOPO_VHHAD_Tag0','RECO_WH_LEP_LOW_Tag0','RECO_VH_MET_Tag0','RECO_ZH_LEP_Tag0','RECO_TTH_HAD_PTH_0_60_Tag0','RECO_TTH_LEP_PTH_0_60_Tag0','RECO_THQ_LEP']
cat_lines = ['RECO_0J_PTH_0_10_Tag0','RECO_VBFTOPO_VHHAD_Tag0','RECO_WH_LEP_PTV_0_75_Tag0','RECO_VH_MET_Tag0','RECO_ZH_LEP_Tag0','RECO_TTH_HAD_PTH_0_60_Tag0','RECO_TTH_LEP_PTH_0_60_Tag0','RECO_THQ_LEP']
#cat_lines = ['RECO_ZH_LEP_Tag0','RECO_TTH_HAD_LOW_Tag0','RECO_THQ_LEP']
#cat_lines = []
for cat in cat_lines:
  cidx = cats.index(cat)
  lines["l_cat_%g"%cidx] = ROOT.TLine(0,cidx,nParams,cidx)
  lines["l_cat_%g"%cidx].SetLineColorAlpha(ROOT.kBlack,0.5)
  lines["l_cat_%g"%cidx].SetLineWidth(2)
# Border lines
lines['l_bd_bottom'] = ROOT.TLine(0,0,nParams,0)
lines['l_bd_bottom'].SetLineColorAlpha(ROOT.kBlack,0.5)
lines['l_bd_bottom'].SetLineWidth(2)
lines['l_bd_left'] = ROOT.TLine(0,0,0,nCats)
lines['l_bd_left'].SetLineColorAlpha(ROOT.kBlack,0.5)
lines['l_bd_left'].SetLineWidth(2)
lines['l_bd_top'] = ROOT.TLine(0,nCats,nParams,nCats)
lines['l_bd_top'].SetLineColorAlpha(ROOT.kBlack,0.5)
lines['l_bd_top'].SetLineWidth(2)
lines['l_bd_right'] = ROOT.TLine(nParams,0,nParams,nCats)
lines['l_bd_right'].SetLineColorAlpha(ROOT.kBlack,0.5)
lines['l_bd_right'].SetLineWidth(2)

for l in lines.values(): l.Draw()

# Writing text
drawCMS(True)
#if opt.mode == 'purity': drawEnPu(lumi="137 fb^{-1}")
if opt.mode == 'purity': drawEnPu(lumi="")
if opt.mode == 'migration': drawEnYear(year=opt.year)

extStr = "_%s"%opt.ext if opt.ext != '' else ''
if opt.mode == 'purity': 
  canv.SaveAs("/eos/home-j/jlangfor/www/CMS/thesis/appendix/purityMatrix%s.pdf"%extStr)
  canv.SaveAs("/eos/home-j/jlangfor/www/CMS/thesis/appendix/purityMatrix%s.png"%extStr)
elif opt.mode == 'migration': 
  canv.SaveAs("/eos/home-j/jlangfor/www/CMS/thesis/appendix/migrationMatrix_%s%s.png"%(opt.year,extStr))
  canv.SaveAs("/eos/home-j/jlangfor/www/CMS/thesis/appendix/migrationMatrix_%s%s.pdf"%(opt.year,extStr))



