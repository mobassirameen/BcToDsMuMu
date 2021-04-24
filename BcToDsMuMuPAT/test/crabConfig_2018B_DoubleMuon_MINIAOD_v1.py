from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'job_crab_data_Doublemu_finaljob_MINIAOD_CMSSW10218_18B_v2'
config.General.workArea = 'crab_data_Doublemu_finaljob_MINIAOD_CMSSW10218_18B_v2'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BcToDsMuMuRootupler.py'
config.JobType.outputFiles = ['Rootuple_BctoDsMuMu_2018_MiniAOD.root']

config.Data.inputDataset = '/DoubleMuonLowMass/Run2018B-17Sep2018-v1/MINIAOD'
#config.Data.inputDataset = '/Charmonium/Run2018D-PromptReco-v2/MINIAOD'

config.Data.inputDBS = 'global'
#config.Data.splitting = 'FileBased'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 5

config.JobType.allowUndistributedCMSSW = True
# config.Data.ignoreLocality = True
# config.Site.whitelist = ['T2_CH_*', 'T2_UK_*', 'T2_IT_*', 'T2_US_*']

#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON_MuonPhys.txt'
config.Data.lumiMask = 'Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON_MuonPhys.txt'

#config.Data.runRange = '315252-316995' #Era A
config.Data.runRange = '317080-319310' #Era B
#config.Data.runRange = '319337-320065' #era C
#config.Data.runRange = '320673-325175' #EraD
                  

config.Data.outLFNDirBase = '/store/user/ckar/'
config.Data.publication = False


config.Site.storageSite = 'T3_CH_CERNBOX'

