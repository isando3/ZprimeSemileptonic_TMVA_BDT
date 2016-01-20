from ROOT import * 
#Create output file of the training 
fout = TFile("WJetsHT_TTBar_Zprime_BDTFirstStep.root", "RECREATE")
#Declare the factory
factory = TMVA.Factory('TMVAClassification', fout, ":".join([
                                "!V",
                                "!Silent",
                                "Color",
                                "DrawProgressBar",
                                "Transformations=I;D;P;G,D",
                                "AnalysisType=Classification"]
                                     ))
#Get the ntuples for signal and background
fsig1 = TFile('uhh2.AnalysisModuleRunner.MC.ZP3000w30.root')
fsig2 = TFile('uhh2.AnalysisModuleRunner.MC.ZP2000w20.root')
fbkg1 = TFile('uhh2.AnalysisModuleRunner.MC.WJets_HT100to200.root')
fbkg2 = TFile('uhh2.AnalysisModuleRunner.MC.WJets_HT200to400.root')
fbkg3 = TFile('uhh2.AnalysisModuleRunner.MC.WJets_HT400to600.root')
fbkg4 = TFile('uhh2.AnalysisModuleRunner.MC.WJets_HT600toInf.root')
fbkg5 = TFile('uhh2.AnalysisModuleRunner.MC.TTbar.root')
sig1Tree = fsig1.Get('AnalysisTree')
sig2Tree = fsig2.Get('AnalysisTree')
bkg1Tree = fbkg1.Get('AnalysisTree')
bkg2Tree = fbkg2.Get('AnalysisTree')
bkg3Tree = fbkg3.Get('AnalysisTree')
bkg4Tree = fbkg4.Get('AnalysisTree')
bkg5Tree = fbkg5.Get('AnalysisTree') 
#Add ntuples to the factory, signalweight=1.0 and backgroundweight=1.0
factory.AddSignalTree(sig1Tree,1.0)
factory.AddSignalTree(sig2Tree,1.0)
factory.AddBackgroundTree(bkg1Tree,1.0)
factory.AddBackgroundTree(bkg2Tree,1.0)
factory.AddBackgroundTree(bkg3Tree,1.0)
factory.AddBackgroundTree(bkg4Tree,1.0)
factory.AddBackgroundTree(bkg5Tree,1.0)
#Add cuts to the variables 
sigCut1 = TCut('jet1>300')
bkgCut1 = TCut('jet1>300')
sigCut2 = TCut('jet2>100')
bkgCut2 = TCut('jet2>100')
sigCut = sigCut1 and sigCut2
bkgCut = bkgCut1 and bkgCut2
##Add variables ('NAME', 'TYPE') type could be F for float or I integer 
factory.AddVariable('jet1','F')
factory.AddVariable('jet2','F')
factory.AddVariable('dRMin','F')
factory.AddVariable('njets','I')
##Prepare training and test 
factory.PrepareTrainingAndTestTree(sigCut,   # signal events
                                   bkgCut,    # background events
                                   ":".join([
                                        "nTrain_Signal=0", "nTest_Signal=0",
                                        "nTrain_Background=0", "nTest_Background=0",
                                        "SplitMode=Random",
                                        "NormMode=NumEvents",
                                        "!V"
                                       ]))
##Declare method to be applied, in this case Boosted (ada) Decision Tree
method = factory.BookMethod(TMVA.Types.kBDT, "BDT",
                   ":".join([
                       "!H",
                       "!V",
                       "NTrees=30", "MinNodeSize=10", "MaxDepth=3",
                       "BoostType=AdaBoost",
                       "AdaBoostBeta=0.5",
                       "SeparationType=GiniIndex",
                       "nCuts=20",
                       "PruneMethod=NoPruning",
                       ]))
#Do training, testing and evaluation
print "Methond Booked"
factory.TrainAllMethods()
print "Method Trained"
factory.TestAllMethods()
print "Method Tested"
factory.EvaluateAllMethods()
print "Method Evaluated "






