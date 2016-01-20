from ROOT import *
from array import array

#Define the input file with 'data'
data = TFile('uhh2.AnalysisModuleRunner.MC.ZP3000w30.root')
dataTree = data.Get('AnalysisTree')
print dataTree
#Define the file that will contain the BDT response of each event
target = TFile('uhh2.AnalysisModuleRunner.MC.ZP3000w30.root','UPDATE')
targetTree = target.Get('AnalysisTree')
#Declare the reader parameters
reader = TMVA.Reader()
var01 = array('f',[0])
var02 = array('f',[0])
var03 = array('f',[0])
var04 = array('f',[0])
reader.AddVariable('jet1',var01)
reader.AddVariable('jet2',var02)
reader.AddVariable('dRMin',var03)
reader.AddVariable('njets',var04)
reader.BookMVA("BDT","weights/TMVAClassification_BDT.weights.xml")
#Declare the variables for the data tree 
var1 = array('f',[0])
var2 = array('f',[0])
var3 = array('f',[0])
var4 = array('f',[0])
dataTree.SetBranchAddress('jet1',var1)
dataTree.SetBranchAddress('jet2',var2)
dataTree.SetBranchAddress('dRMin',var3)
dataTree.SetBranchAddress('njets',var4)
#vec = vector('double')()
#targetTree.Branch('BDTResponse', vec)
#targetTree.Branch("pt_jet1",var1)
#targetTree.Branch("pt_jet2",var2)
#targetTree.Branch("dRMin",var3)
#Book histograms for analysis of the output
#histList = []
#histList.append( TH1F( ) )
#mvaValue = TH1F()
#Now loop over data trees
for ievt in range(dataTree.GetEntries()):
    print ievt
    dataTree.GetEntry(ievt)
    #print "Passed here"
    #mvaValue = reader.EvaluateMVA('BDT')
    #mvaErr = reader.GetMVAError()
    #passed = reader.Evaluate('', signalEfficiency)
    #BDTResponse = reader.EvaluateMVA('BDT')
    var01 = var1
    var02 = var2
    var03 = var3
    var04 = var4
    print var1,var2,var3
    BDTResponse = reader.EvaluateMVA('BDT')
    #print BDTResponse 
    #mvaValue.Fill(BDTResponse);
    targetTree.Fill(BDTResponse)
targetTree.Write()
