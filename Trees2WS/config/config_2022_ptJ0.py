# Input config file for running trees2ws

trees2wsCfg = {
  # Name of RooDirectory storing input tree
  'inputTreeDir':'DiphotonTree',

  # Variables to be added to dataframe: use wildcard * for common strings
  'mainVars':["CMS_hgg_mass","weight","weight_central","dZ","*Up","*Down","fiducialGeometricFlag", "diffVariable_GenPTJ0"],
  'dataVars':["CMS_hgg_mass","weight"], # Vars to be added for data
  'stxsVar':'',
  'diffVar':'diffVariable_GenPTJ0',
  'notagVars':[], # Vars to add to NOTAG RooDataset
  'systematicsVars':["CMS_hgg_mass","weight","fiducialGeometricFlag", "diffVariable_GenPTJ0"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{'weight_LHEPdf': 101, 'weight_LHEScale': 9},

  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':["ScaleEB", "ScaleEE", "Smearing", "Material", "FNUF", "energyErrShift", "JerSyst", "JecSystTotal"],
  # 'systematics': [],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats':'auto'
}