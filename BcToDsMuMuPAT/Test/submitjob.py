
import os
from os import system, environ



submitFileTT="""
universe              = vanilla
Executable            = prodDigiReco.sh
Requirements = OpSys=="LINUX"&&(Arch!="DUMMY")
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files  = cmssw_10_6_12.tar.gz,BcToDsMuMuRootupler.py

x509userproxy         = x509up_u137722
+JobFlavour = "tomorrow"
RequestMemory         = 8000
RequestDisk           = 15000

"""
fileParts = [submitFileTT]

system('mkdir -p Bsmini1')
files = open("finalmini_1stBs_test.log","r")
count = 0
for ij in files:
    count += 1
    fileParts.append("error = Bsmini1/jobDs_{0}_$(Cluster)_$(Process).stderr\n".format(count))
    fileParts.append("Log = Bsmini1/jobDs_{0}_$(Cluster)_$(Process).log\n".format(count))
    fileParts.append("output = Bsmini1/jobDs_{0}_$(Cluster)_$(Process).stdout\n".format(count))
    fileParts.append("Arguments ={0} {1}\n".format(ij.strip(),count))
    fileParts.append("Queue\n\n")

    fout = open("condor_sub_Bs_{0}.txt".format(count),"w")
    fout.write(''.join(fileParts))
    fout.close()
    fileParts.pop(-1)
    fileParts.pop(-1)
    fileParts.pop(-1)
    fileParts.pop(-1)
    fileParts.pop(-1)
    system('condor_submit condor_sub_Bs_%i.txt' % count)

files.close()
