import FWCore.ParameterSet.Config as cms
import os
import FWCore.Utilities.FileUtils as FileUtils
#mylist = FileUtils.loadListFromFile ('MiniAOD_2.txt')
#infiles = cms.untracked.vstring(*mylist)

process = cms.Process("Rootuple")

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
# from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')
process.GlobalTag.globaltag = cms.string('106X_upgrade2018_realistic_v4')

FILE1=os.environ.get('FILE1')
FILE2=os.environ.get('FILE2')

#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                #'/store/data/Run2016C/Charmonium/MINIAOD/17Jul2018-v1/20000/9C03CBE2-4B8B-E811-9299-0CC47AC17678.root',
                                #'file:6EF2991A-8E4C-C94A-BE5E-3E5D0A17DE08.root',
                                #'/store/data/Run2018B/DoubleMuonLowMass/MINIAOD/17Sep2018-v1/60000/6EF2991A-8E4C-C94A-BE5E-3E5D0A17DE08.root',
#                                '/store/data/Run2018B/DoubleMuonLowMass/MINIAOD/17Sep2018-v1/100000/32AB25E3-8BF6-ED4F-A72B-FF5E7036C416.root',
#				'file:root://se01.indiacms.res.in:1094//cms/store/user/digupta/BctoDsMuMu_MC_MINIAOD/BctoDsMuMu_MC_MINIAOD_205.root',
#				mylist,
				FILE1,
                                #'/store/data/Run2016H/DoubleMuonLowMass/MINIAOD/17Jul2018-v1/50000/9A79D8BA-D38B-E811-BCD3-0090FAA57AE0.root',                
    )
)

process.load("slimmedMuonsTriggerMatcher_cfi")

process.load("bctodsmumu_analysis.BcToDsMuMuPAT.BcToDsMuMuRootupler_cfi")
process.rootuple.isMC = cms.bool(True)

process.TFileService = cms.Service("TFileService",

       fileName = cms.string(FILE2),
#       fileName = cms.string('BctoDsMuMu_ntuple_v1.root'),
#       fileName = cms.string('BctoDsMuMu_ntuple_test4_For_1_MiniAOD.root'),
#       fileName = cms.string('BctoDsMuMu_ntuple_v2.root'),
#       fileName = cms.string('BctoDsMuMu_ntuple_v3.root')
#       fileName = cms.string('BctoDsMuMu_ntuple_mc_v1.root'),
)

process.p = cms.Path(process.slimmedMuonsWithTriggerSequence *process.rootuple)

