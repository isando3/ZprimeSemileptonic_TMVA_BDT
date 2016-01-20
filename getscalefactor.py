import ROOT as R
import sys
from math import sqrt, pow
from array import array

#R.SetOwnership(central, False)

f1 = R.TFile(sys.argv[1],'r')#data
f2 = R.TFile(sys.argv[2],'r')#MC
graph1 = f1.Get(sys.argv[3])
graph2 = f2.Get(sys.argv[4])
fout = R.TFile(sys.argv[5], 'recreate')

n = graph1.GetN()
x1, y1, yerr_up1, yerr_down1, x2, y2, yerr_up2, yerr_down2, xerr_left, xerr_right  = [], [], [], [], [], [], [],[], [], []
x12, y12 , yerr_up12, yerr_down12, xerr_left12, xerr_right12 = [],[],[],[],[],[]
for i in range(n):
    tmpX1, tmpY1, tmpX2, tmpY2 = R.Double(0), R.Double(0), R.Double(0), R.Double(0)
    graph1.GetPoint(i, tmpX1, tmpY1)
    graph2.GetPoint(i, tmpX2, tmpY2)
    x1.append(tmpX1)
    x2.append(tmpX2)
    y1.append(tmpY1)
    yerr_up1.append(graph1.GetErrorYhigh(i))
    yerr_down1.append(graph1.GetErrorYlow(i))
    y2.append(tmpY2)
    yerr_up2.append(graph2.GetErrorYhigh(i))
    yerr_down2.append(graph2.GetErrorYlow(i))
    xerr_left.append(graph2.GetErrorXlow(i))
    xerr_right.append(graph2.GetErrorXhigh(i))
print len(x1)
print y1[0]
print y2[0]
y12=[0.]*len(x1)
yerr_down12 = [0.]*len(x1)
yerr_up12 = [0.]*len(x1)

for j in  xrange(len(x1)):
     y12[j] = y1[j]/y2[j]
     yerr_down12[j]= sqrt(pow(y12[j],2)*(pow(yerr_down1[j]/y1[j], 2)+pow(yerr_down2[j]/y2[j],2)))
     yerr_up12[j]= sqrt(pow(y12[j],2)*(pow(yerr_up1[j]/y1[j], 2)+pow(yerr_up2[j]/y2[j],2)))
     #x12[j] = x1[j]
     #xerr_left12 = xerr_left[j]
     #xerr_right12 = xerr_right[j]

ax1 = array("d",x1)
ay12 = array("d",y12)
axel = array("d",xerr_left)
axer = array("d", xerr_right)
ayd12 = array("d", yerr_down12)
ayu12 = array("d", yerr_up12)
sf =  R.TGraphAsymmErrors(len(x1),ax1,ay12,axel,axer,ayd12,ayu12)
sf.SetTitle("Trigger Scale Factor")
sf.SetMarkerColor(4)
sf.SetMarkerStyle(21)
sf.Draw("ALP")
fout.WriteTObject(sf, "ScaleFactor")
fout.Close
