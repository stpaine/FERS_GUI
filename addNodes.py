# -- addNodes.py as part of FERS XML File I/O as part of FERS Plugin
# -- Created by James Gripper 
# -- November 2016
# -*- coding: utf-8 -*-#

from lxml import etree
from PyQt4 import QtCore, QtGui
import sys
import os

## creates parser object
parser = etree.XMLParser(remove_blank_text=True,ns_clean=True)

## renames simulation name
def renameSimulation(name, filename):
    doc = etree.parse(filename, parser)
    
    sim = doc.getroot()
    sim.set('name', name)
    doc.write(filename, pretty_print=True)
    print '--Simulation renamed--'

## adds transmitter to simulation
def appendTx(filename, name, trans_type, pulse_name, antenna_name, clock_name, prf_in): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    transmitter = etree.SubElement(root,'transmitter', {'name':name, 'type':trans_type, 'pulse':pulse_name, 'antenna':antenna_name, 'timing':clock_name})
    
    prf = etree.SubElement(transmitter,'prf')
    prf.text = prf_in    
    
    doc.write(filename, pretty_print=True)

## adds transmitter to platform    
def appendTxToPlatform(filename,plat_name, txname, trans_type, pulse_name, antenna_name, clock_name, prf_val): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    for plat in root.findall('platform'):
        name = plat.get('name')
        if name == plat_name:    
            transmitter = etree.Element('transmitter', {'name':txname, 'type':trans_type, 'pulse':pulse_name, 'antenna':antenna_name, 'timing':clock_name})
            plat.append(transmitter)
    
            prf = etree.SubElement(transmitter,'prf')
            prf.text = prf_val
    
            doc.write(filename, pretty_print=True)
            print'--Transmitter Added to Platform--'
        else:
            print'--Invalid Platform. Please Try Again--'

## adds receiver to simulation    
def appendRx(filename, name, antenna_name, clock_name, nd_bool,noploss_bool, skip_time, receiver_window_length, pulse_rf,receiver_temp): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    receiver = etree.SubElement(root, 'receiver', {'name':name, 'antenna':antenna_name,'timing':clock_name, 'nodirect':nd_bool, 'nopropagationloss':noploss_bool})
    
    window_skip = SubElement(receiver, 'window_skip')
    window_skip.text = skip_time
    
    window_length = SubElement(receiver,'window_length')
    window_length.text = receiver_window_length
    
    prf = SubElement(receiver, 'prf')
    prf.text = pulse_rf  

    temp = SubElement(receiver, 'receiver_temp')
    temp.text = receiver_temp
    
    doc.write(filename, pretty_print=True)
    
## adds receiver to platform    
def appendRxToPlatform(filename,plat_name, igh, antenna_name, clock_name, nd_bool,noploss_bool, skip_time, receiver_window_length, pulse_rf,receiver_temp): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    for plat in root.findall('platform'):
        name = plat.get('name')
        if name == plat_name:        
            receiver = etree.Element('receiver', {'name':igh, 'antenna':antenna_name,'timing':clock_name, 'nodirect':nd_bool, 'nopropagationloss':noploss_bool})
            plat.append(receiver)
    
            window_skip = etree.SubElement(receiver,'window_skip')
            window_skip.text = skip_time
    
            window_length = etree.SubElement(receiver,'window_length')
            window_length.text = receiver_window_length
        
            prf = etree.SubElement(receiver,'prf')
            prf.text = pulse_rf
        
            temp = etree.SubElement(receiver,'receiver_temp')
            temp.text = receiver_temp
            
            doc.write(filename, pretty_print=True)
            print '--Receiver Added to Platform--'  
        else:
            print '--Invalid Platform. Please Try Again--'
            
   

## adds parameters to simulation
def appendParameters(filename, start_time, end_time, s_o_l, export_sampling_rate, csv_bool, binary_bool, csvbinary_bool, cw_interpolation_rate, seed_for_PRGN, num_adc_bit, oversampling_ratio): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    parameters = etree.SubElement(root,'parameters')
    
    starttime = etree.SubElement(parameters,'starttime')
    starttime.text = start_time
        
    endtime = etree.SubElement(parameters,'endtime')
    endtime.text =end_time

    sol = etree.SubElement(parameters,'c')
    sol.text = s_o_l      

    rate = etree.SubElement(parameters,'rate')
    rate.text = export_sampling_rate 
    
    export = etree.SubElement(parameters,'export', {'csv':csv_bool, 'binary':binary_bool, 'csvbinary':csvbinary_bool})
        
    endtime = etree.SubElement(parameters,'interpreate')
    endtime.text =end_time 

    randseed = etree.SubElement(parameters,'randomseed')
    randseed.text =seed_for_PRGN
    
    adcbits = etree.SubElement(parameters,'adc_bits')
    adcbits.text =num_adc_bit    

    oversample = etree.SubElement(parameters,'oversample')
    oversample.text =oversampling_ratio
     
    
    doc.write(filename,pretty_print=True)
 
## adds transmission pulse to simulation
def appendTPulse(filename, name, file_type, pulse_filename, power,carrier_freq): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()
    tree = etree.ElementTree(root)
    
    pulse = etree.SubElement(root,'pulse', {'name':name, 'type':file_type,'filename':pulse_filename})
    
    pulse_power = etree.SubElement(pulse, 'power')
    pulse_power.text = power
     
    carrier = etree.SubElement(pulse,'carrier')
    carrier.text = carrier_freq  
    
    doc.write(filename, pretty_print=True)   

## adds clock to simulation    
def appendTiming(filename, name, syncon, clock_freq, jit, alpha_value, mass, freq_offset, phase_offset, Rfreq_off, Rphase_off): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()
    tree=etree.ElementTree(root)
    
    timing = etree.SubElement(root,'timing', {'name':name, 'synconpulse':syncon})
    
    freq = etree.SubElement(timing,'frequency')
    freq.text = clock_freq
    
    jitter = etree.SubElement(timing,'jitter')
    jitter.text = jit
    
    noise = etree.SubElement(timing,'noise')
    
    alpha = etree.SubElement(noise,'alpha')
    alpha.text = alpha_value
    
    weight = etree.SubElement(noise,'weight')
    weight.text = mass
    
    f_offset = etree.SubElement(timing,'freq_offset')
    f_offset.text = freq_offset
    
    p_offset = etree.SubElement(timing,'phase_offset')
    p_offset.text = phase_offset
    
    Rfreq_offset = etree.SubElement(timing,'Random_freq_offset')
    Rfreq_offset.text = Rfreq_off
    
    Rphase_offset = etree.SubElement(timing,'Random_phase_offset')
    Rphase_offset.text = Rphase_off
    
    doc.write(filename,pretty_print=True)    
    
## adds multipath surface to simulation
def appendMultipathSurfaces(filename, refecting_factor, x, y, z,d): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    multipath = etree.Element('multipath')
    root.append(multipath)
    
    factor = etree.SubElement(multipath,'factor')
    factor.text = refecting_factor
    
    nx = etree.SubElement(multipath,'nx')
    nx.text = x

    ny = etree.SubElement(multipath,'ny')
    ny.text = y
    nz = etree.SubElement(multipath,'nz')
    nz.text = z
    
    nd = etree.SubElement(multipath,'d')
    nd.text = d

    doc.write(filename, pretty_print=True)   
    print '--Multipath Added--'
    
## adds monostatics to simulation    
def appendMonostatics(filename, mono_name, trans_type, antenna_name, pulse_name,timing, skip_time,rec_window_length,pulse_rf): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    monostatic = etree.Element('monostatic', {'name':mono_name, 'type':trans_type, 'antenna':antenna_name, 'pulse':pulse_name,'timing':timing})
    root.append(monostatic)
    
    window_skip = etree.SubElement(monostatic,'window_skip')
    window_skip.text = skip_time
    
    window_length = etree.SubElement(monostatic,'window_length')
    window_length.text = rec_window_length

    prf = etree.SubElement(monostatic,'prf')
    prf.text = pulse_rf     
    
    doc.write(filename, pretty_print=True)  


## adds target to user chosen platform    
def appendTargetToPlatform(filename,plat_name, target_name, rcs_type, rcs_value,model, const,standard_dev): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()         ## root node
    tree = etree.ElementTree(root) ## tree object
    
    for plat in root.findall('platform'):
        name = plat.get('name')
        if name == plat_name:    
            
            target = etree.Element('target', {'name':target_name})
            plat.append(target)
    
            rcs = etree.SubElement(target,'rcs', {'type':rcs_type})
            rcs.text = rcs_value
        
            modeled = etree.SubElement(target,'model', {'type':model})
            modeled.text = const
            
            k = etree.SubElement(modeled,'k')
            
            if model == 'constant':
                k.text = standard_dev
                doc.write(filename, pretty_print=True)
                print '--Target added to Platform--'
                
            elif model == 'chi-square':
                k.text = standard_dev
                doc.write(filename, pretty_print=True)
                print '--Target added to Platform--'        
                
            elif model == 'gamma':
                k.text = standard_dev
                doc.write(filename, pretty_print=True)
                print '--Target added to Platform-'
                
            else:
                print"--Not supported type--"
                return    
        else:
            print'--Invalid Platform. Please Try Again--'

    
## adds an antenna to simulation
def appendAntenna(filename, antenna_name, gain_pattern, pattern_file, ant_efficiency,a,b,g,d,az,el,): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    root = doc.getroot()
    tree = etree.ElementTree(root)
    
    antenna = etree.SubElement(root,'antenna', {'name':antenna_name,'pattern':gain_pattern, 'filename':pattern_file})
    
    efficiency = etree.SubElement(antenna,'efficiency')
    efficiency.text = ant_efficiency
    
    alpha = etree.SubElement(antenna,'alpha')
    alpha.text = a
    
    beta = etree.SubElement(antenna,'beta')
    beta.text = b

    gamma = etree.SubElement(antenna,'gamma')
    gamma.text = g
    
    diameter = etree.SubElement(antenna,'diameter')
    diameter.text = d
    
    azscale = etree.SubElement(antenna,'azscale')
    azscale.text = az

    elscale = etree.SubElement(antenna,'elscale')
    elscale.text = el

    doc.write(filename,pretty_print=True) 

## adds platform to simulation
def appendPlatform(filename, platform_name): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    sim = doc.getroot()
    tree=etree.ElementTree(sim)
    platform = etree.SubElement(sim,'platform', {'name':platform_name})
    
    doc.write(filename,pretty_print=True) 
    
##def appendMotionPath(filename,plat_name, interp): 
    ##doc = etree.parse(filename, parser)
    ##root = doc.getroot()
    ##tree=etree.ElementTree(root)
    ##for plat in root.findall('platform'):
        ##name = plat.get('name')
        ##if name == plat_name:
            ##motion = etree.SubElement(plat,'motionpath', {'interpolation':interp})
    
            ##doc.write(filename,pretty_print=True)
        ##else:
            ##print'--Invalid Platform. Please Try Again--'
            
def appendMotionPath(filename,plat_name, type_int,x_val, y_val, alt_val, t_val): 
    doc = etree.parse(filename, parser)
    root = doc.getroot()
    tree=etree.ElementTree(root)
    for platform in root.findall('platform'):
        name = platform.get('name')
        if name == plat_name:
            motion = etree.Element('motionpath', {'interpolation':type_int})
            platform.append(motion)
            doc.write(filename,pretty_print=True) ##motionpath added to platform
            
            document = etree.parse(filename, parser)
            sim = doc.getroot()
            tree=etree.ElementTree(sim)
            for plat in sim.findall('platform'):
                z = plat.get('name')
                if z == plat_name: 
                    for mot in plat.findall('motionpath'):
                        interp = mot.get('interpolation')
                        if interp == type_int:
                            position =etree.Element('positionwaypoint')
                            mot.append(position)                    
                                    
                            x = etree.SubElement(position,'x')
                            x.text = x_val
                            
                            y = etree.SubElement(position,'y')
                            y.text = y_val       
                        
                            alt = etree.SubElement(position,'altitude')
                            alt.text = alt_val   
                            
                            time = etree.SubElement(position,'time')
                            time.text = t_val
                            
                            doc.write(filename,pretty_print=True)            
                            print '--Position Waypoint Added to Existing Motionpath--'
                    
                        else:
                            motion = etree.Element('motionpath', {'interpolation':type_int})
                            plat.append(motion)
                            position =etree.Element('positionwaypoint')
                            mot.append(position)                    
                                    
                            x = etree.SubElement(position,'x')
                            x.text = x_val
                            
                            y = etree.SubElement(position,'y')
                            y.text = y_val       
                        
                            alt = etree.SubElement(position,'altitude')
                            alt.text = alt_val   
                            
                            time = etree.SubElement(position,'time')
                            time.text = t_val
                            
                            doc.write(filename,pretty_print=True)                         
                            print '--Position Waypoint Added to New Motionpath--'
        else:
            print'--Invalid Platform. Please Try Again--'            


## adds fixed rotation surface to platform                
def appendFixedRotation(filename,plat_name, initial_azi_angle, ani_angular_vel, init_el, el_angular_vel,): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    sim = doc.getroot()
    tree=etree.ElementTree(sim)    
    
    for plat in doc.findall('platform'):
        name = plat.get('name')
        if name == plat_name:
            rotation =etree.Element('fixedrotation')
            plat.append(rotation)
    
            a = etree.SubElement(rotation,'startazimuth')
            a.text = initial_azi_angle
    
            b = etree.SubElement(rotation,'azimuthrate')
            b.text = ani_angular_vel
        
            c = etree.SubElement(rotation,'startelevation')
            c.text = init_el
        
            d = etree.SubElement(rotation,'elevationrate')
            d.text = el_angular_vel     
            
            doc.write(filename,pretty_print=True)
            
        else:
            print'--Platform not found--'

## adds rotation waypoint to platform
def appendRotationWaypoint(filename,plat_name, el_angle, azi_angle, t): ##, t1, c, rate, csv, binary, csvbi, int_rate, seed, adc_bits, over_rate, filename):
    doc = etree.parse(filename, parser)
    sim = doc.getroot()
    tree=etree.ElementTree(sim)    
    
    for plat in doc.findall('platform'):
        name = plat.get('name')
        if name == plat_name:
        
            rotation =etree.Element('rotationwaypoint')
            plat.append(rotation)
            
            a = etree.SubElement(rotation,'elevation')
            a.text = el_angle
            
            b = etree.SubElement(rotation,'azimuth')
            b.text = azi_angle   
        
            c = etree.SubElement(rotation,'time')
            c.text = t 
        
            doc.write(filename,pretty_print=True)
        else:
            print '--Platform not found--'
           

     



if __name__ == "__main__":
    import sys
    ## testing functions
    ##createSimulation('hfghsfg', 'wozzles.xml')
    ##appendTiming('wozzles.xml','man','false','5', '6', '7', '8','9','10' )
    ##appendTx('wozzles.xml', 'a', 'b', 'c', 'd', 'e')
    ##appendRx('wozzles.xml','1', '2','3', 'true','false', '4', '5','6', '7')
    ##appendParameters('wozzles.xml', '0','1','45e6','3','false','true','true','4','54','8','3')
    ##appendTPulse('wozzles.xml', '2', 'file', 'dkvgjsdv.xml', '23e10','12')
    ##appendMultipathSurfaces('wozzles.xml', '3', '1', '3', '2', '1010005')
    ##appendMonostatics('wozzles.xml', 'mono_name', 'trans', 'fred','2', '42', '24','5', '7')
    ##appendTarget('wozzles.xml', 'mono_name', 'isotropic', '5', 'eghfg', '3','3')
    ##appendAntenna('wozzles.xml', 'antenna_name', 'gain_pattern', 'rofl.xml','6', '5', '6','7', '4','4','6')
    ##appendPlatform('wozzles.xml', '2')
    ##appendMotionPath('wozzles.xml', '4')
    ##appendPositionWaypoint('wozzles.xml', '53253245', '3', '4', '3')
    ##appendFixedRotation('wozzles.xml', 'initial_azi_angle', 'ani_angular_vel', 'init_el', 'el_angular_vel')
    ##appendRotationWaypoint('wozzles.xml', 'el_angle', 'azi_angle','4')
    ##appendTxToPlatform('wozzles.xml', 'a', 'b', 'c', 'd', 'e')
    ##appendRxToPlatform('wozzles.xml','1', '2','3', 'true','false', '4', '5','6', '7')
    
    