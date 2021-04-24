import FWCore.ParameterSet.Config as cms


import os 

FILE1 = os.environ.get('FILE1')
FILE2 = os.environ.get('FILE2')


process = cms.Process("Rootuple")

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
# from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')
process.GlobalTag.globaltag = cms.string('102X_dataRun2_v12')

#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(600))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(FILE1
        #'/store/data/Run2016C/Charmonium/MINIAOD/17Jul2018-v1/20000/9C03CBE2-4B8B-E811-9299-0CC47AC17678.root',
        #'/store/data/Run2016H/DoubleMuonLowMass/MINIAOD/17Jul2018-v1/50000/9A79D8BA-D38B-E811-BCD3-0090FAA57AE0.root',                
    )
)

process.load("slimmedMuonsTriggerMatcher_cfi")

process.load("bctodsmumu_analysis.BcToDsMuMuPAT.BcToDsMuMuRootupler_cfi")
process.rootuple.isMC = cms.bool(False)

process.TFileService = cms.Service("TFileService",

                                   fileName = cms.string(FILE2),)
                                   #fileName = cms.string('Rootuple_BctoDsMuMu_2018_MiniAOD.root'),)


process.p = cms.Path(process.slimmedMuonsWithTriggerSequence *process.rootuple)

