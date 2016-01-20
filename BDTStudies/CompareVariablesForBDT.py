import sys
import os
from ROOT import * 

filein_1 = TFile(sys.argv[1])
print 'Opening: ', filein_1
filein_2 = TFile(sys.argv[2])
print 'Opening: ', filein_2
filein_3 = TFile(sys.argv[3])
print 'Opening: ', filein_3
filein_4 = TFile(sys.argv[4])
print 'Opening: ', filein_4
directory = sys.argv[5]
print 'Getting directory:', directory
subdir_1 = filein_1.Get(directory)
subdir_2 = filein_2.Get(directory)
subdir_3 = filein_3.Get(directory)
subdir_4 = filein_4.Get(directory)
print 'Getting the list of keys:'
k1= subdir_1.GetListOfKeys()
print k1
k2 = subdir_2.GetListOfKeys()
print k2
k3= subdir_3.GetListOfKeys()
print k1
k4 = subdir_4.GetListOfKeys()
print k4
c1 = TCanvas('c1','c1',1)
for key1 in k1:
    for key2 in k2:
        for key3 in k3:
            for key4 in k4:
                if (key1.GetName()== key3.GetName() and key1.GetName() == key4.GetName() and key2.GetName() == key1.GetName() and 'vs' not in key1.GetName()):
                    c1.cd()
                    h1 = key1.ReadObj().Clone()
                    norm1 = h1.GetEntries()
                    if norm1 ==0 :
                        continue
                    h1.Scale(1/norm1)
                    h1.SetLineColor(kBlue)
                    h1.SetFillColor(kBlue)
                    h1.SetFillStyle(3345)
                    h1.SetMarkerStyle(20)
                    h1.SetMarkerColor(kBlue)
                    h2 = key2.ReadObj().Clone()
                    norm2 = h2.GetEntries()
                    if norm2 == 0:
                        continue
                    h2.Scale(1/norm2)
                    h2.SetLineColor(kRed)
                    h2.SetFillColor(kRed)
                    h2.SetFillStyle(3354)
                    h2.SetMarkerStyle(20)
                    h2.SetMarkerColor(kRed)
                    h3 = key3.ReadObj().Clone()
                    norm3 = h3.GetEntries()
                    if norm3 == 0:
                        continue
                    h3.Scale(1/norm3)
                    h3.SetLineColor(kGreen)
                    h3.SetFillColor(kGreen)
                    h3.SetFillStyle(3354)
                    h3.SetMarkerStyle(20)
                    h3.SetMarkerColor(kGreen)
                    h4 = key4.ReadObj().Clone()
                    norm4 = h4.GetEntries()
                    if norm4 == 0:
                        continue
                    h4.Scale(1/norm4)
                    h4.SetLineColor(kOrange)
                    h4.SetFillColor(kOrange)
                    h4.SetFillStyle(3354)
                    h4.SetMarkerStyle(20)
                    h4.SetMarkerColor(kOrange)
                    maxlist = []
		    max1 = h1.GetMaximum()
                    maxlist.append(max1)
                    max2 = h2.GetMaximum()
                    maxlist.append(max2)
		    max3 = h3.GetMaximum()
                    maxlist.append(max3)
                    max4 = h4.GetMaximum()
                    maxlist.append(max4)
	            totalmax= max(maxlist)
                    h1.GetYaxis().SetRangeUser(0,totalmax)
                    h1.Draw()
                    h3.Draw('SAME')
                    h2.Draw('SAME')
                    h4.Draw('SAME')
                    c1.Update()
                    name =  key1.GetName()
                    c1.SaveAs(directory+'_'+name+'compare.png')
                    del maxlist[:]

   

