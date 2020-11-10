# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:45:39 2020

@author: Tomi
"""

import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import numpy as np
import glob

def running_av(data, n=5):
    
    data_av = np.zeros(len(data))
    
    for i in range(n,len(data)-n):
        
           data_av[i] = np.nanmean(data[i-5:i+5])
           
    data_av[:n] = np.nan
    data_av[-n:] = np.nan
    
    return data_av

date = []
begin = []
peak = []
peak_n = []
end = []
xclass_file = input("Input file: ")
xclass_data = open(xclass_file, "r")
ak = 1
av = 1

xclass_dataline = xclass_data.read().split('\n')

name_list_s = sorted(glob.glob('C:\\Tomi\\AA_SZTE_Mester\\Studies\\Diplomamunka\\4_felev\\Advanced_2\\GOES_10_12_2X\\*.LIS'))
name_list_g = sorted(glob.glob('C:\\Tomi\\AA_SZTE_Mester\\Studies\\Diplomamunka\\4_felev\\Advanced_2\\GOES_10_12_2X\\*.CSV'))

for j in range(0, len(name_list_s)):
    
    lines = name_list_s[j].split('\\')[8]
    a = lines.split('.')[0]
    sc = datetime.datetime.strptime(a, '%Y-%m-%d')
    #print(sc)
    #print(xray)
    linex = name_list_g[j].split('\\')[8]
    b = linex.split('_')[0]
    xray = datetime.datetime.strptime(b, '%Y-%m-%d')
    #print(sc, xray)
    #print(name_list_s[j])
    #print(name_list_g[j])

    if (sc == xray):
  
        source_file_s1 = name_list_s[j]
        clearfile = open(source_file_s1[:-3] + 'txt','w')
        data_s1 = open(source_file_s1, 'r').read().split('\n')
    
        ff1 = []
        ff2 = []
        ff3 = []
        fwa = []
        time = []
        fwa_2 = []
        fa1 = 0.0
        fa2 = 0.0
        fa3 = 0.0
        #print(type(fwa))       
        for k in range (1, len(data_s1)-12):
             
            if data_s1[k][0] == 'C' and data_s1[k+1][0] == '*':
                ts = data_s1[k].split()[2]
                t = datetime.datetime.strptime(a+ts, '%Y-%m-%d%H:%M:%S').time()
                a1 = float(data_s1[k+1].split()[3])
                f1 = float(data_s1[k+1].split()[8])
                a2 = float(data_s1[k+2].split()[1])
                f2 = float(data_s1[k+2].split()[6])
                a3 = float(data_s1[k+3].split()[1])
                f3 = float(data_s1[k+3].split()[6])
        
                ff1.append(f1)
                ff2.append(f2)
                ff3.append(f3)
                time.append(t)
                #print(f1, f2, f3)
                d = (f1 + f2/np.sqrt(1/3) + f3/np.sqrt(6))/3
                #print(d)
                fwa.append(d)
                #print(fwa)
                
                clearfile.write("%s\t%f\t%f\t%f\t%f\t%f\t%f\n" % (t, a1, f1, a2, f2, a3, f3))

        source_file_x = name_list_g[j]
    
        tx = []
        xtime = []
        xa = []
        xl = []
        xl_s = []
        xs = []
        xl_s = []
        xs_s = []
    
        data_x = open(source_file_x, 'r').read().split('\n')
        for l in range (158, len(data_x)-1):
            dataline = data_x[l].split(',')
            #print(dataline)
            xl_s.append(dataline[2].split(';'))
            xs_s.append(dataline[1].split(';'))
            #print(bs)
            for m in range (len(xl_s)-1, len(xl_s)):
                #print(j)
                #print(bs[j][0])
                s = float(xl_s[m][0])
                #print(s)
                if (s == np.nan):
                    s = 0
                xl.append(s)

                ss = float(xs_s[m][0])
                #print(s)
                if (ss == np.nan):
                    ss = 0
                xs.append(ss)
            
                tx = dataline[0]
                #print(ts1)
                date_time_obj = datetime.datetime.strptime(tx, '%Y-%m-%d %H:%M:%S.%f')
                #print('Time:', date_time_obj.time())
                t = date_time_obj.time()
                xtime.append(t)

        for i in range (0,len(xclass_dataline)):
            y = (xclass_dataline[i].split()[0])
            yt = datetime.datetime.strptime(y, "%Y-%m-%d")
            date.append(yt)
            b = (xclass_dataline[i].split()[1])
            bt = datetime.datetime.strptime(y+b, "%Y-%m-%d%H%M")
            begin.append(bt)
            e = (xclass_dataline[i].split()[2])
            et = datetime.datetime.strptime(y+e, "%Y-%m-%d%H%M")
            end.append(et)
            p = (xclass_dataline[i].split()[3])
            pt = datetime.datetime.strptime(y + p, "%Y-%m-%d%H%M")
            pt1 = pt.time()
            peak_n.append(pt)
            peak.append(pt1)
            #print(ts2)
            
            if(yt == sc):
    
                hours_to_sub = 1
                bn = begin[i] - timedelta(hours = hours_to_sub)
                begin_new = bn.time()
                #print(begin[i])
                #print(begin_new)
                hours_to_add = 1
                en = end[i] + timedelta(hours = hours_to_add)
                end_new = en.time()
                #print(end[i])
                #print(peak_n[i])
                #print(end_new)
                    
                name_string = str(peak_n[i])
                #print(name_string)
                name_1 = name_string[0:4]
                #print(name_1)
                name_2 = name_string[5:7]
                #print(name_2)
                name_3 = name_string[8:10]
                #print(name_3)
                name_4 = name_string[11:13]
                #print(name_4)
                name_5 = name_string[14:16]
                #print(name_5)
                filename_aw = source_file_s1[:-14] + name_1 + name_2 + name_3 + "_" + name_4 + name_5 + "_run_aw"
                filename_3m = source_file_s1[:-14] + name_1 + name_2 + name_3 + "_" + name_4 + name_5 + "_3 modus_run_aw"
                peak_string = name_string[11:13] + ":" + name_string[14:16]
                #print(filename)
                #print(peak_string)
                
                n = 0
                for n in range(len(time)):
                    #print(time[n])
                    #print(begin_new)
                    if (time[n] < begin_new):
                        ak = int(n)
                    #print(end_new)    
                    if (time[n] < end_new):
                        av = int(n)
                        
                #print(type(ak))
                #print(type(av))
                #Ez resz oldja meg az időablakra vett átlagolást
                wa = 0
                #print(j)
                #print(ak)
                #print(av)
                #print(len(fwa))
                s = 0
                wa2 = 0
                #itt átlagol, néha nincs értelem az időablakra vett átlagolásnak, ekkor nem telejes napra
                if (ak < len(fwa)):
                    
                    for s in range(ak, av):
                        #print(s)
                        #print(wa)
                        #print(len(fwa))
                        wa = wa + fwa[s]
                    
                    wa2 = wa/(av-ak)
                    #print(np.average(fwa))
                    #print(wa2)
                    fwa = fwa - wa2*np.ones(len(fwa))
                    
                else:

                    fwa = fwa - np.average(fwa)
                
                if (ak < len(ff1)):
                    
                    for s in range(ak, av):
                        #print(s)
                        #print(wa)
                        #print(len(fwa))
                        fa1 = fa1 + ff1[s]
                    
                    fa1 = fa1/(av-ak)
                    
                if (ak < len(ff2)):
                    
                    for s in range(ak, av):
                        #print(s)
                        #print(wa)
                        #print(len(fwa))
                        fa2 = fa2 + ff2[s]
                    
                    fa2 = fa2/(av-ak)
                    
                if (ak < len(ff3)):
                    
                    for s in range(ak, av):
                        #print(s)
                        #print(wa)
                        #print(len(fwa))
                        fa3 = fa3 + ff3[s]
                    
                    fa3 = fa3/(av-ak)
        
                run_aw = running_av(fwa)
                run_f1 = running_av(ff1)
                run_f2 = running_av(ff2)
                run_f3 = running_av(ff3)
                
                plt.clf()
                plt.figure(1)
                
                plt.subplot(311)
                plt.grid()
                plt.plot(time, fwa, 'g-')
                plt.plot(time, run_aw, 'g-', linewidth = 2.0)
                plt.xlabel('')
                plt.xticks([begin_new, pt1, end_new], fontsize = 7)
                plt.yticks(fontsize = 7)
                plt.xlim(begin_new, end_new)
                plt.ylim([min(fwa), max(fwa)])
                plt.ylabel('Frekvencia(Hz)', fontsize = 7)
                plt.title("%s %s Schumann rezonancia (súlyozott átlag frekvencia)\n és röntgen fluxus (kék = 0,1 - 0,8 nm; lila = 0,05 - 0,4 nm)" % (source_file_s1[-14:-4], peak_string))
                plt.axvline(peak[i], 0, 8, color='r')
                #plt.axhline(wa2, 0, 8, color='r')
                
                plt.subplot(212)
                plt.grid()
                plt.yscale('log')
                plt.plot(xtime, xl, 'b-')
                plt.plot(xtime, xs, 'm-')
                plt.xticks([begin_new, pt1, end_new], fontsize = 7)
                plt.yticks(fontsize = 6)
                plt.xlim(begin_new, end_new)
                plt.ylabel('Röntgen sugárzás fluxus (W/m^2)', fontsize = 7)
                plt.xlabel('Idő (óra)', fontsize = 7)
                #plt.title("%s %s; X-ray radiation flux 1 - 8 nm" % (source_file_s1[-14:-4], peak_string))
                plt.axvline(peak[i], 0, 4, color='r')
            
                plt.tight_layout()
                plt.savefig(filename_aw, dpi = 300)
                plt.close()
                
                plt.clf()
                plt.figure(2)
              
                plt.subplot(411)
                plt.grid()
                plt.plot(time, ff1, 'g-')
                plt.plot(time, run_f1, 'g-', linewidth = 2.0)
                plt.xlabel('')
                plt.xticks([begin_new, pt1, end_new], fontsize = 7)
                plt.yticks(fontsize = 7)
                plt.xlim(begin_new, end_new)
                plt.ylim([min(ff1),max(ff1)])
                plt.ylabel('Frekvencia (Hz)', fontsize = 7)
                plt.title("%s %s; Schumann rezonancia 1 - 3. módus (zöld, vörös, sárga)\n és röntgen fluxus (kék = 0,1 - 0,8 nm; lila = 0,05 - 0,4 nm)" % (source_file_s1[-14:-4], peak_string))
                plt.axvline(peak[i], 0, 4, color='r')
                plt.axhline(fa1, 0, 4, color='k')
               
                plt.subplot(412)
                plt.grid()
                plt.plot(time, ff2, 'r-')
                plt.plot(time, run_f2, 'r-', linewidth = 2.0)
                plt.xlabel('')
                plt.xticks([begin_new, pt1, end_new], fontsize = 7)
                plt.yticks(fontsize = 7)
                plt.xlim(begin_new, end_new)
                plt.ylim([min(ff2),max(ff2)])
                plt.ylabel('Frekvencia (Hz)', fontsize = 7)
                #plt.title("%s %s; 2. mode" % (source_file_s1[-14:-4], peak_string))
                plt.axvline(peak[i], 0, 4, color='r')
                plt.axhline(fa2, 0, 4, color='k')
                               
                plt.subplot(413)
                plt.grid()
                plt.plot(time, ff3, 'y-')
                plt.plot(time, run_f3, 'y-', linewidth = 2.0)
                plt.xlabel('')
                plt.xticks([begin_new, pt1, end_new], fontsize = 7)
                plt.yticks(fontsize = 7)
                plt.xlim(begin_new, end_new)
                plt.ylim([min(ff3),max(ff3)])
                plt.ylabel('Frekvencia (Hz)', fontsize = 7)
                #plt.title("%s %s; 3. mode" % (source_file_s1[-14:-4], peak_string))
                plt.axvline(peak[i], 0, 4, color='r')
                plt.axhline(fa3, 0, 4, color='k')
              
                plt.subplot(414)
                plt.grid()
                plt.plot(xtime, xl, 'b-')
                plt.plot(xtime, xs, 'm-')
                plt.yscale('log')
                plt.xlabel('')
                plt.xticks([begin_new, pt1, end_new], fontsize = 7)
                plt.yticks(fontsize = 7)
                plt.xlim(begin_new, end_new)
                plt.ylabel('Röntgen fluxus (W/m^2)', fontsize = 7)
                plt.xlabel('Idő (óra)', fontsize = 6)
                #plt.title("%s %s; X-ray radiation flux 0,1 - 0,8 nm" % (source_file_s1[-14:-4], peak_string))
                plt.axvline(peak[i], 0, 4, color='r')
                
                
                
                plt.show()
                plt.tight_layout()
                plt.savefig(filename_3m, dpi = 300)
                plt.close()
    
                clearfile.close()