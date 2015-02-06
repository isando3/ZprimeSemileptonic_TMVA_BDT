import sys
import re
from ROOT import *
from array import array
import tdrstyle, CMS_lumi

#tdrstyle.setTDRStyle()

H_ref = 600; 
W_ref = 800; 
W = W_ref
H  = H_ref

f1 = TFile(sys.argv[1])
sample = sys.argv[1].split('.root') #Zprime2
f2 = TFile(sys.argv[2])
sample2 = sys.argv[2].split('.root') #Zprime3


hname = sys.argv[3]
hn = 'h_'+hname
hnum = hn+'num'
hden = hn+'den'
h_num = f1.Get(hnum)
h_den = f1.Get(hden)
h2_num = f2.Get(hnum)
h2_den = f2.Get(hden)

#c1 = TCanvas('c1',"Plot",1)
T = 0.08*H_ref
B = 0.12*H_ref 
L = 0.12*W_ref
R = 0.04*W_ref

c1 = TCanvas("c2","c2",50,50,W,H)
c1.SetFillColor(0)
c1.SetBorderMode(0)
c1.SetFrameFillStyle(0)
c1.SetFrameBorderMode(0)
c1.SetLeftMargin( L/W )
c1.SetRightMargin( R/W )
c1.SetTopMargin( T/H )
c1.SetBottomMargin( B/H )
c1.SetTickx(0)
c1.SetTicky(0)
CMS_lumi.extraText = "Preliminary"
if hname == 'epT':
#if hname == 'leadingjetpT':
    c1.cd()    
    gStyle.SetOptTitle(1)
    gStyle.SetOptStat(0)
    gStyle.SetTitleFontSize(0.1)
    c1.Modified()
    CMS_lumi.CMS_lumi(c1,4,11)
    c1.Update()
    #p = h_num.Rebin(3)
    #q = h_den.Rebin(3)
    x = array("d",[0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,120.,140.,160.,180.,200.,250.,300.,350.,400.,450.,500.])
    #x = array("d",[0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,120.,140.,160.,180.,200.,250.,300.,350.,400.,450.,500.,650.,700.,750.,800.,850.,900.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.])
    p = TH1F()
    q = TH1F()
    p2 = TH1F()
    q2 = TH1F()
    p = h_num.Rebin(21,"p",x)#21,38
    q = h_den.Rebin(21,"q",x)
    #p2 = h_num.Rebin(21,"p2",x)
    #q2 = h_den.Rebin(21,"q2",x)
    eff = TEfficiency(p,q)
    #eff2 = TEfficiency(p2,q2)
    eff.SetMarkerStyle(20)
    #eff2.SetMarkerStyle(20)
    #eff.SetMarkerColor(kBlue)
    #eff2.SetMarkerStyle(kRed)
    eff.SetTitle("ZPrimeToTTJets_M3000GeV_W30GeV; pT_{e} [GeV];Eff [HLTEle45CaloIdVTGsfTrkIdTPFJet200PFJet50v1]")
   ##HOW TO DRAW Efficiency plots from a range 0 to 1 using TGraphAssymErrors, need to use .Paint() and .GetPaintedGraph() to then have access to .SetRangeUser()
    tgraph2 = TGraphAsymmErrors()
    gPad.Update()
    eff.Draw()
    eff.Paint("")
    tgraph2 = eff.GetPaintedGraph()
    tgraph2.GetYaxis().SetRangeUser(0.,1.1)
    tgraph2.SetLineColor(0)
    tgraph2.SetMarkerStyle(20)
#tgraph1.SetMinimum(0)
    tgraph2.Draw("P") 
    c1.Update()
    c1.SetGrid()
    gStyle.SetTitleFontSize(0.1)
    c1.Update()
    c1.Modified()
    CMS_lumi.CMS_lumi(c1,4,11)
    text = TLatex()
    text.SetNDC()
    text.DrawText(0.4,0.95,hname)
    c1.SaveAs('Efficiency_'+hname+'_'+sample[0]+'_'+sample2[0]+'.png')
elif hname == 'mupT':
    c1.cd()    
    gStyle.SetOptTitle(1)
    gStyle.SetOptStat(0)
    gStyle.SetTitleFontSize(0.1)
    c1.Modified()
    CMS_lumi.CMS_lumi(c1,4,11)
    c1.Update()
    #p = h_num.Rebin(3)
    #q = h_den.Rebin(3)
    x = array("d",[0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,120.,140.,160.,180.,200.,250.,300.,350.,400.,450.,500.])
    p = TH1F()
    q = TH1F()
    p = h_num.Rebin(21,"p",x)
    q = h_den.Rebin(21,"q",x)
    eff = TEfficiency(p,q)
    eff.SetMarkerStyle(20)
    eff.SetTitle("ZPrimeToTTJets_M3000GeV_W30GeV; pT_{\mu} [GeV];Eff [HLTMu40e2p1PFJet200PFJet50v1]")
    #eff.Draw()
    tgraph2 = TGraphAsymmErrors()
    gPad.Update()
    eff.Draw()
    eff.Paint("")
    tgraph2 = eff.GetPaintedGraph()
    tgraph2.GetYaxis().SetRangeUser(0.,1.1)
    tgraph2.SetLineColor(0)
    tgraph2.SetMarkerStyle(20)
#tgraph1.SetMinimum(0)
    tgraph2.Draw("P") 
    c1.Update()
    c1.SetGrid()
    gStyle.SetTitleFontSize(0.1)
    c1.Update()
    c1.Modified()
    CMS_lumi.CMS_lumi(c1,4,11)
    text = TLatex()
    text.SetNDC()
    text.DrawText(0.4,0.95,hname)
    c1.SaveAs('Efficiency'+hname+sample[0]+'.png')
