from casatasks.private import tec_maps
import os

name = 'pbandB1'

listobs_file = listobs(vis=f'{name}.ms', verbose=True, listfile=f'{name}.listobs')

plotants(vis=f'{name}.ms', figfile=f'{name}_plotants.png')

plotms(vis=f'{name}.ms', xaxis='freq', yaxis='amp', antenna='ea02', correlation='XX,YY', field='3C286',  plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', xlabel='Frequency', ylabel='Amplitude', iteraxis='baseline')

flagdata(vis=f'{name}.ms', mode='manual', scan='1~2')

flagdata(vis=f'{name}.ms', mode='shadow', tolerance=0.0, flagbackup=False)

flagdata(vis=f'{name}.ms', mode='clip', clipzeros=True, flagbackup=False)

flagdata(vis=f'{name}.ms', mode='quack', quackinterval=5.0, quackmode='beg', flagbackup=False)

# cd calibration
os.system('cd calibration')

hanningsmooth(vis=f'../{name}.ms', outputvis=f'{name}_hanning.ms', datacolumn='data', spw='0~15')

# plotms(vis=f'{name}_hanning.ms', xaxis='freq', yaxis='amp', antenna='ea02', correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw',iteraxis='baseline')

gencal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.antpos', caltype='antpos')

tec_image, tec_rms_image, plotname = tec_maps.create(vis=f'{name}_hanning.ms', doplot=True)

gencal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.tecim', caltype='tecim', infile=tec_image)

gencal(vis=f'{name}_hanning.ms', caltype='rq', caltable=f'{name}_hanning.rq')

# plotms(vis=f'{name}_hanning.ms',correlation='RR,LL',antenna='ea01',xaxis='freq',yaxis='amp',coloraxis='spw',iteraxis='baseline')

flagdata(vis=f'{name}_hanning.ms', field='*', mode='tfcrop', datacolumn='data', timecutoff=4., freqcutoff=3., maxnpieces=5, action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s', correlation='ABS_XY,ABS_YX')

flagdata(vis=f'{name}_hanning.ms', field='*', mode='tfcrop', datacolumn='data',timecutoff=3., freqcutoff=3., maxnpieces=2, action='apply', display='report', flagbackup=False, combinescans=True, ntime='3600s', correlation='ABS_XX,ABS_YY')

flagdata(vis=f'{name}_hanning.ms', mode='extend')

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp', ydatacolumn = 'corrected', antenna='ea02',correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline')

spw_chan = '0:5~15,1:55~65,3:37~47,4:55~65,5:85~95,6:75~85,7:55~65,8:55~65,9:100~110,10:55~65,11:30~40,12:90~100,13:55~65,14:20~30,15:55~65'

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.G0', gaintype='G', calmode='p', solint='int', field='3C286',refant='ea25', spw=spw_chan, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim'])

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.K0', gaintype='K', solint='inf', field='3C286',refant='ea25', spw=spw_chan, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.G0'])

bandpass(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.B0', solint='inf', field='3C286',refant='ea25', minsnr=2.0, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.G0',f'{name}_hanning.K0'])

plotms(vis=f'{name}_hanning.B0', xaxis='freq', yaxis='amp', iteraxis='antenna', coloraxis='spw')  # interactive flagging of outliers

applycal(vis=f'{name}_hanning.ms', field='3C286', applymode='calflagstrict', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.G0',f'{name}_hanning.K0',f'{name}_hanning.B0'] )

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp', ydatacolumn = 'corrected', antenna='ea01',correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline')

flagdata(vis=f'{name}_hanning.ms', mode='rflag', field='3C286,J1330+2509', datacolumn='corrected', timedevscale=3., freqdevscale=3.,action='calculate', display = 'both', flagbackup=False, combinescans=True, ntime='3600s')

flagdata(vis=f'{name}_hanning.ms', mode='manual', spw='2,9', flagbackup=True)

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp',antenna='ea02',correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline', ydatacolumn='corrected')

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp',antenna='ea02',correlation='XX,YY', field='J1330+2509', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline', ydatacolumn='data')

clearcal(vis=f'{name}_hanning.ms')

setjy(vis=f'{name}_hanning.ms', field='3C286', standard='Scaife-Heald 2012', usescratch=True)

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.K1', field='3C286', solint='inf', refant='ea27', gaintype='K', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.tecim',f'{name}_hanning.rq'])

# plotms(vis=f'{name}_hanning.K1',xaxis='antenna1',yaxis='delay',plotrange=[0,30,-50.,50.])

bandpass(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.B1', field='3C286', solint='inf', refant='ea27', minsnr=3.0, parang = True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.tecim',f'{name}_hanning.rq',f'{name}_hanning.K1'], interp=['','','','nearest,nearestflag'])
##########################################################################
############### stop here for manual flagging of outlisers ###############
##########################################################################
plotms(vis=f'{name}_hanning.B1', xaxis='freq', yaxis='amp', iteraxis='antenna', coloraxis='spw')

plotms(vis=f'{name}_hanning.B1', xaxis='freq', yaxis='phase', iteraxis='antenna', plotrange=[0,0,-180.,180.], coloraxis='spw')

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.G1', field='3C286', solint='int', refant='ea27', minsnr=3.0, gaintype='G', calmode='ap', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1'], interp=['','','','nearest,nearestflag','nearest,nearestflag'])

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.G1', field='J1330+2509', solint='int', refant='ea27', minsnr=3.0, gaintype='G', calmode='ap', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1'], interp=['','','','nearest,nearestflag','nearest,nearestflag'], append=True)

# plotms(vis=f'{name}_hanning.G1', xaxis='time', yaxis='amp', iteraxis='antenna', coloraxis='spw')

# plotms(vis=f'{name}_hanning.G1', xaxis='time', yaxis='phase', plotrange=[0,0,-180.,180.], iteraxis='corr', coloraxis='baseline')

# plotms(vis=f'{name}_hanning.G1', xaxis='time', yaxis='phase', correlation='/', coloraxis='baseline', plotrange=[-1,-1,-180,180])


myscale = fluxscale(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.G1', fluxtable=f'{name}_hanning.fluxscale1', reference='3C286', transfer=['J1330+2509'], incremental=False)

applycal(vis=f'{name}_hanning.ms', field='3C286', parang=True, applymode='calflagstrict', flagbackup=True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1',f'{name}_hanning.G1', f'{name}_hanning.fluxscale1'], gainfield=['', '', '', '', '', '', '3C286'], interp=['','','','nearest,nearestflag','nearest,nearestflag','nearest,nearestflag', 'nearest'])

applycal(vis=f'{name}_hanning.ms', field='J1330+2509', parang=True, applymode='calflagstrict', flagbackup=True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1',f'{name}_hanning.G1', f'{name}_hanning.fluxscale1'], gainfield=['', '', '', '', '', '', 'J1330+2509'], interp=['','','','nearest,nearestflag','nearest,nearestflag','nearest,nearestflag', 'nearest'])

applycal(vis=f'{name}_hanning.ms', field='NGC4869', parang=True, applymode='calflagstrict', flagbackup=True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1',f'{name}_hanning.G1', f'{name}_hanning.fluxscale1'], gainfield=['', '', '', '', '', '', 'J1330+2509'], interp=['','','','nearest,nearestflag','nearest,nearestflag','nearest,nearestflag', 'linear'])

split(vis=f'{name}_hanning.ms', outputvis=f'../coma_{name}_hanning.ms', datacolumn='corrected', field='NGC4869')

# cd ..
os.system('cd ..')

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag')

flagdata(vis=f'coma_{name}_hanning.ms', mode='extend')

statwt(vis=f'coma_{name}_hanning.ms', datacolumn='data', timebin=30)

################################################################
###################### SELF-CALIBRATION ########################
################################################################

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 4000 4000 -scale 2.5asec -data-column DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 3 3 -name selfcal_images/selfcal_cycle_0 -niter 200000 coma_pbandB1_hanning.ms > selfcal_images/wsclean.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_0.cal', solint='inf', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_0.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_0.cal', calwt=False)

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 4000 4000 -scale 2.5asec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 4 4 -name selfcal_images/selfcal_cycle_1 -niter 200000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc1.log

gaincal(vis='coma_pbandB1_hanning.ms', caltable='selfcal/gains_cycle_1.cal', solint='300s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_1.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis='coma_pbandB1_hanning.ms', gaintable='selfcal/gains_cycle_1.cal', calwt=False)

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 4 4 -name selfcal_images/selfcal_cycle_2 -niter 200000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc2.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_2.cal', solint='200s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_2.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_2.cal', calwt=False)

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_3 -niter 200000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc3.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_3.cal', solint='150s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_3.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_3.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_4 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc4.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_4.cal', solint='100s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_4.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_4.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_5 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc5.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_5.cal', solint='80s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_5.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_5.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5100 5100 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.2 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_6 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc6.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_6.cal', solint='40s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_6.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_6.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.2 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_7 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc7.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_7.cal', solint='20s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_7.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_7.cal', calwt=False)

# flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.2 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_8 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc8.log
############# here #############
gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_8.cal', solint='10s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_8.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_8.cal', calwt=False)

# flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_9 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc9.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_9.cal', solint='int', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_9.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_9.cal', calwt=False)

# flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_10 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc10.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_10.cal', solint='inf', refant='ea27', gaintype='G', calmode='ap', solnorm=True, gaintable=['selfcal/gains_cycle_9.cal'])

# plotms(vis='selfcal/gains_cycle_10.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable=['selfcal/gains_cycle_10.cal', 'selfcal/gains_cycle_9.cal'], calwt=False)

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_11 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc11.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_11.cal', solint='100s', refant='ea27', gaintype='G', calmode='ap', solnorm=True, gaintable=['selfcal/gains_cycle_9.cal'])

# plotms(vis='selfcal/gains_cycle_11.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable=['selfcal/gains_cycle_11.cal', 'selfcal/gains_cycle_9.cal'], calwt=False)

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_12 -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/wsclean_sc12.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_12.cal', solint='60s', refant='ea27', gaintype='G', calmode='ap', solnorm=True, gaintable=['selfcal/gains_cycle_9.cal'])

# plotms(vis='selfcal/gains_cycle_12.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable=['selfcal/gains_cycle_12.cal', 'selfcal/gains_cycle_9.cal'], calwt=False)





######### for spectral index imaging #############
singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5100 5100 -scale 2arcsec -data-column CORRECTED_DATA -no-update-model-required -beam-size 9arcsec-reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/coma_pbandB0704_alpha -niter 300000 coma_pbandB1_hanning.ms > selfcal_images/pband0704_alpha.log




################################################################

tclean(vis=f'coma_{name}_hanning.ms', imagename='tclean_test2', cell=['5.0arcsec','5.0arcsec'], imsize=[2048,2048], deconvolver='mtmfs',nterms=2, gridder='standard', stokes='I', niter=20000, interactive=True, scales=[0,20,30], pblimit=0.01, savemodel='modelcolumn', weighting='briggs', robust=0.0, mask='tclean_test.mask')

