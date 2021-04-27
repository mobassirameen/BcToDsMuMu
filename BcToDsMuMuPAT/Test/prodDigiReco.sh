#! /bin/bash

export RECREL=CMSSW_10_6_12
export SCRAM_ARCH=slc7_amd64_gcc700


#export FILE1=file:root://se01.indiacms.res.in:1094//cms/store/user/moameen/BcToDsMuMu_MC_MINIAOD/$1
export FILE1=file:root://eosuser.cern.ch//eos/user/m/moameen/BcToDsMuMu_MC_MINIAOD/$1
#export FILE1=file:root://afs/cern.ch/work/p/psadangi/crabjobs_2_30k/$1
#export FILE2=file:BctoDsMuMu_MC_SIM_$2.root
#export FILE2=file:BctoDsMuMu_MC_DIGI_$2.root
export FILE2=file:BcToDsMuMu_MC_Ntuple_$2.root
#"BsToMuMuPhi-2018_nofilter_$1.root"


echo "========================"
echo "====> SGE  wrapper <===="
echo "========================"

echo "--> Running SGE digi-reco job wrapper"

echo $FILE1
echo $FILE2
#echo $FILE3
#echo $FILE4


# ----------------------------------------------------------------------
# -- The Basics
# ----------------------------------------------------------------------
echo "--> Environment"
date
hostname
uname -a
df -kl
#limit coredumpsize 0

source /cvmfs/cms.cern.ch/cmsset_default.sh
echo "-> which edg-gridftp-ls"
which edg-gridftp-ls
echo "-> which globus-url-copy"
which globus-url-copy
echo "-> which srmcp"
which srmcp

pwd
echo "--> End of env testing"

# BATCH START

# ----------------------------------------------------------------------
# -- Setup CMSSW
# ----------------------------------------------------------------------
echo "--> Setup CMSSW"
pwd
date
pwd
date
eval `scramv1 project CMSSW CMSSW_10_6_12`

cd CMSSW_10_6_12/src/
tar -zxvf ../../cmssw_10_6_12.tar.gz

ls -ltr
eval `scramv1 runtime -sh`
pwd

scramv1 b ProjectRename
scramv1 b


cd bctodsmumu_analysis/BcToDsMuMuPAT/Test/
#mv ../../BctoDsMuMu_MC_SIM_cfg.py  step1.py
#mv ../../BctoDsMuMu_MC_DIGI_cfg.py  step1.py
cp ../../../../../BctoDsMuMu_MC_step3_cfg.py
#mv ../../BctoDsMuMu_MC_step3_cfg.py  step3.py


cmsRun  BctoDsMuMu_MC_step3_cfg |& tee step1.log

ls -rtl
ls -ltr
#echo "cmsRun step2.py "
#cmsRun step2.py |& tee step2.log
#date
#pwd
#ls -rtl
#ls -ltr

#echo "cmsRun step3.py "
#cmsRun step3.py |& tee step3.log
#date
#pwd
#ls -rtl
#ls -ltr

# ----------------------------------------------------------------------
# -- Save Output to SE
# ----------------------------------------------------------------------

#xrdcp BPH-RunIIAutumn18DRPremix-XX-JpsiKs30k_step3_$2.root root://se01.indiacms.res.in:1094//cms/store/user/psadangi/BsToJpsiKs/BPH-RunIIAutumn18DRPremix-XX-JpsiKs30k_step3_$2.root
#xrdcp BcToDsMuMu_MC_$2.root root://se01.indiacms.res.in:1094//cms/store/user/moameen/BctoDsMuMu_MC_Ntuples_test/BcToDsMuMu_MC_$2.root	
xrdcp BcToDsMuMu_MC_$2.root root://eosuser.cern.ch//eos/user/m/moameen/BcToDsMuMu_MC_Ntuples_test/BcToDsMuMu_MC_$2.root
# BATCH END

echo "run: This is the end, my friend"
